from lxml import etree
import json
import re
import os

if not os.path.exists('test.txt'):
    json.dump({}, open('test.txt', 'w', encoding='utf-8'), ensure_ascii=False)
if not os.path.exists('question_text.txt'):
    json.dump({}, open('question_text.txt', 'w', encoding='utf-8'), ensure_ascii=False)

with open(r'答卷详情.txt','r',encoding='utf-8') as f:
    data = f.read()

html_tree = etree.HTML(data)



ans_dic = json.load(open('test.txt','r',encoding='utf-8'))
question_answer_text_dic = json.load(open('question_text.txt', 'r', encoding='utf-8'))

# 查找大题区域
q_list = html_tree.xpath('//div[starts-with(@class,"rep_loop")]')
for q in q_list:
    # 获取q_id
    queid = str(q.xpath('.//a[@queid]/@queid')[0])

    # test列表
    ans_lt = []
    question_answer_lt = []


    # 查找小题题区域
    sq_area = q.xpath('.//div[starts-with(@class,"exercise ")]')
    for sq in sq_area:
        answer_num = len(sq.xpath('.//li'))
        div = sq.xpath('.//div[@class="mb20 clearfix answer_area"]')[0]

        # 查看正确test
        answer = str(div.xpath('.//span[@class="fl analy_x"]/text()')[0]).replace('\n', '').replace('\t', '').replace(' ', '')
        print(answer,type(answer))
        answers = answer.replace('\n', '').replace('\t', '').replace(' ', '')
        sansids = []

        if answer == '正确':
            sansids.append('1')
        elif answer == '错误':
            sansids.append('2')
        else:
            for answer in answer:
                sansids.append(str(ord(answer) - 64))

        for i in range(1,answer_num+1):
            if str(i) in sansids:
                ans_lt.append(True)
            else:
                ans_lt.append(False)
    # 将答案写入字典
    ans_dic[queid] = ans_lt

    #查找问题内容div
    examMain_divs = q.xpath('.//div[@class="examMain"]')
    for examMain_div in examMain_divs:
        question_answer_text = examMain_div.xpath('string()').replace('\t', '').replace('\n', '').replace(' 解析', '')
        question_answer_text = re.compile(' {1,}').sub(' ',question_answer_text)
        question_answer_text = re.compile('纠错 得分： 0 知识点： .+? 展开解析 ').sub(' ', question_answer_text)
        question_answer_lt.append(question_answer_text)
        print(question_answer_text)

    question_answer_text_dic[queid] = '\n'.join(question_answer_lt)









for k,v in ans_dic.items():
    print(k,v)

json.dump(ans_dic,open('test.txt','w',encoding='utf-8'),ensure_ascii=False)
json.dump(question_answer_text_dic,open('question_text.txt','w',encoding='utf-8'),ensure_ascii=False)