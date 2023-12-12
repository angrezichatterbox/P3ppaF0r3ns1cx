from PIL import Image
def exiftool():
    image_path = input("Enter the path of the image 🎆 ")

    img = Image.open(image_path)
    width, height = img.size
    format_type = img.format
    mode = img.mode
    print(f"Image Details: Width = {img.width}px, Height = {img.height}px, Format = {img.format}, Mode = {img.mode}")
exiftool()