from urllib import request
url = 'http://tw.yahoo.com/'
req = request.urlopen(url)
bs = req.read()
html = bs.decode('utf-8')
print(html)
