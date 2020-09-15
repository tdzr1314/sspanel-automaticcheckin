# -*- coding: utf-8 -*-
"""
@Time ： 2020/9/15 9:52
@Auth ： Ne-21
@Des : sspanel自动每日签到脚本
@File ：sspanel_qd.py
@IDE ：PyCharm
@Motto：Another me.
sspanel自动每日签到脚本，基于项目https://github.com/zhjc1124/ssr_autocheckin修改
"""
import requests

requests.packages.urllib3.disable_warnings()

class SspanelQd(object):
    def __init__(self):
        # 机场地址
        self.base_url = 'https://*****/'
        # 登录信息
        self.email = ''
        self.password = ''
        # Server酱推送
        self.sckey = ''

    def checkin(self):
        email = self.email.split('@')
        email = email[0] + '%40' + email[1]
        password = self.password

        session = requests.session()

        session.get(self.base_url, verify=False)

        login_url = self.base_url + '/auth/login'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }

        post_data = 'email=' + email + '&passwd=' + password + '&code='
        post_data = post_data.encode()
        response = session.post(login_url, post_data, headers=headers, verify=False)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Referer': self.base_url + '/user'
        }

        response = session.post(self.base_url + '/user/checkin', headers=headers, verify=False)
        print((response.json()).get('msg'))
        return (response.json()).get('msg')

    # Server酱推送
    def server_send(self, msg):
        if self.sckey == '':
            return
        server_url = "https://sc.ftqq.com/" + str(self.sckey) + ".send"
        data = {
                'text': msg,
                'desp': msg
            }
        requests.post(server_url, data=data)


    def main(self):
        msg = self.checkin()
        self.server_send(msg)

# 云函数入口
def main_handler(event, context):
    run = SspanelQd()
    run.main()

if __name__ == '__main__':
    run = SspanelQd()
    run.main()
