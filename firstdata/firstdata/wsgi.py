"""
firstdata 项目的 WSGI 配置。

它将 WSGI 可调用对象作为模块级变量 application 暴露出来。

有关此文件的更多信息，请参见
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstdata.settings')

application = get_wsgi_application()
