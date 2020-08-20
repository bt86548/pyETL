import requests
from bs4 import BeautifulSoup
'''爬取其中一篇文章的內容'''
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

url  ='https://www.ptt.cc/bbs/movie/M.1590167478.A.AF8.html'

res_article = requests.get(url,headers=headers)
soup_article = BeautifulSoup(res_article.text,'lxml')
article_content_list = soup_article.select('#main-content')#把內文都抓出來
print(article_content_list[0].text) #列出所有內文
print(article_content_list[0].text.split('※ 發信站')[0]) #以發信站分割內文與回文

