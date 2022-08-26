#coding=gb18030
import requests,json,os

# server酱开关，填off不开启(默认)，填on同时开启cookie失效通知和签到成功通知
# sever = 'off'

# 填写server酱sckey,不开启server酱则不用填
sckey = 'on'

# 填入glados账号对应cookie
cookie = '_ga=GA1.2.118034753.1655121120; koa:sess=eyJ1c2VySWQiOjE3MjA1OCwiX2V4cGlyZSI6MTY4MTcxOTkwNzcxNiwiX21heEFnZSI6MjU5MjAwMDAwMDB9; koa:sess.sig=t6-2eHj-wx0LtD5SQNikWmNPGFw; _gid=GA1.2.768372009.1660044450; Cookie=enabled; Cookie.sig=lbtpENsrE0x6riM8PFTvoh9nepc; __cf_bm=L_ug2R4CGCAPYBk50xNSdnqjKFXqmCFniy_ZkBTQBbk-1660112867-0-ActA93md1RzAltix4iGkMsJeRzTNPxZ3n95lkoiPzVfgL5X5nu2whIIHyXoX151ZKbi8wtwWsME8D5pUo9Hz8hvskeXaeMxGaITEiNQGHx5HIPsGjg1xSXbCY/JzU1LtZA==; _gat_gtag_UA_104464600_2=1'

def start():
    url= "https://glados.rocks/api/user/checkin"
    url2= "https://glados.rocks/api/user/status"
    referer = 'https://glados.rocks/console/checkin'
    #checkin = requests.post(url,headers={'cookie': cookie ,'referer': referer })
    #state =  requests.get(url2,headers={'cookie': cookie ,'referer': referer})
    origin = "https://glados.rocks"
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47"
    payload={
        'token': 'glados.network'
    }
    checkin = requests.post(url,headers={'cookie': cookie ,'referer': referer,'origin':origin,'user-agent':useragent,'content-type':'application/json;charset=UTF-8'},data=json.dumps(payload))
    state =  requests.get(url2,headers={'cookie': cookie ,'referer': referer,'origin':origin,'user-agent':useragent})
   # print(res)


    if 'message' in checkin.text:
        mess = checkin.json()['message']
        time = state.json()['data']['leftDays']
        time = time.split('.')[0]
        print(time)
        if sever == 'on':
            requests.get('https://sc.ftqq.com/' + sckey + '.send?text='+mess+'，you have '+time+' days left')
    else:
        requests.get('https://sc.ftqq.com/' + sckey + '.send?text=cookie过期')

def main_handler(event, context):
  return start()

if __name__ == '__main__':
    start()
