import base64 as base
import json
import os
import sys
import time
import urllib
#from tkinter import *
import easygui as gui
import requests

import functions
###############################软件信息信息初始化#############################################
about_creater = {
    "eng_name":"Zhi_Ling",
    "zh_name":"知凌",
    "BiliBili_ID":"知凌今天也在咕咕呐",
    "Github_ID":"ZhiLing-Bilibili"
    }
about_software = {
    "version":"2.4 (beta 20-11-a)",
    "name_zh_cn":"Minecraft Api工具箱",
    "name_en_us":"Minecraft Api Toolbox"
    }
intergrade_language_file_zh_cn = {"help":["输入'help'获取帮助信息","输入'dlskin'来下载皮肤","输入'exit'来退出","输入'getuuid'来获取UUID","输入'getid'来获取用户所有使用过的ID","输入'info'来获取软件信息","输入'en_us'来切换至英文显示","输入'viewsettings'来查看设置项"],"version":"版本：","creaters":"制作者：","Warning":"警告: ","ID":"国际版ID","getskin_error":"ID不存在或发生异常","getting_json":"正在从MOJANG网站获取用户JSON","parsing_json":"正在分析JSON","getting_skin_json":"正在从MOJANG获取带有皮肤信息的JSON","ecoding_base64":"正在BASE64解码","geted_skin_url":"成功获取皮肤连接：","downloading_skin_1":"正在下载皮肤文件(文件名:","downloading_skin_2":".png)","skin_download_finsh":"完成！耗时：","millisecond":" 毫秒","exiting":"退出中...","ID_to_UUID_error":"ID不存在或发生异常","UUID_is":" 的UUID是:","getid_command_help":"如果不知到UUID，可以使用'getuuid'查询(需要提供现有玩家名)","request_player_UUID":"国际版UUID","UUID_to_ID_Fail":"UUID不存在或出现错误","UUID_to_ID_Finsh_1":"该UUID一共拥有过 ","UUID_to_ID_Finsh_2":" 个名称","nick_now":"当前名称：","more":"更多：","reg_name":"原始名称：","ID_No._1":"第 ","ID_No._2":" 个ID：","Change_Time":"更改时间：","lang_switch_to_english":"Language had switch to English","lang_switch_to_chinese":"语言已切换至中文","unknow_command":"未知指令，输入'help'以获取帮助","gui.error":"错误","gui.error.button":"我知道了","gui.view_settings.title":"查看设置"}
def Show_SoftwareInfo():
    print(about_software['name_en_us'] + "      " + about_software['name_zh_cn'])
    print(language_display['version'] + about_software['version'])
    print(language_display['creaters'] + about_creater['zh_name'])
    print('')
    print(SoftwareData['more_info'])
    print('')
    print(language_display['Warning'] + SoftwareData['note'])
    for i in range(3):
        print("")
    print("BiliBili @" + about_creater['BiliBili_ID'])
    print("Github @" + about_creater['Github_ID'])
    print("")

#Tk().iconbitmap(default = r'.\MinecraftApiToolbox.ico')
#Tk().destroy()

###############################配置文件检查###########################################
if not(os.path.exists("./config/setting.json")):
    with open("./config/setting.json","w") as create_setting_config:
        setting = {"language":"zh_cn","Gui":"off"}
        setting_file = json.dumps(setting)
        json.dump(setting_file,create_setting_config)
    print("Setting not found.Run as default.")
    print("没有找到设置，以默认运行。")

###############################语言文件读取###########################################
with open("./config/setting.json",'r') as setting_load:
    setting = json.loads(''.join(str(''.join(json.load(setting_load)))))
language = setting['language']

if(language == "zh_cn"):
    for i in range(5):
        print("")
    SoftwareData = {
		"more_info":"本软件只能访问国际正版用户信息",
		"note":"请连接至互联网，否则会出现报错"
        }
    try:
        with open("./config/languages/zh_cn.json",'r', encoding="utf-8") as language_file_load:
            language_display = json.load(language_file_load)
    except:
        language_display = intergrade_language_file_zh_cn
        print("The set language file was not found, using the integrated language file."+'\n'+"未找到所设定的语言文件，正在使用集成语言文件。")
elif(language == "en_us"):
    for i in range(5):
        print("")
    SoftwareData = {
		"more_info":"This software can only access to 'minecraft.net' users' account data",
		"note":"Please connect to the Internet, otherwise an error will appear"
        }
    try:
        with open("./config/languages/en_us.json",'r', encoding="utf-8") as language_file_load:
            language_display = json.load(language_file_load)
    except:
        language_display = intergrade_language_file_zh_cn
        print("The set language file was not found, using the integrated language file."+'\n'+"未找到所设定的语言文件，正在使用集成语言文件。")

##################################初始屏幕############################################
#没什么卵用只是为了好收起代码用的只循环一次的For循环
for i in range(1):
    print(about_software['name_en_us'] + "      " + about_software['name_zh_cn'])
    print(language_display['version'] + about_software['version'])
    print(language_display['creaters'] + about_creater['zh_name'])
    print('')
    print(SoftwareData['more_info'])
    print('')
    print(language_display['Warning'] + SoftwareData['note'])
    print('')
####################################---------Main------------############################################
while True:
    print('')
    do = input("Minecraft Api Toolbox>>>")
    print('')

    #皮肤下载模块
    if(do == "downloadskin"):
        id = input(language_display['ID'] + ">>>")
        print(language_display['getting_json'])
        command_output = functions.downloadskin(id)
        if(command_output["error"] == ""):
            print(language_display['geted_skin_url'] + command_output["url"])
            print(language_display['downloading_skin_1'] + command_output["path"] + language_display['downloading_skin_2'])
            print(language_display['skin_download_finsh'] + str(command_output["time"]) + language_display['millisecond'])
        else:
            print(language_display["getskin_error"])
            if(setting["Gui"] == "on"):
                gui.msgbox(language_display['getskin_error'],title=language_display['gui.error'],ok_button=language_display['gui.error.button'])


    #帮助模块
    elif(do == "help"):
        for i in range(0,int(len(language_display['help'])),1):
            print(language_display['help'][i])

    #退出模块
    elif(do == "exit"):
        print(language_display['exiting'])
        break

    #获取UUID模块
    elif(do == "getuuid"):
        id = input(language_display['ID'] + ">>>")
        command_output = functions.getuuid()
        print(language_display['getting_json'])
        if(command_output["error"] == ""):
            print(language_display['parsing_json'])
            print(id + language_display['UUID_is'] + hjson['id'])
        else:
            print(language_display["ID_to_UUID_error"])
            if(setting["Gui"] == "on"):
                gui.msgbox(language_display['ID_to_UUID_error'],title=language_display['gui.error'],ok_button=language_display['gui.error.button'])
        


    #获取ID模块
    elif(do == "getid"):
        print(language_display['getid_command_help'])
        uuid = input(language_display['request_player_UUID'] + ">>>")
        command_output = functions.getid(uuid)
        print(language_display['getting_json'])
        if(command_output["error"] == ""):
            hjson = command_output["ids"]
            cash = int(len(hjson) - 1)
            print('')
            print('')
            print(language_display['UUID_to_ID_Finsh_1'] + str(int(cash + 1)) + language_display['UUID_to_ID_Finsh_2'])
            print('')
            print(language_display['nick_now'] + hjson[cash]['name'])
            print('')
            if(cash > 0):
                print(language_display['more'])
                print('')
                print(language_display['reg_name'] + hjson[0]['name'])
                print('')
                for i in range(1,int(cash + 1),1):
                    print(language_display['ID_No._1'] + str(i + 1) + language_display['ID_No._2'] + hjson[i]['name'])
                    name_changed_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(hjson[1]['changedToAt'])/1000))
                    print(language_display['Change_Time'] + name_changed_time)
                    print('')
            else:
                print("ID：" + hjson[0]['name'])

    #获取软件信息模块
    elif(do == "info"):
        Show_SoftwareInfo()

    #切换至英文显示
    elif(do == "en_us"):
        setting["language"] = "en_us"
        setting_file = json.dumps(setting)
        with open("./config/setting.json","w") as f:
            json.dump(setting_file,f)

        SoftwareData = {
		    "more_info":"This software can only access to 'minecraft.net' users' account data",
		    "note":"Please connect to the Internet, otherwise an error will appear"
            }

        with open("./config/languages/en_us.json",'r', encoding="utf-8") as language_file_load:
            language_display = json.load(language_file_load)
        print(language_display['lang_switch_to_english'])

    #切换至中文显示
    elif(do == "zh_cn"):
        setting["language"] = "zh_cn"
        setting_file = json.dumps(setting)
        with open("./config/setting.json","w") as f:
            json.dump(setting_file,f)

        SoftwareData = {
		    "more_info":"本软件只能访问国际正版用户信息",
		    "note":"请连接至互联网，否则会出现报错"
            }

        with open("./config/languages/zh_cn.json",'r', encoding="utf-8") as language_file_load:
            language_display = json.load(language_file_load)
        print(language_display['lang_switch_to_chinese'])

##查看设置
    elif(do == "viewsettings"):
        with open("./config/setting.json",'r') as setting_load:
            setting = json.loads(''.join(str(''.join(json.load(setting_load)))))
        print(setting)
        if(setting["Gui"] == "on"):
            gui.msgbox(setting,title=language_display["gui.view_settings.title"])

#GUI设置
    elif(do == "guion"):
        setting["Gui"] = "on"
        setting_file = json.dumps(setting)
        with open("./config/setting.json","w") as f:
            json.dump(setting_file,f)
    elif(do == "guioff"):
        setting["Gui"] = "off"
        setting_file = json.dumps(setting)
        with open("./config/setting.json","w") as f:
            json.dump(setting_file,f)
    elif((do == "egg") or (do == "eggs") or (do == "colloregg") or (do == "colloreggs")):
        functions.colloreggs()
    else:
        print(language_display['unknow_command'])
