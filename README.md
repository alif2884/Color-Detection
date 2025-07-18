# 🎨 Color Detection Tool (High School Project)
This is a simple Python program that detects the color of a pixel when you click on it in an image. It shows the closest color name and RGB values using OpenCV.

## 🔧 Requirements
- Python 3.x
- OpenCV (`cv2`)
- pandas
- A `colors.csv` file containing color names and RGB values (already included)

You can install the dependencies with:
```bash
pip install opencv-python pandas

▶️ How to Run
Open your terminal or command prompt and run the script using the following format:
python color_detection.py -i <image_path> -a <image_format>

-i: Path to the image file (e.g., a.jpg, b.png)
-a: Image format (e.g., jpg, png)

🖱️ How to Use
Double Left Click on the image: detects the RGB color of the selected pixel.
Right Click: optionally clear or exit (if implemented).
Enter key: may be used to confirm or save (depending on version).

📁 Example:
python color_detection.py -i a.jpg -a jpg

🧠 What I Learned
Working with images in Python using OpenCV
Reading and searching CSV datasets with pandas
Handling mouse events and CLI arguments
Designing simple but interactive tools
