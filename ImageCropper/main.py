from PIL import Image
import os

# Folder containing images to crop
folder_path = '/Users/pranavkulkarni/Desktop/ImageCropper/Raw '
edited_images_path = '/Users/pranavkulkarni/Desktop/ImageCropper/Cropped'
# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if  filename.endswith('.png'):
        # Open image using Pillow library
        img = Image.open(os.path.join(folder_path, filename))
        
        # Get dimensions of the image
        width, height = img.size
        
        # Crop the image into four equal parts
        cropped_imgs = []
        crop_width = width // 2
        crop_height = height // 2
        for i in range(2):
            for j in range(2):
                left = i * crop_width
                top = j * crop_height
                right = left + crop_width
                bottom = top + crop_height
                cropped_imgs.append(img.crop((left, top, right, bottom)))
        
        # Save cropped images
        for i, cropped_img in enumerate(cropped_imgs):
            cropped_img.save(os.path.join(edited_images_path, f'{i+1}_{filename}'))
