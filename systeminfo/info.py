import os
import platform
import socket
import psutil
def getMachineName():
    print(socket.gethostname())

def getOSInfo():
    print("OS:", platform.uname().system )
    print("OS version:", platform.uname().release)

def getCPUInfo():
    print("CPU cores:", os.cpu_count())

def getMemoryInfo():
    print("System memory:", get_size(psutil.virtual_memory().total))

def machineIpAddress():
    print("IP:", socket.gethostbyname(socket.gethostname()))

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def summary():
    getMachineName()
    getOSInfo()
    getCPUInfo()
    getMemoryInfo()
    machineIpAddress()
