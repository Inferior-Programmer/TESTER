#sequence_2

import os
import random
import time

fname = "upload_2.txt"

time_to_upload = time.clock()

def create_file():
    l1 = 0
    f = open(fname,"w+")
    ref_time = time.clock()
    while l1 <  5:
        curtime = time.clock()
        if ref_time+0.32 < curtime:
            ref_time +=curtime
            rand_int1 = random.randint(0,20)
            rand_int2 = random.randint(20,40)
            rand_int3 = random.randint(40,60)
            new_string = str(rand_int1) + "," + str(rand_int2) + "," + str(rand_int3)+'\n'
            f.write(new_string)
            l1 +=1
            print('done {}'.format (l1) )
        else:
            print(curtime)
           
    f.close()
    upload_to_git()

def upload_to_git():
    os.system('git add .')
    os.system('git commit -m "repeat" ')
    os.system('git push -u origin master')
    os.system("\r\n")
    
    

while True:
    if time_to_upload+30  > time_to_upload:
        create_file()
    
