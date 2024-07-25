import cv2
import numpy as np
import os

# Function to read coordinates from file


def read_coordinates_from_file(file_name):
    coordinates = []
    with open(file_name, 'r') as file:
        for line in file:
            x, y = map(float, line.strip('\n').split(','))
            coordinates.append((x, y))
            print(coordinates)
    return coordinates

# Function to mask image based on coordinates


def mask_image(image, coordinates):
    mask = np.zeros_like(image[:, :, 0])
    pts = np.array(coordinates, np.int32)
    cv2.fillPoly(mask, [pts], (255, 255, 255))
    masked_image = cv2.bitwise_and(image, image, mask=mask)
    return masked_image


# Create output directory if it doesn't exist
output_dir = 'test_result'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Read coordinates from file
coordinates = read_coordinates_from_file('coordinate_mask_file.txt')

# Read and process images from folder
input_folder = 'test'
for filename in os.listdir(input_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        img_path = os.path.join(input_folder, filename)
        img = cv2.imread(img_path)
        masked_img = mask_image(img, coordinates)
        output_path = os.path.join(output_dir, filename)
        cv2.imwrite(output_path, masked_img)
        print(f"Masked image saved: {output_path}")
