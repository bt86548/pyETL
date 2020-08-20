'''不用cookie就可以進入八卦版的方式:session'''
import requests
from bs4 import BeautifulSoup

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
#準備進入cookie的網站
url='https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html'

ss = requests.session() #當session1執行完session2還是可以執行cookie=18

'''session1'''
#res = requests.get(url, headers = headers)
res = ss.get(url, headers = headers) #使用session的方法
soup = BeautifulSoup(res.text, 'lxml')
button = soup.select('button[class="btn-big"]')[0] #抓取button標籤中所有的輸出
print(button)
print(button['name']) #取得postdata : key 固定寫法
print(button['value']) #取得pstdata : value 固定寫法

# hidden  = soup.select('input') #當butoon值中有hidden時要抓hidden的方法
# print(hidden)

data = {}
data[button['name']] = button['value'] #
'''session1'''

# for k in hidden: #當butoon值中有hidden時要抓hidden的方法
#     data[k['name']]=k['value']
# print(data)



'''session2'''
target_url = 'https://www.ptt.cc/ask/over18'
#res_target =  requests.post(target_url,data=data,headers=headers)#目標網站
res_target = ss.post(target_url,data=data,headers=headers)
'''session2'''



'''session3'''
final_url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
#final_res = requests.get(final_url,headers=headers)
final_res = ss.get(final_url, headers=headers)
print(final_res.text)
'''session3'''

print(ss.session) #印出來確認cookie=18
