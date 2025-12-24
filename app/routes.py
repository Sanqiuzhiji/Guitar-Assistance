from flask import Blueprint, render_template

# 创建蓝图（便于模块化开发，后期可拆分多个蓝图）
main_bp = Blueprint("main", __name__)


# 定义首页路由（访问根路径"/"时触发）
@main_bp.route("/")
@main_bp.route("/index")  # 支持多个URL映射到同一个视图函数
def index():
    # 传递模板变量（可在HTML中使用）
    page_title = "我的网页应用首页"
    user_name = "测试用户"
    # 渲染index.html模板，并传递变量
    return render_template("index.html", title=page_title, name=user_name)


# 可扩展其他路由，例如关于页
@main_bp.route("/about")
def about():
    return render_template("about.html", title="关于我们")
