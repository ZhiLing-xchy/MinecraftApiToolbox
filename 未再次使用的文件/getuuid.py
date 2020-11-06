import base64 as base
import json
import os
import time
import urllib
import requests

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