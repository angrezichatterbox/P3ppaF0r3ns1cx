print("1.Blue Planes")
print("2. Data Insert")
print("3. exiftool")
print("4. Green Plane")
print("5. Red Plane")
print("7.XOR TWO IMAGES")
A = int(input())

if A == 1:
    import cv2
    import numpy as np
    import os 

    def extract_blue_bit_planes(image_path):
        # Read the image
        img = cv2.imread(image_path)

        # Ensure the image is not None
        if img is None:
            print("Error: Image not loaded.")
            return

        # Split the image into its color channels (BGR order)
        blue_channel, _, _ = cv2.split(img)

        # Extract the individual bit planes for the blue channel
        blue_bit_planes = [cv2.bitwise_and(blue_channel, 1 << i) * 255 for i in range(8)]

        # Create a blue-tinted image for visualization
        # blue_tinted_planes = [cv2.merge([plane, np.zeros_like(blue_channel), np.zeros_like(blue_channel)]) for plane in blue_bit_planes]

        # Display the original image and the blue bit planes
        cv2.imshow('Original Image', img)
        os.makedirs(os.path.join(f'{image_path}_bitplanes','blue'), exist_ok=True)
        for i, tinted_plane in enumerate(blue_bit_planes):
            cv2.imshow(f'Blue Bit Plane {i}', tinted_plane)
            cv2.imwrite(f'{image_path}_bitplanes/blue/_bit{i}.png', tinted_plane)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    image_path = input("Enter the path of Image")
    extract_blue_bit_planes(image_path)

elif A == 3 :
    from PIL import Image
    def exiftool():
        image_path = input("Enter the path of the image 🎆 ")

        img = Image.open(image_path)
        width, height = img.size
        format_type = img.format
        mode = img.mode
        print(f"Image Details: Width = {width}px, Height = {height}px, Format = {format_type}, Mode = {mode}")
    exiftool()

elif A ==4 :

    import cv2
    import numpy as np

    def extract_green_bit_planes(image_path):

        img = cv2.imread(image_path)


        if img is None:
            print("Error: Image not loaded.")
            return
        _, green_channel, _ = cv2.split(img)

        # Extract the individual bit planes for the blue channel
        green_bit_planes = [cv2.bitwise_and(green_channel, 1 << i) * 255 for i in range(8)]
        cv2.imshow('Original Image', img)
        
        for i, tinted_plane in enumerate(green_bit_planes):
            cv2.imshow(f'green Bit Plane {i}', tinted_plane)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

  
    image_path = input("Enter the path of Image")
    extract_green_bit_planes(image_path)    

elif A ==5 :
    import cv2
    import numpy as np

    def extract_red_bit_planes(image_path):

        img = cv2.imread(image_path)


        if img is None:
            print("Error: Image not loaded.")
            return
        _, _, red_channel = cv2.split(img)
        red_bit_planes = [cv2.bitwise_and(red_channel, 1 << i) * 255 for i in range(8)]
        red_tinted_planes = [cv2.merge([np.zeros_like(red_channel), np.zeros_like(red_channel), plane]) for plane in red_bit_planes]
        cv2.imshow('Original Image', img)
        
        for i, tinted_plane in enumerate(red_tinted_planes):
            cv2.imshow(f'Red Bit Plane {i}', tinted_plane)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    image_path = input("Enter Image Path")
    extract_red_bit_planes(image_path)

elif A == 2 :
    def append_data_to_png(file_path, data_to_append):
        with open(file_path, 'rb') as file:
            png_data = file.read()

        # Find the index of the IEND chunk
        iend_index = png_data.rfind(b'IEND') + 4

        if iend_index == -1:
            raise ValueError("No IEND chunk found in the PNG file.")
        # Convert additional data to bytes if it's not already
        if not isinstance(data_to_append, bytes):
            data_to_append = data_to_append.encode('utf-8')  # or use the appropriate encoding
        # Append your data after the IEND chunk
        new_png_data = png_data[:iend_index] + data_to_append + png_data[iend_index:]
        # Write the modified data back to the file
        with open('modified.png', 'wb') as modified_file:
            modified_file.write(new_png_data)
    file_path = input("Enter path")
    data_to_append = b'India'
    append_data_to_png(file_path, data_to_append)
"""
elif A == 7:
    import cv2
    input1 = input("Enter path of image 1")
    input2 = input("Enter path of image 2")
    img1 = cv2.imread(input1)
    img2 = cv2.imread(input2)

    # compute bitwise XOR on both images
    xor_img = cv2.bitwise_xor(img1,img2)

    # display the computed bitwise XOR image
    cv2.imshow('Bitwise XOR Image', xor_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
else:
    print("Please Enter an option which matches which the labelling")
"""