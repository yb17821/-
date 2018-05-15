from selenium.webdriver import Chrome
from lxml import etree

import threading
import time
import json
import os
import pyautogui
import re

# username = '9179310493'
# password = 'yb1122yb'

# MYDXJ
# username = '9179114795'
# password = '199518'

# 张楠
username = '9179310424'
password = '120561'

# 张强 （拉黑）
# username = '9179100649'
# password = '850423'

# 句号先森
# username = '9179307757'
# password = '090110'

def w():
    time.sleep(10)
    pyautogui.typewrite(username)
    pyautogui.press('tab')
    pyautogui.typewrite(password)
    pyautogui.press('enter')



if not os.path.exists('answers.txt'):
    json.dump({}, open('answers.txt', 'w', encoding='utf-8'), ensure_ascii=False)

w = threading.Thread(target=w, args=[])
w.start()
browser = Chrome('D:\webdriver\chromedriver.exe')
browser.get('http://jwstu.cmjnu.com.cn:8080/')
while True:
    print('''选项:
        1)自动点击answers（若answers库没有该题，则提示还没做过这道题）
        2）读取并保存answers（提交试卷之后，选择此项可将所有题的answers保存到answers库）
        3）退出程序
		''')
    go = input('选择:')
    if go == '1':

        browser.switch_to_window(browser.window_handles[-1])
        page = browser.page_source
        html_tree = etree.HTML(page)


        ans_dic = json.load(open('answers.txt', 'r', encoding='utf-8'))

        q_list = browser.find_elements_by_xpath('//div[starts-with(@class,"uniQueItem")]')

        for q in q_list:

            queid = q.get_attribute('lqueid')
            print('题目ID:', queid)

            # li集合
            answers_li = q.find_elements_by_xpath('.//li')

            # answers
            ans_lt = ans_dic.get(queid)

            if not ans_lt:

                print('还没做过这道题，请先提交。')

            else:
                for i in range(len(ans_lt)):
                    if ans_lt[i] == True:
                        browser.execute_script("window.scrollTo(0,%s)" % answers_li[i].location['y'])
                        answers_li[i].click()



    elif go == '2':

        browser.switch_to_window(browser.window_handles[-1])
        page = browser.page_source
        html_tree = etree.HTML(page)


        question_text = 'question_text/' + html_tree.xpath('//h3[starts-with(@id,"ans_Title")]/text()')[0] + '.txt'
        if not os.path.exists(question_text):
            json.dump({}, open(question_text, 'w', encoding='utf-8'), ensure_ascii=False)


        ans_dic = json.load(open('answers.txt', 'r', encoding='utf-8'))
        question_answer_text_dic = json.load(open(question_text, 'r', encoding='utf-8'))
        q_list = html_tree.xpath('//div[starts-with(@class,"rep_loop")]')



        for q in q_list:

            # 获取q_id
            queid = str(q.xpath('.//a[@queid]/@queid')[0])

            # answers列表
            ans_lt = []
            question_answer_lt = []
            # 查找问题区域
            sq_area = q.xpath('.//div[starts-with(@class,"exercise")]')

            for sq in sq_area:

                answer_num = len(sq.xpath('.//li'))
                div = sq.xpath('.//div[@class="mb20 clearfix answer_area"]')[0]

                # 查看正确answers
                answers = str(div.xpath('.//span[@class="fl analy_x"]/text()')[0]).replace('\n', '').replace('\t',
                                                                                                            '').replace(
                    ' ', '')
                answers = answers.replace('\n', '').replace('\t', '').replace(' ', '')
                sansids = []
                if answers == '正确':
                    sansids.append('1')
                elif answers == '错误':
                    sansids.append('2')
                else:
                    for answer in answers:
                        sansids.append(str(ord(answer) - 64))

                for i in range(1, answer_num + 1):
                    if str(i) in sansids:
                        ans_lt.append(True)
                    else:
                        ans_lt.append(False)



            ans_dic[queid] = ans_lt


            # 查找问题内容div
            examMain_divs = q.xpath('.//div[@class="examMain"]')
            for examMain_div in examMain_divs:
                question_answer_text = examMain_div.xpath('string()').replace('\t', '').replace('\n', '').replace(' 解析',
                                                                                                                  '')
                question_answer_text = re.compile(' {1,}').sub(' ', question_answer_text)
                question_answer_text = re.compile('纠错 得分： 0 知识点： .+? 展开解析 ').sub(' ', question_answer_text)
                question_answer_lt.append(question_answer_text)
                print(question_answer_text)

            question_answer_text_dic[queid] = '\n'.join(question_answer_lt)
        for k, v in ans_dic.items():
            print('题目ID:', k)
            print('保存answers列表:', v)

        json.dump(ans_dic, open('answers.txt', 'w', encoding='utf-8'), ensure_ascii=False)
        json.dump(question_answer_text_dic, open(question_text, 'w', encoding='utf-8'), ensure_ascii=False)
    elif go == '3':

        browser.quit()
        break

    else:

        pass
