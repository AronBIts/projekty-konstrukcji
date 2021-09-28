from PIL import Image
import os
import PIL
import glob

images = [file for file in os.listdir() if file.endswith(('jpeg', 'png','jpg'))]
fixed_height = 420
for image in images:
    img = Image.open(image)
    height_percent = (fixed_height / float(img.size[1]))
    width_size = int((float(img.size[0]) * float(height_percent)))
    img.resize((width_size, fixed_height), PIL.img.NEAREST)
    img.save("resized_"+image, optimize=True, quality=100)