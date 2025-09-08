import cv2
import subprocess
import time,os
fw,fh=2560,1440
id=0
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
cap.set(cv2.CAP_PROP_FPS, 30)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, fw)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, fh)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 8)
time.sleep(5)
t0=time.time()
frameid=0
outpath="/home/amov/buffertest"
os.makedirs(outpath,exist_ok=True)
os.makedirs(os.path.join(outpath,"imgs"),exist_ok=True)
# os.makedirs(os.path.join(outpath,"logs"),exist_ok=True)
while True:                                
                # if cap.isOpened():
                    # print("camera is opened")
    _, frame = cap.read()
    # if success == True:
    if time.time()-t0>=30:
        # print("code exit by point")
        break
    # out.write(frame)
    cv2.imwrite(os.path.join(outpath,f'{frameid}.jpg'),frame)
    
    # allimgdata = pos.Imgdata(pos=[local_x, local_y, local_z],  num=-1, 
    #                         yaw=local_yaw, cropTensorList=[(0,0),(0,0),(0,0),(0,0)],
    #                         speed=[local_vel_x, local_vel_y, local_vel_z],)
    # alldataList.append(allimgdata)
    #todo 所有坐标结果记录下来，同时记录图片对应的pos和
    with open(os.path.join(outpath,"odom.txt"),'a') as file:
        file.write(str(time.time()))
        # file.write("local: "+str(odom_x)+' '+str(odom_y)+' '+str(odom_z)+' '+str(odom_vel_x)+' '+str(odom_vel_y)+' '+str(odom_vel_z)+' '+str(odom_yaw)+'\n')
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break
    frameid+=1