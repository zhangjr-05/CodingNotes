import time
from DrissionPage import Chromium

browser = Chromium()
browser.set.retry_times(10)
tab = browser.latest_tab
tab.get('https://cslab-cms.nju.edu.cn/classrooms')
time.sleep(0.2)

tab.ele('@text()=我的').click()
time.sleep(0.2)
tab.ele('@text()=人工智能程序设计-25-春').click()
time.sleep(2)
while True:
    tab = browser.latest_tab
    tab.refresh()
    time.sleep(1)
browser.quit()

