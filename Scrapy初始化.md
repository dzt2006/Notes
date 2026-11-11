

```cmd
scrapy startproject scrapy_first
```

自动创建 Scrapy 项目并生成完整的标准目录结构



```cmd
scrapy genspider demo example.com
```

这里会生成一个模板的爬虫文件



- `demo`：既是爬虫文件名，也是爬虫的内部唯一标识，通过 `scrapy crawl demo` 启动该爬虫
- `example.com`：初始化的允许爬取域名，自动写入 `allowed_domains`，用于限定爬取范围





```txt
scrapy_first/
├── scrapy_first/
│   ├── spiders/
│   │   ├── __init__.py     # 爬虫包标识文件
│   │   └── demo.py         # 爬虫业务脚本，编写爬取逻辑
│   ├── __init__.py         # 项目包标识文件
│   ├── items.py            # 定义爬取数据的字段结构
│   ├── middlewares.py      # 请求/响应中间件，处理反爬、代理
│   ├── pipelines.py        # 数据管道，负责数据清洗、存储
│   └── settings.py         # 项目核心配置文件
└── scrapy.cfg              # 项目全局配置、部署入口

```

[打开 scrapy_first 项目文件夹（中文版）](scrapy_first)



```cmd
cd scrapy_first
```

终端路径必须进入外层 `scrapy_first` 目录（也就是包含 `scrapy.cfg` 文件的那一层



```cmd
scrapy crawl demo
```


