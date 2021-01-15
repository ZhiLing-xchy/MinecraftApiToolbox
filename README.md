# MinecraftApiToolbox（Minecraft Api 工具箱）
## 用于获取MOJANG Api中的数据和一些其他的功能 
##### （会不会最后做成了Minecraft User's Helper [doge]）

#### 获取JSON途径：
api.mojang.com
sessionserver.mojang.com

#### 使用到的库文件：
urllib
json
base64
requests
time
os
sys
easygui

#### 使用到的Api(除MOJANG Api)：
Hitokoto(一言)(v1.hitokoto.cn)
百度翻译(api.fanyi.baidu.com)

### 使用时请解压，打开MinecraftApiToolbox.exe

###### ###############不推荐##################
###### MinecraftSkinDownloader则直接打开exe文件


### 说明
#### 命令行版本语法：
    help---------------获取帮助信息
    downloadskin-------下载皮肤
    exit---------------退出
    getuuid------------获取UUID
    getid--------------获取用户所有使用过的ID
    en_us--------------切换至英文显示
    zh_cn--------------切换至中文显示
    info---------------获取软件信息
    viewsettings-------查看当前设置
    hitokoto(或yiyan)--一言

#### GUI版本目录结构
    Main
        downloadskin
        getuuid
        getid
        setup
            language
                zh_cn
                en_us
            viewsettings
        info
        help
        hitokoto