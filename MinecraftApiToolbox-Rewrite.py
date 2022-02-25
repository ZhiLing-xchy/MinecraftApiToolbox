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
## Language File Check ##
try:
    with open("./config/languages/forrewrite/"+setting['language']+".json",'r') as language_file:
        language_display = json.load(language_file)
except:
    print("Error While Loading Language File")
## MAIN START ##

print(softwareinfo.aboutsoftware(setting['language']))
print("☆KIRA～")
def crash():
    with open("./config/this/file/doesn't/excist/it's/use/to/crash/the/app",'r') as crash:
        print(crash.read())


try:
    while True:
        execution = input(language_display['cmd']['main']['input'])

#########  DWONLOAD SKIN ##########
        if(execution == "downloadskin"):
            print()
            result = functions.downloadskin(input(language_display['cmd']['downloadskin']['input']))
            if(not result['error'] == ''):
                print(language_display['cmd']['downloadskin']['error'],end='')
                print(result['error_detalle'])
            else:
                print()

########## getuuid ##########
        elif(execution == "getuuid"):
            print()

########## CRASH ##########
        elif(execution == "crash"):
            crash()

########## HELP LIST ##########
        elif(execution == "help"):
            for i in range(0,int(len(language_display['cmd']['help']))):
                print(language_display['cmd']['help'][i])

########## EXIT SOFTWARE ##########
        elif(execution == "exit"):
            break

########## UNKONW COMMAND ##########
        elif(execution == "colloregg"):
            functions.colloregg()
        else:
            print(language_display['cmd']['main']['unknowcommand'])
except:
    input(language_display['cmd']['main']['error'])