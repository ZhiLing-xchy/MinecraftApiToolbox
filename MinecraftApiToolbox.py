import urllib
import json
import base64 as base
import requests
import time
import os
###############################软件信息信息初始化#############################################
about_creater = {
    "eng_name":"Zhi_Ling",
    "zh_name":"知凌",
    "BiliBili_ID":"绝不中二的知凌",
    "Github_ID":"ZhiLing-Bilibili"
    }
about_software = {
    "version":"2.3",
    "name_zh_cn":"Minecraft Api工具箱",
    "name_en_us":"Minecraft Api Toolbox"
    }
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

###############################配置文件检查###########################################
if not(os.path.exists("./config/language.json")):
    with open("./config/language.json","w") as creat_language_config:
        language_setting = {"language":"zh_cn"}
        language_file = json.dumps(language_setting)
        json.dump(language_file,creat_language_config)
    print("Language setting not found.Language had ben set to default.")
    print("没有找到语言设置，语言已被设置为默认。")

###############################语言文件读取###########################################
with open("./config/language.json",'r') as language_load:
    language_setting = json.loads(''.join(str(''.join(json.load(language_load)))))
language = language_setting['language']

if(language == "zh_cn"):
    for i in range(5):
        print("")
    SoftwareData = {
		"more_info":"本软件只能访问国际正版用户信息",
		"note":"请连接至互联网，否则会出现报错"
        }
    with open("./config/languages/zh_cn.json",'r', encoding="utf-8") as language_file_load:
        language_display = json.load(language_file_load)

elif(language == "en_us"):
    for i in range(5):
        print("")
    SoftwareData = {
		"more_info":"This software can only access to 'minecraft.net' users' account data",
		"note":"Please connect to the Internet, otherwise an error will appear"
        }
    with open("./config/languages/en_us.json",'r', encoding="utf-8") as language_file_load:
        language_display = json.load(language_file_load)
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
    if(do == "dlskin"):
        id = input(language_display['ID'] + ">>>")
        print(language_display['getting_json'])
        #第一次JSON获取并解析
        try:
            hjson = json.loads(urllib.request.urlopen('https://api.mojang.com/users/profiles/minecraft/' + id).read())#按照MOJANG api格式请求JSON
        except:
            print(language_display["getskin_error"])
        else:
            print(language_display['parsing_json'])
            #第二次JSON获取并解析
            print(language_display['getting_skin_json'])
            url = 'https://sessionserver.mojang.com/session/minecraft/profile/' + hjson['id']
            html = urllib.request.urlopen(url)
            hjson = json.loads(html.read())
            print(language_display['parsing_json'])
            hjson = hjson['properties']
            BASE64_JSON = hjson[0]['value']
            #由于MOJANG的存储特性，在第二份JSON文件中含有被BASE64编码的另一份JSON文件，需要进行BASE64解码
            print(language_display['ecoding_base64'])
            #第三次JSON解析
            hjson = json.loads(''.join(str(base.b64decode(BASE64_JSON).decode())))
            skin_url = hjson['textures']['SKIN']['url']
            print(language_display['geted_skin_url'] + skin_url)
            #下载皮肤用代码
            path =id + ".png"
            r=requests.get(skin_url)
            urllib.request.urlopen(skin_url)
            print(language_display['downloading_skin_1'] + id + language_display['downloading_skin_2'])
            with open(path,"wb") as f:
                f.write(r.content)
            f.close()
            print(language_display['skin_download_finsh'] + str(len(r.content)) + language_display['millisecond'])

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
        print(language_display['getting_json'])
        try:
            hjson = json.loads(urllib.request.urlopen('https://api.mojang.com/users/profiles/minecraft/' + id).read())#按照MOJANG api格式请求JSON
        except:
            print(language_display['ID_to_UUID_error'])
        else:
            print(language_display['parsing_json'])
            print(id + language_display['UUID_is'] + hjson['id'])

    #获取ID模块
    elif(do == "getid"):
        print(language_display['getid_command_help'])
        uuid = input(language_display['request_player_UUID'] + ">>>")
        print(language_display['getting_json'])
        try:
            hjson = json.loads(urllib.request.urlopen('https://api.mojang.com/user/profiles/' + uuid + '/names').read())#按照MOJANG api格式请求JSON
        except:
            print(language_display['UUID_to_ID_Fail'])
        else:
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
                    print(language_display['ID_No._1'] + str(i) + language_display['ID_No._2'] + hjson[i]['name'])
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
        language_setting = {"language":"en_us"}
        language_file = json.dumps(language_setting)
        with open("./config/language.json","w") as f:
            json.dump(language_file,f)

        SoftwareData = {
		    "more_info":"This software can only access to 'minecraft.net' users' account data",
		    "note":"Please connect to the Internet, otherwise an error will appear"
            }

        with open("./config/languages/en_us.json",'r', encoding="utf-8") as language_file_load:
            language_display = json.load(language_file_load)
        print(language_display['lang_switch_to_english'])

    #切换至中文显示
    elif(do == "zh_cn"):
        language_setting = {"language":"zh_cn"}
        language_file = json.dumps(language_setting)
        with open("./config/language.json","w") as f:
            json.dump(language_file,f)

        SoftwareData = {
		    "more_info":"本软件只能访问国际正版用户信息",
		    "note":"请连接至互联网，否则会出现报错"
            }

        with open("./config/languages/zh_cn.json",'r', encoding="utf-8") as language_file_load:
            language_display = json.load(language_file_load)
        print(language_display['lang_switch_to_chinese'])

    else:
        print(language_display['unknow_command'])