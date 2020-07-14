import requests


class NeteaseReview():
    def __init__(self,id=516997458):
        self.url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_'+str(id)
        self.params = {
            'offset':'0',
            'limit':'20'
        }
    
    def getComments(self):
        comments = []
        more = True
        while more:
            res = requests.get(self.url, params=self.params)
            json = res.json()
            print(json)
            for each in json['comments']:
                comments.append(each['content'])
            self.params['offset']= str(int(self.params['offset'])+20)
            more = json['more']
        print(self.params['offset'])
        return comments
            


def main():
    crawler = NeteaseReview()
    print(crawler.getComments())


if __name__ == '__main__':
    main()