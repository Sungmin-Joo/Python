# -*- coding: utf-8 -*-
import os
#Use "./" to search the current directory
def Find_dir(root):
    return os.listdir(root)
    #Check using print(find_dir("./"))  
def Find_dir_format(root, file_format):
    lsit = os.listdir(root)
    file_list = [file for file in lsit if os.path.splitext(file)[-1] == file_format]
    return file_list
    #Check using print(find_dir("./"),".txt")
def Write_file(root,filename,text_str):
    with open(root + filename, 'w') as f:
        f.write(text_str)
        
def Read_file(root,filename):
    with open(root + filename, 'r') as f:
        text = f.read()
    return text

if __name__ == '__main__':
    print('Func_called - main')
    print(Find_dir("./"))
    print(Find_dir_format("./",'.txt'))
    text_str = "20 17:00 22:00"
    Write_file("./","output.txt",text_str)
    print(Read_file("./","output.txt"))
else:
    print('Func_called - imported')
'''
Func_called - main
['output.txt', 'Smart_File.py']
['output.txt']
20 17:00 22:00
'''
