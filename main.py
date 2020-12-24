#!/usr/bin/env python3
# coding=utf-8

import sys
#import classes.mem_analyzer as mem_analyzer
from classes.proc_monitor import Proc_Monitor
from classes.mem_analyzer import Mem_Analyzer

analyzor = Mem_Analyzer()

def test_proc_monitor():
    counter=0
    for stdout_line in proc.get_stdout_line():
        counter+=1
        print(stdout_line,end="")
        n = sys.stdin.readline().strip()
        if n=="End":
            proc.proc_stop()

def mem_analyze(cmd):
    proc = Proc_Monitor(cmd)
    counter=0
    for stdout_line in proc.get_stdout_line():
        analyzor.str_entrence(stdout_line)
        if 2 == analyzor.input_next_data():
            proc.proc_stop()
            del proc
            break


print("hello")
#test_proc_monitor()

list_param = list(range(0,1025,16))
#list_param = list(range(0,65,16))
list_param[0] = 1

for i in list_param:
    cmd = "/home/sen/Workspace/personal/data_collecter/proc/mem {:d}".format(i)
    print(cmd)
    mem_analyze(cmd)
analyzor.list_save()
