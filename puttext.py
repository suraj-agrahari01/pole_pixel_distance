import cv2
import os

# Define the file path
file_path = 'pixel_distance .jpg'

# Check if the file exists
if not os.path.isfile(file_path):
    print(f"Error: File '{file_path}' does not exist.")
else:
    # Read the image
    img = cv2.imread(file_path)

    # Check if the image is loaded successfully
    if img is None:
        print(f"Error: Unable to read the image '{file_path}'.")
    else:
        # Add text to the image
        cv2.putText(img, f'Length: 8.99m ', (350, 400),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

        cv2.imwrite('result.jpg', img)

        # Display or save the modified image
        cv2.imshow('Image with text', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
