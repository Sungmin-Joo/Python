# -*- coding: utf-8 -*-
import wifi


def Search():
    wifilist = []

    cells = wifi.Cell.all('wlan0')

    for cell in cells:
        wifilist.append(cell)

    return wifilist
if __name__ == '__main__':
    # Search WiFi and return WiFi list
    print(Search())
    
'''
----------result----------
Func_called - main
My local ip is 114.xxx.xx.x
202
b''
Server: nginx
Date: Wed, 13 Mar 2019 05:15:57 GMT
Content-Type: text/plain; charset=utf-8
Content-Length: x
Connection: xxxxx
X-Message-Id: xxxxxxxxxxxxx
Access-Control-Allow-Origin: xxxxxxxxxx
Access-Control-Allow-Methods: xxxx
Access-Control-Allow-Headers: xxxxxxxxxxxxxxxx
Access-Control-Max-Age: xxx
X-No-CORS-Reason: xxxxxxxxxxxxxxxxxxxxxxxxxx


complete
--------------------------

'''