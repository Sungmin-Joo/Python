def check_num(num):
    num = num.replace("-", "") #Point - A
    Flag = 3
    if num[0:2] == '01':
        Region = 'Mobile'
    elif num[0:2] == '02':
        Region = 'Seuol'
        Flag = 2
    elif num[0:3] == '031':
        Region = 'Gyeonggi'
    elif num[0:3] == '070':
        Region = 'Internet Phone'
    else:
        return "error :<"
    Front_Num = num[0:Flag]
    Real_Num = num[Flag:]
    return 'Front_Num = ' + Front_Num + ' \nReal_Num = ' + Real_Num + '\nRegion = ' + Region

'''
#Line "Point - A" detect '-' and remove '-'. - because replace with "" ("" means 'None str')
If input '010-1234-5678' then result is '01027704367'
'''


if __name__ == '__main__':
    print('Func_called - main')
    A = input('Input number : ')
    print('Your input value is ' + A)
    print(check_num(A))
else:
    print('Func_called - imported')
    
    