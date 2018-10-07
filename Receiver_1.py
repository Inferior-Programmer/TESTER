#error checking code for url if it has an error message or csv won't work
# then magintay pa for the url na tinatawag

from bs4 import BeautifulSoup
import urllib3
import re
import csv

def get_datas():
    data_number = 0

    http = urllib3.PoolManager()

    url = 'https://raw.githubusercontent.com/Inferior-Programmer/TESTER/master/upload1_.txt' # or https://raw.githubusercontent.com/Inferior-Programmer/TESTER/master/upload1_2.txt
    response = http.request('GET', url)
    soup = BeautifulSoup(response.data)
    text = str(soup.get_text())



    if "Not Found" in text: #pwede siguro dito mag break kung nakita yung Not Found
        #and then magintay ulit
        print('error')

    text = text.splitlines()

    print(text)

    temp,humid,press = [] ,[], []

    for line in text:
        lin = line.split(",")
        ind = 1
        for lis in lin:
            if ind == 1:
                temp.append(float(lis))
            elif ind == 2:
                humid.append(float(lis))
            elif ind == 3:
                press.append(float(lis))
            else:
                print("some error")
            ind +=1

    print(temp)
    print(humid)
    print(press)

get_datas()
