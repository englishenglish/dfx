from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# 20条温馨提示
messages = [
    "早安，开启美好一天！", "天冷了，多穿衣服", "不顺心的话就找我叭", "多喝水哦~", "要天天开心吖~",
    "保持好心情", "照顾好自己", "别熬夜", "早点休息", "今天过的开心嘛",
    "今天也要加油哦！", "梦想成真", "保持微笑吖", "愿你所有烦恼都消失",
    "多吃水果", "要按时吃饭", "你值得被世界温柔以待", "好好爱自己", "顺顺利利", "愿你笑容常在。"
]

# 淡暖色调（hex）
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
    msg = random.choice(messages)
    color = random.choice(warm_colors)
    return jsonify({"message": msg, "color": color})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
