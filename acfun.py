import time
from webbase import WebBase
from logging_sign import logging


class Acfun(WebBase):
    def __init__(self, username='', password=''):
        WebBase.__init__(self)
        self.username = username
        self.password = password

    def url_generator(self, action):
        if action == 'login':
            date = str(time.time()+2).replace('.', '')[:13]  # time加二秒，登录时生成url比签到时间有几秒时间差
            url = {
                    'login': 'http://www.acfun.cn/login.aspx',
                    'sign': 'http://www.acfun.cn/webapi/record/actions/signin?channel=0&date={}'.format(date),
                }
            self.url.update(url)

    def data_generator(self, action):
        if action == 'login':
            data = {
                    'login': {'username': self.username, 'password': self.password},
                    'sign': {},
                }
            self.data.update(data)

    def head_generator(self):
        header = {
            'host': 'www.acfun.cn',
        }
        return header


@logging
def main():
    username = 'username'  # 用户名
    password = 'password'  # 密码
    instance = Acfun(username=username, password=password)
    print(10)
    if 'true' in instance.do('login'):
        time.sleep(2)
        if '蕉' in instance.do('sign'):
            print(instance.now_time + '签到成功!')

if __name__ == '__main__':
    main()
