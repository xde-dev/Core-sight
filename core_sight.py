#Copyright (c) 2026 xde-dev

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
import psutil
import time
import subprocess
import platform
while True:
    print("Core sight")
    time.sleep(1)
    print("hello user! what do you want to check?")
    time.sleep(1)
    print("1.CPU")
    time.sleep(0.5)
    print("2.RAM")
    time.sleep(0.5)
    print("3.DISK")
    time.sleep(0.5)
    print("4.OS")
    time.sleep(0.5)
    print("5.BIOS SETTINGS")
    time.sleep(1)
    user_input=input("Choose...>").strip()
    if user_input=="1":
        count=psutil.cpu_count()
        freq=psutil.cpu_freq()
        percent=psutil.cpu_percent(interval=1)
        stats=psutil.cpu_stats()
        times=psutil.cpu_times()    
        processor_id=platform.processor()
        max_ghz = round(freq.max / 1000, 2)
        print(f"Your cpu has {count} cores")
        time.sleep(0.5)
        print(f"Your cpu's frequinsy is {max_ghz} GHZ")
        time.sleep(0.5)
        print(f"your cpu is loaded by {percent}%")
        time.sleep(0.5)
        print(f"your cpu id is {processor_id}")
        time.sleep(0.5)
        input("press enter to exit to the menu")
    if user_input=="2":
        ram = psutil.virtual_memory()
        swap=psutil.swap_memory()
        total_gb = round(ram.total / (1024**3), 2)
        used_gb = round(ram.used / (1024**3), 2)
        available_gb = round(ram.available / (1024**3), 2)
        swap_gbs = round(swap.total / (1024**3), 2)
        print(f"Total Capacity: {total_gb} GB")
        time.sleep(0.5)
        print(f"Used Memory:    {used_gb} GB")
        time.sleep(0.5)
        print(f"Available:      {available_gb} GB")
        time.sleep(0.5)
        print(f"swap memory: {swap_gbs}gb")
        time.sleep(0.5)
        input("press enter to exit to the menu")
    if user_input=="3":
        disk=psutil.disk_usage("C:")
        partitions=psutil.disk_partitions()
        total = round(disk.total / (1024**3), 2)
        used = round(disk.used / (1024**3), 2)
        free = round(disk.free / (1024**3), 2)
        time.sleep(0.5)
        print(f"Total storage is {total}GBS")
        time.sleep(0.5)
        print(f"Used gbs of them is {used}gbs")
        time.sleep(0.5)
        print(f"Free of them is {free}GBs")
        time.sleep(0.5)
        print(f"and you have {partitions} partitions")
        input("press enter to exit to the menu")
    if user_input=="4":
        os_name = platform.system()
        os_release = platform.release()
        os_version = platform.version()
        architecture = platform.machine()
        print(f"OS core: {os_name} {os_release}")
        time.sleep(0.5)
        print(f"build: {os_version}")
        time.sleep(0.5)
        print(f"archihecture: {architecture}")
        time.sleep(0.5)
        input("\nPress enter to exit to the menu")
    if user_input=="5":
        cmd="wmic bios get manufacturer,smbiosbiosversion,releasedate /format:list"
        bios_data=subprocess.check_output(cmd, shell=True).decode().strip()
        print("bios data:")
        time.sleep(0.5)
        print(bios_data)
        time.sleep(0.5)
        input("press enter to exit")
