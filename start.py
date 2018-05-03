from selenium.webdriver import Chrome, PhantomJS
from lxml import etree

import threading
import time
import json
import os
import pyautogui


def w():
    time.sleep(10)
    pyautogui.typewrite('9179310493')
    pyautogui.press('tab')
    pyautogui.typewrite('yb1122yb')
    pyautogui.press('enter')


w = threading.Thread(target=w, args=[])
w.start()
browser = Chrome('D:\webdriver\chromedriver.exe')
browser.get('http://jwstu.cmjnu.com.cn:8080/')

while True:
    go = input('go?:')
    if go == '1':
        browser.switch_to_window(browser.window_handles[-1])
        page = browser.page_source
        html_tree = etree.HTML(page)

        if not os.path.exists('daan2.txt'):
            json.dump({}, open('daan2.txt', 'w', encoding='utf-8'), ensure_ascii=False)
        ans_dic = json.load(open('daan2.txt', 'r', encoding='utf-8'))

        q_list = browser.find_elements_by_xpath('//div[starts-with(@class,"uniQueItem")]')

        for q in q_list:

            queid = q.get_attribute('lqueid')
            print(queid)

            # li集合
            answers_li = q.find_elements_by_xpath('.//li')

            # 答案
            ans_lt = ans_dic.get(queid)

            if not ans_lt:
			
                print('还没做过这道题，请先提交。')
                
            else:
                for i in range(len(ans_lt)):
                    if ans_lt[i] == True:
                        answers_li[i].click()


        json.dump(ans_dic, open('daan2.txt', 'w', encoding='utf-8'), ensure_ascii=False)
		
    elif go == '2':

        browser.switch_to_window(browser.window_handles[-1])
        page = browser.page_source
        html_tree = etree.HTML(page)
        ans_dic = json.load(open('daan2.txt', 'r', encoding='utf-8'))
        q_list = html_tree.xpath('//div[starts-with(@class,"rep_loop")]')

        for q in q_list:
		
            # 获取q_id
            queid = str(q.xpath('.//a[@queid]/@queid')[0])

            # 答案列表
            ans_lt = []

            # 查找问题区域
            sq_area = q.xpath('.//div[starts-with(@class,"exercise")]')
			
            for sq in sq_area:
			
                answer_num = len(sq.xpath('.//li'))
                div = sq.xpath('.//div[@class="mb20 clearfix answer_area"]')[0]

                # 查看正确答案
                answer = str(div.xpath('.//span[@class="fl analy_x"]/text()')[0]).replace('\n', '').replace('\t',
                                                                                                            '').replace(
                    ' ', '')
                sansid = str(ord(answer) - 64)
				
                for i in range(1, answer_num + 1):

                    if str(i) == sansid:
					
                        ans_lt.append(True)
						
                    else:
					
                        ans_lt.append(False)
						
            ans_dic[queid] = ans_lt

        for k, v in ans_dic.items():
		
            print(k, v)

        json.dump(ans_dic, open('daan2.txt', 'w', encoding='utf-8'), ensure_ascii=False)

    elif go == 'n':
	
        browser.quit()
        break

    else:

        pass
