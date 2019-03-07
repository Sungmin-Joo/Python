class Numbers:
    
    def __init__(self,Name,Num):
        Num = Num.replace("-", "") #Point - A
        self.Name = Name
        self.Num = Num

    def D_Region(self):
        if self.Num[0:2] == '02':
            Region = 'Seuol'
        elif self.Num[0:2] == '01':
            Region = 'Mobile'
        elif self.Num[0:2] == '031':
            Region = 'Gyeonggi'
        elif self.Num[0:2] == '070':
            Region = 'Internet Phone'
        else:
            return "No data :<"
        return Region
    
    def D_Name(self):
        return self.Name
    
    def D_Number(self):
        return self.Num
        
    def Change_Num(self,Num):
        Num = Num.replace("-", "") #Point - A
        self.Num = Num
        
    def Change_Name(self,Name):
        self.Name = Name
    

'''
#Line "Point - A" detect '-' and remove '-'. - because replace with "" ("" means 'None str')
If input '010-1234-5678' then result is '01012345678'
'''


if __name__ == '__main__':
    print('Func_called - main')
    User_1 = Numbers(input("Input your name : "), input("Input your number : "))
    print(User_1.D_Name())
    print(User_1.D_Region())
    print(User_1.D_Number())
else:
    print('Func_called - imported')
    
'''
----------reslut----------
Func_called - main

Input your name : Sung_Min Joo

Input your number : 010-2770-4367
Sung_Min Joo
Mobile
01027704367
--------------------------
'''