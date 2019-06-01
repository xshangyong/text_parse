# coding: utf-8  
import re
import time
import calendar 
import gd



def get_format_time(time_str):
	res = re.search(r'\d\d(?=月)|(?<=2019\.0)[1-9](?=\.)', time_str, )
	if res :
		mon = res.group();
		if mon[0] == "0":
			mon=mon[1]
		print (mon) 
		res = re.search(r'(?<=月)\d\d(?=日)', time_str, )
		if res :
			day = res.group();
			if day[0] == "0":
				day = day[1]
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
	return "" 







def parse3():
	fd = open("3.txt","r+", encoding='utf-8') #comment	
	result = open("out3.txt","w+", encoding='utf-8')
	
	full_txt = fd.readlines()
	clear_line = []
	name_list = []
	
	i = 0
	info_dic = {}
	result.write('序号\t活动类型\t活动内容\t时间\t嘉宾\t地点\t所属类型\n')
	number = 1
	first = 1
	
	for ix in range(len(full_txt)):
		tmp_str  = full_txt[ix]
		res = re.search(r'人感兴趣', tmp_str, )

		if res or first == 1 :
			if 'location' in info_dic and 'name' in info_dic:
				result.write("%d" % (number))
				number = number + 1
				result.write('\t')
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
			else :
				print ("line %d empty" % (ix))  
				print (full_txt[ix])
			start = 1;
			first = 0;
			info_dic.clear()
		else :
			res = re.search(r'^\s+$', tmp_str, )
			if res :
				pass
			else : 
				if start == 1:
					tmp_str = re.sub(r'\n', "", tmp_str)
					info_dic['name'] = tmp_str
					start = 0
				else :
					#search: 时间:  地点: 
					res = re.search(r'(?<=(地点：\s)).+' , tmp_str , )
					if res :
						tmp = res.group()
						info_dic['location'] = tmp
						info_dic['district'] = gd.get_district(tmp)
						print (tmp)
					else :
						pass
						#print ("no location")
					res = re.search(r'(?<=(时间：\s)).+' , tmp_str , )
					if res :
						tmp = get_format_time(res.group())
						# two kinds format of time
						# 时间： 05月20日 周日 09:30-12:00
						# 时间： 2019年05月13日 ~ 2019年06月24日 每周日 17:00 - 18:30
						if tmp != "":
							info_dic['time'] = tmp
							print (tmp)
						else :
							print ("wrong time")
					else :
						pass
						#print ("no time")
	
	
	local_time = time.localtime(time.time())
	print (local_time)
	result.close()
	fd.close()

if __name__ == '__main__':
	parse3()


