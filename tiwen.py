import requests
import time
import random
import json
headers=[{ "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36" },
 { "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68" },
 { "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56" }]
ti=str(time.strftime("%Y-%m-%d", time.localtime())) # 时间
hour=int(time.strftime("%H", time.localtime())) #小时
ls=[]
# 酷推机器人
def qmsg(name,txt):
    url = "https://qmsg.zendee.cn/send/0cb7ec3b53ee6db28ff921b6af54f9db"
    data= {'msg':str('【'+ ti+'】:' +name + txt + '@face=67@'),'qq':'2079986882'}
    requests.post(url, data)

def tiwen_daka(headers,name,id_uid):
    # 时间
    ti_for_title = ti  # 获取时间，这个时间是放在SBRQ里面
    # 体温打卡数据
    data_tiWen = {"ID": id_uid[0], "SBRQ": ti_for_title + " 00:00:00", "UID": id_uid[1], "UType": "1",
                    "WSTJSJ": ti_for_title + " 15:01:01", "WSTW": "36.5", "YXDM": "10623",
                    "ZCTJSJ": ti_for_title + " 15:01:01", "ZCTW": "36.6", "ZWTJSJ": ti_for_title + " 15:01:01",
                    "ZWTW": "36.5"}
    res=requests.post("https://yqfkapi.zhxy.net/api/ClockIn/SaveTem", data=data_tiWen, headers=headers)
    resp=eval(res.text)
    try:
        if resp['code']==200 and resp["info"]=="响应成功":
            print(name+":success")       
    except:
        print(name+":Error")
#         ls.append(0)
        qmsg(name,txt='体温填报失败')
    print("五分钟后下一个体温填报")
    time.sleep(60*50)
    
if __name__ == '__main__':
    try:
        tiwen_daka(headers=random.choice(headers),name="小周",id_uid=["8496477","1462508"])
        tiwen_daka(headers=random.choice(headers),name="琴琴",id_uid=["8517367","1463569"])
        tiwen_daka(headers=random.choice(headers),name="天宇",id_uid=["8742297","1462506"])
        tiwen_daka(headers=random.choice(headers),name="陈菲",id_uid=["8776518","1462528"])
        tiwen_daka(headers=random.choice(headers),name="东东",id_uid=["9008423","1462498"])
        tiwen_daka(headers=random.choice(headers),name="阿强",id_uid=["9002387","1462514"])
        print('全部成功------------')
        qmsg(name='',txt='全部体温填报成功')
    except:
        qmsg(name='',txt='体温填报出错')



    

   
