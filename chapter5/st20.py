# 与串行端口的数据通信
import serial
ser = serial.Serial('/dev/tty.usbmodem641',
                    baudrate=9600,
                    bytesize=8,
                    parity='N',
                    stopbits=1)
ser.write(b'G1 X50 Y50\r\n')
resp = ser.readline()