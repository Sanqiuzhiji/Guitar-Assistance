# 项目配置类
class Config:
    # 调试模式（开发环境开启，生产环境关闭）
    DEBUG = True
    # 应用密钥（用于会话管理、加密等，可自定义任意字符串）
    SECRET_KEY = "your_secret_key_123456"  # 建议生产环境使用更复杂的随机字符串


# 开发环境配置（可继承Config类扩展）
class DevelopmentConfig(Config):
    ENV = "development"


# 配置映射，便于切换环境
config = {
    "development": DevelopmentConfig,
    "default": DevelopmentConfig
}
