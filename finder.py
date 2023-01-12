# Project : 03 (finder project)

import os
import time
from threading import Thread
import pickle
import re
import argparse
from colorama import init,Fore,Back,Style
init(autoreset=True)

t1= time.time()
d1 = {}

def IndexCreation(drive):
    resp = os.walk(drive)
    j=0
    for each in resp:
        r,dirs,files = each
        for file in files:
            file = file.lower()
            if file in d1:
                file = file + "|" + str(j)
                j=j+1
            d1[file] = r
                
        for d in dirs:
            d = d+"-->"
            if d in d1:
                d = d+ "|" + str(j)
                j=j+1
            d1[d] = r
                
def GetDrive():
    resp = os.popen("wmic logicaldisk get caption")
    data = resp.read()
    drives = data.replace("caption","").replace("\n","").split()
    return drives
    
def save_data():
    fr = open("mydata.txt","wb")
    pickle.dump(d1,fr)
    fr.close()
    
def LoadData():
    fr = open("mydata.txt","rb")
    data = pickle.load(fr)
    return data
    
def StartIndex():
    listofthreads =[]
    ListofDrives = GetDrive()
    for drive in ListofDrives:
        th1 = Thread(target=IndexCreation,args=(drive,))
        th1.start()
        listofthreads.append(th1)
    for th1 in listofthreads:
        th1.join()
    save_data()
    t2 = time.time()
    print("time taken to create index",t2-t1)

def SearchFile(p,file=True, folder=True):
    data = LoadData()
    i=1
    for k,v in data.items():
        m = re.search(p,k,re.I)
        if m:
            first = k.split("|")[0]
            if first.endswith("-->") and folder:
                print(i,":",Fore.RED+first,"\t",v,Fore.CYAN+"--D")
            elif file1:
                print(i,":",Fore.RED+first,"\t",v)
            i=i+1
                
    t2 = time.time()
    print("time taken to search",t2-t1)
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name",nargs = "?")
    parser.add_argument("-c",help="To create the index database",action= 'store_true')
    parser.add_argument("-v",help="To show the current version",action= 'store_true')
    parser.add_argument("-of",help="Display only folders",action= 'store_true')
    parser.add_argument("-f",help="Display only files",action= 'store_true')
    args = parser.parse_args()
    
    if args.c:
        StartIndex()
    elif args.v:
        print("current version = 1.0")
    else:
        if args.file_name!=None or args.file_name=="":
            if args.file_name.isspace():
                print("please provide the file name")
            else:
                if args.of:
                    SearchFile(args.file_name, file1=False, folder=True)
                elif args.f:
                    SearchFile(args.file_name, file1=True, folder=False)
                else:
                    SearchFile(args.file_name, file1=True, folder=True)
        else:
            print("please provide the file name")

main()