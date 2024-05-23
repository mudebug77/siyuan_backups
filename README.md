# 思源笔记备份脚本

用青龙面板 备份 思源笔记
- whyour/qinglong
- b3log/siyuan
- siyuan-note

- 发送登录认证请求到思源地址。
- 导出数据并下载备份文件。
- 构造保存文件名，文件名包含日期时间信息。
- 删除旧备份文件，保留指定天数内的备份文件。

  我的做法是创建青龙面板时，映射一个目录进青龙容器，
  这个目录可以是挂载的网络磁盘，也可以是磁盘，也可以是青龙本身的目录。看个人需求
  然后执行时把备份放到对应的目录下

  - 恢复数据,在设置中,点击导入选择对应的备份文件

## 使用方法

1. 在脚本中设置变量：
   - `QINGLONG_URL`: 思源 的地址。
   - `AUTH_CODE`: 认证代码。
   - `SAVE_PATH`: 备份文件保存路径。
   - `PREFIX`: 备份文件名前缀。
   - `DAYS_TO_KEEP`: 保留备份文件的天数，设置为 0 时不删除。
2. 青龙依赖管理 python 添加 requests 依赖库
3. 在青龙面板中设置定期执行即可

![image](https://github.com/mudebug77/siyuan_backups/assets/34656102/6325be5a-cb00-465e-8226-429e1720a3d3)
