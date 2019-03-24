# -*- coding: utf-8 -*-
import re
def issafe(text):
    return (len(text) >= 10
            and re.search('\d', text)
            and re.search('[A-Z]', text)
            and re.search('[a-z]', text))
if __name__ == '__main__':
    print('Func_called - main')
    
    print('\n------- Fisrt test -------')
    print('Find pl in "Nice apple"')
    print('re.match :' ,bool(re.match('pl',"Nice apple")))
    print('re.search :' ,bool(re.search('pl',"Nice apple")))
    print("Cannot find 'pl' in match because string has spaces")
    
    print('\n------- Second test -------')
    print('Find pl in "Nice apple"')
    print("re.findall(\"\w*pl\w*\",\"Nice apple\") : ",re.findall("\w*pl\w*","Nice apple"))
    
    print('\n------- Third test -------')
    print('Find pl in "Nice apple" and replace "##"')
    print("re.sub('pl','##',\"Nice apple\") : ",re.sub('pl','##','Nice apple'))
    print('\nReplace example')
    print("re.sub('[:,|,-]',', ',\"A:B|C-D\") : ",re.sub('[:,|,-]',', ',"A:B|C-D")) 
             
    print('\n------- Fourth test -------')
    obj = re.compile("\w*PL\w*",re.I)#'I' means ignorecase
    print('obj.findall("Nice apple") : ', obj.findall("Nice apple"))
    
    print('\n------- Final test -------')
    print('Password stability check')
    text = input('Enter yout password :')
    print('If your password safe?? : ', bool(issafe(text)))
    
else:
    print('Func_called - imported')
    
'''
----------result----------
Func_called - main

------- Fisrt test -------
Find pl in "Nice apple"
re.match : False
re.search : True
Cannot find 'pl' in match because string has spaces

------- Second test -------
Find pl in "Nice apple"
re.findall("\w*pl\w*","Nice apple") :  ['apple']

------- Third test -------
Find pl in "Nice apple" and replace "##"
re.sub('pl','##',"Nice apple") :  Nice ap##e

Replace example
re.sub('[:,|,-]',', ',"A:B|C-D") :  A, B, C, D

------- Fourth test -------
obj.findall("Nice apple") :  ['apple']

------- Final test -------
Password stability check

Enter yout password :1q2W3E4q2g4h
If your password safe?? :  True
--------------------------

'''