
'''如果有需要使用post資料的網址可以使用此方式假裝有data進去'''
import requests

url = 'http://ea4b5b22.ngrok.io/hello_post'

res_get = requests.get(url)
print(res_get.text)
print('==============')
#創造postdata
data= {'username':'Alkll'}
res_post = requests.post(url,data=data)
print(res_post.text)

