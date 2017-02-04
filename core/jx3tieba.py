# -*- coding:gbk -*- 
import urllib.request
import sys
import time
import re
import heapq
import time
import datetime
from core.debug import *

def tiebatop_update(name_tieba,fout):
	debug("���� �����������ģ�� ������"+ name_tieba+" "+fout,1)
	url = 'http://tieba.baidu.com/f?ie=utf-8&kw='+urllib.request.quote(name_tieba)+'&pn='
	tiebascore = {}
	tiebaauthor = {}
	tiebareply = {}
	tiebadian = {}
	tiebadate = {}
	tiebapostid = {}
	tiebapostdate = {}
	countoverday = 0
	repeat_i = 0
	datetoday = datetime.date.today()
	todaym = str(datetoday.month)
	todayd = str(datetoday.day)
	while (repeat_i<60): #need try
		response =  urllib.request.urlopen(url + str(repeat_i * 50))
		page = response.read()
		type = sys.getfilesystemencoding()
		html = page.decode(type)
		
		reauthor = re.compile('"��������: (.*?)"')
		retime = re.compile('"����ʱ��">(.*?)<\/span>')
		replyn = re.compile('title="�ظ�">(.*?)</span>')
		retitleadd = re.compile('<a href="/p/(.*?)" title="(.*?)" target="_blank" class="j_th_tit ">').findall(html)

		authors = reauthor.findall(html)
		times = retime.findall(html)
		replyn = replyn.findall(html)
		
		for i in range(0,len(retitleadd)):
			if (int(replyn[i])>=50): #try
				title = retitleadd[i][1]
				tiebapostid[title] = retitleadd[i][0]
				tiebapostdate[title] = times[i]
				
				tiebaauthor[title] = authors[i]
				try:
					tiebareply[title] = int(replyn[i])
				except:
					tiebareply[title] = 0

		repeat_i += 1
		debug(str(repeat_i)+ " / 60",2)
	
	debug("ǰ60ҳ�й��У�"+ str(len(tiebareply))+" ����50�ظ�������",2)
	scoresort = sorted(tiebareply.items(),key = lambda item:item[1],reverse = True)
	toptodaylist = []
	toplist = []
	i = 0
	while (len(toptodaylist)<100)and(i<len(scoresort)):
		title,score = scoresort[i]
		toplist.append(title)
		if tiebapostdate[title].find(":")>=0:
			toptodaylist.append(title)
			
		i += 1
	
	f = open(fout+"_1",'w',encoding =type)
	for title in toplist:
		i += 1
		f.write(str(i)+"---"+title+"---"+str(tiebareply[title])+"---"+str(tiebaauthor[title])+"---"+str(tiebapostdate[title])+"---"+str(tiebapostid[title])+"\n")
	i = 0
	f.close()
	#����ʮ��
	f = open(fout+"_2",'w',encoding =type)
	for title in toptodaylist:
		i += 1
		f.write(str(i)+"---"+title+"---"+str(tiebareply[title])+"---"+str(tiebaauthor[title])+"---"+str(tiebapostdate[title])+"---"+str(tiebapostid[title])+"\n")
	f.close()
	debug("�����������ģ�� ����",1)
