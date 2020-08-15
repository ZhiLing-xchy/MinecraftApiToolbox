import urllib.request
import urllib
import json
import base64 as base
import requests


SoftwareData = {"version":"1.2","name":"Minecraft Skin Downloader","more_info":"This software can only download skin that people uploaded on 'minecraft.net'.","note":"Please connect to the Internet, otherwise an error will appear"}
SoftwareData_zh_cn = {"version":"1.2","name":"Minecraft 皮肤下载器","more_info":"本软件只能下载用户上传至'Minecraft.net'的皮肤","note":"请连接至互联网，否则会出现报错"}
about_creater = {"eng_name":"Zhi_Ling","zh_name":"知凌","BiliBili_ID":"绝不中二的知凌","Github_ID":"ZhiLing-Bilibili"}

print(SoftwareData['name'] + "     " + SoftwareData_zh_cn['name'])
print("Version: " + SoftwareData['version'] + "                  版本： " + SoftwareData_zh_cn['version'])
print("By: " + about_creater['eng_name'] + "                  制作者： " + about_creater['zh_name'])
print('')
print('')
print(SoftwareData['more_info'])
print(SoftwareData_zh_cn['more_info'])
print('')
print("Warning: " + SoftwareData['note'])
print("警告: " + SoftwareData_zh_cn['note'])
for i in range(4):
    print("")
print("BiliBili @" + about_creater['BiliBili_ID'])
print("Github @" + about_creater['Github_ID'])
for i in range(5):
    print("")

id = input("国际版ID(Minecraft PlayerName) >>>")
print("正在从MOJANG网站获取用户JSON")
#第一次JSON获取并解析
html = urllib.request.urlopen('https://api.mojang.com/users/profiles/minecraft/' + id)#按照MOJANG api格式请求JSON
print("正在分析JSON")
hjson = json.loads(html.read())
#第二次JSON获取并解析
print("正在从MOJANG获取带有皮肤信息的JSON")
url = 'https://sessionserver.mojang.com/session/minecraft/profile/' + hjson['id']
html = urllib.request.urlopen(url)
hjson = json.loads(html.read())
print("正在分析JSON")
hjson = hjson['properties']
BASE64_JSON = hjson[0]['value']
#由于MOJANG的存储特性，在第二份JSON文件中含有被BASE64编码的另一份JSON文件，需要进行BASE64解码
print("正在BASE64解码")
#第三次JSON解析
hjson = json.loads(''.join(str(base.b64decode(BASE64_JSON).decode())))
skin_url = hjson['textures']['SKIN']['url']
print("成功获取皮肤连接：" + skin_url)

#下载皮肤用代码
r=requests.get(skin_url)
urllib.request.urlopen(skin_url)
path = id + ".png"
print("正在下载皮肤文件(文件名:"+id+".png)")
with open(path,"wb") as f:
    f.write(r.content)
f.close()
print("Done! in: " + str(len(r.content)) + " millisecond")
