# -*- coding: utf-8 -*-
if __name__ == '__main__':
    print('Func_called - main')
    Array = ['A',1,'B',2]
    for i in Array:
        try:#point - A
            int(i)
            print(str(i)+ ' = int')
        except:#point - B
            print(i + ' = Not int')
        '''
        If variation is possible with int, part #point - A runs,
        or part #point - B runs.
        '''
        
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