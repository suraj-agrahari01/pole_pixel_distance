import cv2
import numpy as np


def crop_masked_image(masked_image, roi):
    cropped_image = masked_image[roi[1]
        :roi[1] + roi[3], roi[0]:roi[0] + roi[2]]
    return cropped_image


def adjust_img(orgi_image):
    h, w, c = orgi_image.shape
    letterboxed_image = cv2.resize(orgi_image, (w // 3, h // 3))
    return letterboxed_image


def select_roi(image):
    r = cv2.selectROI("Select the area", image)
    cv2.destroyWindow("Select the area")
    return r


def upscale_coordinates(coord, original_size, letterbox_size):
    ratio_x = original_size[1] / letterbox_size[1]
    ratio_y = original_size[0] / letterbox_size[0]
    coord_upscaled = [int(coord[0] * ratio_x), int(coord[1] * ratio_y),
                      int(coord[2] * ratio_x), int(coord[3] * ratio_y)]
    return coord_upscaled


def create_mask(image, roi):
    mask = np.zeros_like(image)
    cv2.rectangle(mask, (roi[0], roi[1]), (roi[0] +
                  roi[2], roi[1] + roi[3]), (0, 0, 0), -1)
    return mask


def apply_mask(original_image, mask):
    mask_inv = cv2.bitwise_not(mask)
    masked_image = cv2.bitwise_and(original_image, mask_inv)
    return masked_image


def save_coordinates(coordinates, filename):
    with open(filename, 'w') as f:
        for coord in coordinates:
            f.write(','.join(map(str, coord)) + '\n')


def main():
    original_image = cv2.imread('frame8150.jpg')
    adjust_image = adjust_img(original_image)
    selected_roi = select_roi(adjust_image)

    save_coordinates([selected_roi], 'roi_coordinates.txt')

    upscaled_roi = upscale_coordinates(
        selected_roi, original_image.shape[:2], adjust_image.shape[:2])

    save_coordinates([upscaled_roi], 'upscaled_coordinates.txt')

    mask = create_mask(original_image, upscaled_roi)
    masked_image = apply_mask(original_image, mask)
    if masked_image.shape[0] > 0 and masked_image.shape[1] > 0:
        cv2.imwrite('Masked.jpg', masked_image)

    cropped_image = crop_masked_image(original_image, upscaled_roi)

    if cropped_image.shape[0] > 0 and cropped_image.shape[1] > 0:
        cv2.imwrite('Cropped.jpg', cropped_image)

    # Print ROI coordinates
    print("ROI Coordinates:", selected_roi)
    print("Upscaled Coordinates:", upscaled_roi)


if __name__ == '__main__':
    main()
