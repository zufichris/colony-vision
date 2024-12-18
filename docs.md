# Colony Vision: Image Segmentation project

## Introduction
The **Colony Image Processing** project is designed to address the challenge of automating the analysis of colonies on microscopy images. The solution emphasizes precision, consistency, and scalability, making it an excellent tool for research labs, diagnostic facilities, and educational purposes.

## Problem Statement
This project processes a dataset of **26 colony images** by performing **image segmentation** to isolate colonies. It ensures the outputs meet specific deliverables:
1. **Original Images** remain unaltered.
2. **Segmented Images** highlight individual colonies.
3. **Combined Images** provide a side-by-side comparison of the original and segmented images.
4. Unique **Verification Codes** confirm processing integrity for each image.

The key requirements:
- Preserve the original image resolution across all outputs.
- Automate the pipeline to deliver 78 images (26 originals, 26 segmented, 26 combined) within a strict **4-day deadline**.

---

## Solution Overview
The project is powered by a Python-based script that employs efficient image processing techniques, ensuring high-quality outputs. Here's a summary of its features:

### Key Functionalities
1. **Colony Segmentation**: Uses adaptive thresholding (Otsu's method) combined with morphological operations to isolate colonies from the background.
2. **Side-by-Side Comparison**: Generates a visual comparison between the original and processed images.
3. **Metadata Logging**: Creates JSON files with paths, unique verification codes, and processing details for each image.
4. **Automation**: Processes all images in batch mode, ensuring timely delivery.
5. **Traceability**: Maintains a detailed log of actions for reproducibility and debugging.

### Core Technologies
- **Python Libraries**: OpenCV, NumPy, scikit-image.
- **Image Processing Techniques**: Grayscale conversion, Gaussian blurring, adaptive thresholding, and noise reduction.

---

## Workflow

### 1. Image Segmentation
The algorithm:
- Converts images to grayscale for uniformity.
- Reduces noise with Gaussian blur.
- Applies Otsu's thresholding to segment colonies.
- Refines results using morphological operations to remove small artifacts.

### 2. Image Outputs
Three types of images are generated:
- **Original Images**: Saved without modifications.
- **Segmented Images**: Binary masks highlighting colonies.
- **Combined Images**: Side-by-side visual comparisons.

### 3. Metadata and Logs
Each processed image generates:
- A **JSON metadata file** with file paths and a unique verification code.
- An entry in a **log file** documenting processing details.

### 4. Verification Codes
Each code combines:
- A timestamp for temporal traceability.
- A hash of the segmented image for uniqueness.

---

## Code Implementation

The project code is modular and structured for scalability:
- **Initialization**: Sets up input/output directories and creates subdirectories for organized outputs.
- **Segmentation Logic**: Encapsulated in the `segment_colonies()` function, which applies the image processing pipeline.
- **Automation**: The `process_all_images()` method processes all images in the input directory.
- **Error Handling**: Logs errors for unsupported formats or corrupted files, ensuring smooth execution.

---

## Outputs

### Directory Structure
The output directory contains:
```
output/
├── combined/        # Side-by-side images
├── original/        # Original images
├── segmented/       # Segmented images
├── metadata.json    # Metadata for each image
└── processing_log.txt  # Logs processing actions
```

### Metadata Example
A JSON file (`image1_metadata.json`) contains:
```json
{
    "original_path": "./output/original/image1_original.png",
    "segmented_path": "./output/segmented/image1_segmented.png",
    "combined_path": "./output/combined/image1_combined.png",
    "verification_code": "PROC_20241117213045_1a2b3c4d"
}
```

---

## Usage Instructions

### Prerequisites
- **Python 3.7+**
- Libraries: Install dependencies via:
  ```bash
  pip install -r requirements.txt
  ```

### Running the Script
Run the script using:
```bash
python main.py --input_dir <path_to_input_images> --output_dir <path_to_output_dir>
```

### Example
```bash
python main.py --input_dir ./images/input --output_dir ./images/output
```

---

## Scalability and Customization

### Extensibility
- **Advanced Segmentation**: Replace `segment_colonies()` with custom algorithms for more complex datasets.
- **Parallel Processing**: Incorporate multiprocessing to handle larger datasets efficiently.
- **Visualization Enhancements**: Add additional outputs like 3D plots or quantitative analysis.

### Troubleshooting
| Issue                       | Solution                                                                |
|-----------------------------|------------------------------------------------------------------------|
| **Image not found error**    | Check if `--input_dir` path exists and contains supported image files. |
| **Empty output directory**   | Review `processing_log.txt` for error details.                        |
| **Unsupported file format**  | Ensure files are `.jpg`, `.png`, `.tif`, or `.tiff`.                  |

---

## Conclusion

The **Colony Image Processing** project is a robust and flexible tool tailored for image segmentation tasks in scientific and research applications. By automating tedious workflows and ensuring high-quality outputs, it empowers users to focus on insights rather than manual image analysis. For further inquiries or contributions, visit the [GitHub repository](https://github.com/zufichris/colony-vision).
