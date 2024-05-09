import cv2
import numpy as np

# Global variable to store clicked points
clicked_points = []

# Function to save clicked points to a file


def save_coordinates_to_file(file_name, points):
    with open(file_name, 'w') as file:
        for point in points:
            file.write(f'{point[0]},{point[1]}\n')

# Function to display the coordinates of the points clicked on the image


def click_event(event, x, y, flags, params):
    global clicked_points

    # Checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        print('Left Click')
        print(f'({x},{y})')

        # Add the clicked point to the list
        clicked_points.append((x, y))

        # Put coordinates as text on the image
        cv2.putText(img, f'({x},{y})', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

        # If four points are clicked, draw a line joining them and mask the area
        if len(clicked_points) == 4:
            # Draw a line joining the clicked points
            for i in range(3):
                cv2.line(img, clicked_points[i],
                         clicked_points[i+1], (0, 255, 0), 2)
            # Draw a line between the first and last points to complete the square
            cv2.line(img, clicked_points[3], clicked_points[0], (0, 255, 0), 2)

            # Create a mask with same dimensions as the image
            mask = np.zeros_like(img[:, :, 0])

            # Create a polygon with the clicked points
            pts = np.array(clicked_points, np.int32)
            cv2.fillPoly(mask, [pts], (255, 255, 255))

            # Mask the area outside the polygon
            masked_img = cv2.bitwise_and(img, img, mask=mask)

            # Save the clicked points to a file
            save_coordinates_to_file(
                'coordinate_mask_file.txt', clicked_points)

            # Display the masked image
            cv2.imshow('Masked Image', masked_img)

    # Right mouse click event
    if event == cv2.EVENT_RBUTTONDOWN:
        print('Right Click')
        print(f'({x},{y})')

        # Add the clicked point to the list
        clicked_points.append((x, y))

        # Put coordinates as text on the image
        cv2.putText(img, f'({x},{y})', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)


# Read the input image
img = cv2.imread('frame0.jpg')

h, w, c = img.shape
img = cv2.resize(img, (w // 3, h // 3))


# Create a window
cv2.namedWindow('Point Coordinates')

# Bind the callback function to window
cv2.setMouseCallback('Point Coordinates', click_event)

# Display the image
while True:
    cv2.imshow('Point Coordinates', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
