#sequence_2

import os
import random
import time
import threading


fname = "upload_.txt"

file_list = [1]

time_to_upload = time.clock()

def create_file():
    l1 = 0
    f = open(fname,"w+")
    ref_time = 0
    while l1 !=  5:
        curtime = time.clock()
        if ref_time+10 < curtime:
            ref_time =curtime
            curtime = time.clock()
            rand_int1 = random.randint(0,20)
            rand_int2 = random.randint(20,40)
            rand_int3 = random.randint(40,60)
            new_string = str(rand_int1) + "," + str(rand_int2) + "," + str(rand_int3)+'\n'
            f.write(new_string)
            l1 +=1
            print('done {}'.format (l1) )
        else:
            print(int(curtime))

           
    f.close()
    print(fname)
    upload_to_git()

def upload_to_git():
    norm_name = "upload_"
    os.system('git add .')
    os.system('git commit -m "repeat" ')
    os.system('git push -u origin master')
    os.system("\r\n")
    global fname
    fname = norm_name + str(file_list[-1]) +'.txt'
    file_list.append(file_list[-1] + 1)
    
    


        
        
    
