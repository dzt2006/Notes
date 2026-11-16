"""
firstdata 项目的 Django 全局配置文件
由 django-admin startproject 命令基于 Django 4.2.30 自动生成

关于本文件的更多说明，可查看官方文档：
https://docs.djangoproject.com/zh-hans/4.2/topics/settings/

完整的配置项列表与取值说明，可查看：
https://docs.djangoproject.com/zh-hans/4.2/ref/settings/
"""

# 导入 Python 路径处理模块
from pathlib import Path

# 项目根目录：指向最外层有 manage.py 的文件夹
# 后续拼接项目内路径统一用 BASE_DIR / '子目录名' 的写法
BASE_DIR = Path(__file__).resolve().parent.parent


# 快速开发环境配置 —— 不适合直接用于生产环境
# 生产环境部署检查清单：https://docs.djangoproject.com/zh-hans/4.2/howto/deployment/checklist/

# 安全警告：生产环境必须严格保密该密钥，不能泄露
# 用于会话加密、签名、密码重置令牌等核心加密场景
SECRET_KEY = 'django-insecure-%*(n&#c=zb4!a@&@3dxy*8m9o%*tpw&@uu7k1^oxutpe&5&bsi'

# 安全警告：生产环境绝对不能开启 Debug 模式
# 开启后页面报错会显示详细代码、环境信息，存在严重安全风险
DEBUG = True

# 允许访问的域名/主机列表
# Debug 开启时默认可空，仅本地 127.0.0.1 可访问；生产环境必须填写你的域名
ALLOWED_HOSTS = []


# ========== 已注册的应用列表 ==========
# 所有启用的 Django 应用都要写在这里，否则模型、迁移、模板都不会生效
INSTALLED_APPS = [
    'django.contrib.admin',         # 自带后台管理系统
    'django.contrib.auth',          # 用户认证与权限系统
    'django.contrib.contenttypes',  # 内容类型框架（模型关联的基础依赖）
    'django.contrib.sessions',      # 会话管理
    'django.contrib.messages',      # 消息提示框架
    'django.contrib.staticfiles',   # 静态文件管理
]

# ========== 中间件列表 ==========
# 请求/响应的全局处理流水线，按从上到下的顺序依次执行
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',             # 安全相关响应头处理
    'django.contrib.sessions.middleware.SessionMiddleware',      # 会话数据处理
    'django.middleware.common.CommonMiddleware',                 # 通用处理（URL斜杠补全、规范化）
    'django.middleware.csrf.CsrfViewMiddleware',                # CSRF 跨站请求伪造防护
    'django.contrib.auth.middleware.AuthenticationMiddleware',   # 绑定当前请求的用户身份
    'django.contrib.messages.middleware.MessageMiddleware',      # 消息提示处理
    'django.middleware.clickjacking.XFrameOptionsMiddleware',    # 点击劫持防护
]

# 项目根路由配置文件的入口
ROOT_URLCONF = 'firstdata.urls'

# ========== 模板引擎配置 ==========
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # 使用 Django 自带模板引擎
        'DIRS': [],                                                    # 全局模板文件夹路径，自定义公共模板放这里
        'APP_DIRS': True,                                              # 自动在每个已注册应用的 templates 目录下查找模板
        'OPTIONS': {
            'context_processors': [  # 模板全局上下文处理器，每个模板都能拿到这些公共变量
                'django.template.context_processors.debug',       # Debug 相关变量
                'django.template.context_processors.request',     # 当前请求对象
                'django.contrib.auth.context_processors.auth',    # 当前登录用户信息
                'django.contrib.messages.context_processors.messages',  # 消息提示
            ],
        },
    },
]

# WSGI 应用入口，用于同步模式的线上部署
WSGI_APPLICATION = 'firstdata.wsgi.application'


# ========== 数据库配置 ==========
# 官方文档：https://docs.djangoproject.com/zh-hans/4.2/ref/settings/#databases

# 默认使用轻量级 SQLite 文件数据库，无需额外安装数据库服务
# 本次任务需要把这里改成 MySQL 配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # 数据库引擎，当前为 SQLite
        'NAME': BASE_DIR / 'db.sqlite3',         # 数据库文件路径，放在项目根目录
    }
}


# ========== 用户密码强度校验规则 ==========
# 官方文档：https://docs.djangoproject.com/zh-hans/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        # 校验：密码不能和用户名、邮箱等用户属性过于相似
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        # 校验：密码最小长度限制
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        # 校验：密码不能是常见弱密码
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        # 校验：密码不能全是数字
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# ========== 国际化与时区配置 ==========
# 官方文档：https://docs.djangoproject.com/zh-hans/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'  # 默认语言，英文（美国）；改成 'zh-hans' 即为简体中文

TIME_ZONE = 'UTC'         # 默认时区，世界标准时间；改成 'Asia/Shanghai' 即为北京时间

USE_I18N = True           # 开启国际化翻译功能

USE_TZ = True             # 开启时区感知，数据库统一存 UTC 时间，展示时自动转换


# ========== 静态文件配置（CSS、JS、图片等） ==========
# 官方文档：https://docs.djangoproject.com/zh-hans/4.2/howto/static-files/

STATIC_URL = 'static/'  # 静态文件的访问 URL 前缀


# ========== 默认主键字段类型 ==========
# 官方文档：https://docs.djangoproject.com/zh-hans/4.2/ref/settings/#default-auto-field

# 模型没手动指定主键时，Django 自动创建的主键类型
# BigAutoField 是 64 位自增整数，兼容大数据量场景
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
