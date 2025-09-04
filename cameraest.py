import cv2

if True:
    id=0
    while id<=30:
        cap = cv2.VideoCapture(id)
        if not cap.isOpened():
            id+=1
        else:
            print(id)
#                     subprocess.run(["v4l2-ctl", f"--device=/dev/video{id}", "--set-ctrl", "exposure_auto=1"])

# # # 设置曝光值为90谢谢
#                     subprocess.run(["v4l2-ctl", f"--device=/dev/video{id}", "--set-ctrl", f"exposure_absolute={expo}"])
            break
    cap.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
    cap.set(cv2.CAP_PROP_FPS, 30)
    fw=1920
    fh=1080
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, fw)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, fh)
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 8)