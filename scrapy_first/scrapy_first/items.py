# 在此定义爬取数据模型（Item）
# 作用：结构化声明需要采集的字段，统一封装爬取数据，便于后续管道处理
# 官方文档：https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyFirstItem(scrapy.Item):
    """
    项目默认的数据模型类
    继承自 scrapy.Item，本质是专用的数据容器（类似字典）
    所有爬取到的单条数据，都可以封装成该类的对象再提交给管道
    在此按格式定义你需要的字段：字段名 = scrapy.Field()
    示例：
        title = scrapy.Field()   # 页面标题
        price = scrapy.Field()   # 商品价格
        link = scrapy.Field()    # 详情链接
    """
    # 在此定义你的爬取字段，示例：
    # name = scrapy.Field()
    pass
