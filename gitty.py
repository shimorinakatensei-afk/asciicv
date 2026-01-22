import cv2
import numpy as np
import os
import sys

ASCII_CHARS = " .'`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

def resize_image(image, new_width):
    (original_height, original_width) = image.shape
    aspect_ratio = original_height / float(original_width)
    new_hight = int(aspect_ratio * new_width * 0.55)
    new_dim = (new_width, new_hight)
    return cv2.resize(image, new_dim)

def pixels_to_ascii(image):
    """Заменяем пиксели на символы"""

    pixels = image.flatten().astype(int)
    
  
    indices = (pixels * (len(ASCII_CHARS) - 1)) // 255
    
    ascii_str = "".join([ASCII_CHARS[int(index)] for index in indices])
    return ascii_str

def main():
   
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Не удалось открыть камеру")
        return

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
           
            resized_gray = resize_image(gray_frame, new_width=120)
            
            
            ascii_str = pixels_to_ascii(resized_gray)
            
            
            img_width = resized_gray.shape[1]
            ascii_img = "\n".join([ascii_str[i:(i+img_width)] for i in range(0, len(ascii_str), img_width)])
            
         
            sys.stdout.write("\033[H" + ascii_img)
            sys.stdout.flush()

            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except KeyboardInterrupt:
        pass
    finally:
        cap.release()
        cv2.destroyAllWindows()
        print("\nКамера выключена.")

if __name__ == "__main__":
    main()