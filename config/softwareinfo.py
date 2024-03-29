info = {
    "about_software":{
        "version":"rever3 beta 22-1-a",
        "name_zh_cn":"Minecraft Api工具箱",
        "name_en_us":"Minecraft Api Toolbox",
        "about":"用于更方便的使用MOJANG 提供的Api"
    },
    "about_creater":{
        "en_name":"Zhi_Ling",
        "zh_name":"知凌",
        "Bilibili_ID":"知凌今天也在咕咕呐",
        "Github_ID":"ZhiLing-Bilibili"
    }
}

def aboutsoftware(language):
    if language == "zh_cn":
        output = \
            info["about_software"]["name_zh_cn"]+"\n"+\
            info["about_software"]["about"]+"\n"+\
            "BILIBILI @"+info["about_creater"]["Bilibili_ID"]+"\n"+\
            "GITHUB   @"+info["about_creater"]["Github_ID"]+"\n"+\
            ""
    elif language == "en_us":
        output = \
            info["about_software"]["name_zh_cn"]+"\n"+\
            info["about_software"]["about"]+"\n"+\
            "BILIBILI @"+info["about_creater"]["Bilibili_ID"]+"\n"+\
            "GITHUB   @"+info["about_creater"]["Github_ID"]
    return(output)