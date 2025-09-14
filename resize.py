import cv2
import os
path=r"E:\2024-2025summer\socialpractice\914pics_copy"
# newpath=path
for i in os.listdir(path):
    frame=cv2.imread(os.path.join(path,i))
    frame=cv2.resize(frame,(6400,3600),interpolation=cv2.INTER_LANCZOS4)
    cv2.imwrite(os.path.join(path,i),frame)