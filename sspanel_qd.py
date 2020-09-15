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
import re

requests.packages.urllib3.disable_warnings()

class SspanelQd(object):
    def __init__(self):
        # 机场地址
        self.base_url = 'https://****.net'
        # 登录信息
        self.email = '****@qq.com'
        self.password = '****'
        # Server酱推送
        self.sckey = 'SCU109245Tf34928bcea84db0a*************'

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
        msg1 = (response.json()).get('msg')

        info_url = self.base_url + '/user'
        response = session.get(info_url, verify=False)
        level = re.findall(r'\["Class", "(.*?)"],', response.text)[0]
        day = re.findall(r'\["Class_Expire", "(.*)"],', response.text)[0]
        rest = re.findall(r'\["Unused_Traffic", "(.*?)"]', response.text)[0]
        msg = "- 今日签到信息："+str(msg1)+"\n- 用户等级："+str(level)+"\n- 到期时间："+str(day)+"\n- 剩余流量："+str(rest)
        print(msg)
        return msg

    # Server酱推送
    def server_send(self, msg):
        if self.sckey == '':
            return
        server_url = "https://sc.ftqq.com/" + str(self.sckey) + ".send"
        data = {
                'text': "签到完成，点击查看详细信息~",
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
