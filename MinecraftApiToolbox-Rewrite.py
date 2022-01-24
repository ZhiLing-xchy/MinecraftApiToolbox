import base64 as base
import json
import os
import random
import sys
import time
from hashlib import md5

import functions
import config.softwareinfo as softwareinfo
### Profile Check ###
def profilerewrite():
        with open("./config/setting.json","w") as create_setting_config:#创建“./config/setting.json”并打开
            setting = {"language":"zh_cn","Gui":"off"}#设定的json设置
            setting = json.dumps(setting)
            json.dump(setting,create_setting_config)#json格式文件写入
        print("Setting not found,or was broken.Run as default.")
        print("没有找到设置或文件损坏，以默认运行。")
        print('\n'+'\n'+'\n')
if not(os.path.exists("./config/setting.json")):#如果文件“./config/setting.json”不存在
    profilerewrite()

### 配置文件读取
try:
    with open("./config/setting.json",'r') as setting_load:
        setting = json.loads(''.join(str(''.join(json.load(setting_load)))))
except:
    profilerewrite()
    with open("./config/setting.json",'r') as setting_load:
        setting = json.loads(''.join(str(''.join(json.load(setting_load)))))
## MAIN START ##

print(softwareinfo.aboutsoftware(setting['language']))
print("☆KIRA～")

