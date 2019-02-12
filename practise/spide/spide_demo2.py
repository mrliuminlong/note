
import requests
import json
import os,re
 
 
def get():
    str = input("请输入查询的城市：（汉字吆）")
    url ='http://wthrcdn.etouch.cn/weather_mini?city='+str
    response= requests.get(url)
    wearher_json=json.loads(response.text)
    if "data" not in wearher_json :
        print("未查询到该城市，请从新查询")
        return get()
    else:
        
        a=wearher_json['data']
        print("当前位置："+a['city'])
        print("温馨提示："+a['ganmao'])
        print("当前温度："+a['wendu']+'℃')
        print("昨天："+a['yesterday']['date'])
        print("风力："+a['yesterday']['fl'][9:\
        [m.start() for m in re.finditer(']', a['yesterday']['fl'])][0]])
        print("风向："+a['yesterday']['fx'])
        print(a['yesterday']['high'])
        print(a['yesterday']['low'])
        print("天气："+a['yesterday']['type'])
        print("--------------------------------")
        for i in range(0,5):
            print("时间："+a["forecast"][i]['date'])
            print('风力: '+a["forecast"][i]['fengli'][9:\
            [m.start() for m in re.finditer(']', a['yesterday']['fl'])][0]])
            print('风向：'+a["forecast"][i]['fengxiang'])
            print(a["forecast"][i]['high'])
            print(a["forecast"][i]['low'])
            print("天气："+a["forecast"][i]['type'])
            print("--------------------------------")
	url ='http://api.help.bj.cn/apis/aqi?id='
    response= requests.get(url)
    if response.text=='':
        print("未查询到该城市，请从新查询")
        return get()
    else :
        a=json.loads(response.text)
        print("当前位置："+a['city'])
        print("空气污染指数："+a['aqi'])
        print("采样点信息如下：")
        pos = a["data"]
        for i in range(0,len(pos)):
            print("采集点: "+pos[i]['add'])
            print("空气污染指数: "+pos[i]['aqi'])
            print("天气质量等级: "+pos[i]['lv']+"级")
            print("天气评价: "+pos[i]['per'])
            print("PM2.5 : "+pos[i]['pm25'])
            print("--------------------------------")
    os.system("pause")
 
 
if __name__ == '__main__':
    print("天气查询小工具")
    ##圣诞树
    for i in range(0,3):
        for j in range(4,i,-1):
            if j>i:
                print(" ",end="")
        for j in range(0,2*i+1):
            print("*",end="")
        print("\n")
    for i in range(0,4):
        for j in range(4,0,-1):
            if j>i:
                print(" ",end="")
        for j in range(0,2*i+1):
            print("*",end="")
        print("\n")
    for i in range(0,5):
        for j in range(4,0,-1):
            if j>i:
                print(" ",end="")
        for j in range(0,2*i+1):
            print("*",end="")
        print("\n")
    for i in range(0,5):
        for j in range(0,3):
            print(" ",end="")
        for j in range(0,3):
            print("*",end="")
        print("\n")
    for i in range(0,2):
        for j in range(0,10):
            print("*",end="")
        print("\n")
    get()        
 
