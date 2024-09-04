# Virtual Paint Application

This Python project leverages OpenCV to create a virtual paint application. The application tracks colored objects using a webcam and allows users to draw on the screen in real-time. It detects specific colors and contours, mapping them to brush strokes that are displayed on the video feed.

## Features

- **Real-Time Color Detection:** Detects specific colors using the HSV color space.
- **Contour Detection:** Identifies the contour of the detected color and draws a bounding circle at the center.
- **Virtual Painting:** Draws on the screen based on the detected colors and their movements.
- **Customizable Colors:** Supports customization of color ranges and drawing colors.

## Requirements

- Python 3.x
- OpenCV
- NumPy

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/virtual-paint.git
