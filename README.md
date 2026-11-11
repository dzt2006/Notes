## Git 操作速查

### 首次初始化并推送

```bash
# 1. 初始化本地仓库
git init

# 2. 关联远程仓库
git remote add origin https://github.com/dzt2006/Projects.git

# 3. 拉取远程已有文件（如 README），合并不相关历史
#    如果远程仓库完全为空，可跳过此步
git pull origin main --allow-unrelated-histories

# 4. 暂存所有文件
git add .

# 5. 检查暂存状态（确认无误后再提交）
git status

# 6. 提交到本地仓库
git commit -m "初始化仓库，上传所有项目代码"

# 7. 基于当前 master 分支，创建并切换到 main 分支
git checkout -b main

# 8. 推送到远程 main 分支，并建立追踪关系
git push -u origin main
```

### 日常提交流程

```bash
git add .
git commit -m "你的提交说明"
git push
```

### 删除多余的 master 分支

```bash
# 1. 确保当前在 main 分支
git checkout main

# 2. 安全删除本地 master（仅当 master 的所有提交已合并到 main 时生效）
git branch -d master

# 3. 删除远程 master 分支
git push origin --delete master
```
