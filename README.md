## 介绍：

​	这是一个基于Python Selenium实现的京东购物车秒杀脚本，因为是基于Selenium进行的制作，所以需要提前下载好浏览器驱动并进行相关配置，源文件提供了MacOS下的使用，前提是满足运行环境要求，如果你的电脑不是MacOS或者你的Chrome浏览器版本不对，那么请看环境配置篇

## 运行环境：

- Python3.10
- MacOS
- Chrome浏览器(版本号：105.0.5195.102)

## 环境配置：

- 电脑下载Chrome浏览器，获取Chrome浏览器的版本号
![This is an image](/image/image-20220910191259740.png)
- 前往 http://chromedriver.storage.googleapis.com/index.html 下载对应版本号对应操作系统的浏览器驱动(非常重要！！！！)
![This is an image](/image/image-20220910191413359.png)
- 将下载下来的驱动放进utils文件夹下，打开depend.py，修改第22行参数，例如Windows下可能需要改为 文件名.exe!
![This is an image](/image/image-20220910191910122.png)
- 运行jd.py，如果程序打开了一个Chrome浏览器，则说明设置正确，可以开始正式使用了

## 使用步骤：

- 将需要购买的商品添加进购物车
- 在main.py中修改buyTime和cnt的值
- 运行main.py(首次使用需要扫码进行登录)

## Tips:

1. 软件会自动保存和读取历史的cookie以用于自动登陆，如果长期未使用，请清空cookie文件夹下的内容
2. 如果程序提示路径错误，请前往cookieUtil.py进行检查
3. 目前该脚本只支持购物车抢购，如果需要定制，欢迎联系我，我的闲鱼：https://m.tb.cn/h.UYTjaoi?tk=Bru62Eu75Og CZ3457 点击链接直接打开
4. 因为测试样本有限，可能会有一些流程没有考虑到而导致出现bug，欢迎提出issue，如果你觉得满意，也请给我star
