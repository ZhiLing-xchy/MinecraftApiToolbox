import base64 as base
import json
import os
import time
import urllib
import requests
def downloadskin(id):
    download_result = {
        "time":0,
        "url":"",
        "path":"",
        "error":""
    }
    try:
        hjson = json.loads(urllib.request.urlopen('https://api.mojang.com/users/profiles/minecraft/' + id).read())#按照MOJANG api格式请求JSON
    except:
        download_result["error"] = "getskin_error"
        return(download_result)
    else:
        url = 'https://sessionserver.mojang.com/session/minecraft/profile/' + hjson['id']
        html = urllib.request.urlopen(url)
        hjson = json.loads(html.read())
        hjson = hjson['properties']
        BASE64_JSON = hjson[0]['value']
        #由于MOJANG的存储特性，在第二份JSON文件中含有被BASE64编码的另一份JSON文件，需要进行BASE64解码
        #第三次JSON解析
        hjson = json.loads(''.join(str(base.b64decode(BASE64_JSON).decode())))
        skin_url = hjson['textures']['SKIN']['url']
        #下载用代码
        path ="./result/" + id + ".png"

        download_result["path"] = path

        r=requests.get(skin_url)
        urllib.request.urlopen(skin_url)
        with open(path,"wb") as f:
            f.write(r.content)
        f.close()

        download_result["time"] = len(r.content)
        download_result["url"] = url

        return(download_result)