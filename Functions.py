# Unknown2123 版权所有(bushi)
# 日期:2021/9/15

# 导入模块
import os
import urllib.request
import urllib.parse
import json


# 定义函数
def split_line():  # 分割线
    print("*" * 50)


# 备份函数
def backup():
    split_line()
    # 输入盘符以设定保存位置
    drive_letter = input("输入备份的盘符(只限大写字母)")
    # 输入要保存的路径
    path = input("输入要备份文件的路径(附带文件的地址，仅限文件，附带拓展名):")
    # 输入新文件的名字
    name = input("输入新文件的名字")
    # 打开文件
    with open(path, "rb") as file:
        # 读取数据
        temp = bytes(file.read())
        # 找到点的位置以判断是什么文件
        dot = path.rfind(".")
        # 判断位置并保存后缀名
        Extension = path[dot:]
        # 保存
        with open(drive_letter + ":\\" + "[备份]" + name + Extension, "wb+") as beifen_file:
            beifen_file.write(temp)
    input(f"备份完成，文件在{drive_letter}盘根目录里，名为[备份]{name}，按回车退出")
    split_line()


# 自动关机函数
def autoshutdown():
    # ***************************
    # 初始化变量
    real_time = 0
    time = 0
    # ***************************
    # 判断单位
    unit = input("输入单位(时 分 秒)")
    time = float(input("多少时/分/秒后自动关闭？"))
    if unit == "时":
        real_time = time * 3600
    elif unit == "分":
        real_time = time * 60
    elif unit == "秒":
        real_time = time
    else:
        print("语句无效")
        raise TypeError
    # ***************************
    # 设定自动关机
    os.system(f"shutdown -s -t {int(real_time)}")
    input(f"设置完毕，你的电脑将在{int(real_time) // 60}分钟后关闭，按回车退出")


# 翻译
def translation():
    will_translation = input("输入要翻译的字符：")
    url = "https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    data = {}
    data["i"] = will_translation
    data["from"] = "AUTO"
    data["to"] = "AUTO"
    data["smartresult"] = "dict"
    data["client"] = "fanyideskweb"
    data["doctype"] = "json"
    data["keyfrom"] = "fanyi.web"
    data["action"] = "FY_BY_REALTlME"
    data = urllib.parse.urlencode(data).encode("utf-8")
    jieshou = urllib.request.urlopen(url, data)
    get = jieshou.read().decode("utf-8")
    get = json.loads(get)
    print(get["translateResult"][0][0]["tgt"])


# 小彩蛋
def about_this():
    print("本程序为'函数集'，英文名：'Function collection'")
    print("由2123ABC(又名Unknown2123)开发")
    print("还有一件事")
    print("我真的只是一个垃圾啊o((>ω< ))o")
    input()


# 欢迎界面
split_line()
print("欢迎使用函数集")
print("版本号：0.000114514")
print("这个作品只是2123ABC(Unknown2123)临时想出来的东西")
print("因此请不要在意那些细节(*/ω＼*)")
split_line()
print("选择函数:")
print("1.backup() / bk() 备份文件")
print("2.autoshutdown() / asd() 定时关机")
print("3.translation() / tr() 翻译（有道翻译的API）")
split_line()
Diao_Yong_Han_Shu = input("输入调用的函数")
# 判断调用的函数
if Diao_Yong_Han_Shu == "backup()" or Diao_Yong_Han_Shu == "bk()" or Diao_Yong_Han_Shu == "1":
    backup()
    pass
elif Diao_Yong_Han_Shu == "autoshutdown()" or Diao_Yong_Han_Shu == "asd()" or Diao_Yong_Han_Shu == "2":
    autoshutdown()
    pass
elif Diao_Yong_Han_Shu == "translation()" or Diao_Yong_Han_Shu == "tr()" or Diao_Yong_Han_Shu == "3":
    translation()
elif "/" in Diao_Yong_Han_Shu:
    print("这里不是我的世界啊(っ °Д °;)っ")
    input()
    pass
elif "()" not in Diao_Yong_Han_Shu:
    print("你是不是忘记加括号了(⊙_⊙)？")
    input()
else:
    print("无效的输入")
    aaa = input()
    if aaa == "about this":
        about_this()
