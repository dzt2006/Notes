# Git 操作速查



## 首次配置（新电脑只做一次）

```bash
git config --global user.name "dzt2006"

git config --global user.email "430249441@qq.com"
```



## 新电脑拉取

```bash
git clone https://github.com/dzt2006/Notes.git

cd Notes
```

拉取之后，按下面的「日常更新」操作即可。



## 新建仓库

```bash
git init -b main

git remote add origin https://github.com/dzt2006/Notes.git

git add .

git commit -m "首次上传"

git push -u origin main
```



## 日常更新

```bash
git add .

git commit -m "改动说明"

git push
```
