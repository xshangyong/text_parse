# coding: utf-8  
import re
import time
import calendar 
import gd

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
	print(time_str)
	res = re.search(r'(?<=2019年)[12][0-9](?=月)|(?<=2019年0)[1-9](?=月)|(?<=2019年)[1-9](?=月)', time_str, )
	if res :
		mon = res.group();
		print (mon) 
		res = re.search(r'(?<=\d月)[123][0-9](?=日)|(?<=\d月0)[1-9](?=日)|(?<=\d月)[1-9](?=日)', time_str, )
		if res :
			day = res.group();
			print (day) 
			if((calendar.weekday(2019, int(mon), int(day))) == 0) :
				weekday = "（周一）"
			elif((calendar.weekday(2019, int(mon), int(day))) == 1): 
				weekday = "（周二）"
			elif((calendar.weekday(2019, int(mon), int(day))) == 2):
				weekday = "（周三）"
			elif((calendar.weekday(2019, int(mon), int(day))) == 3):
				weekday = "（周四）"
			elif((calendar.weekday(2019, int(mon), int(day))) == 4):
				weekday = "（周五）"
			elif((calendar.weekday(2019, int(mon), int(day))) == 5):
				weekday = "（周六）"
			elif((calendar.weekday(2019, int(mon), int(day))) == 6):
				weekday = "（周日）"
			return mon + "." + day + weekday
		else :
			print ("no day")
	else :
		print ("no month")
	return "" 






def parse1():
	fd = open("1.txt","r+", encoding='gbk') #comment	
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
	result.write('序号\t活动类型\t活动内容\t时间\t嘉宾\t地点\t所属类型\t区\n')
	for index in range(len(clear_line)) :
	#    print ("index = %d:" % (index))
		tmp_str = clear_line[index]
		print (clear_line[index]) 
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
			
		res = re.search(r'(?<=(地点】)|(的地】)|(地址】)).+?(?=【)' , tmp_str , )
		if res :
			tmp = res.group()
			info_dic['location'] = tmp
			info_dic['district'] = gd.get_district(tmp)
			print (tmp)
		else:
			res = re.search(r'(?<=(地点】)|(的地】)|(地址】)).+' , tmp_str , )
			if res :
				tmp = res.group()
				info_dic['location'] = tmp
				info_dic['district'] = gd.get_district(tmp)
				print (tmp)
		if 'name' in info_dic :
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
	
	result.close()

if __name__ == '__main__':
	parse1()
