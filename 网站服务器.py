# -*- coding: UTF-8 -*-
import os
from flask import Flask, render_template, request, send_from_directory
from 生成器算法 import 生成器

app = Flask(__name__)
生成器 = 生成器()


def 统计字数(作文:list)->(int, int):
    总字数 = 0
    总段数 = len(作文)
    for 段落 in 作文:
        总字数 += len(段落)
    return 总字数, 总段数


@app.route('/',methods = ['POST', 'GET'])
def 显示网页():
    # 初始化默认值
    主题谓语 = "勇于"
    主题宾语 = "尝试"
    作文 = ['欢迎使用小嘿作文生成器！',
            '可生成作文总量为：',
            '{:,d}'.format(生成器.作文总数),
            '要开始使用，首先输入主题谓语、宾语。例如：“树立、理想”，“融入、爱国主义洪流”，“热爱、生命之美好”。然后点击生成按钮。',]
    总段数 = len(作文)
    # 点击生成获取表单信息
    if request.method == 'POST':
        表单 = request.form
        主题谓语 = 表单["主题谓语"]
        主题宾语 = 表单["主题宾语"]
        # 调用生成器算法
        作文 = 生成器.生成作文(主题谓语=主题谓语, 主题宾语=主题宾语)
        总字数, 总段数 = 统计字数(作文)
        作文[-1] += "（共" + str(总字数) + "字）"
    return render_template(
            "index.html", 
            主题谓语 = 主题谓语,
            主题宾语 = 主题宾语,
            作文 = 作文,
            总段数 = 总段数
            )

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
            './favicon.ico', mimetype='image/vnd.microsoft.icon')


# 本地测试代码
if __name__ == '__main__':
    app.run(port=80, debug=True)