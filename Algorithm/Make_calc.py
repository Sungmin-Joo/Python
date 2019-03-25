# -*- coding: utf-8 -*-
def add(num):
    global pre_num
    pre_num += num 

def diff(num):
    global pre_num
    pre_num -= num 

def mult(num):
    global pre_num
    pre_num *= num 

def div(num):
    global pre_num
    pre_num /= num 


if __name__ == '__main__':
    print('Func_called - main')
    pre_num = 0
    buf_num = 0
    flag = None
    pre_flag = None
    first = 0
    while(1):
        print('---- "reset" = reset ----',end='')
        input_num = input('----- "exit" = out -----\n')
        try:
            input_num = int(input_num)
            if(first == 0):
                pre_num = input_num
                first = 1
            else:
                buf_num = input_num
            print('########################')
            print('\tresult = ', pre_num)
            if(buf_num != None):
                print('\tbuffer = ', buf_num)
            print('########################')
        except:
            if(input_num in ['+', '-', 'x', '/']):
                if(flag != None):
                    pre_flag = flag
                flag = ['+', '-', 'x', '/'].index(input_num)
                if(pre_flag == 0):
                    if(buf_num != None):
                        add(buf_num)
                        buf_num = pre_num
                elif(pre_flag == 1):
                    if(buf_num != None):
                        diff(buf_num)
                        buf_num = pre_num
                elif(pre_flag == 2):
                    if(buf_num != None):
                        mult(buf_num)
                        buf_num = pre_num
                elif(pre_flag == 3):
                    if(buf_num != None):
                        if(buf_num == 0):
                            print('Error! divid 0 is not correct expression')
                        else:
                            div(buf_num)
                            buf_num = pre_num
                print('########################')
                print('\tresult = ', pre_num)
                if(buf_num != None):
                    print('\tbuffer = ', buf_num)
                print('########################')
            elif(input_num == '='):
                if(flag == 0):
                    if(buf_num != None):
                        add(buf_num)
                        buf_num = None
                elif(flag == 1):
                    if(buf_num != None):
                        diff(buf_num)
                        buf_num = None
                elif(flag == 2):
                    if(buf_num != None):
                        mult(buf_num)
                        buf_num = None
                elif(flag == 3):
                    if(buf_num != None):
                        if(buf_num == 0):
                            print('Error! divid 0 is not correct expression')
                        else:
                            div(buf_num)
                            buf_num = None
                print('result = ',pre_num)
                print("press 'r' to reset")
                while(1):
                    A = input()
                    if(A == 'r'):
                        pre_num = 0
                        buf_num = 0
                        flag = None
                        pre_flag = None
                        first = 0
                        break
            elif(input_num == 'exit'):
                print('Exit the program.')
                break
            elif(input_num == 'reset'):
                pre_num = 0
                buf_num = 0
                flag = None
                pre_flag = None
                first = 0
            else:
                print('Please check the input value.')
else:
    print('Func_called - imported')
    
'''
---- "reset" = reset ----
----- "exit" = out -----
59
########################
        result =  59
        buffer =  0
########################
---- "reset" = reset ----
----- "exit" = out -----
x
########################
        result =  59
        buffer =  0
########################
---- "reset" = reset ----
----- "exit" = out -----
5
########################
        result =  59
        buffer =  5
########################
---- "reset" = reset ----
----- "exit" = out -----
=
result =  295
press 'r' to reset

r
---- "reset" = reset ----
----- "exit" = out -----
exit
Exit the program.
'''