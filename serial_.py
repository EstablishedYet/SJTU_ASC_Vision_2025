import serial
import time
SERIAL_PORT = "/dev/ttyUSB0"   # 如果是 COM10 以上要写成 r"\\.\COM10"
BAUD_RATE = 115200

# 打开串口
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

# 要发送的数据
send_buf = bytearray([0x55, 0x66, 0x01, 0x04, 0x00, 0x00, 0x00, 
                    0x0E, 0x00, 0x00, 0x7C, 0xFC, 0x4F, 0xA4])

print("Sending:", send_buf.hex())
ser.write(send_buf)
ser.flush()

# 等待响应
time.sleep(0.5)
response = ser.read(ser.in_waiting or 1)

if response:
    print("Received:", response.hex())
else:
    print("No response received.")

ser.close()