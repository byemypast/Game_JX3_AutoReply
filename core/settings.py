# -*- coding: gbk -*-
import datetime
#�汾��
VERSION = 0.6
#��������ʱ��
STARTTIME = datetime.datetime.now()
#�����ļ���
debugname = "debug.txt"
#����ʮ��ǿ�Ƴ�������ʱ����ʮ����Ϣ4
TIEBA_UPDATE_FORCE = 0
#��¼�û�ID�ļ���
recordname = "record.txt"
#����ʮ�󣺶���ͨ�û����Űٴ���
TIEBA_TOP100_TONONVIP = 1
#Ư��ƿ�ļ�
floaterdbname = "floater_pool.txt"


#�ʼ�ģ������
mail_host="mail.xxxx"  #���÷�����
mail_user="xxxxxxxx@xxx"    #�û���
mail_pass="xxxxxxxx"   #���� 
var = {}
var["TIEBA_UPDATE_TO"] = ""
var['TIEBA_SHIDA'] = []
var['TIEBA_SHIDA_UPDATE'] = ""
var['TIEBA_UPDATETIME'] = "18-00"

def set_value(svar,value):
	var[svar] = value

def get_value(svar):
	try:
		return var[svar]
	except:
		return None