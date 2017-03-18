import requests
import time


class LoginSign:
    def __init__(self, username, password, encoding='utf8', debug=0):
        self.username = username
        self.password = password
        self.debug = debug
        self.r = ''
        self.session = requests.session()
        self.encoding = encoding
        self.header = {"Accept": "*/*",
                       "Accept-Encoding": "gzip, deflate",
                       "Accept-Language": "zh-CN,zh;q=0.8",
                       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64)  Chrome/56.0.2924.87 Safari/537.36", }
        self.session.headers.update(self.header)

    def do(self, action, method=''):
        url, data, headers, params = self.all_generator(action)
        if not method:
            self.r = self.session.post(url=url, data=data, headers=headers, params=params)
        if method == 'GET':
            self.r = self.session.get(url=url, data=data, headers=headers, params=params)
        self.r.encoding = self.encoding
        if self.debug:
            print(action+' result:'+self.r.text)

    def check(self, content):
        return True if content in self.r.text else False

    def all_generator(self, action):
        return self.url_gen(action), self.data_gen(action), self.head_gen(action), self.params_gen(action)

    def url_gen(self, action):
        pass

    def data_gen(self, action):
        pass

    def head_gen(self, action):
        pass

    def params_gen(self, action):
        pass

    @property
    def now_time(self):
        return time.strftime("%m-%d %H:%M:%S", time.localtime(time.time()))

    def log_success(self, message=' 签到成功！'):
        print(self.now_time + message)
