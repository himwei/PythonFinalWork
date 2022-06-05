import requests
import json
#import demjson#解决使用dump转成json存到本地后会发现原本的"号边\"多了转义字符
import re
import numpy as np

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }
request = requests.get('https://cdn.mdeer.com/data/yqstaticdata.js',headers=headers)

# data=str(request.content,'utf-8')#将request.content返回的byte通过str方法转成utf8 为什么不用text方法呢 因为默认传回的数据导致中文乱码 所以不用text方法而用content来获取到原始的byte数据后再手动转为utf8 这样中文就正常显示了
data = request.text

data = data[19:-1]

data_json = json.loads(data)

# print(data_json['incTrend'])





