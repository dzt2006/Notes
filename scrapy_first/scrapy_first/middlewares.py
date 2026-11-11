# 在此定义蜘蛛中间件与下载中间件
# 官方文档：https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# is_item：判断对象是否为 Item 类型
# ItemAdapter：统一适配不同类型的数据对象，提供一致的读写方式
from itemadapter import is_item, ItemAdapter


class ScrapyFirstSpiderMiddleware:
    """
    蜘蛛中间件：在蜘蛛（Spider）层面拦截处理
    作用时机：响应进入蜘蛛前、蜘蛛产出结果后、异常发生时
    常用于：数据预处理、异常捕获、起始请求修改等
    无需全部方法都实现，未定义的方法相当于不做任何修改
    """

    @classmethod
    def from_crawler(cls, crawler):
        """
        Scrapy 创建中间件实例的入口方法
        可在此获取配置、绑定信号事件
        """
        s = cls()
        # 绑定「蜘蛛启动」信号，触发 spider_opened 方法
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        """
        响应进入蜘蛛的 parse 方法前调用
        返回 None：继续向下传递；抛出异常：进入异常处理流程
        """
        return None

    def process_spider_output(self, response, result, spider):
        """
        蜘蛛 parse 方法执行完成后，处理其 yield 产出的结果
        result 包含请求（Request）和数据（Item）
        必须返回可迭代的请求或数据对象
        """
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        """
        蜘蛛或上游蜘蛛中间件抛出异常时调用
        可返回 None 继续传递异常，或返回请求/数据终止异常传递
        """
        pass

    def process_start_requests(self, start_requests, spider):
        """
        处理蜘蛛的起始请求（爬虫启动时的第一批请求）
        只能返回请求对象，不能返回数据
        """
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        """蜘蛛启动完成时触发，打印启动日志"""
        spider.logger.info("Spider opened: %s" % spider.name)


class ScrapyFirstDownloaderMiddleware:
    """
    下载中间件：在下载器层面全局拦截请求和响应
    作用时机：请求发出前、响应返回后、下载异常时
    最常用场景：设置UA池、代理IP、请求重试、Cookie处理等反爬逻辑
    无需全部方法都实现，未定义的方法相当于不做任何修改
    """

    @classmethod
    def from_crawler(cls, crawler):
        """
        Scrapy 创建中间件实例的入口方法
        可在此获取配置、绑定信号事件
        """
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        """
        每个请求发出前都会调用（最常用的方法）
        可选返回值：
        - None：继续处理请求，传递给下一个中间件
        - Response 对象：直接返回响应，不再发送真实请求
        - Request 对象：重新调度新请求，终止当前中间件链
        - 抛出 IgnoreRequest：丢弃该请求，进入异常处理
        """
        return None

    def process_response(self, request, response, spider):
        """
        下载器拿到响应后、交给蜘蛛前调用
        可选返回值：
        - Response 对象：继续向下传递给蜘蛛
        - Request 对象：重新调度新请求
        - 抛出 IgnoreRequest：丢弃该响应
        """
        return response

    def process_exception(self, request, exception, spider):
        """
        下载失败或上游中间件抛出异常时调用
        可选返回值：
        - None：继续传递异常
        - Response 对象：终止异常链，当作正常响应返回
        - Request 对象：终止异常链，重新调度请求（常用于重试）
        """
        pass

    def spider_opened(self, spider):
        """蜘蛛启动完成时触发，打印启动日志"""
        spider.logger.info("Spider opened: %s" % spider.name)
