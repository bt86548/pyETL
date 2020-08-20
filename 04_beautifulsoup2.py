from urllib import request
from bs4 import BeautifulSoup


headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
url = 'https://www.ptt.cc/bbs/Baseball/index.html'

req = request.Request(url=url,headers=headers)
res  = request.urlopen(req)

soup = BeautifulSoup(res.read(),'html.parser')

title = soup.findAll('div',class_= 'title') #產生list
print(title[0]) #擷取title中的第一行
print(title[0].text)
print(title[0].a)
print('https://www.ptt.cc/bbs' + title[0].select('a')[0]['href'])
