# Colony Image Processor Documentation
**[View Problem](https://github.com/colony-vision/README.md)**
## Overview

The **Colony Image Processor** is a Python-based utility for processing microscopy images of colonies. It supports segmentation, generating side-by-side comparisons, and metadata logging. The script is customizable via command-line arguments, making it versatile for various workflows.

---

## Features

1. **Colony Segmentation**  
   Automatically segments colonies from the background using adaptive thresholding (Otsu's method) and noise reduction.

2. **Image Comparison**  
   Generates a side-by-side comparison of the original and segmented images.

3. **Metadata Generation**  
   Creates a JSON metadata file for each image, including the file paths and a unique verification code.

4. **Logging**  
   Logs processing details into a text file for easy traceability.

5. **Command-Line Arguments**  
   Fully customizable input/output directories using `--input_dir` and `--output_dir` options.

---

## Installation

### Prerequisites

Ensure you have the following installed:
- Python 3.7+
- Pip

### Install Required Libraries

Run the following command to install dependencies:
```bash
pip install numpy opencv-python scikit-image
```

---

## Usage

### Command-Line Syntax

```bash
python ./main.py --input_dir <path_to_input_images> --output_dir <path_to_output_dir>
```

### Example

```bash
python ./main.py --input_dir ./images/input --output_dir ./images/output
```

### Arguments

| Argument      | Required | Description                                   |
|---------------|----------|-----------------------------------------------|
| `--input_dir` | Yes      | Directory containing input images to process. |
| `--output_dir`| Yes      | Directory where processed images will be saved.|

---

## Outputs

After processing, the script generates the following outputs in the `output_dir`:

1. **Original Images**  
   Saved in the `original/` subdirectory.

2. **Segmented Images**  
   Binary masks of the segmented colonies saved in `segmented/`.

3. **Combined Images**  
   Side-by-side comparisons saved in `combined/`.

4. **Metadata**  
   JSON files with metadata for each processed image:
   ```json
   {
       "original_path": "./output/original/image1_original.png",
       "segmented_path": "./output/segmented/image1_segmented.png",
       "combined_path": "./output/combined/image1_combined.png",
       "verification_code": "PROC_20241117213045_1a2b3c4d"
   }
   ```

5. **Processing Log**  
   A `processing_log.txt` file recording all processing actions:
   ```
   Processed image1.jpg - Verification Code: PROC_20241117213045_1a2b3c4d
   ```

---

## How It Works

1. **Initialization**  
   The processor sets up the input and output directories, creating subdirectories (`original/`, `segmented/`, `combined/`) as needed.

2. **Colony Segmentation**  
   - Converts images to grayscale.
   - Applies Gaussian blur to reduce noise.
   - Uses Otsu's thresholding to segment colonies.
   - Removes small artifacts with morphological operations.

3. **Side-by-Side Comparison**  
   Combines the original image and its segmentation result into one.

4. **Verification Code**  
   Generates a unique code for each processed image using:
   - The current timestamp.
   - A hash of the segmented image data.

5. **Metadata and Logs**  
   Outputs metadata as JSON files and appends processing details to a log file.

---

## Directory Structure

Example output directory structure:
```
output/
├── combined/
│   ├── image1_combined.png
│   └── image2_combined.png
├── original/
│   ├── image1_original.png
│   └── image2_original.png
├── segmented/
│   ├── image1_segmented.png
│   └── image2_segmented.png
├── image1_metadata.json
├── image2_metadata.json
└── processing_log.txt
```

---

## Development

### Project Structure

```
.
├── main.py            # Main script
├── requirements.txt   # Python dependencies
```

---

## Extending the Script

1. **Custom Segmentation**  
   Replace the `segment_colonies()` function to use alternative segmentation techniques.

2. **Additional Outputs**  
   Add new types of visualizations or metadata exports by extending `process_single_image()`.

3. **Parallel Processing**  
   Use libraries like `multiprocessing` or `concurrent.futures` to process images faster.

---

## Troubleshooting

| Issue                       | Solution                                                                 |
|-----------------------------|-------------------------------------------------------------------------|
| **Image not found error**    | Ensure the `--input_dir` path is correct and contains valid image files.|
| **Empty output directory**   | Check logs in `processing_log.txt` for specific error messages.         |
| **Unsupported image format** | Ensure input images are in `.jpg`, `.jpeg`, `.png`, `.tif`, or `.tiff`. |

---

## License

This project is licensed under the MIT License.

---

## Contributors

- **[Your Name]** - Developer
- Contributions welcome! Submit pull requests or open issues for new features or bug fixes.

---

## Support

For questions or feedback, feel free to [open an issue](https://github.com/colony-vision/issues).