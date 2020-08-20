from bs4 import BeautifulSoup
import requests
import urllib.request as req
from urllib.request import urlopen
import bs4

# url='https://www.ptt.cc/bbs/Gossiping/M.1590659136.A.A1D.html'
url = 'https://www.ptt.cc/bbs/Gossiping/M.1567851620.A.90E.html'

request = req.Request(url, headers={
        "cookie": "over18=1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
})
with req.urlopen(request) as response:
        # urllib.error.HTTPError: HTTP Error 403: Forbidden 因網站會誤認錯誤,覺得連線是異常輸入
    data = response.read().decode("utf-8")
    # 解析原始碼,取得每篇文章的標題
root = bs4.BeautifulSoup(data, "html.parser")  # 讓beautifulsoup解析HTNL的文章
main_content = root.select('#main-content')[0].text.split('--')[0]
print(main_content)
print('---split---')
push_up  = 0
push_down =0
push_list = root.findAll('div',class_='push')
for i in push_list:
        a = i.select('span')[0].text
        if '推' in a:
                push_up += 1
        elif '噓' in a:
                push_down += 1
print('推:',push_up)
print('噓:',push_down)
print('分數',str(push_up-push_down))
author = root.findAll('span',class_='article-meta-value')[0].text
print('作者:',author)
title = root.findAll('span',class_='article-meta-value')[2].text
print('標題:',title)
time = root.findAll('span',class_='article-meta-value')[3].text
print('時間:',time)

