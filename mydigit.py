from login_sign_base import LoginSign
import time
from logging_sign import logging
from lxml import etree


class Mydigit(LoginSign):
    def __init__(self, username, password, encoding):
        LoginSign.__init__(self, username, password, encoding)

    def get_verif(self):
        r = self.session.get("http://bbs.mydigit.cn/index.php")
        selector = etree.HTML(r.text)
        time.sleep(1)
        return selector.xpath("//input[@name='verify']/@value")[0]

    def url_gen(self, action):
        if action == 'login':
            return 'http://bbs.mydigit.cn/login.php'
        if action == 'sign':
            return 'http://bbs.mydigit.cn/jobcenter.php'

    def data_gen(self, action):
        return {"jumpurl": "http://bbs.mydigit.cn/index.php", "step": "2", "ajax": "1", "lgt": "2",
                "pwuser": self.username, "pwpwd": self.password} if action == 'login' else {"step": "2"}

    def head_gen(self, action):
        return {'Host': 'bbs.mydigit.cn'}

    def params_gen(self, action):
        date = str(time.time() + 2).replace('.', '')[:13]
        if action == 'login':
            return {'nowtime': date, 'verify': self.get_verif()}
        if action == 'sign':
            return {'action': 'punch', 'verify': self.get_verif(), 'nowtime': date}


@logging
def main():
    m = Mydigit('1518598569@qq.com', 'Lqmy986156', 'gbk')
    m.do('login')
    if m.check('success'):
        time.sleep(2)
        m.do('sign')
        if m.check('M币'):
            m.log_success()

if __name__ == '__main__':
    main()
