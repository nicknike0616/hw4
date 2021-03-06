import serial
import time
import locale
import matplotlib.pyplot as plt
import numpy as np
import threading

# XBee setting
serdev = '/dev/ttyUSB0'
s = serial.Serial(serdev, 9600)

s.write("+++".encode())
char = s.read(2)
print("Enter AT mode.")
print(char.decode())

s.write("ATMY 0x140\r\n".encode())
char = s.read(3)
print("Set MY 0x140.")
print(char.decode())

s.write("ATDL 0x240\r\n".encode())
char = s.read(3)
print("Set DL 0x240.")
print(char.decode())

s.write("ATID 0x1\r\n".encode())
char = s.read(3)
print("Set PAN ID 0x1.")
print(char.decode())

s.write("ATWR\r\n".encode())
char = s.read(3)
print("Write config.")
print(char.decode())

s.write('ATWR\r\n'.encode())
char = s.read(3)
print('Write config.')
print(char.decode())

s.write('ATCN\r\n'.encode())
char = s.read(3)
print('Exit AT mode.')
print(char.decode())
x=[]
print("start sending RPC")

time_stamp = np.array([0,1,2,3,4,5,6,7,8,9,10.11,12,13,14,15,16,17,18,19,20])

query_time = 0

s.write("/getAcc/run\r".encode())
time.sleep(0.5)
s.write("/getAcc/run\r".encode())
time.sleep(0.5)
line=s.read(1)
line1=0

def job(a,b):
    while 1:
        a=[]
        b=[]
        s.write("/getAcc/run\r".encode())
        time.sleep(1)

thread_get = threading.Thread(target = job, args=(line,line1))
thread_get.start()

while query_time <= 19:
    s.write("/getAcc/run\r".encode())
    line=s.readline()
    line1=s.readline()
    x.append(10*int(line)+int(line1))
    print(x)
    query_time = query_time + 1
    time.sleep(1)

fig, ax = plt.subplots(1, 1)
l1,=ax.plot(time_stamp,x)
ax.set_xlabel('timestamp')
ax.set_ylabel('acc value')
plt.show()

s.close()