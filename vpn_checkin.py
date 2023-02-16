# 只要机场网站''' Powered by SSPANEL ''',就可以进行签到
# 特别感谢原脚本作者 @bighammer-link
# 以及青龙面板通知模块作者 @Kirin
# Modify: benlw4,2023-02-16
# 使用方法，订阅此脚本到青龙面板，并修改对应的url，登陆用户名及密码即可
import requests, json, re, os
from sendNotify import *


session = requests.session()
# 以下为修改区-开始
url = '' # 机场的地址
email = '' # 配置用户名（一般是邮箱）
passwd = '' # 配置用户名对应的密码 和上面的email对应上
sendmesg = True # 默认开启通知
# 修改区-结束
login_url = '{}/auth/login'.format(url)
check_url = '{}/user/checkin'.format(url)


header = {
        'origin': url,
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
data = {
        'email': email,
        'passwd': passwd
}
try:
    print('进行登录...')
    response = json.loads(session.post(url=login_url,headers=header,data=data).text)
    print(response['msg'])
    # 进行签到
    result = json.loads(session.post(url=check_url,headers=header).text)
    print(result['msg'])
    content = result['msg']
    # 进行推送
    if sendmesg:
        send('机场签到通知[Party]',content)  
except:
    content = '签到失败,请检查'
    print(content)
    if sendmesg:
        send('机场签到通知',content)
