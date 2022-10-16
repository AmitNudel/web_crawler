
import requests
from bs4 import BeautifulSoup
import validators

class Crawler(object):
    def get(self, url):
        raise NotImplementedError()
    def verify(self, url):
        raise NotImplementedError()

class Link_crawler(Crawler):

    def verify(self, url):
        valid = validators.url(url)
        if valid==True:
            print("Url is valid: ", url)
        else:
            print("Invalid url: ", url)

    def get(self,url):
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        
        urls = []
        for link in soup.find_all('a'):
            self.verify(link.get('href'))


class Photo_crawler(Crawler):

    def __init__(self):
        self.dict = {}

    def verify(self, url):
        if url in self.dict:
            return 1
        return 0

    def get(self,url):
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        
        for item in soup.find_all('img'):
            if 0 == self.verify(url):
                self.dict[item] = 1
                print("img: ",item['src'])
