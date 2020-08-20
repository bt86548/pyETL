import requests
import json
from urllib import request #此方法下載圖片沒用到header,所以可能無法爬進去網站
from bs4 import BeautifulSoup
'''***********dcard往下拉會自動讀取頁面用get方法***********'''
'''抓到網頁json形式'''
headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
url = 'https://www.dcard.tw/service/api/v2/forums/game/posts?limit=30&before=233743555'
     #url後面的before,只會搜尋在此before之前的文章
res = requests.get(url,headers=headers)
print(res.text) #回傳網頁json的字串

json_data = json.loads(res.text) #字串被轉換為串列
print(json_data[0])
print(json_data[1])
print(json_data[2])
print(json_data[3])

for k in json_data[0]: #把key值取出來,每個迴圈裡面都是一篇文章
    print(k)
print('=================================')
for k in json_data[1]: #把key值取出來
    print(k)

'''把標題拿出來'''
for t in json_data:
     #json格式中會自動轉換型別
    title_name = t['title']
    print(title_name)
    #抓出文章網址
    article_url = 'https://www.dcard.tw/f/game/p/'+str(t['id'])
    print(article_url)
    #抓出圖片
    image_url_list = [img['url'] for img in t['mediaMeta']]
    print(image_url_list)
    for image_url in image_url_list:
        #urlretrieve後面接的參數為儲存的位置
        #request.urlretrieve(image_url, './dcardimg/' + image_url.split('/')[-1])
        #因為網站是用Request Method: GET方法,所以可以用get
        res_img = requests.get(image_url, headers=headers)#直接訪問圖片的網址
        img_content = res_img.content
        with open('./dcardimg/' + image_url.split('/')[-1],'wb') as f:
            f.write(img_content)