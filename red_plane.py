import cv2
import numpy as np

def extract_red_bit_planes(image_path):
    # Read the image
    img = cv2.imread(image_path)

    # Ensure the image is not None
    if img is None:
        print("Error: Image not loaded.")
        return

    # Split the image into its color channels (BGR order)
    _, _, red_channel = cv2.split(img)

    # Extract the individual bit planes for the red channel
    red_bit_planes = [cv2.bitwise_and(red_channel, 1 << i) * 255 for i in range(8)]

    # Create a red-tinted image for visualization
    red_tinted_planes = [cv2.merge([np.zeros_like(red_channel), np.zeros_like(red_channel), plane]) for plane in red_bit_planes]

    # Display the original image and the red bit planes
    cv2.imshow('Original Image', img)

    for i, tinted_plane in enumerate(red_tinted_planes):
        cv2.imshow(f'Red Bit Plane {i}', tinted_plane)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
image_path = 'image.png'
extract_red_bit_planes(image_path)