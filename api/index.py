from flask import Flask, render_template, jsonify
import random

# 因为当前文件在 api/ 目录下，所以要指明模板和静态目录位置
app = Flask(__name__, static_folder="../static", template_folder="../templates")

nicknames = ["宝宝", "戴戴", "小猪崽子", "老婆", "猪包"]

messages = [
    "要多多吃饭哟！💓", "天天都要开开心心哒💓", "我爱你💖", "能不能做我老婆呀🌹", "你好可爱呀",
    "今天也要元气满满呀🤭", "要多喝水哟👀", "早早睡觉呀", "你眼泡子好大👀", "感觉你像一个大笨蛋",
    "要多多关心你的小狗🤭", "带小狗吃好吃的🌹", "别忘了每天想我哟", "哥想做你的依靠🥰",
    "你睡觉的样子太可爱啦✨", "要按时吃饭😁", "想你想的得了相思病🌹", "你好香呀想闻死你✨", "拉屎好臭呀咦~嫌弃✨", "不要老是焦虑啦！😘"
]

warm_colors = [
    "#FFEFD5", "#FFE4B5", "#FFDEAD", "#FFB6C1", "#FFCC99",
    "#FFFACD", "#FFF5EE", "#FFE4E1", "#FFDAB9", "#FFA07A",
    "#FFEC8B", "#FFD7B4", "#FFDFD3", "#FFF0F5", "#FFFAF0",
    "#FFEFD5", "#FFE4B5", "#FFC0CB", "#FFE4E1"
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/random_message")
def random_message():
    nickname = random.choice(nicknames)
    msg = random.choice(messages)
    color = random.choice(warm_colors)
    full_msg = f"{nickname}，{msg}"
    return jsonify({"message": full_msg, "color": color})

# ✅ 关键：Vercel 入口函数
def handler(event, context):
    return app(event, context)
