# 🎨 Color Detection Tool using OpenCV and Pandas

A simple Python project built during high school that allows users to detect the color name of any pixel in an image using OpenCV and a custom color dataset.

## 🧠 Overview
This project marked my first hands-on experience with image processing, pixel analysis, and color recognition in Python.

When you double-click anywhere on the image window, the program reads the pixel’s RGB values and matches it to the closest color name in a CSV file.
 
--- 
 
## 🔧 Technologies / Topics

- Python  
- OpenCV
- pandas 
- argparse
---

## ⚙️ How to Use

1. **Open your terminal (or Command Prompt), navigate to the project folder, and run:**

   ```bash
   python color_detection.py -i <image_path> -a <image_format>
   ```

   Example:

   ```bash
   python color_detection.py -i a.jpg -a jpg
   ```

   **Arguments:**

   - `-i` → Path to the image file (e.g., `a.jpg`, `b.png`)
   - `-a` → Image format (e.g., `jpg`, `png`)

2. **After the program runs, you can perform the following actions:**

   - **Double Left Click** on any part of the image: detects and displays the RGB value and closest color name.

   - **Right Click**: optional, may be used to exit or reset.

   - **Enter Key**: optional, may trigger save or exit (if implemented).

---

## 📷 Preview

https://github.com/user-attachments/assets/4f99145c-2adb-4803-879d-4915cae2e512


---
