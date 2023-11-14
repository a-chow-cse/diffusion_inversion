from PIL import Image
import os
import random

# Define the folder path containing the images
folder_path = '/home/chowdhury.150/Projects/cl_dm/diffusion_inversion/inversion_data/cifar100/scaling20_embd_32/res32_bicubic/class_068/tstep4500_infstep100_gs2.0_noise0.1_itep0.1_seed42'

# Get a list of image filenames in the folder
image_files = [f for f in os.listdir(folder_path) if f.endswith('.png')]
#image_files = random.sample(image_files, 100)

images = []


for image_file in image_files:
    image = Image.open(os.path.join(folder_path, image_file))
    images.append(image)

width, height = images[0].size

images_per_row = 4

num_rows = len(images) // images_per_row + (len(images) % images_per_row > 0)

combined_width = width * images_per_row
combined_height = height * num_rows
combined_image = Image.new('RGB', (combined_width, combined_height))

# Paste each image into the combined image, arranging them in rows
for i, image in enumerate(images):
    row = i // images_per_row
    col = i % images_per_row
    combined_image.paste(image, (col * width, row * height))

# Save the combined image
combined_image.save('./combined_image.png')