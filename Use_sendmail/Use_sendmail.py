import sendgrid
from sendgrid.helpers.mail import Email,  Mail, Content

API_KEY = 'SG.ywKWUHMCSgqQ1WdYnBNaSA.xxxxxxxxxxxxxxxxxxxxxxxxxxxxx-xxxxxxxxxxxxx'
#API_KEY format is 'XX.xxxxxxx~~-xxxxxxxxxxxxx'
sg = sendgrid.SendGridAPIClient(apikey=API_KEY)

def send_email(email, name):
    from_email = Email("wntjdals2012@gmail.com")
    #If you enter the wrong email, a compilation error will occur.
    to_email = Email(email)
    subject = 'This is email subject'
    content = Content("text/plain","This is content of email.\n Hi " + name + '!')
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)
    
if __name__ == '__main__':
    print('Func_called - main')
    send_email('wntjdals2015@naver.com', 'Sungmin-Joo')
    '''
    send_email's first parameter is the recipient's email address.
    send_email's second parameter is the recipient's name
    '''
    print('Done')
else:
    print('Func_called - imported')
    
'''
---------- result ----------
Func_called - main
202
b''
Server: nginx
Date: Tue, 12 Mar 2019 09:27:29 GMT
Content-Type: text/plain; charset=utf-8
Content-Length: 0
Connection: close
X-Message-Id: HR3UxtslRXCR81BF0x6twQ
Access-Control-Allow-Origin: https://sendgrid.api-docs.io
Access-Control-Allow-Methods: POST
Access-Control-Allow-Headers: Authorization, Content-Type, On-behalf-of, x-sg-elas-acl
Access-Control-Max-Age: 600
X-No-CORS-Reason: https://sendgrid.com/docs/Classroom/Basics/API/cors.html

Done
----------------------------
'''