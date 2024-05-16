# Qinglong 备份脚本

用青龙面板 备份 思源笔记
	whyour/qinglong
  b3log/siyuan

- 发送登录认证请求到指定的 Qinglong 地址。
- 导出数据并下载备份文件。
- 构造保存文件名，文件名包含日期时间信息。
- 删除旧备份文件，保留指定天数内的备份文件。

## 使用方法

1. 在脚本中设置变量：
   - `QINGLONG_URL`: 思源 的地址。
   - `AUTH_CODE`: 认证代码。
   - `SAVE_PATH`: 备份文件保存路径。
   - `PREFIX`: 备份文件名前缀。
   - `DAYS_TO_KEEP`: 保留备份文件的天数，设置为 0 时不删除。
2. 青龙依赖管理 python 添加 requests 依赖库
3. 在青龙面板中设置定期执行即可
