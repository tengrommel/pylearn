from flask import Flask
# Flask('模块的名字')


# # 从配置对象加载配置信息
# class DefaultConfig(object):
#     """
#     默认配置
#     """
#     SECRET_KEY = "chidldop234dfffadjfke3e"


app = Flask(__name__, static_url_path='/s', static_folder='/static_files')
# 设置
# app.config.from_object(DefaultConfig)
app.config.from_pyfile('settings.py')

# 定义视图
@app.route('/')
def index():
    # 读取配置信息
    print(app.config['SECRET_KEY'])
    return "hello world"


if __name__ == '__main__':
    app.run()
