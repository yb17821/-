from selenium.webdriver import Chrome, PhantomJS
from lxml import etree

import threading
import time
import json
import os
import pyautogui
browser = Chrome('D:\webdriver\chromedriver.exe')
browser.get('https://www.cnblogs.com/hjhsysu/p/5735339.html')
# next = browser.find_element_by_id('green_channel_digg')
next = browser.find_element_by_partial_link_text('更多知识库文章...')
a = next.location
# print(a,type(a))
# {'x': 311, 'y': 3169}
browser.execute_script("window.scrollTo(0,%s)" % a['y'])
print('找到了')

# browser.quit()