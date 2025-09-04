gnome-terminal -- bash -c "chmod +x px.sh;./px.sh"
echo "1" 
sleep 5s

gnome-terminal -- bash -c "chmod +x send.sh;./send.sh"
echo "2" 
sleep 1s


gnome-terminal -- bash -c "chmod +x vision.sh;./vision.sh"
echo "3" 
sleep 1s
gnome-terminal -- bash -c "chmod +x rostest.sh;./rostest.sh"
sleep 1s
gnome-terminal -- bash -c "chmod +x mision.sh;./mision.sh"
echo "4"
sleep 1s

gnome-terminal -- bash -c "chmod +x calculate.sh;./calculate.sh"
echo "5"
sleep 1s
