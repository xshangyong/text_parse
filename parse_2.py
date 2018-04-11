# coding: utf-8  
import re
import time
import calendar 

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

i = 0
info_dic = {}
result.write('序号\t活动类型\t活动内容\t时间\t嘉宾\t地点\t所属类型\n')
number = 1

for ix in range(len(full_txt)):
    tmp_str  = full_txt[ix]
    res = re.search(r'^\s+$', tmp_str, )
    if res :
        if i >= 3:
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
            info_dic['name'] = tmp_str
            i = i + 1
        elif i==1 :
            print ("line %d not empty" % (ix))  
            print (full_txt[ix])
            tmp_str = re.sub(r'(^\s+)|(\n)', "",tmp_str  )
            info_dic['location'] = tmp_str
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



