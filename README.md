# 📹 Terminal ASCII Video Player

A real-time video rendering engine that converts webcam feed (or video files) into ASCII art directly in the terminal window. Built with Python, OpenCV, and NumPy.

## 🚀 How It Works

The program processes video frames using a computer vision pipeline:

1.  **Frame Capture**: Uses `OpenCV` to grab raw frames from the webcam.
2.  **Grayscale Conversion**: Converts the frame to grayscale (`cv2.COLOR_BGR2GRAY`) since ASCII representation relies on luminance (brightness), not color.
3.  **Resizing**: Downscales the image to fit the terminal window while correcting the aspect ratio (since terminal characters are typically twice as tall as they are wide).
4.  **Pixel-to-ASCII Mapping**:
    * Utilizes **NumPy vectorization** instead of slow Python loops for performance.
    * Maps pixel brightness (0-255) to a specific index in a character string (e.g., ` .:-=+*#%@`).
    * Formula used: `index = (pixel_value * (len(chars) - 1)) // 255`.
5.  **Rendering**: Flushes the standard output buffer frame-by-frame to create a smooth animation effect.

## 🛠️ Tech Stack

* **Python 3.10+**
* **OpenCV (`cv2`)**: For video capture and image manipulation.
* **NumPy**: For high-performance matrix operations on image data.

## 📦 Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/shimorinakatensei-afk/asciicv](git clone https://github.com/shimorinakatensei-afk/asciicv.git)
    cd ascii-video-player
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the player:**
    ```bash
    python main.py
    ```
    *Press `q` to exit the application.*

## 🧮 Code Highlight

Efficiently mapping pixels to characters using NumPy (no `for` loops):

```python
# Vectorized mapping of 0-255 pixel values to ASCII character indices
indices = (pixels * (len(ASCII_CHARS) - 1)) // 255
ascii_str = "".join([ASCII_CHARS[int(index)] for index in indices])
