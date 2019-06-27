# -*- coding: utf-8 -*-
import Smart_File
#It must be on the same path as Smart_File.
if __name__ == '__main__':
    print('Func_called - main')
    print(Smart_File.Find_dir("./"))
    print(Smart_File.Find_dir_format("./",'.txt'))
    text_str = "20 17:00 22:00"
    Smart_File.Write_file("./","output.txt",text_str)
    read = Smart_File.Read_file("./","output.txt")
    print(read)
        
else:
    print('Func_called - imported')
    
'''
-------------------------------------------------------------------------------
Func_called - imported
Func_called - main
['Import_text.py', 'output.txt', 'Smart_File.py', '__pycache__']
['output.txt']
20 17:00 22:00
-------------------------------------------------------------------------------
'''