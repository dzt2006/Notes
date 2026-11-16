"""
firstdata 项目的 ASGI 配置文件

本文件会将 ASGI 可调用对象，以名为 ``application`` 的模块级变量对外暴露

如需了解本文件的更多信息，可访问官方文档：
https://docs.djangoproject.com/zh-hans/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstdata.settings')

application = get_asgi_application()
