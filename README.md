##### Git 操作速查

##### 首次配置（新电脑只做一次）

```bash
git config --global user.name "dzt2006"

git config --global user.email "430249441@qq.com"
```

##### 新电脑拉取

```bash
git clone https://github.com/dzt2006/Notes.git

cd Notes
```

拉取之后，按下面的「日常更新」操作即可。

##### 新建仓库

```bash
git init -b main

git remote add origin https://github.com/dzt2006/Notes.git

git add .

git commit -m "首次上传"

git push -u origin main
```

##### 日常更新

```bash
git add .

git commit -m "改动说明"

git push
```

---

##### 目录

所有笔记的总入口，点击任意条目可直接跳转到对应文件的小节（Git 操作就在本文件上方，不再列入）。

##### Django 项目初始化

- [一、创建项目与应用](django初始化.md#一创建项目与应用)

- [二、注册应用并启动](django初始化.md#二注册应用并启动)

- [三、配置 MySQL](django初始化.md#三配置-mysql)

- [四、把已有的表映射成模型](django初始化.md#四把已有的表映射成模型)

- [五、手写模型](django初始化.md#五手写模型)

- [六、数据库迁移](django初始化.md#六数据库迁移)

- [七、写入数据](django初始化.md#七写入数据)

- [八、查询](django初始化.md#八查询)

- [九、修改](django初始化.md#九修改)

- [十、删除](django初始化.md#十删除)

##### Scrapy 项目初始化

- [一、创建项目](Scrapy初始化.md#一创建项目)

- [二、生成爬虫](Scrapy初始化.md#二生成爬虫)

- [三、运行爬虫](Scrapy初始化.md#三运行爬虫)

##### 函数记忆

- [取文本（XPath）](模板补充.md#取文本xpath)

- [类型统计](模板补充.md#类型统计)

- [数据写入](模板补充.md#数据写入)

  - [列表转字典](模板补充.md#列表转字典)

  - [原生 csv.writer 写法](模板补充.md#原生-csvwriter-写法)

  - [Pandas 写法](模板补充.md#pandas-写法)

  - [JSON 写入](模板补充.md#json-写入)

##### 模板

- [爬虫通用模板](模板.md#爬虫通用模板)

- [数据清洗](模板.md#数据清洗)

  - [数据清洗流程](模板.md#数据清洗流程)

- [分批写入数据库](模板.md#分批写入数据库)
