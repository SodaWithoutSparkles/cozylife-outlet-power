#!/usr/bin/env python3
import socket
import time
import json

# captured requests: "{"msg":{"attr":[26,28]},"pv":0,"cmd":2,"sn":"1713186810749"}"
# captured response: "{"msg":{"attr":[26,28],"data":{"26":600,"28":115}},"pv":0,"cmd":2,"sn":"1713186810749","res":0}"
# raw request values from packet capture:
# 7b226d7367223a7b2261747472223a5b32362c32385d7d2c227076223a302c22636d64223a322c22736e223a2231373133313836383130373439227d0d0a

# Adapted from https://stackoverflow.com/a/34655152/9566810

# TODO: CHANGE THIS IP
host = "192.168.0.123"
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
attrs = [1, 2, 26, 28]

def askAttribute(s, attr):
    payload = {
        "msg": {
            "attr": attr
        },
        "pv": 0,
        "cmd": 2,
        "sn": str(int(time.time() * 1000)),
    } 
    payload = json.dumps(payload, separators=(',', ':')) + "\r\n"
    print("sending: \n", payload)
    s.sendall(payload.encode())
    return str(s.recv(1024))

data = askAttribute(s, attrs)
s.close()

data = json.loads(data.replace('\\r\\n\'', '').replace('b\'', ''))['msg']['data']

for key, value in data.items():
    print(key + ':', value)
# print('Received', repr(data))


