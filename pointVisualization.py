import matplotlib.pyplot as plt
import re
import os
log_folder=""
logs=[]
for i in os.listdir(log_folder):
    str_num=i.split('.')[0]
    try:
        float(str_num)
        flag=True
    except Exception:
        flag=False
    if flag:
        logs.append(os.path.join(log_folder,i))
for file in logs:
    with open(file,'r') as f:
        for line in f:
