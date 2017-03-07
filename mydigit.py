import time
from webbase import WebBase
from logging_sign import logging
from lxml import etree


class MyDigit(WebBase):
    def __init__(self, username='', password='', encoding='utf8'):
        WebBase.__init__(self)
        self.username = username
        self.password = password
        self.encoding = encoding

    def get_verif(self):
        page = self.opener.open("http://bbs.mydigit.cn/index.php").read().decode(self.encoding)
        selector = etree.HTML(page)
        time.sleep(0.5)
        return selector.xpath("//input[@name='verify']/@value")[0]

    def data_generator(self, action):
        if action == 'login':
            data = {
                'login': {"jumpurl": "http://bbs.mydigit.cn/index.php", "step": "2", "ajax": "1", "lgt": "2",
                          "pwuser": self.username,
                          "pwpwd": self.password}
            }
            self.data.update(data)
        if action == 'sign':
            data = {
                'sign': {"step": "2"}
            }
            self.data.update(data)

    def url_generator(self, action):
        if action == 'login':
            nowtime = str(time.time()).replace('.', '')[:13]
            verify = self.get_verif()
            url_login = 'http://bbs.mydigit.cn/login.php?nowtime=[]&verify=[]'.format(nowtime, verify)
            self.url.update({'login': url_login})
        if action == 'sign':
            nowtime = str(time.time()).replace('.', '')[:13]
            verify = self.get_verif()
            url_sign = 'http://bbs.mydigit.cn/jobcenter.php?action=punch&verify=[]&nowtime=[]'.format(verify, nowtime)
            self.url.update({'sign': url_sign})

    def head_generator(self):
        head = {
            'Host': 'bbs.mydigit.cn',
        }
        return head


@logging
def main():
    username = "username"  # 邮箱(用户名登录需修改post内容)
    password = "password"  # 密码
    encoding = 'gbk'
    instance = MyDigit(username=username, password=password, encoding=encoding)
    if 'success' in instance.do('login'):
        time.sleep(0.5)
        print(1)
        if 'M币' in instance.do('sign'):
            print(instance.now_time + '签到成功')

if __name__ == "__main__":
    main()
