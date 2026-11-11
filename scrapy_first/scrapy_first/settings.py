# Scrapy_first 项目配置文件
# 本文件仅列出常用核心配置，完整配置参考官方文档：
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html


# ========== 1. 基础项目配置（自动生成，无需修改） ==========
# 爬虫项目名称（运行日志中会显示）
BOT_NAME = "scrapy_first"

# 爬虫代码所在的模块路径
SPIDER_MODULES = ["scrapy_first.spiders"]
# 执行 genspider 命令时，新爬虫默认存放的目录
NEWSPIDER_MODULE = "scrapy_first.spiders"


# ========== 2. 请求身份与爬取规则（新手建议修改） ==========
# 设置请求的 User-Agent，伪装成浏览器访问，避免被反爬直接拦截
# 取消注释后替换成真实浏览器的 UA 字符串
#USER_AGENT = "scrapy_first (+http://www.yourdomain.com)"

# 是否遵守网站的 robots.txt 爬取规则
# 学习/测试阶段建议改为 False，否则很多网站会直接禁止爬取
ROBOTSTXT_OBEY = True


# ========== 3. 并发与请求限速（控制爬速，防止被封IP） ==========
# 全局最大并发请求数，默认 16
# 数值越大爬取越快，同时被网站封禁的风险越高
#CONCURRENT_REQUESTS = 32

# 同一网站两次请求之间的最小间隔时间（单位：秒）
# 设置后会降低爬取速度，减小服务器压力和封禁风险
# 参考文档：https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
#DOWNLOAD_DELAY = 3

# 以下两个配置二选一生效，分别按「域名」或「IP」限制并发数
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16


# ========== 4. 基础功能开关 ==========
# 是否启用 Cookie，默认开启（需要登录的网站必须保持开启）
#COOKIES_ENABLED = False

# 是否启用 Telnet 远程调试控制台，默认开启
#TELNETCONSOLE_ENABLED = False

# 全局默认请求头，可统一设置 Accept、语言等参数
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}


# ========== 5. 中间件配置（进阶扩展用） ==========
# 蜘蛛中间件：处理蜘蛛层面的请求、响应和深度控制等
# 参考文档：https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "scrapy_first.middlewares.ScrapyFirstSpiderMiddleware": 543,
#}

# 下载中间件：处理代理、UA池、重试、IP池等反爬逻辑
# 参考文档：https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "scrapy_first.middlewares.ScrapyFirstDownloaderMiddleware": 543,
#}


# ========== 6. 扩展与数据管道 ==========
# 功能扩展配置
# 参考文档：https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# 数据管道：用于数据清洗、去重、保存到文件/数据库
# 参考文档：https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "scrapy_first.pipelines.ScrapyFirstPipeline": 300,
#}


# ========== 7. 自动限速扩展（根据网络延迟自动调速） ==========
# 参考文档：https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# 初始下载延迟（秒）
#AUTOTHROTTLE_START_DELAY = 5
# 高延迟场景下的最大下载延迟（秒）
#AUTOTHROTTLE_MAX_DELAY = 60
# 目标平均并发请求数
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# 是否开启自动限速的调试日志
#AUTOTHROTTLE_DEBUG = False


# ========== 8. HTTP缓存（调试时开启，重复爬取省流量） ==========
# 参考文档：https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"


# ========== 9. 底层兼容配置（请勿删除或修改） ==========
# 请求指纹算法版本
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
# 异步事件循环配置
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
# 数据导出编码，设为 utf-8 解决中文乱码问题
FEED_EXPORT_ENCODING = "utf-8"
