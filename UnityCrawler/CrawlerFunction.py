import json


def WriteToJson(path: str, data: any):
    '''将数据以json文本的方式写到本地'''
    f = open(path, 'w')
    jsonString = json.dumps(data)
    f.write(jsonString)
    f.close()


def ReadFromJson(path: str):
    '''从本地文件读取json文本数据'''
    f = open(path, "r")
    jsonString = f.read()
    result = json.loads(jsonString)
    f.close()
    return result
