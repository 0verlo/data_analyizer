#!/usr/bin/env python3
# coding=utf-8
import subprocess
import shlex
import time

class Proc_Monitor(object):
    def __init__(self,cmd):
        self.__cmd=shlex.split(cmd)
        self.__proc_p=subprocess.Popen(self.__cmd,stdout=subprocess.PIPE)

    def get_stdout_line(self):
        print("Proc starting.Plase wait...")
        for stdout_line in iter(self.__proc_p.stdout.readline,""):
            if self.__proc_p.poll() is not None:
                break
            yield str(stdout_line,encoding="utf-8")
        yield "Programm stop!\n"

    def proc_stop(self):
        self.__proc_p.kill()
        #while(0 != self.__proc_p.poll()):
            #time.sleep(.1)

