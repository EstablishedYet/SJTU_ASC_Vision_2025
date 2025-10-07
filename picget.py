import math
import time
from collections import Counter
import cv2
import cv_methods as cm
import numpy as np
from ultralytics import YOLO
import pos
import rospy
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry
from std_msgs.msg import Float64
from std_msgs.msg import String
from mavros_msgs.msg import WaypointReached
from sensor_msgs.msg import NavSatStatus
from geometry_msgs.msg import Point
import tf
import datetime
import os
from math import pi
import argparse
import random
import multiprocessing
import sys
import subprocess
parser=argparse.ArgumentParser()
parser.add_argument('--c1start',type=int,default=7)
parser.add_argument('--c1end',type=int,default=8)
parser.add_argument('--c2start',type=int,default=13)
parser.add_argument('--c2end',type=int,default=14)
parser.add_argument('--c3start',type=int,default=13)
parser.add_argument('--c3end',type=int,default=14)
parser.add_argument('--checkpoint',type=int)
arg=parser.parse_args()
c1start=arg.c1start
c1end=arg.c1end
c2start=arg.c2start
c2end=arg.c2end
c3start=arg.c3start
c3end=arg.c3end
checkpoint=arg.checkpoint

# MODELOBB = r"/home/amov/sjtu_asc_v2_ws-main/src/mission_offboard/script/models/18_obb.pt"
    # print("loading obb model")
# modelObb = YOLO(MODELOBB)  # 通常是pt模型的文件
# print("loading classify model")
# MODELCLASSIFY = modelclassify_pattern
# modelClassify = YOLO(MODELCLASSIFY)

rospy.init_node("picget_node")
rate = rospy.Rate(10)
wp=0
def wp_reach_cb(msg):
    global wp
    wp = msg.wp_seq
rospy.Subscriber("/mavros/mission/reached",WaypointReached, wp_reach_cb, queue_size = 1)
# while True:
#     # if wp==c1start or wp==c2start or wp==c3start:
#     if wp==checkpoint:
id=0
    
lastframe_sum=0
sum_low=45
sum_high=95
exposures=[1,4,8,15,30,50,90,200,500,1000,2000]
fw=2560
fh=1440

def find_max_numeric_folder(path):
        max_val = -1
        for name in os.listdir(path):
            folder_path = os.path.join(path, name)
            if os.path.isdir(folder_path) and name.isdigit():
                num = int(name)
                if num > max_val:
                    max_val = num
        return max_val

source=r"/home/amov/sjtu_asc_v2_ws-main/log_shi" 
os.makedirs(source,exist_ok=True)
path=os.path.join(source,str(find_max_numeric_folder(source)+1))
os.makedirs(path,exist_ok=True)
outpath=os.path.join(path,'frames')
os.makedirs(outpath,exist_ok=True)


while True:
    if wp>=checkpoint:
        while id<=30:
            cap = cv2.VideoCapture(id)
            if not cap.isOpened():
                id+=1
            else:
                # if(cameraType!='siyi'):
                cap.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
                cap.set(cv2.CAP_PROP_FPS, 30)
                cap.set(cv2.CAP_PROP_FRAME_WIDTH, fw)
                cap.set(cv2.CAP_PROP_FRAME_HEIGHT, fh)
                cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
                expo_id=2
                # while(True):
                subprocess.run(["v4l2-ctl", f"--device=/dev/video{id}", "--set-ctrl", "exposure_auto=1"])
                subprocess.run(["v4l2-ctl", f"--device=/dev/video{id}", "--set-ctrl", f"exposure_absolute={exposures[expo_id]}"])
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
        cap.read()
        cap.read()
        _,testframe=cap.read()
        # cv2.imwrite(os.path.join(path,f"{expo}.jpg"),testframe)
        testframe=cv2.cvtColor(testframe,cv2.COLOR_BGR2GRAY)
        lastframe_sum=testframe_sum=np.sum(testframe)/(testframe.shape[0]*testframe.shape[1])
        if testframe_sum>=sum_high:
            while expo_id>0:
                expo_id-=1
                subprocess.run(["v4l2-ctl", f"--device=/dev/video{id}", "--set-ctrl", f"exposure_absolute={exposures[expo_id]}"])
                cap.read()
                cap.read()
                _,testframe=cap.read()
                testframe=cv2.cvtColor(testframe,cv2.COLOR_BGR2GRAY)
                testframe_sum=np.sum(testframe)/(testframe.shape[0]*testframe.shape[1])
                if testframe_sum<sum_high:
                    if sum_low-testframe_sum<lastframe_sum-sum_high:
                        break
                    else:
                        expo_id+=1
                        subprocess.run(["v4l2-ctl", f"--device=/dev/video{id}", "--set-ctrl", f"exposure_absolute={exposures[expo_id]}"])
                        break
                lastframe_sum=testframe_sum
        elif testframe_sum<=sum_low:
            while expo_id<len(exposures)-1:
                expo_id+=1
                subprocess.run(["v4l2-ctl", f"--device=/dev/video{id}", "--set-ctrl", f"exposure_absolute={exposures[expo_id]}"])
                cap.read()
                cap.read()
                _,testframe=cap.read()
                testframe=cv2.cvtColor(testframe,cv2.COLOR_BGR2GRAY)
                testframe_sum=np.sum(testframe)/(testframe.shape[0]*testframe.shape[1])
                if testframe_sum>sum_low:
                    if sum_low-lastframe_sum>testframe_sum-sum_high:
                        break
                    else:
                        expo_id-=1
                        subprocess.run(["v4l2-ctl", f"--device=/dev/video{id}", "--set-ctrl", f"exposure_absolute={exposures[expo_id]}"])
                        break
                lastframe_sum=testframe_sum
        print(exposures[expo_id])
        break
    rate.sleep()
frameid=0
circle_number=0
while True:
    if wp==c1start or wp==c2start or wp==c3start:
        circle_number+=1
        cap.read()
        cap.read()
        while True:
            if wp == c1end or wp== c2end or wp==c3end:
                        # print("code exit by point")
                break
            _, frame = cap.read()
            cv2.imwrite(os.path.join(outpath,f'{frameid}.jpg'),frame)
            frameid+=1
            rate.sleep()
    if circle_number==3:
        break
    rate.sleep()
