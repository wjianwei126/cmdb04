#!/usr/bin/env python
import os
import subprocess  
import signal  
import time 

def createpics(cmd,timeout):
    p = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)
    t_beginning = time.time()
    seconds_passed = 0  
    while True:  
        if p.poll() is not None:  
            break  
        seconds_passed = time.time() - t_beginning  
        if timeout and seconds_passed > timeout:
           chpic =  cmd.split('/')[-1]
           os.system('cp -rf statics/livepics/../error.jpg statics/livepics/%s'%chpic)
           os.kill(p.pid, signal.SIGTERM)
        time.sleep(0.1)  
    return True
