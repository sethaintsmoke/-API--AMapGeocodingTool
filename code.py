import time
import json
import numpy as np
import requests
import math as Math
import pandas as pd

# 读取Excel文件
file_path = 'file-1'  # 替换为你的文件路径
df = pd.read_excel(file_path)

# AMap API的key
api_key = "key-1"


# 定义一个函数来调用AMap Geocoder API
def get_location(address):
    url = "https://restapi.amap.com/v3/geocode/geo"
    params = {
        "address": address,
        "key": api_key
    }
    response = requests.get(url, params=params)
    data = response.json()

    if data['status'] == '1' and data['geocodes']:
        location = data['geocodes'][0]['location']
        longitude, latitude = location.split(',')
        return latitude, longitude
    return None, None


# 读取地址1列，调用API获取地理坐标，并写入Converted_latitude和Converted_longtitude列
df['Converted_latitude'], df['Converted_longtitude'] = zip(*df['file-1'].apply(get_location))

# 保存更新后的数据到新的Excel文件
output_file_path = ('file-2')  # 替换为你想保存的文件路径
df.to_excel(output_file_path, index=False)