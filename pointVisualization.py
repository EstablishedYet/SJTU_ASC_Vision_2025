import matplotlib.pyplot as plt
import re
import matplotlib
import os
log_folder1=r"E:\2025-2026fall\cuadc\34"
log_folder2=r"E:\2024-2025summer\917download\log_shi\42thelast"
logs1=[]
logs2=[]
names=[]
for i in os.listdir(log_folder1):
    str_num=i.split('.')[0]
    try:
        float(str_num)
        if str_num not in names:
            names.append(str_num)
        logs1.append(os.path.join(log_folder1,i))
    except Exception:
        pass
# for i in os.listdir(log_folder2):
#     str_num=i.split('.')[0]
#     try:
#         float(str_num)
#         logs2.append(os.path.join(log_folder2,i))
#     except Exception:
#         pass
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
xs1={names[0]:[],names[1]:[],names[2]:[]}
ys1={names[0]:[],names[1]:[],names[2]:[]}
# xs2={names[0]:[],names[1]:[],names[2]:[]}
# ys2={names[0]:[],names[1]:[],names[2]:[]}
for file in logs1:
    with open(file,'r') as f:
        filename=file.split('\\')[-1].split('.')[0]
        for line in f:
            line=line.strip()
            if line.startswith('['):
                continue
            tokens=line.split()
            xs1[filename].append(float(tokens[0]))
            ys1[filename].append(float(tokens[1]))
# for file in logs2:
#     with open(file,'r') as f:
#         filename=file.split('\\')[-1].split('.')[0]
#         for line in f:
#             line=line.strip()
#             if line.startswith('['):
#                 continue
#             tokens=line.split()
#             xs2[filename].append(float(tokens[0]))
#             ys2[filename].append(float(tokens[1]))
ax.scatter(xs1[names[0]],ys1[names[0]],c='green',marker='o',label=f'{names[0]} 1')
ax.scatter(xs1[names[1]],ys1[names[1]],c='red',marker='o',label=f'{names[1]} 1')
ax.scatter(xs1[names[2]],ys1[names[2]],c='blue',marker='o',label=f'{names[2]} 1')
# ax.scatter(xs2[names[0]],ys2[names[0]],c='green',marker='+',label=f'{names[0]} 2')
# ax.scatter(xs2[names[1]],ys2[names[1]],c='red',marker='+',label=f'{names[1]} 2')
# ax.scatter(xs2[names[2]],ys2[names[2]],c='blue',marker='+',label=f'{names[2]} 2')
ax.set_xlabel("X (m)")
ax.set_ylabel("Y (m)")
# ax.set_zlabel("Z (m)")
ax.set_title(f"{log_folder1}")
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.show()