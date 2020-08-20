import requests
from bs4 import BeautifulSoup

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

url = 'https://www.ptt.cc/bbs/movie/index.html'

res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text,'lxml')

title = soup.find_all('div',class_ = 'title')
print([title.select('a')[0].text for title in title])


title = soup.find_all('div',class_ = 'title',a  = 'href')


