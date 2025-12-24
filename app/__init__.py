from flask import Flask
from config import config


# 初始化Flask应用
def create_app(config_name="default"):
    # 创建应用实例
    app = Flask(__name__)
    # 加载配置
    app.config.from_object(config[config_name])

    # 注册路由（避免循环导入，在函数内导入routes）
    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
