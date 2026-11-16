"""
firstdata 项目的 URL 路由配置文件

urlpatterns 列表负责将 URL 路径映射到对应的视图函数。
更多详细说明可查看官方文档：
    https://docs.djangoproject.com/zh-hans/4.2/topics/http/urls/

使用示例：
1. 函数视图写法
    第一步：导入视图函数  from my_app import views
    第二步：添加路由规则  path('', views.home, name='home')

2. 类视图写法
    第一步：导入视图类  from other_app.views import Home
    第二步：添加路由规则  path('', Home.as_view(), name='home')

3. 引入子应用的路由配置
    第一步：导入 include 函数  from django.urls import include, path
    第二步：挂载子路由  path('blog/', include('blog.urls'))
"""

# 导入 Django 自带的后台管理站点模块
from django.contrib import admin
# 导入路径匹配函数 path，用来定义一条条 URL 路由规则
from django.urls import path

# 项目根路由总列表，所有 URL 规则按从上到下的顺序匹配
urlpatterns = [
    # 匹配地址 admin/，直接交给 Django 自带的后台管理系统处理
    path('admin/', admin.site.urls),
]
