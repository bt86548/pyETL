'''上一頁'''
'''import套件'''
import requests
from bs4 import BeautifulSoup
'''設立user-agent及url'''
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

url = 'https://www.ptt.cc/bbs/movie/index.html'


for i in range(0,5):

    res = requests.get(url, headers=headers) #對網址進行請求,得到html的編碼

    soup = BeautifulSoup(res.text,'lxml') #利用beaitifulsoup轉換html的編碼

    title_list  = soup.select('div.title') #select出來的為list

    for title_soup in title_list:
        try:
            title =title_soup.select('a')[0].text #利用text取出標題文字
            title_url = 'https://www.ptt.cc' + title_soup.select('a')[0]['href'] #利用select取出標題網域
            print(title)
            print(title_url)
        except IndexError as e :
            print(title_soup)

    '''上一頁標籤'''
    page_url = soup.select('a[class="btn wide"]') #找到上頁標籤的class
    last_page = 'https://www.ptt.cc' + page_url[1]['href'] #給他完整的上一頁連結網址
    url = last_page


