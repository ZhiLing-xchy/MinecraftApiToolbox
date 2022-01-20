import json
import urllib
import requests


def downloadfile(url,path):
    download_result = {
        "time":0,
        "url":"",
        "path":"",
        "error":""
    }
    try:
        hjson = json.loads(urllib.request.urlopen('https://api.mojang.com/').read())#使用MOJANG API尝试互联网
    except:
        download_result["error"] = "INTERNET_CONECTION_ERROR"
        return(download_result)
    else:
        try:
            download_result["path"] = path
            download_result["url"] = url

            r=requests.get(url)
            urllib.request.urlopen(url)
            with open(path,"wb") as f:
                f.write(r.content)
            f.close()
            download_result["time"] = len(r.content)

            return(download_result)
        except:
            download_result["error"] = "INTERNET_CONECTION_ERROR"
            return(download_result)

############################################################################################

def getjsonfrominternet(url):
    try:
        hjson = json.loads(urllib.rquest.urlopen(url).read())
        return(hjson)
    except:
        return('ERROR')
        
############################################################################################
