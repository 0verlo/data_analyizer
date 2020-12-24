#!/usr/bin/env python3
# coding=utf-8
import re
import time
import json
import numpy as np

ave_collect_time = 20

class Mem_Analyzer:
    def __init__(self):
        self.list_loop_0 = []
        self.list_ave = []
        self.list_tmp_for_ave = []
        self.counter = 0
        self.status = 0

    def str_entrence(self,str_input):
        num_list = self.str_split(str_input)
        if num_list is not None:
            print(num_list)
            self.status = 1
        else:
            time.sleep(.1)
            return
        if 1 != self.status:
            return
        elif 0 == num_list[0]:
            self.list_loop_0.append([num_list[1],num_list[2]])
        else:
            self.list_tmp_for_ave.append([num_list[1],num_list[2]])
            if ave_collect_time <= len(self.list_tmp_for_ave):
                numb_ave_0=round(np.mean([self.list_tmp_for_ave[x][0] for x in range(ave_collect_time)]),2)
                numb_ave_1=round(np.mean([self.list_tmp_for_ave[x][1] for x in range(ave_collect_time)]),2)
                self.list_ave.append([numb_ave_0,numb_ave_1])
                self.status = 2
                print("done")
                #print(self.list_ave)

    def input_next_data(self):
        cur_status = self.status
        if 2 == self.status:
            self.status = 0 
            self.counter += 1
            self.list_tmp_for_ave = []
        else:
            print("Date collect in this round havent done yet.")
        return cur_status

    def str_split(self,str_input):
        key = re.search(r'.*(?<=(loop ))(\d+).*(?<=(in ))(\d+.\d+).*(?<=(th: ))(\d+.\d+).*',str_input)
        if not(key):
            print("Wrong input:"+str_input,end='')
            return None
        else:
            numbs=[int(key.group(2)),float(key.group(4)),float(key.group(6))]
            return numbs
        
    def list_save(self):
        dict_save=dict()
        dict_save["list_loop_0"]=self.list_loop_0
        dict_save["list_ave"]=self.list_ave
        with open("test.txt","w") as fp:
            json.dump(dict_save,fp)
#print("hello")

#str_analyze("loop 1593 in 0.12 ms (bandwidth: 8144.28 MB/s)\n")
'''
analyzor = Mem_Analyzer()
analyzor.str_entrence("loop 0 in 0.12 ms (bandwidth: 8144.28 MB/s)\n")
for i in range(ave_collect_time):
    analyzor.str_entrence("loop 1593 in 0.12 ms (bandwidth: 8144.28 MB/s)\n")
analyzor.list_save()
'''
