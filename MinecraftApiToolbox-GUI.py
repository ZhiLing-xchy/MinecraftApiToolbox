import base64 as base
import json
import os
import sys
import time

import easygui as gui

#from tkinter import *
import functions

###############################软件信息信息初始化#############################################
about_creater = {
    "eng_name":"Zhi_Ling",
    "zh_name":"知凌",
    "BiliBili_ID":"知凌今天也在咕咕呐",
    "Github_ID":"ZhiLing-Bilibili"
    }
about_software = {
    "version":"2.4",
    "name_zh_cn":"Minecraft Api工具箱",
    "name_en_us":"Minecraft Api Toolbox"
    }
intergrade_language_file_zh_cn = {"gui.setupscreen.msg":"请选择你要执行的命令","gui.ok_button":"好的","gui.setup.title":"setup-设置","gui.setup.msg":"设置项","gui.setup.language.title":"设置-语言","gui.setup.language.msg":"请选择语言","gui.hitokoto.title":"一言(Hitokoto)","help":{"cmd":["输入'help'获取帮助信息","输入'downloadskin'来下载皮肤","输入'exit'来退出","输入'getuuid'来获取UUID","输入'getid'来获取用户所有使用过的ID","输入'info'来获取软件信息","输入'en_us'来切换至英文显示","输入'viewsettings'来查看设置项","输入'hitokoto'来获取'一言'"],"gui":["Main   (主页面)","    downloadskin   (获取皮肤)","    getuuid    (获取UUID)","    getid  (获取所有历史ID)","    setup  (设置)","        language   (语言)","            zh_cn  (中文-简体)","            en_us  (英文)","        viewsettings   (查看设置)","    info   (关于)","    help   (帮助)","    hitokoto   (一言)"]},"version":"版本：","creaters":"制作者：","Warning":"警告: ","ID":"国际版ID","gui.downloadskin.download_finsh":"下载成功，详细信息如下:","getskin_error":"ID不存在或发生异常","getting_json":"正在从MOJANG网站获取用户JSON","parsing_json":"正在分析JSON","getting_skin_json":"正在从MOJANG获取带有皮肤信息的JSON","ecoding_base64":"正在BASE64解码","geted_skin_url":"成功获取皮肤连接：","downloading_skin_1":"正在下载皮肤文件(文件名:","downloading_skin_2":")","skin_download_finsh":"完成！耗时：","millisecond":" 毫秒","exiting":"退出中...","ID_to_UUID_error":"ID不存在或发生异常","UUID_is":" 的UUID是:","getid_command_help":"如果不知到UUID，可以使用'getuuid'查询(需要提供现有玩家名)","request_player_UUID":"国际版UUID","UUID_to_ID_Fail":"UUID不存在或出现错误","UUID_to_ID_Finsh_1":"该UUID一共拥有过 ","UUID_to_ID_Finsh_2":" 个名称","nick_now":"当前名称：","more":"更多：","reg_name":"原始名称：","ID_No._1":"第 ","ID_No._2":" 个ID：","Change_Time":"更改时间：","lang_switch_to_english":"Language had switch to English","lang_switch_to_chinese":"语言已切换至中文","unknow_command":"未知指令，输入'help'以获取帮助","gui.error":"错误","gui.error.button":"我知道了","gui.view_settings.title":"查看设置","info.api_used.title":"使用到的API接口","info.api_used.apis":["Hitoko(一言)(v1.hitokoto.cn)","百度翻译(api.fanyi.baidu.com)","Mojang Api(api.mojang.com)","Mojang Session Server Api(sessionserver.mojang.com)"],"info.libraries_used.title":"使用到的库文件","info.libraries_used":["urllib","requests","time","os","json","base64","sys","easygui"]}
def Show_SoftwareInfo():
    print(about_software['name_en_us'] + "      " + about_software['name_zh_cn'])
    cash = "" + about_software['name_en_us'] + "      " + about_software['name_zh_cn']
    print(language_display['version'] + about_software['version'])
    cash = cash + '\n' + language_display['version'] + about_software['version']
    print(language_display['creaters'] + about_creater['zh_name'])
    cash = cash + '\n' + language_display['creaters'] + about_creater['zh_name']
    print('')
    cash = cash + '\n'
    print(SoftwareData['more_info'])
    cash = cash + '\n' + SoftwareData['more_info']
    print('')
    cash = cash + '\n'
    print(language_display['Warning'] + SoftwareData['note'])
    cash = cash + '\n' + language_display['Warning'] + SoftwareData['note']
    for i in range(3):
        print("")
        cash = cash + '\n'
    print("BiliBili @" + about_creater['BiliBili_ID'])
    cash = cash + '\n' + "BiliBili @" + about_creater['BiliBili_ID']
    print("Github @" + about_creater['Github_ID'])
    cash = cash + '\n' + "Github @" + about_creater['Github_ID']
    print("")
    print('\n'*3)
    cash = cash + '\n' +'\n'*3
    print(language_display['info.api_used.title'])
    cash = cash + '\n' + language_display['info.api_used.title']
    cash2 = ""
    for i in range(0,len(language_display['info.api_used.apis'])):
        cash2 = cash2 + "\n" + language_display['info.api_used.apis'][i]
    print(cash2)
    cash = cash + '\n' + cash2
    print('\n'*2 + language_display['info.libraries_used.title'])
    cash = cash + '\n'*3 + language_display['info.libraries_used.title']
    cash2 = ""
    for i in range(0,len(language_display['info.libraries_used'])):
        cash2 = cash2 + "\n" + language_display['info.libraries_used'][i]
    print(cash2)
    cash = cash + '\n' + cash2

    gui.msgbox(title = about_software['name_en_us'] + "(" + about_software['version'] + ")",msg=cash)

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
#title = about_software['name_en_us'] + " -- " + about_software['name_en_us'] + "(" + about_software['version'] + ")"

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
    gui.msgbox(msg=about_software['name_en_us'] + "      " + about_software['name_zh_cn'] + '\n' + language_display['version'] + about_software['version'] + '\n' + language_display['creaters'] + about_creater['zh_name'] + '\n' + '\n' + SoftwareData['more_info'] + '\n' + '\n' + language_display['Warning'] + SoftwareData['note'],ok_button=language_display['gui.ok_button'])
####################################---------Main------------############################################
while True:
    print('')
    do = gui.choicebox(msg=language_display['gui.setupscreen.msg'],title = about_software['name_en_us'] + "(" + about_software['version'] + ")",choices=["downloadskin","getuuid","getid","setup","info","help","hitokoto"])
    print('')
    #皮肤下载模块
    if(do == "downloadskin"):
        id = gui.enterbox(title = about_software['name_en_us'] + "(" + about_software['version'] + ") " + "——" + "downloadskin",msg=language_display['ID'])
        print(language_display['getting_json'])
        command_output = functions.downloadskin(id)
        if(command_output["error"] == ""):
            print(language_display['geted_skin_url'] + command_output["url"])
            print(language_display['downloading_skin_1'] + command_output["path"] + language_display['downloading_skin_2'])
            print(language_display['skin_download_finsh'] + str(command_output["time"]) + language_display['millisecond'])
            gui.msgbox(title = about_software['name_en_us'] + "(" + about_software['version'] + ")" + "——" + "downloadskin",msg=(language_display['geted_skin_url'] + command_output["url"] + '\n' + language_display['downloading_skin_1'] + command_output["path"] + language_display['downloading_skin_2'] + "\n" + language_display['skin_download_finsh'] + str(command_output["time"]) + language_display['millisecond']))
        else:
            print(language_display["getskin_error"])
            gui.msgbox(msg=language_display['getskin_error'],title=language_display['gui.error'],ok_button=language_display['gui.error.button'])


    #帮助模块
    elif(do == "help"):
        cash = ""
        for i in range(0,int(len(language_display['help']['gui'])),1):
            print(language_display['help']['gui'][i])
            cash = cash + '\n' + language_display['help']['gui'][i]
        gui.msgbox(title = about_software['name_en_us'] + "(" + about_software['version'] + ") " + "——" + "help",msg=cash,ok_button=language_display['gui.ok_button'])

    #退出模块
    elif(do == "None" or do == "exit" or do == None):
        print(language_display['exiting'])
        break

    #获取UUID模块
    elif(do == "getuuid"):
        id = gui.enterbox(title = about_software['name_en_us'] + "(" + about_software['version'] + ")" + " ——" + "getuuid",msg=language_display['ID'])
        command_output = functions.getuuid(id)
        print(language_display['getting_json'])
        if(command_output["error"] == ""):
            print(language_display['parsing_json'])
            print(id + language_display['UUID_is'] + command_output['uuid'])
            gui.msgbox(title = about_software['name_en_us'] + "(" + about_software['version'] + ")" + " ——" + "getuuid",msg=id + language_display['UUID_is'] + command_output['uuid'])
        else:
            print(language_display["ID_to_UUID_error"])
            gui.msgbox(language_display['ID_to_UUID_error'],title=language_display['gui.error'],ok_button=language_display['gui.error.button'])



    #获取ID模块
    elif(do == "getid"):
        print(language_display['getid_command_help'])
        uuid = gui.enterbox(title= about_software['name_en_us'] + "(" + about_software['version'] + ")" + " ——" + "getid",msg=language_display['request_player_UUID'])
        command_output = functions.getid(uuid)
        print(language_display['getting_json'])
        if(command_output["error"] == ""):
            hjson = command_output["ids"]
            cash = int(len(hjson) - 1)
            text_cash = '\n' + '\n'
            print('')
            print('')
            print(language_display['UUID_to_ID_Finsh_1'] + str(int(cash + 1)) + language_display['UUID_to_ID_Finsh_2'])
            text_cash = text_cash + '\n' + language_display['UUID_to_ID_Finsh_1'] + str(int(cash + 1)) + language_display['UUID_to_ID_Finsh_2'] + '\n'
            print('')
            print(language_display['nick_now'] + hjson[cash]['name'])
            print('')
            text_cash = text_cash + '\n' + language_display['nick_now'] + hjson[cash]['name'] + '\n'
            if(cash > 0):
                print(language_display['more'])
                text_cash = text_cash + '\n'+ '\n' + language_display['reg_name'] + hjson[0]['name'] + '\n'
                print('')
                print(language_display['reg_name'] + hjson[0]['name'])
                print('')
                for i in range(1,int(cash + 1),1):
                    print(language_display['ID_No._1'] + str(i + 1) + language_display['ID_No._2'] + hjson[i]['name'])
                    text_cash = text_cash + '\n' + language_display['ID_No._1'] + str(i + 1) + language_display['ID_No._2'] + hjson[i]['name']
                    name_changed_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(hjson[i + 1]['changedToAt'])/1000))
                    print(language_display['Change_Time'] + name_changed_time)
                    text_cash = text_cash + '\n' + language_display['Change_Time'] + name_changed_time
                    print('')
            else:
                print("ID：" + hjson[0]['name'])
                text_cash = text_cash + '\n' + "ID：" + hjson[0]['name']
            gui.msgbox(title = about_software['name_en_us'] + "(" + about_software['version'] + ")" + " ——" + "getid",msg=text_cash)
        else:
            print(language_display['UUID_to_ID_Fail'])
            gui.msgbox(language_display['UUID_to_ID_Fail'],title=language_display['gui.error'],ok_button=language_display['gui.error.button'])

    #获取软件信息模块
    elif(do == "info"):
        Show_SoftwareInfo()

    elif(do == "setup"):
        do = gui.choicebox(title = language_display["gui.setup.title"] + "-----" + about_software['name_en_us'] + " -- " + about_software['name_en_us'] + "(" + about_software['version'] + ")",msg= language_display["gui.setup.msg"],choices=["language","viewsettings"])
        if(do == "language"):
            do = gui.choicebox(title =language_display["gui.setup.language.title"] + "-----" + about_software['name_en_us'] + " -- " + about_software['name_en_us'] + "(" + about_software['version'] + ")",msg=language_display["gui.setup.language.msg"],choices=["zh_cn","en_us"])
            #切换至英文显示
            if(do == "en_us"):
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
            gui.msgbox(setting,title=language_display["gui.view_settings.title"])

#hitokoto###Not finsh yet
    elif(do == "yiyan" or do == "hitokoto"):
        command_output = functions.yiyan(False)
        cash = command_output['yiyan'] + "——" + command_output['from']
        if setting["language"] == "en_us":
            cash = functions.baidufanyi(cash,"en")
        elif setting["language"] == "zh_cn":
            cash = cash
        print(cash)
        gui.msgbox(title = about_software['name_en_us'] + "(" + about_software['version'] + ")" + "——" + language_display['gui.hitokoto.title'],msg = cash)
#        gui.msgbox(title = about_software['name_en_us'] + "(" + about_software['version'] + ")" + " ——" + "Unknow command",msg="No finsh yet.暂未完成")

    elif((do == "egg") or (do == "eggs") or (do == "colloregg") or (do == "colloreggs")):
        functions.colloreggs()
    else:
        print(language_display['unknow_command'])
        gui.msgbox(title = about_software['name_en_us'] + "(" + about_software['version'] + ")" + " ——" + "Unknow command",msg=language_display['unknow_command'])

