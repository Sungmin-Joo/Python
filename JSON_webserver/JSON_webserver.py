# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
import json
 
test_data = None
app = Flask(__name__)
 
#Dapp.config['DEBUG'] = False 

@app.route("/test")
def test():
    print('Func_called')
    return "PyJoo " + str(test_data) 
 
@app.route("/curlc",methods=['GET','POST']) # C에서 ip address:port/router 주소로 전송햇음
def curlc():
    global test_data# 정말 test용 데이터
    if request.headers['Content-Type']== 'application/json': # c프로그램 CURLOPT_HTTPHEADER를 설정햇으니 같이 맞춰줌
        test_data=request.data.decode('utf-8') # binary로 날아오기 때문에 
        print(test_data,type(test_data)) # data 내용과 data의 type 확인
    return 0 # 이 부분은 응답 값이 필요가 없기때문에 0으로 넘겨버림. 요청에 대한 응답이 필요하면 그에 응하는 값을 return
 
 
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8008)

