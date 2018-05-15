import os
import json
import re
question_text_dir = 'question_text'
test_paper_dir = 'test_paper'
filename_list = os.listdir(question_text_dir)
for filename in filename_list:
    new_filename = os.path.join(question_text_dir,filename)
    test_paper_filename = os.path.join(test_paper_dir,filename)
    file_dic = json.load(open(new_filename, 'r', encoding='utf-8'))
    with open(test_paper_filename,'w',encoding='utf-8') as f:
        for _,v in file_dic.items():
            v = re.compile('得分： .*? 展开解析').sub('',v)
            v = v.replace('A.','\nA.').replace('B.','\nB.').replace('C.','\nC.').replace('D.','\nD.').replace('E.','\nE.').replace('F.','\nF.').replace('G.','\nG.').replace('纠错','').replace('答案','\n答案')
            duan = int(len(v)/80)
            v = list(v)
            for i in range(1,duan+1):
                for j in range(80*i,80*i+20):
                    try:
                        if v[j] == ' ':
                            v[j] = ' \n'
                            break
                    except IndexError:
                        break
            v = ''.join(v)



            f.write(v)
            f.write('\n')


