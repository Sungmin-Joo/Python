import Func_called as A

A.check_func()#point - 1
if __name__ == '__main__':
    print('end')
    
    
    
'''
----------result------------
Outside of Func_called
Func_called - imported
Inside of check_func
end
----------------------------
++
During #point - 1
Func_called is not runned but imported,
then Func_called's #C -{print('Func_called - imported')}- is runned 
'''