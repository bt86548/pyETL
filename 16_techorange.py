import requests
import json #因為是動態網頁可能需要json
from bs4 import BeautifulSoup

'''科技報橘網站抓取post方法'''
headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
#url需要使用每次下拉找到的php檔
url = 'https://buzzorange.com/techorange/wp-admin/admin-ajax.php'

#帶入參數,從form data裡面挑
data = {
'action': 'fm_ajax_load_more',
'nonce': 'd8c08f1381',
'page': '7'}

#先猜測是否為json格式
res = requests.post(url,headers=headers,data=data)
json_data = json.loads(res.text)

# print(json_data)
# print(json_data.keys())
# print(json_data['data']) #發現為html格式

soup = BeautifulSoup(json_data['data'],'lxml')
title_list = soup.select('a[class = "post-thumbnail nljf"]')
title_list = soup.find_all('a',{'class': "post-thumbnail nljf"}) #寫法同上

for i in title_list:
    x = i['onclick'].split(',')
    print(i['onclick'].split(','))
    for j in x :
        print(j)

    # for link in bs.find_all('a', href=re.compile('^(http|www)((?!'+excludeUrl+').)*$')):
    #     if link.attrs['href'] is not None:
    #         if link.attrs['href'] not in externalLinks:
    #             externalLinks.append(link.attrs['href'])
    # return externalLinks
