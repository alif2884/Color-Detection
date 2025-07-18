# 🎨 Color Detection Tool (High School Project)
This is a simple Python program I created in high school to detect the color of a pixel when you click on it in an image.  
It shows the closest color name and its RGB values using OpenCV and pandas.

---

## 🔧 Requirements
- Python 3.x  
- `opencv-python`  
- `pandas`  
- A `colors.csv` file containing color names and RGB values (already included in this repo)

Install the required packages using:
pip install opencv-python pandas

### ▶️ How to Run
Open your terminal (or Command Prompt), navigate to the project folder, and run:
python color_detection.py -i <image_path> -a <image_format>

Arguments:
-i → Path to the image file (e.g., a.jpg, b.png)
-a → Image format (e.g., jpg, png)

#### 🖱️ How to Use
Double Left Click on any part of the image: detects and displays the RGB value and closest color name.
Right Click: optional, may be used to exit or reset.
Enter Key: optional, may trigger save or exit (if implemented).

##### 📁 Example
python color_detection.py -i a.jpg -a jpg

###### 🧠 What I Learned
Working with images in Python using OpenCV
Reading and searching color datasets using pandas
Handling mouse events and CLI arguments
Building small interactive tools with real-world applications
