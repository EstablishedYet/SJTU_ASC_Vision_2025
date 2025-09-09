import cv2
from ultralytics import YOLO
modelClassify=YOLO(r"E:\2024-2025summer\909_2nd.pt")
results_classify1 = modelClassify.predict(
                    source=r"F:\47\less",
                    imgsz=640,
                    # device='0',
                    save=True,
                    batch=12,
                    half=True,
                    max_det=2
                )
# for result in results_classify1:
#     name=result.path
#     boxes=result.boxes

    # if(boxes.xywh.size(0)>=2):
    #     x1=boxes.xywh[0][0]
    #     prob1=boxes.conf[0]
    #     num1=(int)(boxes.cls[0])
    #     x2=boxes.xywh[1][0]
    #     prob2=boxes.conf[1]
    #     num2=(int)(boxes.cls[1])
    #     if x1<=x2:
    #         num=num1*10+num2
    #     else:
    #         num=num1+num2*10
    #     # dict1[int(name.split('/')[-1].split('.')[0].split('_')[1])][name.split('/')[-1].split('.')[0].split('_')[-1]]=(int(result.probs.top1),result.probs.top1conf)
    #     alldata=alldataList[mapofclear[int(name.split('/')[-1].split('.')[0].split('_')[0])]]
    #     imgdata = pos.Imgdata(pos=alldata.pos,num=num,
    #                         yaw=alldata.yaw,cropTensorList=cls_sources[int(name.split('/')[-1].split('.')[0].split('_')[1])][int(name.split('/')[-1].split('.')[0].split('_')[-1])],
    #                         speed=alldata.speed,filename=name)
    #     prob=min(prob1,prob2)
    #     num_and_prob=(num,prob)
    #     num_list.append(num_and_prob)
    #     dataList.append(imgdata)
    #     if prob>=0.7:
    #         trusted_num_list.append(num)
    #         trusted_dataList.append(imgdata)
    #     # print("Classify num is:" + str(num))
    #     # savepath=os.path.join(path,'output.txt')
    #     # with open(savepath, 'a') as file:
    # file.write("Classify num is:" + str(num) +' '+str(prob)+' '+str(name)+"\n")