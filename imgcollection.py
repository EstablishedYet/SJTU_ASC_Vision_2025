import cv2
import time
import subprocess,os

time.sleep(20)
fw,fh=2560,1440
id=0
expo=20
while id<=30:
    cap = cv2.VideoCapture(id)
    if not cap.isOpened():
        id+=1
    else:
        # if(cameraType!='siyi'):
        subprocess.run(["v4l2-ctl", f"--device=/dev/video{id}", "--set-ctrl", "exposure_auto=1"])
        subprocess.run(["v4l2-ctl", f"--device=/dev/video{id}", "--set-ctrl", f"exposure_absolute={expo}"])
        break
cap.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
cap.set(cv2.CAP_PROP_FPS, 1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, fw)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, fh)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
t0=time.time()
frameid=0
outpath="/home/amov/imgs"
os.makedirs(outpath,exist_ok=True)
# os.makedirs(os.path.join(outpath,"imgs"),exist_ok=True)
while True:
    img=cap.read()
    cv2.imwrite(os.path.join(outpath,f"{frameid}.jpg"),img)
    frameid+=1
    if time.time()-t0>=300:
        break
    time.sleep(1)
