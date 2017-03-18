from login_sign_base import LoginSign
import time
from logging_sign import logging
import random


class TianHui(LoginSign):
    def __init__(self, username, password):
        LoginSign.__init__(self, username, password)

    def url_gen(self, action):
        if action == 'login':
            return 'http://www.mytianhui.com/webapi/yjf/UserLogin'
        if action == 'sign':
            return 'http://www.mytianhui.com/webapi/yjf/Sign'

    def data_gen(self, action):
        return {'username': self.username, 'password': self.password, 'saveCookie': ''} if action == 'login' else ''

    def head_gen(self, action):
        return {'Host': 'www.mytianhui.com'}

    def params_gen(self, action):
        return ''


@logging
def main():
    m = TianHui('18994796806', 'Lqth986156')
    m.do('login')
    if m.check('"error":0'):
        time.sleep(random.randint(1, 300))
        m.do('sign')
        if m.check('签到获得'):
            m.log_success()

if __name__ == '__main__':
    main()
