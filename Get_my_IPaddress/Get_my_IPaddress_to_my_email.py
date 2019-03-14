import socket
import sendgrid
from sendgrid.helpers.mail import Email,  Mail, Content

API_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
#API_KEY format is 'XX.xxxxxxx~~-xxxxxxxxxxxxx'
sg = sendgrid.SendGridAPIClient(apikey=API_KEY)

def send_email(email, IP):
    from_email = Email("wntjdals2012@gmail.com")
    #If you enter the wrong email, a compilation error will occur.
    to_email = Email(email)
    subject = "Raspberry Pi's IP information"
    content = Content("text/plain","Raspberry Pi's IP is " + IP )
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)

if __name__ == '__main__':
    print('Func_called - main')
    My_IP = socket.gethostbyname(socket.gethostname())
    print("My local ip is " + My_IP)
    send_email('wntjdals2015@naver.com', My_IP )
    print("complete")
else:
    print('Func_called - imported')
    
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