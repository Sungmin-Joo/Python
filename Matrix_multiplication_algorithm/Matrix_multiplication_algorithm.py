# -*- coding: utf-8 -*-
import numpy as np
if __name__ == '__main__':
    print("Func_called - main")
    A = np.array([[5,7,-3,4],[2,-5,3,6]])
    B = np.array([[3,0,8],[-5,1,-1],[7,4,4],[2,4,3]])
    len_row_A = A.shape[0]
    len_col_A = A.shape[1]
    len_col_B = B.shape[1]
    result = np.zeros((len_row_A,len_col_B))
    print("---------- use numpy function ----------")
    print(np.dot(A,B))
    print("----------------------------------------")
    '''
    Python can easily implement difficult algorithms.
    But I wanted to practice implementing algorithms with python.
    '''
    for row in  range(0,len_row_A):
        for col in range(0,len_col_B):
            for index in range(0,len_col_A):
                result[row,col] = result[row,col] + A[row,index]*B[index,col]
    print("----------- use my algorithm -----------")
    print(result)
    print("----------------------------------------")
            
else:
    print('Func_called - imported') 
'''
----------result----------
Func_called - main
---------- use numpy function ----------
[[-33  11  33]
 [ 64  31  51]]
----------------------------------------
----------- use my algorithm -----------
[[-33.  11.  33.]
 [ 64.  31.  51.]]
----------------------------------------
--------------------------

'''