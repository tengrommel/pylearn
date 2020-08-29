from flask import Flask
app = Flask(__name__, static_url_path='/s', static_folder='/static_files')
# Flask('模块的名字')


# 定义视图
@app.route('/')
def index():
    return "hello world"


if __name__ == '__main__':
    app.run()
