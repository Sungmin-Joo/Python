def Make_Lambda(Num):
    return lambda x : True if x % Num ==0 else False
'''
The above function produces a lambda to determine the multiple of Num.
'''

if __name__ == '__main__':
    print('Func_called - main')
    Temp_lambda = Make_Lambda(4)
    [print(Temp_lambda(i)) for i in range(0,10)]
    #pratice code!!
    #Processes repeating statements and arrangements with a single line of command.
    #Array = list([Temp_lambda(i) for i in range(0,10)])
    #print(Array)

else:
    print('Func_called - imported')
    
'''
----------result----------
Func_called - main
True
False
False
False
True
False
False
False
True
False
--------------------------
True - 0,4,8
False - 2,3,4,5,6,7,9
'''