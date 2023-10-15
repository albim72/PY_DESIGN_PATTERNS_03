from abc import ABCMeta,abstractmethod
import urllib.request
import urllib.parse


class ResourceContent:
    def __init__(self,imp):
        self._imp = imp

    def show_content(self,path):
        self._imp.fetch(path)

class ResourceContentFetcher(metaclass=ABCMeta):
    @abstractmethod
    def fetch(self,path):
        pass


class URLFetcher(ResourceContentFetcher):
    def fetch(self, path):
        req = urllib.request.Request(path)
        with urllib.request.urlopen(req) as response:
            if response.code == 200:
                this_page = response.read()
                print(this_page)

class LocalFileFetcher(ResourceContentFetcher):
    def fetch(self, path):
        with open(path,encoding='utf-8') as f:
            print(f.read())

def main():
    url_fetcher = URLFetcher()
    iface = ResourceContent(url_fetcher)
    iface.show_content('http://python.org')

    print("_"*30)

    locals_fetcher = LocalFileFetcher()
    iface = ResourceContent(locals_fetcher)
    iface.show_content('info.txt')

if __name__ == '__main__':
    main()
