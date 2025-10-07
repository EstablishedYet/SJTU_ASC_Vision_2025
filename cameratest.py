import cv2,os,shutil

id=0
while id<=30:
    cap = cv2.VideoCapture(id)
    if not cap.isOpened():
        id+=1
    else:
        print(id)
for i in range(3):
    cap.read()
flag,frame=cap.read()
print(flag)
path="/home/amov/cameratest"
if os.path.exists(path):
    os.remove(path)
    os.mkdir(path)
cv2.imwrite(os.path.join(path,'1.jpg'),frame)
cap.release()