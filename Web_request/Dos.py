# -*- coding: utf-8 -*-
import requests
url = 'http://www.q-net.or.kr/man001.do?gSite=Q&gId='
while(1):
    response = requests.get(url = url)
