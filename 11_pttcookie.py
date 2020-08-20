import requests
from bs4 import BeautifulSoup

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
cookie = {'over18':'1'}
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

res = requests.get(url, headers=headers,cookies=cookie)
print(res.text)

soup = BeautifulSoup(res.text,'lxml')