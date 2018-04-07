# coding: utf-8  
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def strQ2B(ustring):
    rstring = ""
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code == 12288:                              #全角空格直接转换            
            inside_code = 32 
        elif (inside_code >= 65281 and inside_code <= 65374): #全角字符（除空格）根据关系转化
            inside_code -= 65248

        rstring += unichr(inside_code)
    return rstring
    
def strB2Q(ustring):
    rstring = ""
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code == 32:                                 #半角空格直接转化                  
            inside_code = 12288
        elif inside_code >= 32 and inside_code <= 126:        #半角字符（除空格）根据关系转化
            inside_code += 65248

        rstring += unichr(inside_code)
    return rstring

fd = open("1.txt","r+") #comment	
fw= open("fw.txt","w+") #comment	
ft= open("ft.txt","w+") #comment	
result = open("2.txt","w+")

full_txt = fd.readlines()

clear_line = []
i = 0
for line in full_txt:
	res = re.search(r'^\s+$', line, )
	if res :
		i = 1
	else :
		clear_line.append(line)

print "len of clear line is " , len(clear_line)

info_res = []
info_dic = {}
tmp_str = ""

number = 1
result.write('序号\t活动类型\t活动内容\t时间\t嘉宾\t地点\t所属类型\n')
for index in range(len(clear_line)) :
	print "index = %d:" % (index)
	tmp_str=clear_line[index].decode('gbk').encode('utf-8')
	ft.write(tmp_str)
#	标题
	tmp = ""
	res = re.search(r'(?<=【).+?(?=】)' , tmp_str , )
	if res :
		tmp = res.group()
		info_res.append(tmp)
		info_dic['name'] = tmp
#	时间   2018年4月3日（周二）14:00  转换为  3.31（周六）
#	res = re.search(r'(?<=】\d\d\d\d年).+?）' , tmp_str , )
	tmp = ""	
	res = re.search(r'(?<=\d\d\d\d年)\d{1,2}(?=月)' , tmp_str , )
	if res :
		tmp = res.group()
	res = re.search(r'(?<=月)\d{1,2}?(?=日)' , tmp_str , )
	if res :
		tmp =tmp + "." + res.group()
	res = re.search(r'(（|\()(周.+?)(）|\))' , tmp_str , )
	if res :
		tmp =tmp + res.group()
		# 转换时间为 2.3(周一)
#		res = re.search(r'(?<=年).+?(?=日)' , tmp_str , )
	info_res.append(tmp)
	info_dic['time'] = tmp
	tmp = ""
	res = re.search(r'(?<=(主讲】)|(嘉宾】)|(术家】)|(讲人】)).+?(?=【)' , tmp_str , )
	if res :
		tmp = res.group()
		info_res.append(tmp)
		info_dic['speecher'] = tmp
	else:
		res = re.search(r'(?<=(主讲】)|(嘉宾】)|(术家】)|(讲人】)).+' , tmp_str , )
		if res :
			tmp = res.group()
			info_res.append(tmp)
			info_dic['speecher'] = tmp

	res = re.search(r'(?<=(地点】)|(的地】)).+?(?=【)' , tmp_str , )
	if res :
		tmp = res.group()
		info_res.append(tmp)
		info_dic['location'] = tmp
	else:
		res = re.search(r'(?<=(地点】)|(的地】)).+' , tmp_str , )
		if res :
			tmp = res.group()
			info_res.append(tmp)
			info_dic['location'] = tmp
	if info_dic.has_key('name') and info_dic['time'] != "": # and info_dic.has_key('location'):
		if info_dic.has_key('name') :
			ft.write(info_dic['name'])
			ft.write('\n')
		if info_dic.has_key('time') :		
			ft.write(info_dic['time'])
			ft.write('\n')
		if info_dic.has_key('speecher') :		
			ft.write(info_dic['speecher'])
			ft.write('\n')
		if info_dic.has_key('location') :		
			ft.write(info_dic['location'])
			ft.write('\n')
		ft.write('\n')
		result.write("%d" % (number))
		number = number + 1
		result.write('\t')
#		result.write(index) 活动类型
		result.write('\t')
		if info_dic.has_key('name') :
			result.write(info_dic['name'])
		result.write('\t')
		if info_dic.has_key('time') :
			result.write(info_dic['time'])
		result.write('\t')
		if info_dic.has_key('speecher') :	
			result.write(info_dic['speecher'])
		result.write('\t')
		if info_dic.has_key('location') :		
			result.write(info_dic['location'])
		result.write('\t')
		result.write('\t')
		result.write('\n')
	info_dic.clear();
	
fd.close()
fw.close()
ft.close()


result.close()


