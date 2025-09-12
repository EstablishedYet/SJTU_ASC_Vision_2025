import cv2
import os
import numpy as np
path=r"F:\8\2clearframes"

for i in os.listdir(path):
    frame=cv2.imread(os.path.join(path,i))
    nframe=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    grayframe=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    h,s,v=cv2.split(nframe)
    sum_v=np.sum(v)/(v.shape[0]*v.shape[1])
    sum_g=np.sum(grayframe)/(v.shape[0]*v.shape[1])
    print(f"{i} {sum_v} {sum_g}")
    cv2.imshow('img',frame)
    cv2.waitKey(0)
