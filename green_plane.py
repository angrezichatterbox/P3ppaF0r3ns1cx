import cv2
import numpy as np

def extract_green_bit_planes(image_path):
    # Read the image
    img = cv2.imread(image_path)

    # Ensure the image is not None
    if img is None:
        print("Error: Image not loaded.")
        return

    # Split the image into its color channels (BGR order)
    _, green_channel, _ = cv2.split(img)

    # Extract the individual bit planes for the blue channel
    green_bit_planes = [cv2.bitwise_and(green_channel, 1 << i) * 255 for i in range(8)]

    # Create a blue-tinted image for visualization
    #blue_tinted_planes = [cv2.merge([plane, np.zeros_like(blue_channel), np.zeros_like(blue_channel)]) for plane in blue_bit_planes]

    # Display the original image and the blue bit planes
    cv2.imshow('Original Image', img)
    
    for i, tinted_plane in enumerate(green_bit_planes):
        cv2.imshow(f'green Bit Plane {i}', tinted_plane)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
image_path = 'sample2.png'
extract_green_bit_planes(image_path)