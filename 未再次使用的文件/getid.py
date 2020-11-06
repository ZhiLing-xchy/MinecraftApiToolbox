import base64 as base
import json
import os
import time
import urllib
import requests

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