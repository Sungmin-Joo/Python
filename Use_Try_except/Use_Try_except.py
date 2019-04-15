# -*- coding: utf-8 -*-
import time
import math
if __name__ == '__main__':
    print('Func_called - main')
    start = time.time()
    n = int('1000000')
    print(time.time() - start)
    h = int(math.ceil(math.log(n,2)))
    
    start = time.time()
    B = [0 for i in range(1000000)]
    print(time.time() - start)
    
    start = time.time()
    A = [0]*n
    B = [0]*(1<<(h+1))
    print(time.time() - start)
    
    
    
    
else:
    print('Func_called - imported')
    
'''
----------result----------
Func_called - main
A = Not int
1 = int
B = Not int
2 = int
--------------------------
A,B = str(-char), not int
1,2 = int
'''