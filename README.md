# 🎨 Color Detection Tool (High School Project)

This is a simple Python program I created in high school to detect the color of a pixel when you click on it in an image.  
It shows the closest color name and its RGB values using OpenCV and pandas.

## 🔧 Requirements

- Python 3.x
- `opencv-python`
- `pandas`
- A `colors.csv` file containing color names and RGB values (already included in this repo)

Install the required packages using pip:

```bash
pip install opencv-python pandas
▶️ How to Run
Open your terminal (or Command Prompt), navigate to the project directory, and run:

bash
Copy
Edit
python color_detection.py -i <image_path> -a <image_format>
Arguments:

-i → Path to the image file (e.g., a.jpg, b.png)

-a → Image format (e.g., jpg, png)

🖱️ How to Use the Program
Double Left Click: Detects the RGB values of the selected pixel and shows the closest color name.

Right Click: (Optional) Used for clearing or exiting depending on implementation.

Enter Key: May be used to confirm or save (optional feature).

📁 Example
bash
Copy
Edit
python color_detection.py -i a.jpg -a jpg
🧠 What I Learned
How to work with images in Python using OpenCV

How to read and search color datasets using pandas

How to handle mouse events and command-line arguments

How to build a small but interactive and useful tool
