import cv2,os
import numpy as np
import subprocess,time
expo=1
id=0
while id<=30:
    cap = cv2.VideoCapture(id)
    if not cap.isOpened():
        id+=1
    else:
        # if(cameraType!='siyi'):
        cap.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
        cap.set(cv2.CAP_PROP_FPS, 30)
        fw,fh=2560,1440
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, fw)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, fh)
        cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        
        # while(True):
        subprocess.run(["v4l2-ctl", f"--device=/dev/video{id}", "--set-ctrl", "exposure_auto=1"])
        
        # for i in range(5):
        #     cap.read()
            # testframe=cap.read()

            # testframe_sum=np.sum(testframe)/(testframe.shape[0]*testframe.shape[1])
            # if testframe_sum>=25 and testframe_sum<=125:
            #     break
            # elif testframe_sum<25:
            #     expo-=4
            #     if expo<=0:
            #         break
            # else:
            #     expo+=10
            # for i in range(5):
            #     cap.read()
        break
path=rf"/home/amov/expotest/{time.time_ns()}"
os.makedirs(path)
# t1=time.time_ns()
# while True:
#     print(expo)
#     t0=time.time_ns()
#     for i in range(5):
#         _,frame=cap.read()
#         curTime=time.time_ns()
#         frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#         frame_sum=np.sum(frame)
#         print(frame_sum,curTime-t0,curTime-t1)
#         t0=curTime
#     _,testframe=cap.read() 
#     cv2.imwrite(os.path.join(path,f"{expo}.jpg"),testframe)
#     testframe=cv2.cvtColor(testframe,cv2.COLOR_BGR2GRAY)
#     testframe_sum=np.sum(testframe)/(testframe.shape[0]*testframe.shape[1])
#     if (testframe_sum>=25 and testframe_sum<=125):
#         break
#     elif testframe_sum>125:
#         expo-=5
#         if expo<=0:
#             break
#     else:
#         expo+=10
#     subprocess.run(["v4l2-ctl", f"--device=/dev/video{id}", "--set-ctrl", "exposure_auto=1"])
#     subprocess.run(["v4l2-ctl", f"--device=/dev/video{id}", "--set-ctrl", f"exposure_absolute={expo}"])
#     t1=time.time_ns()
for i in range(100):
    subprocess.run(["v4l2-ctl", f"--device=/dev/video{id}", "--set-ctrl", f"exposure_absolute={i}"])
    time.sleep(1)
    _,frame=cap.read()
    cv2.imwrite(os.path.join(path,f"{i}.jpg"),frame)