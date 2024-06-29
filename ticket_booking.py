from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# 设置ChromeDriver路径
driver_path = 'chromedriver'  # 替换为你的chromedriver路径
url = 'https://mall.bilibili.com/mall-dayu/neul-next/ticket/detail.html?id=85939&from=itemshare&noTitleBar=1&share_source=weixin&share_medium=iphone&bbid=41F10451-36E1-E5CC-20E4-F5C84BC2679506228infoc&ts=1719628034444'

# 初始化浏览器
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=driver_path, options=options)
driver.get(url)

try:
    # 等待页面加载
    time.sleep(3)

    # 找到并点击“即将开售”按钮
    start_button = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div[4]/div[2]/div[1]/div/button')
    ActionChains(driver).move_to_element(start_button).click().perform()

    # 等待弹出登录框（如果需要登录）
    time.sleep(1)
    try:
        login_username = driver.find_element(By.XPATH, '//*[@id="login-username"]')
        login_password = driver.find_element(By.XPATH, '//*[@id="login-password"]')
        login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')

        # 输入用户名和密码并点击登录
        login_username.send_keys('your_username')  # 替换为你的用户名
        login_password.send_keys('your_password')  # 替换为你的密码
        login_button.click()

        # 等待登录完成
        time.sleep(2)
    except:
        print("已登录，继续执行抢票")

    # 选择票种和数量（假设选择第一个票种）
    ticket_type = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div[4]/div[2]/div[2]/div[1]')
    ActionChains(driver).move_to_element(ticket_type).click().perform()
    time.sleep(0.5)

    # 点击“立即购买”按钮
    buy_button = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div[4]/div[2]/div[3]/button')
    ActionChains(driver).move_to_element(buy_button).click().perform()

    # 进入支付页面并完成支付（假设自动完成）
    time.sleep(1)
    print("抢票成功，请手动完成支付")

except Exception as e:
    print(f"操作失败: {e}")
finally:
    # 关闭浏览器
    driver.quit()
