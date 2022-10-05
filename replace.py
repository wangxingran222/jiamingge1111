import os
from os.path import isfile
path = '/home/runner/work/jiamingge1111/jiamingge1111'
for file_name in os.listdir(path):
    if isfile(file_name):
        print(file_name)
        with open(os.path.join(path,file_name),"r",encoding='utf-8')as f1,open(os.path.join(path,file_name+".bak"),"w",encoding='utf-8')as f2:
            for line in f1:
                if "1" in line:
                    line = line.replace("1","2222")
                    print(line)
                f2.write(line)
        os.remove(os.path.join(path,file_name))
        os.rename(os.path.join(path,file_name+".bak"),os.path.join(path,file_name))
