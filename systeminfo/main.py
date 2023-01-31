# This program should display:
# 1. name of machine
# 2. operating system name
# 3. operating system version
# 4. number of cpu's
# 5. amount of memory
# 6. IP address of machine
# ©UCD Semester II/ Modular
# 7. Using the time taken to execute a simple numerical task, compute a CPU strength score for the machine.
# Use the timeit module and consider using the sample code 1 at the end, or some modiûcation of it.
import os
import platform
import socket
def getMachineName():
    print(socket.gethostname())

def getOSName():
    print("OS:", platform.uname().system )
    print("OS version:", platform.uname().release)

def cpuInformation():
    print("CPU cores:", os.cpu_count())

def machineIpAddress():
    print("IP:", socket.gethostname(socket.gethostname()))




print(socket.gethostname())
# getMachineName()