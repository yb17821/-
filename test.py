# import requests
# import urllib.request
# # url = "9179310493=FdzID=3402&FdzName=(%e5%ae%89%e5%be%bd%e8%8a%9c%e6%b9%96)%e5%ae%89%e5%be%bd%e5%95%86%e8%b4%b8%e8%81%8c%e4%b8%9a%e6%8a%80%e6%9c%af%e5%ad%a6%e9%99%a2&NodeID=&NodeName=&UserName=%e6%9d%a8%e6%96%8c&StuID=9179310493&StuLevel=201709&StudyKindID=3&StudyKind=%e4%b8%9a%e4%bd%99%e4%b8%93%e5%8d%87%e6%9c%ac&Subject=%e8%ae%a1%e7%ae%97%e6%9c%ba%e7%a7%91%e5%ad%a6%e4%b8%8e%e6%8a%80%e6%9c%af&SubjectID=305&StudentStatus=1&ArchieveID=3402010170902145836053&StuRebate=0.80000&IsGraduated=0&CheckinDate=2017/9/2 14:58:36&CourseID='07008A','07017A','11076A','12004A','03003A','03009A','07003A','12005A','13021A'; _pk_ses.61.4d6a=*; ASP.NET_SessionId=rlhffx00u3fmfluhiftzxcec; _pk_id.61.4d6a=bfe8df247fac2a06.1522029915.6.1524295609.1524295250."
#
# headers = {
#
# 'Authorization': 'Basic OTE3OTMxMDQ5Mzp5YjExMjJ5Yg==',
# # 'Cookie': "9179310493=FdzID=3402&FdzName=(安徽芜湖)安徽商贸职业技术学院&NodeID=&NodeName=&UserName=杨斌&StuID=9179310493&StuLevel=201709&StudyKindID=3&StudyKind=业余专升本&Subject=计算机科学与技术&SubjectID=305&StudentStatus=1&ArchieveID=3402010170902145836053&StuRebate=0.80000&IsGraduated=0&CheckinDate=2017/9/2 14:58:36&CourseID='07008A','07017A','11076A','12004A','03003A','03009A','07003A','12005A','13021A'; _pk_ses.61.4d6a=*; ASP.NET_SessionId=rlhffx00u3fmfluhiftzxcec; _pk_id.61.4d6a=bfe8df247fac2a06.1522029915.6.1524295609.1524295250.",
# 'Cookie': "9179310493=FdzID=3402&FdzName=(%e5%ae%89%e5%be%bd%e8%8a%9c%e6%b9%96)%e5%ae%89%e5%be%bd%e5%95%86%e8%b4%b8%e8%81%8c%e4%b8%9a%e6%8a%80%e6%9c%af%e5%ad%a6%e9%99%a2&NodeID=&NodeName=&UserName=%e6%9d%a8%e6%96%8c&StuID=9179310493&StuLevel=201709&StudyKindID=3&StudyKind=%e4%b8%9a%e4%bd%99%e4%b8%93%e5%8d%87%e6%9c%ac&Subject=%e8%ae%a1%e7%ae%97%e6%9c%ba%e7%a7%91%e5%ad%a6%e4%b8%8e%e6%8a%80%e6%9c%af&SubjectID=305&StudentStatus=1&ArchieveID=3402010170902145836053&StuRebate=0.80000&IsGraduated=0&CheckinDate=2017/9/2 14:58:36&CourseID='07008A','07017A','11076A','12004A','03003A','03009A','07003A','12005A','13021A'; _pk_ses.61.4d6a=*; _pk_id.61.4d6a=bfe8df247fac2a06.1522029915.6.1524296849.1524295250.; ASP.NET_SessionId=kw3o2t1hti5cn54xzykw4cnt",
# 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36'
# }
# response = requests.get('http://jwstu.cmjnu.com.cn:8080/',headers=headers)
# # response.encoding = 'utf-8'
# print(response.text)

import json
a = json.load(open('计算机组成与结构第一阶段.txt','r',encoding='utf-8'))
b = json.load(open('计算机组成与结构第三阶段.txt','r',encoding='utf-8'))
c = json.load(open('计算机组成与结构第二阶段.txt','r',encoding='utf-8'))
d = json.load(open('数据结构第二阶段.txt','r',encoding='utf-8'))
e = json.load(open('数据结构第三阶段.txt','r',encoding='utf-8'))
f = json.load(open('数据结构第一阶段.txt','r',encoding='utf-8'))
g = json.load(open('计算机语言（C）第一阶段.txt','r',encoding='utf-8'))

aa = {}
aa.update(a)
aa.update(b)
aa.update(c)
aa.update(d)
aa.update(e)
aa.update(f)
aa.update(g)

json.dump(aa,open('daan.txt','w',encoding='utf-8'),ensure_ascii=False)