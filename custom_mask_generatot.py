import cv2
import numpy as np

# Global variable to store clicked points
clicked_points = []
ratio = 0
# Function to save clicked points to a file


def save_coordinates_to_file(file_name, points, original_size):
    global ratio
    img = cv2.imread('frame8150.jpg')

    print("img height : ", img.shape[1])
    print("img width : ", img.shape[0])

    # print("original : ", original_size[0])
    # print("orignal width ", original_size[1])

    with open(file_name, 'w') as file:
        for point in points:
            # Upscale the coordinates to the original size
            # (original_size[0] / img.shape[1]))
            x_upscaled = int(point[0] * ratio)
            # (original_size[1] / img.shape[0]))
            y_upscaled = int(point[1] * ratio)

            print("the upscale is ", x_upscaled, y_upscaled)
            file.write(f'{x_upscaled},{y_upscaled}\n')

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
            o_img = cv2.imread('frame8150.jpg')
            for i in range(3):
                cv2.line(img, clicked_points[i],
                         clicked_points[i+1], (0, 255, 0), 2)
                cv2.line(o_img, np.array(clicked_points[i]) * 3,
                         np.array(clicked_points[i+1]) * 3, (0, 255, 0), 2)
            # Draw a line between the first and last points to complete the square
            cv2.line(img, clicked_points[3], clicked_points[0], (0, 255, 0), 2)

            # Create a mask with the same dimensions as the image
            mask = np.zeros_like(img[:, :, 0])

            # Create a polygon with the clicked points
            pts = np.array(clicked_points, np.int32)
            cv2.fillPoly(mask, [pts], (255, 255, 255))

            # Mask the area outside the polygon
            masked_img = cv2.bitwise_and(img, img, mask=mask)

            # Save the clicked points to a file
            save_coordinates_to_file(
                'coordinate_mask_file.txt', clicked_points, (w, h))

            # Display the masked image
            cv2.imshow('Masked Image', masked_img)
            # cv2.imshow('origin ', cv2.resize(o_img, (1000, 1000)))

    # # Right mouse click event
    # if event == cv2.EVENT_RBUTTONDOWN:
    #     print('Right Click')
    #     print(f'({x},{y})')

    #     # Add the clicked point to the list
    #     clicked_points.append((x, y))

    #     # Put coordinates as text on the image
    #     cv2.putText(img, f'({x},{y})', (x, y),
    #                 cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    #     cv2.circle(img, (x, y), 3, (0, 0, 255), -1)


# Read the input image
img = cv2.imread('frame8150.jpg')

h, w, c = img.shape
img = cv2.resize(img, (w // 3, h // 3))
nh, nw, nc = img.shape
ratio = h/nh
print("h,w", h, w)

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
