from urllib import request
from bs4 import BeautifulSoup
import requests

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
url = 'https://www.ptt.cc/bbs/Baseball/index.html'

res = requests.get(url,headers=headers)
print(res.text)
soup = BeautifulSoup(res.text,'html.parser')
print(soup)

