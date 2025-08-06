# 🎨 Color Detection Tool using OpenCV and Pandas

A simple image processing tool in Python that identifies the name of any color in an image by clicking on pixels — built using OpenCV, Pandas, and a custom color dataset.

---

## 🧠 Overview

This project was my first practical dive into image processing and color recognition.  
The goal was to interactively analyze image pixels and map their RGB values to known color names using a CSV dataset.  
It introduced me to concepts like event handling, coordinate tracking, and real-time GUI feedback in OpenCV.

---

## 🔎 Features

- Real-time color name detection by double-clicking on any pixel
- RGB value extraction from image regions
- Matching closest color from dataset
- Interactive image window with user input
- Command-line arguments for image selection

---

## 🔧 Technologies / Topics

- Python
- OpenCV
- Pandas
- argparse
- CSV-based color dataset

---

## ⚙️ How to Use

1. Clone the repo and navigate to the project folder.
2. Run the script with the following command:

   ```bash
   python color_detection.py -i <image_path> -a <image_format>
   ```

   Example:

   ```bash
   python color_detection.py -i a.jpg -a jpg
   ```

3. Interaction:

   - **Double Left Click** → Detects and displays RGB value + closest color name

   - **Right Click / Enter** → May exit or reset (depending on implementation)

---

## 📂 Files

- ```color_detection.py``` – Main script for running the application

- ```colors.csv``` – Dataset mapping RGB values to color names

- Sample images (optional)

---

## 📷 Preview

https://github.com/user-attachments/assets/4f99145c-2adb-4803-879d-4915cae2e512

---

## 📎 Notes

- Make sure all dependencies (```opencv-python```, ```pandas```) are installed.

- The CSV file should remain in the same directory as the script.

- Originally created as a high school project to explore OpenCV and color theory.
