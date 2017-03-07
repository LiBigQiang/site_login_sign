import http.cookiejar
import urllib.request
import urllib.parse
import gzip
import json
import time


class WebBase:
    def __init__(self, encoding='utf8', data_enctype=''):
        self.encoding = encoding
        self.data_enctype = data_enctype
        self.head_add = self.head_generator()
        self.opener = self.opener_generator()
        self.data = {}
        self.url = {}

    def opener_generator(self):
        self.cookie = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cookie))
        head = {
            # Client
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        }
        if self.head_add:
            head.update(self.head_add)
        header = []
        for key, value in head.items():
            if value:
                elem = (key, value)
                header.append(elem)
        opener.addheader = header
        return opener

    @staticmethod
    def ungzip(page):
        # 处理服务器发回的zip压缩网页
        try:  # 尝试解压
            page_unzip = gzip.decompress(page)
            return page_unzip
        except TypeError:
            return page

    def do(self, action):
        self.url_generator(action)
        self.data_generator(action)
        if self.data_enctype =='json':
            data_encode = json.dumps(self.data[action])
        else:
            data_encode = urllib.parse.urlencode(self.data[action]).encode()
        page = self.opener.open(self.url[action], data_encode)
        return self.ungzip(page).read().decode(self.encoding)

    @property
    def now_time(self):
        return time.strftime("%m-%d %H:%M:%S", time.localtime(time.time()))

    def data_generator(self, action):
        pass

    def url_generator(self,action):
        pass

    def head_generator(self):
        pass
