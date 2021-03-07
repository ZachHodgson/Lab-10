import matplotlib.pyplot as plt
import numpy as np
import serial
from drawnow import*

#Part 1:

# plt.plot([0,1,2,3,4], [0,1,4,9,16])
# plt.ylabel('y')
# plt.xlabel('x')
# plt.axis([0,4,0,16])
# plt.show()

#Part 2:

# def math_fun(t):
#     return np.exp(-t) * np.cos(2*np.pi*t)
#
# t1 = np.arange(0.0, 5.0, 0.1)
# t2 = np.arange(0.0, 5.0, 0.02)
#
# plt.figure(1)
# plt.subplot(211)
#
# plt.plot(t1, math_fun(t1), 'r+', t2, math_fun(t2), 'k')
# plt.grid()
#
# plt.subplot(212)
# plt.plot(t2, np.cos(2*np.pi*t2), 'b--')
# plt.grid()
# plt.show()

#Part 3:

# fig = plt.figure()
# ax = plt.axes(projection = "3d")
# z_line = np.linspace(0,15,1000)
# x_line = np.exp(-0.1*z_line) * np.cos(z_line)
# y_line = np.exp(-0.1*z_line) * np.sin(z_line)
# ax.plot3D(x_line, y_line, z_line, 'red')
# ax.set_xlabel("x")
# ax.set_ylabel("y")
# ax.set_zlabel("z")
#
# plt.show()

#Part 4:

Data0 = []
Data1 = []

def PlotSignal():
    plt.ylim(0, 1200)
    plt.title('Plotting in Streaming AD0 from Arduino')
    plt.grid(True)
    plt.ylabel('Analog Signal AD0')
    plt.plot(Data0, 'r', label = 'Signal from A0')
    plt.plot(Data1, 'b', label='Signal from A1')
    plt.legend(loc = 'upper right')


# def PlotSignalA1():
#     plt.ylim(0, 1200)
#     plt.title('Plotting in Streaming AD1 from Arduino')
#     plt.grid(True)
#     plt.ylabel('Analog Signal AD1')
#     plt.plot(Data1, 'b', label = 'digital signal')
#     plt.legend(loc = 'upper right')

if __name__=='__main__':
    ser = serial.Serial('COM5', 9600)
    plt.ion()
    Dcounter = 0
    ser.flush()

    while True:
        while(ser.inWaiting() == 0):
            pass #do nothing if no incoming data
        ardData = ser.readline().decode('utf-8')
        InputData = ardData.split(',')
        temp0 = float(InputData[0])
        temp1 = float(InputData[1])
        Data0.append(temp0)
        Data1.append(temp1)

        drawnow(PlotSignal)
        plt.pause(0.000001)
        plt.pause(0.000001)
        Dcounter = Dcounter+1
        if(Dcounter>60):
            Dcounter = 0
            Data1.pop(0)
            Data0.pop(0)

    ser.close()