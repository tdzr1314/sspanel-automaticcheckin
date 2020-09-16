# sspanel-automaticcheckin
适用于sspanel自动签到脚本(腾讯云函数)

基于项目https://github.com/zhjc1124/ssr_autocheckin 修改,支持Server酱微信推送

# 用法
1. 下载本仓库，将`sspanel_qd.py`上传到腾讯云函数
2. 配置`sspanel_qd.py`中的`init`(如下)
 ```
 def __init__(self):
        # 机场地址
        self.base_url = 'https://****.net'
        # 登录信息
        self.email = '****@qq.com'
        self.password = '****'
        # Server酱推送
        self.sckey = 'SCU109245Tf34928bcea84db0a*************'
  ```
