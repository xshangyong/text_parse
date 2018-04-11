# coding: utf-8  
import re
import time
import calendar 

def get_district(location_str):
    district_pattern = re.compile(r'(海淀)|(北京大学)|(清华大学)|(首图)|(航空航天大学)|(北京外国语)|(北京师范大学)|(中国人民大学)|(北京语言大学)|(中国科学信息技术研究所)|(凯迪拉克中心)|(三堡学术基地)')
    res = district_pattern.search(location_str)
    if res :
        print ("in 海淀")
        return "海淀"
    else :
        print ("not in 海淀")
        return "其他"

def get_activity_type(name_str):
    exhibition_pattern = re.compile(r'(展览)|(个人展)|(首展)')
    performance_pattern = re.compile(r'(演唱会)|(音乐会)|(歌剧)|(话剧)|(相声)|(京剧)|(戏曲)|(话剧)|(昆曲)|(喜剧)|(儿童剧)|(戏剧)|(芭蕾舞)')
    lecture_pattern = re.compile(r'(讲座)')
    res = exhibition_pattern.search(name_str)
    if res :
        print ("is exhibition")
        return "展览"
    res = lecture_pattern.search(name_str)
    if res:
        print ("is lecture")
        return "讲座"
    res = performance_pattern.search(name_str)
    if res:
        print ("is performance")
        return "演出"
    return ""

def get_format_time(time_str):
    res = re.search(r'(?<=2018年)[12][0-9](?=月)|(?<=2018年0)[1-9](?=月)|(?<=2018年)[1-9](?=月)', time_str, )
    if res :
        mon = res.group();
        print (mon) 
        res = re.search(r'(?<=\d月)[123][0-9]|(?<=日)|(?<=\d月0)[1-9]|(?<=日)|(?<=\d月)[1-9]|(?<=日)', time_str, )
        if res :
            day = res.group();
            print (day) 
            if((calendar.weekday(2018, int(mon), int(day))) == 0) :
                weekday = "（周一）"
            elif((calendar.weekday(2018, int(mon), int(day))) == 1): 
                weekday = "（周二）"
            elif((calendar.weekday(2018, int(mon), int(day))) == 2):
                weekday = "（周三）"
            elif((calendar.weekday(2018, int(mon), int(day))) == 3):
                weekday = "（周四）"
            elif((calendar.weekday(2018, int(mon), int(day))) == 4):
                weekday = "（周五）"
            elif((calendar.weekday(2018, int(mon), int(day))) == 5):
                weekday = "（周六）"
            elif((calendar.weekday(2018, int(mon), int(day))) == 6):
                weekday = "（周日）"
            return mon + "." + day + weekday
        else :
            print ("no day")
    else :
        print ("no month")
    return "" 







fd = open("1.txt","r+", encoding='gbk') #comment	
ft= open("ft.txt","w+", encoding='utf-8') #comment	
result = open("2.txt","w+", encoding='utf-8')

full_txt = fd.readlines()


clear_line = []
i = 0
for line in full_txt:
    res = re.search(r'^\s+$', line, )
    if res :
    	i = 1
    else :
        clear_line.append(line)
print ("len of clear line is " , len(clear_line))

name_list = []
info_dic = {}
tmp_str = ""

number = 1
result.write('序号\t活动类型\t活动内容\t时间\t嘉宾\t地点\t所属类型\n')
for index in range(len(clear_line)) :
#    print ("index = %d:" % (index))
    tmp_str = clear_line[index]
    print (clear_line[index]) 
    ft.write(tmp_str)
    tmp = ""
    res = re.search(r'(?<=【).+?(?=】)' , tmp_str , )
    if res and name_list.count(res.group()) == 0:
        tmp = res.group()
        name_list.append(tmp)
        info_dic['name'] = tmp
        info_dic['type'] = get_activity_type(tmp)
        print (tmp)
    else :
        print ("no name or name existed ")

    res = re.search(r'(?<=】).+?(?=【)' , tmp_str , )
    if  res:
        tmp = get_format_time(res.group())       
        if tmp != "":
            info_dic['time'] = tmp
            print (tmp)
        else :
            print ("wrong time")
    else :
        print ("no time")
    tmp = ""
    res = re.search(r'(?<=(主讲】)|(嘉宾】)|(术家】)|(讲人】)).+?(?=【)' , tmp_str , )
    if res :
        tmp = res.group()
        info_dic['speecher'] = tmp
        print (tmp)
    else:
    	res = re.search(r'(?<=(主讲】)|(嘉宾】)|(术家】)|(讲人】)).+' , tmp_str , )
    	if res :
            tmp = res.group()
            info_dic['speecher'] = tmp
            print (tmp)
    
    res = re.search(r'(?<=(地点】)|(的地】)).+?(?=【)' , tmp_str , )
    if res :
        tmp = res.group()
        info_dic['location'] = tmp
        info_dic['district'] = get_district(tmp)
        print (tmp)
    else:
    	res = re.search(r'(?<=(地点】)|(的地】)).+' , tmp_str , )
    	if res :
            tmp = res.group()
            info_dic['location'] = tmp
            info_dic['district'] = get_district(tmp)
            print (tmp)
    if 'name' in info_dic and 'time' in info_dic: 
    	if 'name' in info_dic :
    	    ft.write(info_dic['name'])
    	    ft.write('\n')
    	if 'time' in info_dic :
    	    ft.write(info_dic['time'])
    	    ft.write('\n')
    	if 'speecher' in info_dic :
    	    ft.write(info_dic['speecher'])
    	    ft.write('\n')
    	if 'location' in info_dic :
    	    ft.write(info_dic['location'])
    	    ft.write('\n')
    	ft.write('\n')
    	result.write("%d" % (number))
    	number = number + 1
    	result.write('\t')
    	if 'type' in info_dic :
    	    result.write(info_dic['type'])
    	result.write('\t')
    	if 'name' in info_dic :
    	    result.write(info_dic['name'])
    	result.write('\t')
    	if 'time' in info_dic :
    	    result.write(info_dic['time'])
    	result.write('\t')
    	if 'speecher' in info_dic :
    	    result.write(info_dic['speecher'])
    	result.write('\t')
    	if 'location' in info_dic :
    	    result.write(info_dic['location'])
    	result.write('\t')
    	result.write('\t')
    	if 'district' in info_dic :
    	    result.write(info_dic['district'])
    	result.write('\n')
    info_dic.clear();
	
fd.close()
ft.close()

result.close()


