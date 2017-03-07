from webbase import WebBase
import time
import random
import json
from logging_sign import logging


class JiSiBar(WebBase):
    def __init__(self, username='', password=''):
        WebBase.__init__(self)
        self.username = username
        self.password = password
        self.xsrf = self.get_xsrf()
        self.page = ''

    def get_xsrf(self):
        self.opener.open('https://www.jisibar.com/surveypool/yjf')
        for cookie in self.cookie:
            if cookie.name == '_xsrf':
                return cookie.value

    def url_generator(self, action):
        if action == 'login':
            url = {
                'login': 'https://www.jisibar.com/ajax/esurfingDo',
                'sign': 'https://www.jisibar.com/ajax/esurfingDo',
                'vote': 'https://www.jisibar.com/ajax/esurfingDo',
                'lottery': 'https://www.jisibar.com/ajax/esurfingDo',
            }
            self.url.update(url)

    def data_generator(self, action):
        if action == 'login':
            data = {
                'login': {'user': self.username,
                          'password': self.password,
                          'action': 'login',
                          'xsrf': self.xsrf},
                'sign': {'action': 'checkin',
                         'xsrf': self.xsrf},
            }
            self.data.update(data)
        if action == 'vote':
            message = r'{}'.format(self.page)
            message = json.loads(message)
            options = message['data']['options']
            option = options[random.randint(1, len(options))]
            data = {'vote': {'action': 'vote',
                             'xsrf': self.xsrf,
                             'poll_id': option['pid'],
                             '{}_{}'.format(option['pid'], option['oid']): option['random']}
                    }
            self.data.update(data)
        if action == 'lottery':
            message = r'{}'.format(self.page)
            message = json.loads(message)
            lid = message['data']['checkin']['lottery']
            data = {'lottery': {'action': 'lottery',
                                'lid': lid,
                                'xsrf': self.xsrf, }
                    }
            self.data.update(data)

    def head_generator(self):
        head = {
            'Host': 'www.mytianhui.com',
            'Connection': 'keep-alive', }
        return head


@logging
def main():
    username = 'username'
    password = 'password'
    instance = JiSiBar(username=username, password=password)
    time.sleep(0.5)
    if 'success' in instance.do('login'):
        time.sleep(1)
        instance.page = instance.do('sign')
        if '签到成功' in instance.page:
            print(instance.now_time() + '签到成功')
        if '抽奖机会' in instance.page:
            page = instance.do('lottery')
            if '"code":1' in page:
                print(instance.now_time + '签到成功', end='')
                page = json.loads(page)
                print('连续5天奖励{}:{}'.format(page['data']['unit'], page['data']['prize']))
        if '有个投票' in instance.page:
            time.sleep(0.5)
            instance.page = instance.do('vote')
            if '签到成功' in instance.page:
                print(instance.now_time + '签到成功')
            if '抽奖机会' in instance.page:
                page = instance.do('lottery')
                if '"code":1' in page:
                    print(instance.now_time + '签到成功', end='')
                    page = json.loads(page)
                    print('连续5天奖励{}:{}'.format(page['data']['unit'], page['data']['prize']))

if __name__ == '__main__':
    main()
