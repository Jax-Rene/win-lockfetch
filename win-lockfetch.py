# -*- coding: utf-8 -*-
from PIL import Image
import os, shutil

# win10 锁屏壁纸地址
src = "C:\\Users\\johnny\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets\\"
# 壁纸自定义存放地址
dest = "C:\\Users\\johnny\\Pictures\\Saved Pictures\\壁纸\\"

if __name__ == "__main__":
    # 过滤相同大小的图片（可能为重复图片）
    sendfiles = set()
    for path, dirs, files in os.walk(src):
        for f in files:
            file = path + f
            filesize = os.path.getsize(file)
            img = Image.open(file).size
            # 过滤小文件 以及 手机壁纸(竖)
            if filesize < 100000 or img[0] // img[1] <= 0 or filesize in sendfiles:
                continue
            sendfiles.add(filesize)
            destfile = dest + f + ".jpg"
            shutil.copy2(file, unicode(destfile, "utf-8"))
