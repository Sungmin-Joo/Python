# -*- coding: utf-8 -*-
import time
import random

test_rand = [str(random.randrange(1,100)) for i in range(0,999999)]
def Index_test():
    temp = {}
    for j in range(0,999999):
        temp[test_rand[j]] = temp.get(test_rand[j],0) + 1
    return temp

def Str_test():
    temp = {}
    for j in test_rand:
        temp[j] = temp.get(j,0) + 1
    return temp    

if __name__ == '__main__':
    print('Func_called - main')
    
    start_time = time.time() 
    Index_test()
    print('%0.5f' % (time.time() - start_time))
    
    start_time = time.time() 
    Str_test()
    print('%0.5f' % (time.time() - start_time))
    
else:
    print('Func_called - imported')
    
'''
---------- result ----------
0.30408
0.14782
----------------------------
I could check the power of Python to use list in loop by comparing it with index loop.
'''
    
