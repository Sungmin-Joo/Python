import requests
import os

#test in raspi
file_root='/home/pi/dip/download/'
def Find_dir(root):
    return os.listdir(root)

url='http://192.168.43.79:5000/download'
response = requests.get(url=url)
print(response.status_code)
A=response.json()
print(type(A))
for key,val in A.items():
    f=open(file_root+key,'w')
    f.writelines(val)
    f.close()
    print(key , val)
