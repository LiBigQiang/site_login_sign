from login_sign_base import LoginSign
import time
from logging_sign import logging


class Acfun(LoginSign):
    def __init__(self, username, password):
        LoginSign.__init__(self, username, password)

    def url_gen(self, action):
        if action == 'login':
            return 'http://www.acfun.cn/login.aspx'
        if action == 'sign':
            return 'http://www.acfun.cn/webapi/record/actions/signin'

    def data_gen(self, action):
        return {'username': self.username, 'password': self.password} if action == 'login' else ''

    def head_gen(self, action):
        return {'host': 'www.acfun.cn'}

    def params_gen(self, action):
        date = str(time.time() + 2).replace('.', '')[:13]
        return {'channel': '0', 'date': date} if action == 'sign' else ''


@logging
def main():
    m = Acfun('18994796806', 'Lqhfy986156')
    m.do('login')
    if m.check('lq1518598569'):
        time.sleep(2)
        m.do('sign')
        if m.check('蕉'):
            m.log_success()

if __name__ == '__main__':
    main()
