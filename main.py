import argparse
import cv2
import numpy as np
from pathlib import Path
import hashlib
from datetime import datetime
from skimage import filters
import json

class ColonyImageProcessor:
    def __init__(self, input_dir, output_dir):
        """
        Initialize the colony image processor
        
        Args:
            input_dir (str): Directory containing input images
            output_dir (str): Directory to save processed images
        """
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Create subdirectories for different image types
        self.orig_dir = self.output_dir / 'original'
        self.seg_dir = self.output_dir / 'segmented'
        self.combined_dir = self.output_dir / 'combined'
        
        for dir_path in [self.orig_dir, self.seg_dir, self.combined_dir]:
            dir_path.mkdir(exist_ok=True)
        
        # Log file for processing details
        self.log_file = self.output_dir / "processing_log.txt"

    def generate_verification_code(self, image_path, processed_image):
        """Generate a unique verification code based on image content and processing time"""
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        image_hash = hashlib.md5(processed_image.tobytes()).hexdigest()[:8]
        return f"PROC_{timestamp}_{image_hash}"

    def segment_colonies(self, image):
        """
        Segment colonies from the background
        
        Args:
            image (numpy.ndarray): Input image
            
        Returns:
            numpy.ndarray: Binary mask of segmented colonies
        """
        # Convert to grayscale if not already
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image.copy()
        
        # Apply Gaussian blur to reduce noise
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
        # Use Otsu's method for adaptive thresholding
        threshold = filters.threshold_otsu(blurred)
        binary = (blurred > threshold).astype(np.uint8) * 255
        
        # Remove small noise using morphological operations
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        cleaned = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
        
        return cleaned

    def create_combined_image(self, original, segmented):
        """Create a side-by-side comparison image"""
        # Ensure segmented image is RGB if original is RGB
        if len(original.shape) == 3:
            segmented_rgb = cv2.cvtColor(segmented, cv2.COLOR_GRAY2BGR)
        else:
            segmented_rgb = segmented
            
        # Create side-by-side comparison
        return np.hstack((original, segmented_rgb))

    def save_metadata(self, metadata, metadata_path):
        """Save metadata as a JSON file"""
        with open(metadata_path, 'w') as f:
            json.dump(metadata, f, indent=4)

    def log_processing(self, log_message):
        """Append a processing message to the log file"""
        with open(self.log_file, 'a') as log:
            log.write(log_message + "\n")

    def process_single_image(self, image_path):
        """Process a single image and save all required outputs"""
        # Read image
        image = cv2.imread(str(image_path))
        if image is None:
            raise ValueError(f"Could not read image: {image_path}")
            
        # Get base filename
        base_name = image_path.stem
        
        # 1. Save original image
        orig_path = self.orig_dir / f"{base_name}_original.png"
        cv2.imwrite(str(orig_path), image)
        
        # 2. Create and save segmented image
        segmented = self.segment_colonies(image)
        seg_path = self.seg_dir / f"{base_name}_segmented.png"
        cv2.imwrite(str(seg_path), segmented)
        
        # 3. Create and save combined image
        combined = self.create_combined_image(image, segmented)
        combined_path = self.combined_dir / f"{base_name}_combined.png"
        cv2.imwrite(str(combined_path), combined)
        
        # 4. Generate verification code
        verification_code = self.generate_verification_code(image_path, segmented)
        
        # 5. Save metadata
        metadata = {
            'original_path': str(orig_path),
            'segmented_path': str(seg_path),
            'combined_path': str(combined_path),
            'verification_code': verification_code
        }
        metadata_path = self.output_dir / f"{base_name}_metadata.json"
        self.save_metadata(metadata, metadata_path)
        
        # 6. Log the processing
        log_message = f"Processed {image_path.name} - Verification Code: {verification_code}"
        self.log_processing(log_message)
        
        return metadata

    def process_all_images(self):
        """Process all images in the input directory"""
        results = []
        image_extensions = {'.jpg', '.jpeg', '.png', '.tif', '.tiff'}
        
        for image_path in self.input_dir.glob('*'):
            if image_path.suffix.lower() in image_extensions:
                try:
                    result = self.process_single_image(image_path)
                    results.append(result)
                    print(f"Successfully processed: {image_path.name}")
                    print(f"Verification code: {result['verification_code']}")
                except Exception as e:
                    print(f"Error processing {image_path.name}: {str(e)}")
        
        return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process colony images.")
    parser.add_argument("--input_dir", required=True, help="Directory containing input images")
    parser.add_argument("--output_dir", required=True, help="Directory to save processed images")
    args = parser.parse_args()

    print("==========================Image Processing Started=========================")
    processor = ColonyImageProcessor(input_dir=args.input_dir, output_dir=args.output_dir)
    results = processor.process_all_images()
    print("==========================Image Processing Complete=========================")
