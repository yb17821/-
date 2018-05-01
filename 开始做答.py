from lxml import etree
import json
import os
with open(r'开始作答.txt','r',encoding='utf-8') as f:
    page = f.read()

html_tree = etree.HTML(page)


if not os.path.exists('test.txt'):
    json.dump({},open('test.txt','w',encoding='utf-8'),ensure_ascii=False)
ans_dic = json.load(open('test.txt','r',encoding='utf-8'))

q_list = html_tree.xpath('//div[starts-with(@class,"uniQueItem")]')


for q in q_list:

    queid = str(q.xpath('./@lqueid')[0])
    print(queid)

    answers = q.xpath('.//li')

    for answer in answers:
        sansid = str(answer.xpath('./@ansid')[0])

        print(sansid,answer.xpath('./text()')[0].replace('\t','').replace('\n',''))

