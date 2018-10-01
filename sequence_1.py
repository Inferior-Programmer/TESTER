import os
import random


def write_file():
    f = open('main_upload.txt', 'a')
    for i in range(0,10):
        rand_int1 = random.randint(0,20)
        rand_int2 = random.randint(20,40)
        rand_int3 = random.randint(40,60)
        new_string = str(rand_int1) + "," + str(rand_int2) + "," + str(rand_int3)+'\n'
       
        f.write(new_string)
    f.close()


write_file()
write_file()
     
