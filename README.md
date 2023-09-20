# Recognizing Elevator Number

## Overview

The Elevator Number Recognizing Program is designed to capture images of elevator numbers using the Raspberry Pi Camera Module and accurately recognize those digits. This program leverages the capabilities of OpenCV and Tesseract OCR to enhance image processing and ensure reliable number recognition.


## Key Features

- **Image Capture:** The program utilizes the Raspberry Pi Camera Module (PiCamera) to capture images of elevator numbers.

- **Image Processing:** OpenCV plays a central role in image processing, enhancing OCR (Optical Character Recognition) accuracy by reducing noise and eliminating unnecessary elements in the image. The image processing pipeline includes grayscale conversion, Gaussian blur, thresholding(both Gaussian and Binary), and contour line detection.

- **OCR with Tesseract:** Tesseract OCR is employed to perform optical character recognition, specifically recognizing and extracting digits from the captured elevator number images. Tesseract is set to recognize and print only numeric digits, ensuring accurate and relevant output.


## Application Example

This Elevator Number Recognizing Program was originally employed in the "Dukgo: KMLA Dormitory Application" project. In this application, it served as a valuable feature, assisting users in determining the location of elevators within the dormitory. The program helped users make informed decisions about which elevator to take for the quickest access to their destination.

## Usage

For detailed instructions on how to use the program, set up the Raspberry Pi, and integrate it into your own projects or applications, please refer to the documentation provided in the repository.

## Acknowledgments

This program benefits from the capabilities of OpenCV and Tesseract OCR, powerful open-source libraries that contribute to its image processing and optical character recognition functionality.
