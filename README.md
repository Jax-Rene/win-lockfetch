# win-lockfetch
Win10 有个很好的特性就是每次锁屏的时候，就会随机的弄一张壁纸出来，而且壁纸质量都还不错。遗憾的是只有锁屏有提供而平时更常用的桌面壁纸却没这么贴心的功能了。

因此用Python写了脚本可以获取Win10锁屏的壁纸，到自定义路径。自定义路径可以设置成Win 10的壁纸地址，这样每次一有新锁屏壁纸更新，桌面壁纸也可以自动获得更新。



## 1.开始使用

clone 我的项目

``` bash
git clone https://github.com/iamjohnnyzhuang/win-lockfetch.git
```

编辑脚本，修改地址信息：

``` python
# win10 锁屏壁纸地址
src = "C:\\Users\\johnny\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets\\"
# 壁纸自定义存放地址
dest = "C:\\Users\\johnny\\Pictures\\Saved Pictures\\壁纸\\"

```



**tips:关于Assets的地址**

首先设置文件查看模式为查看隐藏文件，然后可以直接搜索。或者直接进入User目录然后就是差不多跟着我设置的那个路径。具体可以[点击参考](http://jingyan.baidu.com/article/fedf07375ea25135ad897761.html)



最后就是运行脚本，因为脚本使用了PIL对图片比例进行判断，因此需要先去[PIL官网](http://www.pythonware.com/products/pil/)下载对应版本。下载安装后，运行脚本：

``` bash
python win-lockfetch.py
```



## 2.设置开机自动刷新

建议设置成每次开机自动刷新获取一次，否则怎么能叫自动化呢？

下面是Windows设置开机脚本方法：

1. win 键 + r 打开运行窗口
2. 输入 shell:Startup 打开开机会运行的文件窗口
3. 在开文件夹下创建脚本文件 start.bat
4. 编辑文件

``` bash
# python 后面填写脚本地址
python D:\project\GitHub\win-lockfetch\win-lockfetch.py
```





## 结束

脚本虽小却也是挺有意义的一个小脚本，如果觉得该脚本对你有用，麻烦点个Star ^_^