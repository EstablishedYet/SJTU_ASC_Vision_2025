import cv2,numpy as np
import os
fw=2560
fh=1440
# expo=10
mtx = np.array([[2.8724e+03,0.00000000e+00,1.2342e+03],
[0.00000000e+00,2.8657e+03,6.891308e+02],
[0.00000000e+00,0.00000000e+00,1.00000000e+00]])

dist = np.array([-0.5018,0.2920,-0.0034,0.0010,-0.2113])
nmtx, _ = cv2.getOptimalNewCameraMatrix(mtx, dist, (fw,fh), alpha=1)
center=[1234.0,689.0]
center=np.array(center,dtype=np.float32)
path=r"F:\test\output0913\7\2clearframes"
newpath=r"F:\test\output0913\7\2clearframes_un"
os.makedirs(newpath,exist_ok=True)
log=r"F:\test\output0913\7"
files=[]
# with open(os.path.join(log,"log.txt"),'w') as file:
for i in os.listdir(path):
    frame=cv2.imread(os.path.join(path,i))
    cv2.circle(frame,(1234,689),5,(0,0,255),5)
    frame=cv2.undistort(frame,mtx,dist,None,nmtx)
    # frame=cv2.resize(frame,(1280,720),None)
    
    cv2.imwrite(os.path.join(newpath,i),frame)

for i in os.listdir(log):
    i_=i.split('.')[0]
    try:
        i_num=float(i_)
        files.append(os.path.join(log,i))
    except Exception:
        pass
processed=[]
for i in files:
    with open(i,'r') as f:
        for line in f:
            start=line.strip().split()[0]
            if start=='[':
                continue
            filename=line.strip().split()[2].split('/')[-1].split('_')[0]
            print(filename)
            yaw=line.strip().split()[6]
            if filename not in processed:
                # center=np.array(point,dtype=np.float32)
                print(center)
                point=cv2.undistortPoints(np.resize(center,(1,1,2)),mtx,dist,P=nmtx)
                point=np.resize(point,(1,2))
                # print(point)
                point_new=point.copy()
                point_new=point_new.flatten()
                point_y=point_new.copy()
                point_new[0]+=3000*np.sin(float(yaw))
                point_new[1]-=3000*np.cos(float(yaw))
                point_y[0]+=3000*np.sin(float(yaw)-3.14159265/2)
                point_y[1]-=3000*np.cos(float(yaw)-3.14159265/2)
                # print(point_new)
                frame=cv2.imread(os.path.join(newpath,f"{int(filename):04d}.jpg"))
                # print(point.flatten().astype(np.uint8))
                # print(point_new.astype(np.uint8))
                cv2.line(frame,point.flatten().astype(np.int32),point_new.astype(np.int32),(0,0,255),thickness=5)
                cv2.line(frame,point.flatten().astype(np.int32),point_y.astype(np.int32),(0,0,255),thickness=5)
                cv2.imwrite(os.path.join(newpath,f"{int(filename):04d}.jpg"),frame)
                processed.append(filename)
                # cv2.resize(interpolation=cv2.INTER_LANCZOS4)
