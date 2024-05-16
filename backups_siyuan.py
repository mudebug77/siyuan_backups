import requests
import os
from datetime import datetime, timedelta

# 思源地址
QINGLONG_URL = "http://192.168.0.8:6806"
#思源密码
AUTH_CODE = "123456"
#备份储存路径
SAVE_PATH = "/mnt/1/_backups/"
#备份文件前缀
PREFIX = "backups_siyuan_"
# 设置为0时不删除备份文件 (天)
DAYS_TO_KEEP = 30 

def login_auth():
    auth_url = QINGLONG_URL + "/api/system/loginAuth"
    data = {
        "authCode": AUTH_CODE,
        "captcha": ""
    }
    response = requests.post(auth_url, json=data)
    if response.status_code == 200:
        return response.cookies
    else:
        return None

def export_data(cookies):
    export_url = QINGLONG_URL + "/api/export/exportData"
    response = requests.post(export_url, cookies=cookies, json={})
    if response.status_code == 200:
        return response.json()
    else:
        return None

def download_file(url, destination):
    response = requests.get(url)
    if response.status_code == 200:
        with open(destination, 'wb') as f:
            f.write(response.content)
        return True
    else:
        return False

def delete_old_backups(backup_dir, days_to_keep):
    if days_to_keep == 0:
        return
    delete_before_date = datetime.now() - timedelta(days=days_to_keep)
    for file in os.listdir(backup_dir):
        file_path = os.path.join(backup_dir, file)
        if os.path.isfile(file_path):
            # 只删除以指定前缀开头的文件
            if file.startswith(PREFIX) and file.endswith(".zip"):
                file_time = datetime.fromtimestamp(os.path.getctime(file_path))
                if file_time < delete_before_date:
                    os.remove(file_path)
                    print(f"Deleted file: {file_path}")

def main():
    # 登录认证
    cookies = login_auth()
    if cookies is None:
        print("登录认证失败")
        return

    # 导出数据
    export_result = export_data(cookies)
    if export_result is None or export_result["code"] != 0:
        print("导出数据失败")
        return

    # 构造保存文件名
    now = datetime.now()
    date_time_str = now.strftime("%Y%m%d_%H%M%S")
    destination = os.path.join(SAVE_PATH, f"{PREFIX}{date_time_str}.zip")

    # 下载文件
    zip_url = QINGLONG_URL + export_result["data"]["zip"]
    if download_file(zip_url, destination):
        print("文件下载成功")
    else:
        print("文件下载失败")

    # 删除旧备份文件
    delete_old_backups(SAVE_PATH, DAYS_TO_KEEP)

if __name__ == "__main__":
    main()
