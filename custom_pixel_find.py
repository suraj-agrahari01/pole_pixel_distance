import cv2
import numpy as np
import math

# Global variables to store clicked points and distance
clicked_points = []
distance = 0

# Function to save clicked points and distance to a file


def save_coordinates_to_file(file_name, points, distance):
    with open(file_name, 'w') as file:
        file.write(f'Point 1: {points[0]}\n')
        file.write(f'Point 2: {points[1]}\n')
        file.write(f'Pixel length: {distance}\n')

# Function to calculate distance between two points


def calculate_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Function to handle mouse click events


def click_event(event, x, y, flags, params):
    global clicked_points, distance

    # Checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        # Add the clicked point to the list
        clicked_points.append((x, y))

        # Draw a circle at the clicked point
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

        # If two points are clicked, draw a line between them and calculate distance
        if len(clicked_points) == 2:
            # Draw a line between the clicked points
            cv2.line(img, clicked_points[0], clicked_points[1], (0, 0, 255), 2)

            # Calculate distance between the two points
            distance = calculate_distance(clicked_points[0], clicked_points[1])

            # Display the distance on the image
            midpoint = ((clicked_points[0][0] + clicked_points[1][0]) //
                        2, (clicked_points[0][1] + clicked_points[1][1]) // 2)
            cv2.putText(img, f'pixel length: {distance:.2f}', midpoint,
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            # Display both points
            cv2.putText(img, f'Point 1: {clicked_points[0]}', (
                clicked_points[0][0], clicked_points[0][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            cv2.putText(img, f'Point 2: {clicked_points[1]}', (
                clicked_points[1][0], clicked_points[1][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            # Save the clicked points and distance to a file
            save_coordinates_to_file(
                'point_distance.txt', clicked_points, distance)


# Read the input image
img = cv2.imread(
    r'C:\Users\suraj\Desktop\pole_project\mask_testing\send\mask_img_segment.jpeg')

# # Resize the image
# img = cv2.resize(img, (img.shape[1] // 1, img.shape[0] // 1))

# Create a window
cv2.namedWindow('Point Distance')

# Bind the callback function to window
cv2.setMouseCallback('Point Distance', click_event)

# Display the image
while True:
    cv2.imshow('Point Distance', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
