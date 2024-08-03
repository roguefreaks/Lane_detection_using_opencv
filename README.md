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
