import cv2,os,numpy as np

maskup=cv2.imread(r"E:\2024-2025summer\previous\all2024\for_vision_test_only\src\mission_offboard\script\masks\maskup.jpg")
maskdown=cv2.imread(r"E:\2024-2025summer\previous\all2024\for_vision_test_only\src\mission_offboard\script\masks\maskdown.jpg")
imgpath=r"F:\1006noon\5\1raw"
for i in os.listdir(imgpath):
    img=cv2.imread(os.path.join(imgpath,i))
    ROIup=img[maskup==255]
    upsorted=np.sort(ROIup)
    ROIdown=img[maskdown==255]
    downsorted=np.sort(ROIdown)
    # print(upsorted.size)
    ups=[]
    downs=[]
    start=0.1
    ups.append(upsorted[int(upsorted.size*0.05)])
    downs.append(downsorted[int(downsorted.size*0.05)])
    while start<=0.9:
        ups.append(upsorted[int(upsorted.size*start)])
        downs.append(downsorted[int(downsorted.size*start)])
        start+=0.1
    # up_70=upsorted[int(upsorted.size*0.8)]
    
    # down_70=downsorted[int(downsorted.size*0.8)]
    varup=np.var(ROIup)
    sumup=np.sum(ROIup)
    sumdown=np.sum(ROIdown)
    vardown=np.var(ROIdown)
    print(i)
    print(f"up: {varup} {sumup} {ups} {ups[-1]-ups[0]} {ups[-1]-ups[1]}")
    print(f"down: {vardown} {sumdown} {downs} {downs[-1]-downs[0]} {downs[-1]-downs[1]}")
    print(float(ups[-1])-float(ups[0])+float(ups[-1])-float(ups[1])-float(downs[-1]-downs[0])-float(downs[-1]-downs[1]))
    imgup=cv2.bitwise_and(img,maskup)
    imgdown=cv2.bitwise_and(img,maskdown)
    cv2.imshow('up',imgup)
    cv2.imshow('down',imgdown)
    cv2.waitKey(0)