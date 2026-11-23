##### Django 项目初始化

##### 一、创建项目与应用

```cmd
django-admin startproject firstdata 
```

```
python manage.py startapp myapp
```

然后会生成如下的目录结构：

```txt
firstdata/                # 项目根目录：整个项目文件夹
├── firstdata/            # 配置包：全局设置，不用写业务
│   ├── __init__.py       # 包标记，告诉Django这是Python包
│   ├── asgi.py           # 异步部署入口（WebSocket，本地开发基本不用）
│   ├── settings.py       # 核心配置：注册app、数据库、模板路径
│   ├── urls.py           # 总路由：把请求分给各个app
│   └── wsgi.py           # 同步部署入口（上线服务器用，本地开发不用）
├── myapp/                # 应用app：写业务代码的地方
│   ├── __init__.py       # 包标记
│   ├── admin.py          # 后台管理配置，注册模型
│   ├── apps.py           # app自身配置，Django识别这个app
│   ├── migrations/       # 迁移记录：记录数据库表改动
│   ├── models.py         # 模型：定义数据库表结构
│   ├── tests.py          # 写单元测试（检验代码）
│   ├── urls.py           # 子路由：当前app自己的网址
│   ├── views.py          # 视图：接收请求、处理逻辑、返回页面
└── manage.py             # 命令工具：runserver、migrate、startapp

```

[打开 firstdata 项目文件夹（中文版）](firstdata)

##### 二、注册应用并启动

来到 `firstdata/settings.py`，把 `myapp` 加进 `INSTALLED_APPS`：

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
]
```

然后运行下面的命令：

```cmd
python manage.py migrate
```

```cmd
python manage.py runserver
```

##### 三、配置 MySQL

先建好数据库：

```mysql
create database first_db;
show databases;
```

来到 `firstdata/firstdata/__init__.py`，让 Django 用 `pymysql` 代替默认驱动：

```python
import pymysql
pymysql.install_as_MySQLdb()
```

xxxxxxxxxx import pymysql​db_config = {    "host": "localhost",    "port": 3306,    "user": "root",    "password": "123456",    "database": "spider_db",    "charset": "utf8mb4"}​batch_size = 500​insert_sql = """            insert into books(书名, 作者)            values(%s, %s)            """​# 在进行入库的时候，字段一定要清理成相应的字段def books_rows(books):    return [        (            b["书名"],b["作者"]                )        for b in books    ]    def save_mysql(books):    conn = None    try:        conn = pymysql.connect(**db_config)        rows = books_rows(books)                conn.begin()                with conn.cursor() as cursor:            cursor.execute("delete from books")            for i in range(0, len(rows), batch_size):                cursor.executemany(insert_sql, rows[i:i + batch_size])                        conn.commit()                with conn.cursor() as cursor:            cursor.execute("select count(*) from books")            count = cursor.fetchone()[0]            return count             except Exception as e:        if conn:            conn.rollback()        print(f"入库失败，已回滚：{e}")        return None        finally:        if conn:            conn.close()            print("MySQL 连接已关闭")          python

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'first_db',        
        'USER': 'root',            
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

##### 四、把已有的表映射成模型

如果已经有现成的建表 SQL，例如：

```mysql
create database if not exists test_db default character set utf8mb4 collate utf8mb4_unicode_ci;

use test_db;

create table if not exists sample_table(
	id int auto_increment primary key,
    record_date date,
    amount decimal(10,2) not null,
    quantity int not null,
    name varchar(100) not null,
	score float not null
);
```

就可以用 `inspectdb` 直接反向生成模型：

```txt
python manage.py inspectdb [表名1 表名2 ...] | Out-File -Encoding utf8 输出路径
```

中括号只是占位说明，不要照抄；不写表名就映射库里所有表。

##### 五、手写模型

如果还没有现成的表，就手动在 `myapp/models.py` 里定义模型：

```python
from django.db import models

class SampleTable(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="自增主键") 
    record_date = models.DateField(null=True, blank=True, verbose_name="记录日期")
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="金额"
    )
    quantity = models.IntegerField(verbose_name="数量")
    name = models.CharField(max_length=100, verbose_name="名称") 
    score = models.FloatField(verbose_name="评分")

    class Meta:
        db_table = "sample_table"   
        managed = True
        
```

| 参数 | 作用 |
| :--- | :--- |
| `null=True` | 数据库里允许为空（不写默认不允许为空） |
| `blank=True` | 只控制 Django 表单里该字段是否为“必填项” |
| `verbose_name` | 后台和表单里显示的字段标签文字 |
| `db_table` | 数据库里真实的表名 |

##### 六、数据库迁移

把 `models.py` 里 `Meta.managed` 的值改成 `True`，再执行下面的命令：

```
python manage.py makemigrations myapp
python manage.py migrate myapp --fake
```

##### 七、写入数据

回到能看到 `manage.py` 的目录，新建与它同级的 `first_demo.py`，用来准备测试数据：

```python
from datetime import date
from decimal import Decimal
from your_app.models import SampleTable

sample_list = [
    SampleTable(
        record_date=date(2024, 2, 20), amount=Decimal("1234.56"),
        quantity=10, name="苹果", score=88.25
    ),
    SampleTable(
        record_date=date(2024, 4, 1), amount=Decimal("0.01"),
        quantity=0, name="赠品", score=0.0
    ),
    SampleTable(
        record_date=None, amount=Decimal("9999.99"),
        quantity=1, name="无日期记录", score=100.0
    ),
]
```

这是一份测试数据（追加在上面的代码后面）：

```python
SampleTable.objects.bulk_create(sample_list)
```

这条语句可以一次性批量插入数据。

传统方式（逐条保存）：

```python
for item in sample_list:
	item.save()
```

##### 八、查询

下面介绍常用的查询写法。

```python
from django.db.models import Sum, Avg

res = SampleTable.objects.values("record_date").annotate(
    total_amount=Sum("amount"),    # 金额求和
    avg_score=Avg("score")         # 分数平均值
)
```

`values()`：指定按哪个字段分组（对应 SQL 的 group by）。

`annotate()`：分组之后要计算哪些统计值。

```python
res = SampleTable.objects.filter(
    quantity__gt=0
).values("record_date").annotate(
    total_amount=Sum("amount")
)
```

```mysql
select record_date, sum(amount) as total_amount
from sample_table
where quantity > 0
group by record_date;
```

写在 `values()` 之前：先筛行、再分组（对应 SQL 的 where）。

```python
res2 = SampleTable.objects.values("record_date").annotate(
    total_amount=Sum("amount")
).filter(total_amount__gt=2000)
```

```mysql
select record_date, sum(amount) as total_amount
from sample_table
group by record_date
having sum(amount) > 2000;
```

写在 `annotate()` 之后：先分组算完、再筛组（对应 SQL 的 having）。

| 操作符       | 含义 / SQL      | 操作符      | 含义 / SQL            |
| :----------- | :-------------- | :---------- | :-------------------- |
| __gte        | 大于等于        | __lte       | 小于等于              |
| __gt         | 大于            | __lt        | 小于                  |
| __in         | 在列表内        | __range     | 区间                  |
| __contains   | like '%x%' 包含 | __icontains | like '%x%' 忽略大小写 |
| __startswith | like 'x%' 开头  | __isnull    | is null 为空          |

##### 九、修改

先看批量修改：

```python
cnt = SampleTable.objects.filter(name="苹果").update(quantity=3,score=95.0)
print("修改了", cnt, "行")
```

```mysql
update sample_table set quantity=3, score=95.0 where name = '苹果';
```

单条记录修改：

```
obj = SampleTable.objects.get(name="苹果")
obj.quantity = 3
obj.save()
```

##### 十、删除

最后是删除：

```python
del_cnt = SampleTable.objects.filter(name="赠品").delete()
print(del_cnt)
```

```mysql
delete from sample_table where name="赠品"
```
