def check_func():
    print('Inside of check_func')

print('Outside of Func_called')#A
'''
if run this code, result is #B
else (ex - imported), result is #C
'''
if __name__ == '__main__':
    print('Func_called - main')#B
else:
    print('Func_called - imported')#C
    
    
    
'''
----------result------------
Outside of Func_called
Func_called - main
----------------------------
++
#A is zero - level code.
Regardless of whether it is run or imported, #A is run
'''