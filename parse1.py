# coding: utf-8  
import re
import time
import calendar 

def get_district(location_str):
    haidian_pattern = re.compile(r'(海淀)|(北京大学)|(清华大学)|(首图)|(航空航天大学)|(北京外国语)|(北京师范大学)|(中国人民大学)|(北京语言大学)|(中国科学信息技术研究所)|(凯迪拉克中心)|(三堡学术基地)|(国话先锋剧场)|(国图艺术中心)|(海淀剧院)|(红剧场)|(华侨城大剧院)|(五棵松)|(国家图书管)|(北京展览馆剧场)|(中国地质大学)|(中国农业大学)|(中央财经大学)|(枫蓝国际小剧场)|(学清路甲)|(北京林业大学)|(中间剧场)|(中国文联)|(首都体育馆)|(双清大厦)|(国家图书馆艺术中心)')
    nothaidian_pattern = re.compile(r'(国家大剧院)|(假日经典小剧场)|(A33小剧场)|(Blue Note Beijing)|(保利剧院)|(北京天桥艺术中心)|(北京喜剧院)|(北京音乐厅)|(博纳星辉剧院)|(超剧场)|(地质礼堂剧场)|(东方梅地亚中心M剧场)|(繁星戏剧村)|(工人俱乐部)|(国家大剧院)|(假日经典小剧场)|(菊隐剧场)|(老舍茶馆)|(隆福剧场)|(梅兰芳大剧院)|(民族文化宫大剧院)|(蓬蒿剧场)|(青蓝剧场)|(人艺实验剧场)|(世纪剧院)|(天桥剧场)|(长安大戏院)|(正乙祠戏楼)|(中国儿童剧场)|(中国国家话剧院国话剧场)|(中国木偶剧院)|(中山音乐堂)|(首都图书馆)|(西西弗书店)|(北京中医药大学)|(中国现代文学馆)|(中国现代文学馆)|(北京社科书店)|(外交学院)|(对外经济贸易大学)|(永定门公园)|(糖果TANGO)|(北京剧院)|(中国儿童中心)|(首都剧场)|(星博正华)|(正华星博)|(磁剧场)|(全国地方戏演出中心)|(北京剧空间剧场)|(中杂.{0,12}剧场)|(A33剧场)|(北京9剧场)|(东城)|(西城)|(朝阳)|(大兴)|(石景山)|(丰台)|(顺义)|(密云)|(怀柔)|(延庆)|(北京西区剧场)|(大隐剧场)|(对外经贸大学)|(国家话剧院)|(小柯剧场)|(北京民族文化宫展览馆)|(中央美术学院美术馆)|(中国科学院大学雁栖湖校区)|(中国音乐学院)|(国家话剧院)|(大隐剧院)|(中央美术学院)|(中国科学院大学)|(蜂巢剧场)|(鼓楼西剧场)|(北京西区剧场)|(国家话剧院)|(小柯剧场)|(凤凰艺都798艺术空间)|(北京第二外国语学院)|(中国美术馆)')

    res = haidian_pattern.search(location_str)
    if res :
        print ("in 海淀")
        return "海淀"
    else :
        res = nothaidian_pattern.search(location_str)
        if res : 
            print ("not in 海淀")
            return "非海淀"
    return ""

def get_activity_type(name_str):
    exhibition_pattern = re.compile(r'(展览)|(个人展)|(首展)')
    performance_pattern = re.compile(r'(演唱会)|(音乐会)|(歌剧)|(话剧)|(相声)|(京剧)|(戏曲)|(话剧)|(昆曲)|(喜剧)|(儿童剧)|(戏剧)|(芭蕾舞)|(演出)')
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
result = open("out1.txt","w+", encoding='utf-8')

full_txt = fd.readlines()


clear_line = []
i = 0
tmp_line = ""
for line in full_txt:
    res = re.search(r'^\s+$', line, )
    if res :
        i = 1
        if tmp_line != "" : 
            clear_line.append(tmp_line)
            tmp_line = ""
    else :
        tmp_line = tmp_line + line
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
    if 'name' in info_dic : 
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


