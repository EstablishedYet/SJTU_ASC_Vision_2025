import cv2
import numpy as np
def rotate_bound(image, angle):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)

    # rotation matrix
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    # compute new bounding dimensions
    new_w = int((h * sin) + (w * cos))
    new_h = int((h * cos) + (w * sin))

    # adjust rotation matrix (translation)
    M[0, 2] += (new_w / 2) - center[0]
    M[1, 2] += (new_h / 2) - center[1]

    # rotate without cropping
    return cv2.warpAffine(image, M, (new_w, new_h))

img_rotated = rotate_bound(img, 45)
cv2.imwrite("rotated_nocrop.jpg", img_rotated)
