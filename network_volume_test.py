__author__ = 'michaelkapuscik'
#!/usr/bin/env python

import socket
import time

TCP_IP = '10.42.0.75'
TCP_PORT = 33335
BUFFER_SIZE = 1024

minVolume = bytearray([0x02, 0x06, 0xA0, 0x52, 0x00, 0x03, 0x00, 0x00, 0x00])
maxVolume = bytearray([0x02, 0x06, 0xA0, 0x52, 0x00, 0x03, 0x00, 0x4A, 0x00])
muteMessage = bytearray([0x02, 0x04, 0xA0, 0x53, 0x00, 0x01, 0x00])
unmuteMessage = bytearray([0x02, 0x04, 0xA0, 0x53, 0x00, 0x00, 0x00])

commands = [minVolume, maxVolume, muteMessage, unmuteMessage]


for command in commands:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(command)
    data = s.recv(BUFFER_SIZE)
    s.close()
    print "received data:", data
    time.sleep(1)
