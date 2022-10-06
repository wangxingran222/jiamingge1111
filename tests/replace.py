import os
from os.path import isfile

def replace_label(path, old_label:str, new_label:str):
    for file_name in os.listdir(path):
        if isfile(os.path.join(path,file_name)):
            print(file_name)
            with open(os.path.join(path,file_name),"r",encoding='utf-8')as f1,open(os.path.join(path,file_name+".bak"),"w",encoding='utf-8')as f2:
                for line in f1:
                    if old_label in line:
                        line = line.replace(old_label, new_label)
                        print(line)
                    f2.write(line)
            os.remove(os.path.join(path,file_name))
            os.rename(os.path.join(path,file_name+".bak"),os.path.join(path,file_name))
        else:
            replace_label(os.path.join(path,file_name),old_label,new_label)

if __name__ == "__main__":
    cur_dir = os.path.dirname(os.path.abspath(__file__))  #当前文件所在目录
    replace_label(cur_dir,"@pytest.mark.RRRRRR","@pytest.mark.RRRRRR")