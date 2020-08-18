import urllib
import json
import base64 as base
import requests
import time


SoftwareData = {
    "version":"1.3",
    "name":"Minecraft Api Toolbox",
    "more_info":"This software can only access to 'minecraft.net' users' account data",
    "note":"Please connect to the Internet, otherwise an error will appear"
    }
SoftwareData_zh_cn = {
    "version":"1.3",
    "name":"Minecraft Api工具箱",
    "more_info":"本软件只能访问国际正版用户信息",
    "note":"请连接至互联网，否则会出现报错"
    }
about_creater = {
    "eng_name":"Zhi_Ling",
    "zh_name":"知凌",
    "BiliBili_ID":"绝不中二的知凌",
    "Github_ID":"ZhiLing-Bilibili"
    }
help_info_zh_cn = "输入help获取帮助信息"+'       '+"输入‘dlskin来下载皮肤"+'       '+"输入'exit'来退出"+'       '+"输入'getuuid'来获取UUID"+'       '+"输入'getid'来获取用户所有使用过的ID"+'       '+"输入'info'来获取软件信息"
help_info_en_us = "type 'help' to get help"+'       '+"type 'dlskin' to download skin"+'       '+"type 'exit' to exit this software"+'       '+"type 'getuuid' to get UUID"+'       '+"type 'getid' to get all ID that the user used"

def Show_SoftwareInfo():
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


def main():
    do = input("Minecraft Api Toolbox>>>")


#皮肤下载模块
    if(do == "dlskin"):
        id = input("国际版ID(Minecraft PlayerName) >>>")
        print("正在从MOJANG网站获取用户JSON")
    #第一次JSON获取并解析
        print("正在分析JSON")
        hjson = json.loads(urllib.request.urlopen('https://api.mojang.com/users/profiles/minecraft/' + id).read())#按照MOJANG api格式请求JSON
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
        path =id + ".png"
        r=requests.get(skin_url)
        urllib.request.urlopen(skin_url)
        print("正在下载皮肤文件(文件名:"+id+".png)")
        with open(path,"wb") as f:
            f.write(r.content)
        f.close()
        print("Done! in: " + str(len(r.content)) + " millisecond")
        main()

#帮助模块
    elif(do == "help"):
        print(help_info_zh_cn)
        print(help_info_en_us)
        main()
    elif(do == "exit"):
        print("exiting...")

#获取UUID模块
    elif(do == "getuuid"):
        id = input("国际版ID(Minecraft PlayerName) >>>")
        print("正在从MOJANG网站获取用户JSON")
        print("正在分析JSON")
        hjson = json.loads(urllib.request.urlopen('https://api.mojang.com/users/profiles/minecraft/' + id).read())#按照MOJANG api格式请求JSON
        print("The UUID of " + id + " is:" + hjson['id'])
        print(id + " 的UUID是:" + hjson['id'])
        main()

#获取ID模块
    elif(do == "getid"):
        print("如果不知到UUID，可以使用'getuuid'查询(需要提供现有玩家名)")
        uuid = input("国际版UUID(Minecraft Player UUID)>>>")
        print("正在从MOJANG官网获取JSON数据")
        hjson = json.loads(urllib.request.urlopen('https://api.mojang.com/user/profiles/' + uuid + '/names').read())#按照MOJANG api格式请求JSON
        cash = int(len(hjson) - 1)
        print("该UUID一共拥有过 " + str(int(cash + 1)) + " 个名称")
        print("当前名称：" + hjson[cash]['name'])
        
        if(cash > 0):
            print("更多：")
            print("More:")
            print('')
            print("原始名称：" + hjson[0]['name'])
            print('')
            for i in range(1,int(cash + 1),1):
                print("第 " + str(i) + " 个ID：" + hjson[i]['name'])
                name_changed_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(hjson[1]['changedToAt'])/1000))
                print("更改时间：" + name_changed_time)
                print('')
                print("ID No." + str(i) + ": " + hjson[i]['name'])
                print("Changed time: " + name_changed_time)
                print('')
                print('')
        else:
            print("ID：" + hjson[0]['time'])
        main()

#获取软件信息模块
    elif(do == "info"):
        Show_SoftwareInfo()
        main()
    else:
        print("unknow command type 'help' for help")
        print("未知指令，输入'help'以获取帮助")
        main()
####################################---------Main------------############################################
Show_SoftwareInfo()
for i in range(5):
    print("")

main()
