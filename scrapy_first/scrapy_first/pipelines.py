# 在此定义你的数据管道（Item Pipeline）
# 注意：编写完成后，需要到 settings.py 的 ITEM_PIPELINES 配置项中启用对应管道
# 官方文档：https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# ItemAdapter：统一适配不同类型的数据对象（字典、Item类、dataclass等），提供一致的读写方式
from itemadapter import ItemAdapter


class ScrapyFirstPipeline:
    """项目默认的数据管道类，用于处理爬虫提交的数据"""

    def process_item(self, item, spider):
        """
        管道核心处理方法，爬虫提交的每一条数据都会经过此方法
        :param item: 爬虫 yield 提交的爬取数据
        :param spider: 当前运行的爬虫实例
        :return: 处理后的数据，会传递给下一个管道；如需丢弃数据可抛出 DropItem 异常
        """
        # 当前默认无任何处理，直接返回原数据
        return item
