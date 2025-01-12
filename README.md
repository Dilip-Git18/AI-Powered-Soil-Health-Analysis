# AI-Powered-Soil-Health-Analysis

This project analyzes soil conditions from images and provides corresponding preventive measures based on the soil's characteristics. By processing the soil image, it categorizes the soil condition and generates recommendations to help improve soil quality and health.

## Features

- **Image Preprocessing**: The image is resized, converted to grayscale, and normalized for consistent analysis.
- **Soil Condition Analysis**: Based on pixel intensity, the program identifies various soil conditions (e.g., Wet, Dry, Moist, Flooded, etc.).
- **Preventive Measures**: Provides actionable recommendations to improve soil health depending on the identified condition.
- **File Output**: A text file is generated containing the soil condition and preventive measures, saved in a `solutions` folder.
- **Visualization**: The original image and its grayscale version are displayed for better understanding and analysis.

## Execution Instructions

1. **Prepare Image**: Place an image of the soil in project directory.
2. **Run the Code**: Call the `main(image_path)` function with the path to your image.
3. **View Results**: The program will display the soil condition, and a text file with preventive measures will be saved in the `solutions` folder.

### Example Output:

- **Soil Condition**: Dry Soil
- **Preventive Measures**:
    - Increase irrigation frequency and use drip irrigation to ensure water reaches plant roots.
    - Add organic matter to improve moisture retention.
    - Monitor soil moisture to avoid both overwatering and underwatering.

## Technologies Used

- **OpenCV**: For image processing and manipulation.
- **NumPy**: For numerical calculations and matrix operations.
- **Matplotlib**: For visualizing the image and analysis results.

## Installation

To install the required dependencies, you can use `pip`:

```bash
pip install opencv-python numpy matplotlib
