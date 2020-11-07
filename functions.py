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



def getuuid(id):
    result = {
        "uuid":"",
        "error":""
    }
    try:
        hjson = json.loads(urllib.request.urlopen('https://api.mojang.com/users/profiles/minecraft/' + id).read())
        #按照MOJANG api格式请求JSON
    except:
        result["error"] = "ID_to_UUID_error"
    else:
        result["uuid"] = hjson['id']
    return(result)



def getid(uuid):
    result = {
        "ids":"",
        "error":""
    }
    try:
        hjson = json.loads(urllib.request.urlopen('https://api.mojang.com/user/profiles/' + uuid + '/names').read())
        #按照MOJANG api格式请求JSON
    except:
        result["error"] = "UUID_to_ID_Fail"
    else:
        result["ids"] = hjson
    return(result)
    
    
def colloreggs():
    with open("./colloreggs.txt",'w',) as cegg:
        cegg.write(str(''.join(str(base.b64decode("5oGt5Zac5L2g5Y+R546w5b2p6JuL77yI6Jm954S25Lil5qC85p2l6K+054m55Yir566A5Y2V4oCm4oCm77yJ77yM5L2G56Wd6LS677yM5pei54S257+75Yiw5LqG6L+Z6YeM77yM6YKj5bCx54K55Liq5YWz5rOo5ZCnfui+k+WFpWluZm/mn6XnnIvmiJHnmoRCaWxpYmlsaei0puaIt+WTpn7vvIjooqvmiZMK5oC75LmL77yM5oiR5piv5LiN5aSq5aWi5pyb5pyJ5aSa5bCR5Lq655So5oiR55qE6L2v5Lu277yM5L2G5pei54S25L2g6IO955yL5Yiw77yM6K+B5piO5L2g6Iez5bCR6aG2552A572R57uc5bu25pe25LiKZ2l0aHVi77yI6Zmk6Z2e5oiR5Lul5ZCO5Zyo5YW25LuW5Zyw5pa55LiK5Lyg5LqG77yJ5LiL6L295LqG5pys6L2v5Lu277yM55+l5YeM5oiR5Zyo5q2k5a+55L2g6KGo56S66KG35b+D55qE5oSf6LCi77yBCuW4jOacm+aIkeS7peWQjuiDveeBq++8jOiiq+abtOWkmuS6uuefpemBk++8jOS5n+elneaEv+eci+WIsOi/memHjOeahOS9oO+8jOWBpeW6t+OAgeWmguaEj+OAgeeUqOS4jeaMguenke+8jOiAg+eahOWFqOS8mu+8jOiSmeeahOWFqOWvue+8jOW5tOWFpeeZvuS4h++8gQ==").decode()))))