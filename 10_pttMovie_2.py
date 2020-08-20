import requests
from bs4 import BeautifulSoup
import os

if not os.path.exists('pttmovie'): #自動存入pttmovie的資料夾
    os.mkdir('pttmovie')

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'} #建立逼投的user-agent讓使用者看起來更真

url = 'https://www.ptt.cc/bbs/movie/index.html' #把網址貼上


for i in range(0,5): #爬五次

    res = requests.get(url, headers=headers) #對網站進行請求

    soup = BeautifulSoup(res.text,'lxml') #建立物件soup來抓取,請求的網頁內容

    title_list  = soup.select('div.title') #select 出來的為list

    for title_soup in title_list:
        try:
            title =title_soup.select('a')[0].text #取得標題
            title_url = 'https://www.ptt.cc' + title_soup.select('a')[0]['href'] #加上網域取得文章網址
            #再取得文章內文
            res_article = requests.get(title_url,headers=headers) #取得每個標題的文章內容
            soup_article = BeautifulSoup(res_article.text,'lxml')
            article_content_list = soup_article.select('#main-content')#把內文都抓出來
            article_content = article_content_list[0].text.split('※ 發信站')[0] #用發信站來分割文章內容與回文
            try:
                    with open('./pttmovie/%s.txt'%(title),'w',encoding='utf-8') as f:#如果檔名出現"/"不給儲存時'
                        f.write(article_content)
            except FileNotFoundError as e:
                    print(e)
                    print(title)
                    with open('./pttmovie/%s.txt'%(title).replace('/','-'),'w',encoding='utf-8') as f:#把"/"的非法字元換成'-'
                        f.write(article_content)
            print(title)
            print(title_url)
            print(article_content)
            print('============================================================')

        except IndexError as e :
            print(title_soup)