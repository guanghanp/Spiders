import requests
import time
import random
import hashlib

class youdao():
    def __init__(self):
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'Referer': 'http://fanyi.youdao.com/',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-481680322@10.169.0.83;'
        }
        self.data = {
            'i': None,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': None,
            'sign': None,
            'ts': None,
            'bv': None,
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME'
        }
    
    def translate(self, word):
        ts = str(int(time.time()*10000))
        salt = str(int(time.time()*10000)) + str(int(random.random()*10))
        sign = 'fanyideskweb' + word + salt + '97_3(jkMYg@T[KZQmqjTK'
        sign = hashlib.md5(sign.encode('utf-8')).hexdigest()
        bv = '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        bv = hashlib.md5(bv.encode('utf-8')).hexdigest()
        self.data['i'] = word
        self.data['salt'] = salt
        self.data['sign'] = sign
        self.data['ts'] = ts
        self.data['bv'] = bv
        response = requests.post(self.url, headers=self.headers, data=self.data)
        try:
            result = [response.json()['translateResult'][0][0].get('tgt')]
        except KeyError:
            result = ['No translation']
        return result

def main():
    translator = youdao()
    while True:
        try:
            word = input('Word to translate:')
            result = translator.translate(word)
            print(result)
        except KeyboardInterrupt:
            break

if __name__ == '__main__':
    main()
    
