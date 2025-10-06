import cv2
import numpy as np

def apply_filter(image, filter_type):
    filtered_image = image.copy()

    if filter_type == "red_tint":
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 0] = 0
    elif filter_type == "green_tint":
        filtered_image[:, :, 0] = 0
        filtered_image[:, :, 2] = 0
    elif filter_type == "blue_tint":
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 2] = 0
    elif filter_type == "sobel":
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
        combined_sobel = cv2.bitwise_or(
            sobelx.astype('uint8'),
            sobely.astype('uint8')
        )
        filtered_image = cv2.cvtColor(combined_sobel, cv2.COLOR_GRAY2BGR)
    elif filter_type == "canny":
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray_image, 100, 200)
        filtered_image = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    return filtered_image


# Load an image
image_path = 'C://Users//DELL//OneDrive//Pictures//Documents//Desktop//AI//Intro_to_Computer_Vision___OpenCV_asset-e753 (2)//example.jpg'
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found!")
else:
    filter_type = "original"

    print("Press the following keys to apply filters:")
    print("r - Red Tint")
    print("g - Green Tint")
    print("b - Blue Tint")
    print("s - Sobel Edge Detection")
    print("c - Canny Edge Detection")
    print("q - Quit")

    while True:
        # Apply current filter
        if filter_type == "original":
            display_image = image.copy()
        else:
            display_image = apply_filter(image, filter_type)

        # Display the image
        cv2.imshow("Image Filter", display_image)

        # Wait for a key press
        key = cv2.waitKey(0) & 0xFF

        # Map key presses to filters
        if key == ord('r'):
            filter_type = "red_tint"
        elif key == ord('g'):
            filter_type = "green_tint"
        elif key == ord('b'):
            filter_type = "blue_tint"
        elif key == ord('s'):
            filter_type = "sobel"
        elif key == ord('c'):
            filter_type = "canny"
        elif key == ord('q'):
            print("Exiting...")
            break
        else:
            print("Invalid key! Please use 'r', 'g', 'b', 's', 'c', or 'q'.")

    cv2.destroyAllWindows()
