

import cv2
import os

# Read the video from specified path
video_path = "Video_20240628121724174.avi"
output_folder = 'fiber_folder'

cam = cv2.VideoCapture(video_path)

try:
    # creating a folder named output
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

except OSError:
    print('Error: Creating directory of output')

# Get the frame rate of the video
fps = cam.get(cv2.CAP_PROP_FPS)

# Calculate the frame capture frequency for 1 second
# Assuming frame rate is in frames per second
frame_capture_frequency = int(fps)

# Frame count
current_frame = 0

while (True):
    # Reading frame
    ret, frame = cam.read()

    if ret:
        # Checking if the current frame count is a multiple of the capture frequency
        # if current_frame % frame_capture_frequency == 0:
        #     # Creating the image name
        #     name = f'./{output_folder}/elephant_f{current_frame}.jpg'
        #     print('Creating...', name)

        #     # Writing the extracted image
        #     cv2.imwrite(name, frame)

        # # Incrementing the frame counter
        # current_frame += 1

        # Creating the image name
        name = f'./{output_folder}/fiber{current_frame}.jpg'
        print('Creating...', name)

        # Writing the extracted image
        cv2.imwrite(name, frame)

        # Incrementing the frame counter
        current_frame += 1
    else:
        break

# Releasing resources
cam.release()
cv2.destroyAllWindows()
