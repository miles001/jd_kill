from selenium import webdriver

from utils.cookieUtil import checkCookie, mainPath, jobName

# 模拟浏览器代理
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4051.0 Safari/537.36 Edg/82.0.425.0'}

# 设置Chrome浏览器
chrome_options = webdriver.ChromeOptions()
# 隐身访问
# chrome_options.add_argument('--incognito')

# 不加载图片, 提升速度
# chrome_options.add_argument('--blink-settings=imagesEnabled=false')
# 改进：如果存在cookie，则说明无需验证登录，则可以设置为不加载图片以提升速度
if checkCookie(jobName):
    chrome_options.add_argument('--blink-settings=imagesEnabled=false')

# 不打开浏览器窗口
# chrome_options.add_argument("headless")

# 告诉编译器chromedriver在哪个位置并注册(如更换驱动版本则需要进行修改)
chrome = webdriver.Chrome(mainPath + "/utils/chromedriver",
                          chrome_options=chrome_options)
