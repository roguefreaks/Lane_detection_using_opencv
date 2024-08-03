# Lane Detection Using OpenCV

## Project Overview

This project implements a lane detection system using OpenCV and Python. The system processes an input image to detect lane lines and highlight them. It utilizes several computer vision techniques including Canny edge detection, Hough Line Transform, and line averaging to achieve accurate lane detection.

## Features

- **Edge Detection:** Uses Canny edge detection to identify edges in the image.
- **Region of Interest:** Focuses on the region where lane lines are expected to be.
- **Hough Transform:** Detects lines in the image using the Hough Line Transform.
- **Line Averaging:** Computes the average lines for left and right lanes.
- **Visualization:** Combines the detected lanes with the original image for visualization.

## Installation

To run this project, you'll need Python and the required libraries. Follow these steps to set up the environment:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/roguefreaks/Lane_detection_using_opencv
2.Create and activate a virtual environment (optional but recommended):
 ## On macOS/Linux:
    python -m venv env
    source env/bin/activate
 ##  On Windows:
    python -m venv env
    env\Scripts\activate
##  Install the required dependencies:

    With the virtual environment activated, run:pip install opencv-python numpy matplotlib
##  Prepare your image:

    Place an image file named test_image.jpg in the project directory. If you use a different filename, make sure to update the script with the correct filename.
##  Code Explanation:-
    canny(image): Applies Canny edge detection to the input image.
    region_of_interest(image): Masks the image to focus on the region where lanes are typically found.
    average_of_slope_intercept(image, lines): Averages the slope and intercept of detected lines to get a smooth lane line.
    display_lines(image, lines): Draws the detected lane lines on a blank image.
    make_coordinates(image, line_parameters): Converts the line parameters into coordinates for drawing on the image.
##  Contributing:-
    Feel free to contribute to this project by submitting issues, suggestions, or pull requests. Make sure to follow the coding standards and include appropriate tests for any new features.
##  Acknowledgements:-
    OpenCV for computer vision functionalities.
    NumPy for numerical operations.
    Matplotlib for plotting.


