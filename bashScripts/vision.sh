source /home/amov/anaconda3/etc/profile.d/conda.sh
source /opt/ros/noetic/setup.bash
source ~/sjtu_asc_v2_ws-main/devel/setup.bash
conda activate yolov8
python /home/amov/sjtu_asc_v2_ws-main/src/mission_offboard/script/902test.py --mode pattern --c1start 10 --c1end 11 --numOfFrame 40 --numOfCircle 1
