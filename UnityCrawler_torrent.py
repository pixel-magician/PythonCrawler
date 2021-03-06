# =========================================
# 抓取Unity官网所有未加壳安装包版本的种子文件
# by 像素魔法师
# =========================================


import requests
import re
import json
import sys
import urllib.request
import os

url = 'https://unity3d.com/get-unity/download/archive'
# https://download.unity3d.com/download_unity/d81f64f5201d/Unity-2020.1.14f1.torrent
# https://download.unity3d.com/download_unity/413dbd19b6dc/Unity-2017.4.20f2.torrent?_ga=2.259206474.1587081780.1606449822-854676428.1606449822
# https://download.unity3d.com/download_unity/3fb31a95adee/Unity.torrent?_ga=2.90270170.1587081780.1606449822-854676428.1606449822
# https://download.unity3d.com/download_unity/574eeb502d14/Unity.torrent?_ga=2.62131692.1587081780.1606449822-854676428.1606449822
strhtml = requests.get(url)  # Get方式获取网页数据
pattern = re.compile(
    "https://download.unity3d.com/download_unity/.*?/Unity-.*?.torrent")
temp = re.findall(pattern, strhtml.text)
#对结果去重
result = []
for i in temp:
    if i not in result:
        result.append(i)


path = sys.path[0]
path1 = path + r"/Unity_torrent.json"
path2 = path + r"/Unity_torrent_追加.json"
# pathtorrent=path + r"\Unity_torrent_追加.txt"
print(path1)
print(path2)
# 读取已保存数据
if os.path.exists(path1):
    f = open(path1, "r")
    jsonString = f.read()
    result_O = json.loads(jsonString)
    f.close()
    # 获取新增的数据
    result_Append = list(set(result).difference(set(result_O)))

    # 保存新增的数据
    f = open(path2, 'w')
    jsonString = json.dumps(result_Append)
    f.write(jsonString)
    f.close()

# 保存下载的数据
f = open(path1, 'w')
jsonString = json.dumps(result)
f.write(jsonString)
f.close()


# 下载种子文件

# for item in result_Append:
