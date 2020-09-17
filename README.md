# sspanel-automaticcheckin
基于项目https://github.com/zhjc1124/ssr_autocheckin 修改,支持Server酱微信推送

sspanel自动签到脚本(腾讯云函数)
~~适用于Theme by editXY~~

![wRqn2t.png](https://s1.ax1x.com/2020/09/17/wRqn2t.png)

~~其他主题无法使用按下图修改~~

问题已解决！
其他主题适配请issues

**Tip:此流量不是手机运营商流量，是科学上网的流量，懂得自然懂。机场地址填机场官网地址，不是填订阅的地址，注意这一点。有问题欢迎issues**


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
        # 酷推qq推送
        self.ktkey = '**********'
  ```
  3. 配置云函数定时触发
  
# 云函数运行截图
![wRbQAJ.png](https://s1.ax1x.com/2020/09/17/wRbQAJ.png)

