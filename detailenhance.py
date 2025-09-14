import cv2
import os
path=r"E:\2024-2025summer\socialpractice\selected\0.jpg"
frame=cv2.imread(path)
frame=cv2.detailEnhance(frame,sigma_s=15,sigma_r=0.03)
# cv2.imshow('a',frame)
# cv2.waitKey(0)
cv2.imwrite(os.path.join(path.replace(".jpg","_.jpg")),frame)
