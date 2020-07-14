import requests
import re

res = requests.get('http://fanyi.baidu.com').text
token = re.findall(r"token: '(.*?)',",res)[0]
gtk = re.findall(r";window.gtk = '(.*?)';",res)[0]
print(token,gtk)