from app import create_app

# 创建应用实例
app = create_app()

# 当直接运行该文件时，启动服务
if __name__ == "__main__":
    # 启动Flask内置服务器，host=0.0.0.0允许局域网访问
    app.run(host="0.0.0.0", port=5000)
