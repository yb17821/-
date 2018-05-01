from lxml import etree
import json


with open(r'答卷详情.txt','r',encoding='utf-8') as f:
    data = f.read()

html_tree = etree.HTML(data)



ans_dic = json.load(open('test.txt','r',encoding='utf-8'))

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
        answer = str(div.xpath('.//span[@class="fl analy_x"]/text()')[0]).replace('\n', '').replace('\t', '').replace(' ', '')
        sansid = str(ord(answer) - 64)
        for i in range(1,answer_num+1):

            if str(i) == sansid:
                ans_lt.append(True)
            else:
                ans_lt.append(False)
    ans_dic[queid] = ans_lt

for k,v in ans_dic.items():
    print(k,v)

json.dump(ans_dic,open('test.txt','w',encoding='utf-8'),ensure_ascii=False)