from urllib import request
from bs4 import BeautifulSoup


headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
url = 'https://www.ptt.cc/bbs/Baseball/index.html'

req = request.Request(url=url,headers=headers)
res  = request.urlopen(req)

soup = BeautifulSoup(res.read(),'html.parser')


logo = soup.findAll('a', {'id':'logo'})
logo = soup.findAll('a',  id = 'logo') #寫法同上
logo = soup.select('a[id="logo"]') #寫法同上
logo =soup.select('a#logo') #寫法同上
print(logo)
print(logo[0])
print(logo[0].text)
print('https://www.ptt.cc'+logo[0]['href'])




