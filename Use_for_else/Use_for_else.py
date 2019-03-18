# -*- coding: utf-8 -*-
'''
####### Recommand execute in command window #######
'''
import time
import os
if __name__ == '__main__':
    print('Func_called - main')
    member_list = {} #make emty dict
    
    while(1):
        os.system('cls')
        #os.system can deliver os instructions ex) "dir" or "cls"
        print("------------- select menu -------------")
        menu = input("1. Regist member\n2. Find member\n3. logout\n---------------------------------------\n")
        
        if(menu == '1'):
            os.system('cls')
            name = input("Name : ")
            age = input("Age :")
            member_list[name] = age
            print("\nRegist success!")
            time.sleep(2)
        elif(menu == '3'):
            print("Logout")
            time.sleep(2)
            break
        elif(menu == '2'):
            os.system('cls')
            find_name = input("Input member's name :")
            for name, age in member_list.items():
                #"member_list.items()" returns a pair of keys and values 
                if(name == find_name):
                    os.system('cls')
                    print(name + " is our member\n\nMember's age is " + age)
                    time.sleep(3)
                    break
            else:
                os.system('cls')
                print(find_name + " is not our member.\nCheck the name plz")
                time.sleep(3)

else:
    print('Func_called - imported')
    
'''
----------result----------
------------- select menu -------------
1. Regist member
2. Find member
3. logout
---------------------------------------
'
'
'

--------------------------
'''