# coding: utf-8  
import re
import time
import calendar 

def get_district(location_str):
    haidian_pattern = re.compile(r'(海淀)|(北京大学)|(清华大学)|(首图)|(航空航天大学)|(北京外国语)|(北京师范大学)|(中国人民大学)|(北京语言大学)|(中国科学信息技术研究所)|(凯迪拉克中心)|(三堡学术基地)|(国话先锋剧场)|(国图艺术中心)|(海淀剧院)|(红剧场)|(华侨城大剧院)|(五棵松)|(国家图书管)|(北京展览馆剧场)')
    nothaidian_pattern = re.compile(r'(国家大剧院)|(假日经典小剧场)|(A33小剧场)|(Blue Note Beijing)|(保利剧院)|(北京天桥艺术中心)|(北京喜剧院)|(北京音乐厅)|(博纳星辉剧院)|(超剧场)|(地质礼堂剧场)|(东方梅地亚中心M剧场)|(繁星戏剧村)|(工人俱乐部)|(国家大剧院)|(假日经典小剧场)|(菊隐剧场)|(老舍茶馆)|(隆福剧场)|(梅兰芳大剧院)|(民族文化宫大剧院)|(蓬蒿剧场)|(青蓝剧场)|(人艺实验剧场)|(世纪剧院)|(天桥剧场)|(长安大戏院)|(正乙祠戏楼)|(中国儿童剧场)|(中国国家话剧院国话剧场)|(中国木偶剧院)|(中山音乐堂)|(首都图书馆)|(西西弗书店)|(北京中医药大学)|(中国现代文学馆)|(中国现代文学馆)|(北京社科书店)|(外交学院)|(对外经济贸易大学)|(永定门公园)|(糖果TANGO)|(北京剧院)|(中国儿童中心)|(首都剧场)|(星博正华)|(正华星博)|(磁剧场)|(全国地方戏演出中心)|(北京剧空间剧场)|(中杂.{0,12}剧场)|(A33剧场)|(北京9剧场)|(东城)|(西城)|(朝阳)|(大兴)|(石景山)|(丰台)|(顺义)|(密云)|(怀柔)|(延庆)')

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

def get_format_time(time_str):
    res = re.search(r'(?<=2018\.)[12][0-9](?=\.)|(?<=2018\.0)[1-9](?=\.)', time_str, )
    if res :
        mon = res.group();
        print (mon) 
        res = re.search(r'(?<=\.\d\d\.)[123][0-9]|(?<=\.\d\d\.0)[1-9]', time_str, )
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
    return "" 








fd = open("3.txt","r+", encoding='gbk') #comment	
ft= open("ttt.txt","w+", encoding='utf-8') #comment	
result = open("4.txt","w+", encoding='utf-8')

full_txt = fd.readlines()
clear_line = []
name_list = []

i = 0
info_dic = {}
result.write('序号\t活动类型\t活动内容\t时间\t嘉宾\t地点\t所属类型\n')
number = 1

for ix in range(len(full_txt)):
    tmp_str  = full_txt[ix]
    res = re.search(r'^\s+$', tmp_str, )
    if res :
        if i >= 3 and 'name' in info_dic:
            result.write("%d" % (number))
            number = number + 1
            result.write('\t')
            result.write('演出')
            result.write('\t')
            if 'name' in info_dic :
                result.write(info_dic['name'])
            result.write('\t')
            if 'time' in info_dic :
                result.write(info_dic['time'])
            result.write('\t')
            result.write('\t')
            if 'location' in info_dic :
                result.write(info_dic['location'])
            result.write('\t')
            result.write('\t')
            if 'district' in info_dic :
                result.write(info_dic['district'])
            result.write('\n')
        elif i == 0:
            print ("line %d empty" % (ix))  
            print (full_txt[ix])
        i = 0
        info_dic.clear()
    else :
        if i == 0 :
            print ("line %d not empty" % (ix))
            print (full_txt[ix])
            tmp_str = re.sub(r'(^\s+)|(\n)', "",tmp_str )
            if name_list.count(tmp_str) == 0:
                info_dic['name'] = tmp_str
                name_list.append(tmp_str)
            i = i + 1
        elif i==1 :
            print ("line %d not empty" % (ix))  
            print (full_txt[ix])
            tmp_str = re.sub(r'(^\s+)|(\n)', "",tmp_str  )
            info_dic['location'] = tmp_str
            info_dic['district'] = get_district(tmp_str)
            i = i + 1
        elif i==2 :
            print ("line %d not empty" % (ix))  
            print (full_txt[ix]) 
            tmp_str = re.sub(r'(^\s+)|(\n)',  "",tmp_str  )
            info_dic['time'] = get_format_time(tmp_str)
            # change tmp_str to   11.30(星期一)
            #   (?<=\d\d\d\d年)\d{1,2}(?=月)
            i = i + 1







#for index in range(len(full_txt)):
##    tmp_str=full_txt[index].decode('gbk').encode('utf-8')
#    ft.write(tmp_str)
#    res = re.search(r'^\s+$', tmp_str, )
#    if res :
#        if i >= 3:
#            result.write("%d" % (number))
#            number = number + 1
#            result.write('\t')
#            result.write('\t')
#            if info_dic.has_key('name') :
#                result.write(info_dic['name'])
#            result.write('\t')
#            if info_dic.has_key('time') :
#                result.write(info_dic['time'])
#            result.write('\t')
#            result.write('\t')
#            if info_dic.has_key('location') :		
#                result.write(info_dic['location'])
#                result.write('\t')
#                result.write('\t')
#                result.write('\n')
#            elif i == 0:
#                print ("line %d empty" % (index))  
#                print (full_txt[index])
#        i = 0
#        info_dic.clear()
#    else :
#        if i == 0 :
#            print ("line %d not empty" % (index))
#            print (full_txt[index])
#            tmp_str = re.sub(r'(^\s+)|(\n)', "",tmp_str )
#            info_dic['name'] = tmp_str
#            i = i + 1
#        elif i==1 :
#            print ("line %d not empty" % (index))  
#            print (full_txt[index])
#            tmp_str = re.sub(r'(^\s+)|(\n)', "",tmp_str  )
#            info_dic['location'] = tmp_str
#            i = i + 1
#        elif i==2 :
#            print ("line %d not empty" % (index))  
#            print (full_txt[index]) 
#            tmp_str = re.sub(r'(^\s+)|(\n)',  "",tmp_str  )
#            info_dic['time'] = tmp_str
#            i = i + 1

local_time = time.localtime(time.time())
print (local_time)
ft.close()
result.close()
fd.close()



