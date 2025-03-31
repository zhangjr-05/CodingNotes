import time
import ddddocr
import requests
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (NoSuchElementException,
                                        TimeoutException,
                                        ElementClickInterceptedException)

# 配置信息
CONFIG = {
    "no": '241300022',
    "pw": 'zjr985512',
    "driver_path": 'D:/tools/msedgedriver.exe',
    "login_url": 'https://xk.nju.edu.cn',
    "max_retries": 5  # 最大重试次数
}

# 初始化浏览器（只执行一次）
service = Service(executable_path=CONFIG['driver_path'])
options = webdriver.EdgeOptions()
# options.add_argument("--headless")  # 无头模式（可选）
driver = webdriver.Edge(service=service, options=options)
wait = WebDriverWait(driver, 10)  # 全局显式等待

def handle_captcha():
    """处理验证码流程"""
    for _ in range(3):  # 最多重试3次
        try:
            # 下载验证码
            img_element = wait.until(
                EC.presence_of_element_located((By.ID, 'vcodeImg'))
            )
            image_src = img_element.get_attribute('src')
            image_response = requests.get(image_src, timeout=5)
            with open('captcha.jpg', 'wb') as f:
                f.write(image_response.content)
            
            # 识别验证码
            ocr = ddddocr.DdddOcr()
            with open('captcha.jpg', 'rb') as f:
                captcha = ocr.classification(f.read())
            if len(captcha) == 4:
                return captcha
        except Exception as e:
            print(f"验证码处理失败，重试中... ({e})")
            driver.refresh()  # 刷新页面获取新验证码
    raise Exception("验证码处理超过最大重试次数")

def login():
    """执行登录操作"""
    driver.get(CONFIG['login_url'])
    print("成功打开登录页面")
    
    # 输入账号信息
    no_box = wait.until(EC.presence_of_element_located((By.ID, 'loginName')))
    pw_box = driver.find_element(By.ID, 'loginPwd')
    cc_box = driver.find_element(By.ID, 'verifyCode')
    
    # 处理验证码
    captcha = handle_captcha()
    
    # 填写表单
    no_box.send_keys(CONFIG['no'])
    pw_box.send_keys(CONFIG['pw'])
    cc_box.send_keys(captcha)
    
    # 点击登录
    login_btn = driver.find_element(By.ID, 'studentLoginBtn')
    login_btn.click()
    
    # 验证登录是否成功
    try:
        wait.until(EC.presence_of_element_located((By.ID, 'courseBtn')))
        print("登录成功！")
        return True
    except TimeoutException:
        print("登录失败，可能验证码错误")
        return False

def select_courses():
    """执行选课操作"""
    try:
        # 进入选课界面
        wait.until(EC.element_to_be_clickable((By.ID, 'courseBtn'))).click()
        time.sleep(0.5)
        
        # 切换到收藏页面
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, '收藏'))).click()
        time.sleep(0.5)  # 适当等待数据加载
        
        # 获取所有可选课程
        stars = wait.until(
            EC.presence_of_all_elements_located((By.LINK_TEXT, '选择')))
        
        for star in stars:
            try:
                star.click()
                # 处理弹窗
                confirm_btn = wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, '.cv-sure.cvBtnFlag')))
                confirm_btn.click()
                time.sleep(0.3)
                confirm_btn = wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, '.cv-sure.cvBtnFlag')))
                confirm_btn.click()
                time.sleep(0.3)

            except (ElementClickInterceptedException, TimeoutException):
                print("坏了！")
                continue
    except Exception as e:
        print(f"选课过程中出现异常: {e}")

# 主程序逻辑

while True:
    try:
        if login():
            select_courses()
        else:
            print(f"登录失败，正在重试")
    except Exception as e:
        print(f"主流程异常: {e}")
        driver.refresh()  # 刷新页面重试

# 最终清理
driver.quit()
print("程序执行完毕")