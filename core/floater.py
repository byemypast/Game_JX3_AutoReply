# -*- coding:gbk -*-  
#Ư��ƿģ��
#�����ӣ�ֱ�����ļ������ȡ
import core.game
import core.userinfo
import core.settings
import send.sendcore
from core.debug import *
import random

floater_pool = []
needsending = {}

def floater_readall():
	debug("core.floater.floater_readall : ��ȡƯ��ƿ��Ϣ")
	dbname = core.settings.floaterdbname
	f = open(dbname)
	floater_pool = f.readlines()
	f.close()
	return floater_pool

def floater_write(player_id,issecret,msg):
	debug("core.floater.floater_write : Ư��ƿд�� �û���" +player_id+" ����(0=����)��"+str(issecret)+" ���ݣ�"+msg)
	dbname = core.settings.floaterdbname
	f= open(dbname,'a')
	f.write(player_id+"\t"+str(issecret)+"\t"+msg.replace("\t",",").replace("\n"," ")+"\n")
	f.close()


def APP_floater_main(player_id,state,msg,userdata,PlayerState):
	#state: 300 - 399
	#����userdata������ȥ�������ݿ�,userdataΪֻ�����ݿ�
	floater_pool = floater_readall()
	if state==300:
		strcache = ["��ӭ~ ��"+core.game.get_usertype(player_id)+ "�û���" + player_id+" ����Ư��ƿģ�飡",
								"��Ŀǰ�� " + str(userdata[player_id]['FLOATER_LEFT']) +" ����ƿ���ᣬĿǰ�������� " + str(len(floater_pool)) + "����Ϣ����ƿ��������ͨ�����������ƿ������~",
								"��1����һ������2����һ������3���������˵�"
								]
		send.sendcore.sendlist(player_id,strcache)
		PlayerState[player_id] = 301
	elif state==301:
		#*�պ���
		floater_left = userdata[player_id]['FLOATER_LEFT']
		if msg=="1":
			if floater_left<=0:
				send.sendcore.sendstr(player_id,"������ƿ���������꣬��Ͷι~")
				PlayerState[player_id] = 302
			else:
				floater_left += -1
				core.userinfo.database_setvalue("FLOATER_LEFT",floater_left,player_id)
				preshow = ""
				while (preshow.strip("\n")==""):
					preshow = random.choice(floater_pool)
				info = preshow.split("\t")
				floater_author = info[0]
				isshowname = int(info[1])
				floater_msg = info[2]
				if isshowname == 0:
					#������Ϣ 0:����
					floater_author = "һ��������С���"
				strcache = [floater_author + "��",floater_msg,"���������������һҳ"]
				send.sendcore.sendlist(player_id,strcache)
				PlayerState[player_id] = 302
		elif msg=="2":
			strcache = ["���棡������Ϣ����棨�������/QQ����������������Ϣ�����̰���se�顢��don����zhi","����������Ӫ/��ҷ������������κο�����вƽ̨����Ļ��⽫�����˺ű����÷��������ϧ�����˺�",
									"���ڴ����������������ݣ�"]
			PlayerState[player_id] = 303
			send.sendcore.sendlist(player_id,strcache)
		elif msg=="3":
			PlayerState[player_id] = 1
			send.sendcore.sendstr(player_id,'����������������˵�')
	elif state==302:
		strcache = ["��Ŀǰ�� " + str(userdata[player_id]['FLOATER_LEFT']) +" ����ƿ���ᣬĿǰ�������� " + str(len(floater_pool)) + "����Ϣ����ƿ��������ͨ�����������ƿ������~",
								"��1����һ������2����һ������3���������˵�"]
		send.sendcore.sendlist(player_id,strcache)
		PlayerState[player_id] = 301
	elif state==303:
		#����ȷ��
		strcache = ["��Ҫ���͵������ǣ�",msg,"��1��ȷ�Ϸ��ͣ�ʹ������ID������2��ȷ�Ϸ��ͣ�show ID������ϵ������3�������룬���±༭"]
		needsending[player_id] = msg
		PlayerState[player_id] = 304
		send.sendcore.sendlist(player_id,strcache)
	elif state==304:
		#���ͺ���
		if (msg=="1")or(msg=='2'):
			floater_left = userdata[player_id]['FLOATER_LEFT']
			floater_left += 1
			core.userinfo.database_setvalue("FLOATER_LEFT",floater_left,player_id)
			floater_write(player_id,int(msg)-1,needsending[player_id])
			needsending[player_id] = ""
			send.sendcore.sendstr(player_id,"���ͳɹ������������������һҳ")
			PlayerState[player_id] = 302
		elif msg=="3":
			needsending[player_id] = ""
			strcache = ["���棡������Ϣ����棨�������/QQ����������������Ϣ�����̰���se�顢��don����zhi������������Ӫ/��ҷ����������κο�����вƽ̨����Ļ��⽫�����˺ű����÷��������ϧ�����˺�",
									"���ڴ����������������ݣ�"]
			PlayerState[player_id] = 303
			send.sendcore.sendlist(player_id,strcache)
	return PlayerState