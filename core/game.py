# -*- coding:gbk -*-  

import datetime
import core.settings
from core.debug import *
from send.sendcore import *


PlayerState = {}
VIPLevel = {"���峿":1,"ʮ������":1,"����ɨ��ѩ":1,"����Ѱ����":1,"���հ��Ŵ�":1}
TIEBA_state = {}
TotalServiceTime = 0
#0: ��һ�ζԻ�����+��ѡ���г�
#1���ǵ�һ�ζԻ�+��ѡ���г�
#2��ѡ����ѡ��
#100��ְҵѡ��APP��ʼ��
def core_input(player_id,talktime,msg):
	if player_id in VIPLevel:
		if VIPLevel[player_id]==-1:
			sendstr(player_id,"���ں�������")
			return
	if not player_id in PlayerState:
		PlayerState[player_id] = 0 #init
	response(PlayerState[player_id],player_id,msg)

def APP_working(player_id):
	sendstr(player_id,"����ʩ���У������ڴ�~�ظ�������������˵�")
	PlayerState[player_id] = 1

def APP_professiontest(player_id,state,msg):
	if state==100:
		strcache = ['�������һ�����һЩ���⣬�������ʾ����1��2��3',
								'Q1: ��ϲ�������𣿡�1���ҳ�ϲ���ģ���2��ȥ��ô��']
		sendlist(player_id,strcache,0,0,0)
		PlayerState[player_id] = 101
	elif state==101:
		if msg=='1':
			#�� ���� ���� �嶾 ���� �ؽ� ����
			sendstr(player_id,'Q2���ǡ�����ϣ��˳�����������𣿡�1����Ȼ�����гɾ͸У���2�����Ƴ������Ǳ���')
			PlayerState[player_id] = 102
		elif msg=='2':
			#���� �Ե� ���� ��� ؤ�� ���� ����
			sendstr(player_id,'Q2������õ�������ô������1�����Ӿ�Ҫ��С��VIP����2�����۶���Ҫ����')
			PlayerState[player_id] = 103
		else:
			pass #������벻�ش�
	elif state==102:
		if msg=='1':
			#�� ���� ���� �嶾
			sendstr(player_id,'Q3��һ��������ҹ����į�𣿡�1����Ȼ����������ˣ���2����������η��')
			PlayerState[player_id] = 104
		elif msg=='2':
			#���� �ؽ� ����
			sendstr(player_id,'Q3��һ��������ҹ���а�ȫ���𣿡�1���ŵ��ҿ�ʼ��Ϥ�����ˣ���2����������η��')
			PlayerState[player_id] = 105
		else:
			pass #������벻�ش�
	elif state==103:
		if msg=='1':
			#���� ؤ��
			sendstr(player_id,'Q3������Σ�ո�ϲ�����ܱ������ἺΪ�ˣ���1�������Ѳ���ƶ������2���ո��˵���Ȼ���߲嵶��������')
			PlayerState[player_id] = 106
		elif msg=='2':
			#�Ե� ���� ��� ���� ����
			sendstr(player_id,'Q3������Σ�գ����ϣ���Թ�Ϊ�ػ���ȫ����ˣ���1���Թ�Ϊ�أ���2��ȫ����ˣ���3����ص���')
			PlayerState[player_id] = 107
		else:
			pass #������벻�ش�
	elif state==104:
		if msg=='1':
			#���� �嶾
			sendstr(player_id,'Q4������ĺ�ϣ�����������𣿡�1����Ȼ�ˣ���2��������;ͺ�')
			PlayerState[player_id] = 108
		elif msg=='2':
			#�� ����
			sendstr(player_id,'Q4�����������У����Ǹ�ʲô�����ˣ���1��֪�����ģ���2���ܸ������')
			PlayerState[player_id] = 109
	elif state==105:
		if msg=='1':
			#���� ����
			sendstr(player_id,'Q4��ϲ����λ�𣿡�1�������Ҳ����Լ�����������ҲҪ�ñ���������������2�����Ӿ�������������Ұ�')
			PlayerState[player_id] = 110
		elif msg=='2':
			sendstr(player_id,'�ٺٺ٣������ʺϵ�ְҵ����ǣ��ؽ�~���������֡�ϣ������һ���𣿡�1���Ҳ�������������2�������˻����˵�')
			PlayerState[player_id] = 111
	elif state==106:
		if msg=='1':
			sendstr(player_id,'�ٺٺ٣������ʺϵ�ְҵ����ǣ�ؤ��~���������֡�ϣ������һ���𣿡�1���Ҳ�������������2�������˻����˵�')
			PlayerState[player_id] = 111
		elif msg=='2':
			sendstr(player_id,'�ٺٺ٣������ʺϵ�ְҵ����ǣ�����~���������֡�ϣ������һ���𣿡�1���Ҳ�������������2�������˻����˵�')
			PlayerState[player_id] = 111
	elif state==107:
		if msg=='1':
			#���� ���
			sendstr(player_id,'Q4������Ŵ��б���ϵ�ʱ��һ�㶼�̲����𣿡�1�������ֶ���2��������ǳ��¶����ϰ����')
			PlayerState[player_id] = 112
		elif msg=='2':
			#���� ���� �Ե�
			sendstr(player_id,'Q4����Ȩ�ͻ�Ȩ������ĸ����з��Ƹ����Ǳ������1����Ȩ��2����Ȩ')
			PlayerState[player_id] = 113
		elif msg=='3':
			sendstr(player_id,'�ٺٺ٣������ʺϵ�ְҵ����ǣ�����~���������֡�ϣ������һ���𣿡�1���Ҳ�������������2�������˻����˵�')
			PlayerState[player_id] = 111
	elif state==108:
		if msg=='1':
			sendstr(player_id,'�ٺٺ٣������ʺϵ�ְҵ����ǣ��嶾~���������֡�ϣ������һ���𣿡�1���Ҳ�������������2�������˻����˵�')
			PlayerState[player_id] = 111
		elif msg=='2':
			sendstr(player_id,'�ٺٺ٣������ʺϵ�ְҵ����ǣ�����~���������֡�ϣ������һ���𣿡�1���Ҳ�������������2�������˻����˵�')
			PlayerState[player_id] = 111
	elif state==109:
		if msg=='1':
			sendstr(player_id,'�ٺٺ٣������ʺϵ�ְҵ����ǣ���~���������֡�ϣ������һ���𣿡�1���Ҳ�������������2�������˻����˵�')
			PlayerState[player_id] = 111
		elif msg=='2':
			sendstr(player_id,'�ٺٺ٣������ʺϵ�ְҵ����ǣ�����~���������֡�ϣ������һ���𣿡�1���Ҳ�������������2�������˻����˵�')
			PlayerState[player_id] = 111
	elif state==110:
		if msg=='1':
			sendstr(player_id,'�ٺٺ٣������ʺϵ�ְҵ����ǣ�����~���������֡�ϣ������һ���𣿡�1���Ҳ�������������2�������˻����˵�')
			PlayerState[player_id] = 111
		elif msg=='2':
			sendstr(player_id,'�ٺٺ٣������ʺϵ�ְҵ����ǣ�����~���������֡�ϣ������һ���𣿡�1���Ҳ�������������2�������˻����˵�')
			PlayerState[player_id] = 111
	elif state==111:
		#1 ������2�����˵�
		if msg=='1':
			PlayerState[player_id] = 100
			APP_professiontest(player_id,100,"from state 111")
		elif msg=='2':
			PlayerState[player_id] = 1
			response(1,player_id,"from state 111")
	elif state==112:
		if msg=='1':
			sendstr(player_id,'�ٺٺ٣������ʺϵ�ְҵ����ǣ�����~���������֡�ϣ������һ���𣿡�1���Ҳ�������������2�������˻����˵�')
			PlayerState[player_id] = 111
		elif msg=='2':
			sendstr(player_id,'�ٺٺ٣������ʺϵ�ְҵ����ǣ����~���������֡�ϣ������һ���𣿡�1���Ҳ�������������2�������˻����˵�')
			PlayerState[player_id] = 111
	elif state==113:
		if msg=='1':
			sendstr(player_id,'�ٺٺ٣������ʺϵ�ְҵ����ǣ��Ե�~���������֡�ϣ������һ���𣿡�1���Ҳ�������������2�������˻����˵�')
			PlayerState[player_id] = 111
		elif msg=='2':
			sendstr(player_id,'Q5�������𣿡�1��־���ķ���2�����ؼҿ���')
			PlayerState[player_id] = 114
	elif state==114:
		if msg=='1':
			sendstr(player_id,'�ٺٺ٣������ʺϵ�ְҵ����ǣ�����~���������֡�ϣ������һ���𣿡�1���Ҳ�������������2�������˻����˵�')
			PlayerState[player_id] = 111
		elif msg=='2':
			sendstr(player_id,'�ٺٺ٣������ʺϵ�ְҵ����ǣ�����~���������֡�ϣ������һ���𣿡�1���Ҳ�������������2�������˻����˵�')
			PlayerState[player_id] = 111


def APP_ToTUTU(player_id):
	if (player_id =='ʮ������')or(player_id =='���峿')or(player_id =='����Ѱ����'):
		dnow = datetime.datetime.now()
		d0 = datetime.datetime(2017,2,14)
		d1 = datetime.datetime(2016,5,21)
		d2 = datetime.datetime(2016,11,13)
		d3 = datetime.datetime(2016,8,10)
		d4 = datetime.datetime(2016,5,21)
		strcache = [
		'ͺͺ~�ٺٺ���ϲ����~��������������������~',
		'ƽʱ��������æ�ģ�������������Ͳ��ࡣ�ټ���������ٸ���̰˯�����ߵĴ���Ҳ���ˡ���',
		'�Һ��ھΰ� #��ϲ ����һ��ҹ��ͻ�����뿪ʼ����������򣬲�֪�����Ѿ���ǧ����',
		'������˯����ʱ��æ��ʱ�򣬲��������ʱ��ϣ���㿴������������������_(:�١���)_�ٺٺ�~',
		'��������˵�����ͻ�����ʱ�䣬�һ�ܿ������ͺͺ��~'
		'�����Դ˼�������2017��2��14�գ����ǹ��ĵ�һ�����˽� ^_^',
		'#��ϲ #��ϲ �Ұ��㣡'
		'��׼����գ�       2016��12��10�� ��������Ѿ���' + str((dnow-d1).days),
		'��������գ�       2016��11��13�� ��������Ѿ���' + str((dnow-d2).days),
		'��Ե�����գ�       2016�� 8��10�� ��������Ѿ���' + str((dnow-d3).days),
		'��ʶ�����գ�       2016�� 5��21�� ��������Ѿ���' + str((dnow-d4).days),
		'���������գ�       2017�� 2��14�� ��������Ѿ���' + str((dnow-d0).days),
		'���ظ�������������˵�'
		]
		sendlist(player_id,strcache,1,0.1,0.5)
	else:
		strcache = [
		'��һ������~����һЩ����������һЩ~~����~~ #����',
		'��һ������~����һЩ����������һЩ~~���~~ #��ϲ',
		'Ŷ~~���ĸ����ﰡ~~Ŷ~~ #��',
		'Ŷ~~~~�Ǿ��Ǵ�ͺͺ��~ #����'
		'���ظ�������������˵�']
		sendlist(player_id,strcache,1,0.1,0.5)
	PlayerState[player_id] = 1 #���˵�

def APP_TIEBA_TOP10(player_id,state,msg):
	debug("����Ӧ�ã�����ʮ�� "+player_id+" state:"+str(state)+" msg:"+msg)
	global TIEBA_state
	TIEBA_UPDATE_TO = core.settings.get_value("TIEBA_UPDATE_TO")
	TIEBA_SHIDA = core.settings.get_value("TIEBA_SHIDA")
	TIEBA_SHIDA_UPDATE = core.settings.get_value("TIEBA_SHIDA_UPDATE")
	f = open(TIEBA_UPDATE_TO+"_1",encoding = 'utf-8')
	top100_1 = f.readlines()
	f.close()
	
	f = open(TIEBA_UPDATE_TO+"_2",encoding = 'utf-8')
	top100_2 = f.readlines()
	f.close()
		
	if not player_id in VIPLevel:
		#��VIP
		strcache = [
		"���գ�"+TIEBA_SHIDA_UPDATE+"��ʮ��",
		"(*��Ŀǰ��Ȩ��Ϊ ��ͨ�û��������TOP 10)",
		"����--�ظ���--����--����ʱ��--���ɵ�ַ(kz)"]
		sendlist(player_id,strcache,0,0,0)
		sendlist(player_id,TIEBA_SHIDA,0,0,0)
		sendstr(player_id,"������Լ��ÿ�������Զ����£���ʱϵͳ�Ῠסһ��ʱ�䣬�������ĵȴ�")
		PlayerState[player_id] = 1
	else:
		if state == 200:
			sendstr(player_id,"�ٺٺ�~���ѽ~VIP�û� "+player_id+", ��ѡ�������ѯ����𣺡�1�����հٴ󣨽����ڷ���������2��ȫ���ٴ󣨽����ڻظ���")
			PlayerState[player_id] = 201
			TIEBA_state[player_id] = (0,0) #(�ļ������,ҳ��--ҳ��*10)
		elif state == 201:
			if msg =='1':
				strcache = [
				"���գ�"+TIEBA_SHIDA_UPDATE+"���ٴ�",
				"(*��Ŀǰ��Ȩ��Ϊ VIP�û��������TOP 100)",
				"����--�ظ���--����--����ʱ��--���ɵ�ַ(kz)"]
				sendlist(player_id,strcache,0,0,0)
				sendlist(player_id,top100_2[0:10],0,0,0)
				sendstr(player_id,"�� 1 / 10 ҳ ��-1����һҳ ��1����һҳ ��x���˳�")
				PlayerState[player_id] = 202
				TIEBA_state[player_id] = (2,0)
			else:
				strcache = [
				"ȫ����"+TIEBA_SHIDA_UPDATE+"���ٴ�",
				"(*��Ŀǰ��Ȩ��Ϊ VIP�û��������TOP 100)",
				"����--�ظ���--����--����ʱ��--���ɵ�ַ(kz)"]
				sendlist(player_id,strcache,0,0,0)
				sendlist(player_id,top100_1[0:10],0,0,0)
				sendstr(player_id,"�� 1 / 10 ҳ ��-1����һҳ ��1����һҳ ��x���˳�")
				PlayerState[player_id] = 202
				TIEBA_state[player_id] = (1,0)
		elif state == 202:
			fname_id,page = TIEBA_state[player_id]
			if msg.lower()=='x':
				PlayerState[player_id] = 1
				return
			try:
				addmsg = int(msg)
			except:
				addmsg = 0
			page += addmsg
			if page<0:
				page = 9
			if page>9:
				page = 0
			TIEBA_state[player_id] = (fname_id,page)
			sendstr(player_id,"����--�ظ���--����--����ʱ��--���ɵ�ַ(kz)")
			if fname_id == 1:
				sendlist(player_id,top100_1[page*10:(page+1)*10],0,0,0)
			else:
				sendlist(player_id,top100_2[page*10:(page+1)*10],0,0,0)
			sendstr(player_id,"�� "+ str(page+1)+" / 10 ҳ ��-1����һҳ ��1����һҳ ��x���˳�")
			
			
			

def response(state,player_id,msg):
	debug("response received. state: "+str(state)+" "+player_id+" "+msg,1)
	global TotalServiceTime 
	TotalServiceTime += 1
	if state == 0: #��һ�ζԻ���Ӧ���ܱ����򣬲��г����е�application msg:�������
		strcache = [
		'�ٺٺ���ð�~ ' + player_id+'��ץ������~',
		'����ͺͺ��������ˣ�Ŀǰ�汾 '+ str(core.settings.VERSION),
		'ϣ���ܸ������ĵ��������ճ��и���һ����Ȥ�;�ϲ #��ϲ',
		'1: �鿴����ͺͺ���ر���Ϣ',
		'2: ����3 ���� ��������(ÿ���������)',
		'3: ������ʺ��������ְҵ��',
		'4: Ư��ƿ(��δ���ţ������ڴ�)',
		'5: С����������(��δ���ţ������ڴ�)',
		'6: ���/�������������Ӹ��๦��',
		'7: ���ο���ͳ��']
		sendlist(player_id,strcache,1,0.1,0.5)
		PlayerState[player_id] = 2
	elif state == 1: #�ǵ�һ�ζԻ�����ѡ����msg:�������
		strcache = [
		'�ٺٺ�~ ' + player_id+'����ӭ����~ #��ϲ',
		'1: �鿴����ͺͺ���ر���Ϣ',
		'2: ����3 ���� ��������(ÿ���������)',
		'3: ������ʺ��������ְҵ��',
		'4: Ư��ƿ(��δ���ţ������ڴ�)',
		'5: С����������(��δ���ţ������ڴ�)',
		'6: ���/�������������Ӹ��๦��',
		'7: ���ο���ͳ��']
		sendlist(player_id,strcache,1,0.1,0.5)
		PlayerState[player_id] = 2
	elif state == 2: # ѡ����벻ͬӦ�ó��� msg:��ѡ��ѡ��
		if msg=="1":
			APP_ToTUTU(player_id)
		elif msg=="2":
			PlayerState[player_id] = 200
			APP_TIEBA_TOP10(player_id,state,msg)
		elif (msg=='4')or(msg=='5'):
			APP_working(player_id)
		elif msg=="3":
			PlayerState[player_id] = 100
			APP_professiontest(player_id,100,msg)
		elif msg=='6':
			sendstr(player_id,'�ٺٺٻ�ӭ�����ж�������᡾������ѧ��~���ֱ������ͺ�~')
			sendstr(player_id,'�����ʲô���飬��ӭд�Ÿ�ID��������ѧ��������ֱ�������˽�ľͺá�һ������Զ��ص����˵����һῴ����~зз���У�')
			PlayerState[player_id] = 1
		elif msg=="7":
			dnow = datetime.datetime.now()
			strcache = '���γ���ʼ���񣬹����У�' + str((dnow-core.settings.STARTTIME).seconds) + "�룬�յ���ѯ " + str(TotalServiceTime) +" �Σ������û��� "+ str(len(PlayerState))+" �������ǳ���ĵ� "+ str(core.settings.get_value("RESTARTTIME"))+" ��������������������˵�"
			sendstr(player_id,strcache)
			PlayerState[player_id] = 1
		else:
			sendstr(player_id,'��������ȷ��ѡ�')
			PlayerState[player_id] = 1
			response(1,player_id,"")
	elif (int(state)>=100)and(int(state)<200):
		APP_professiontest(player_id,state,msg)
	elif (int(state>=200)and(int(state)<300)):
		APP_TIEBA_TOP10(player_id,state,msg)
		
		
		
'''

�� ���� ���� �Ե� ���� ���� �嶾 ���� �ؽ� ��� ؤ�� ���� ����

-Ը�������
1: �� ���� ���� �嶾 ���� �ؽ� ����
 -ϣ������˳��������
  1: �� ���� ���� �嶾
   -һ���˵�ʱ���į��
    1: ���� �嶾
    -����ĺ���������
     1:�嶾
     2:����
    2: �� ����
    -��ϣ������ӵܻ����������
     1:��
     2:����
  
  2: ���� �ؽ� ����
   -һ���˵�ʱ���а�ȫ����
     1:���� ����
     -ϲ��������ȥ��
      1������
      2: ����
     2:�ؽ�

2: ���� �Ե� ���� ��� ؤ�� ���� ����
 -����������ô��
  1: ���� ؤ��
   -�������ἺΪ�˻������ܱ���
    1:���� 2:ؤ��
  2: �Ե� ���� ��� ���� ����
   -����Σ�յ�ʱ�����ϣ��
    1�Թ�Ϊ��: ���� ���
     -�Ŵ��б���Ϻܷ���һ��Ҳ��������
      1:����
      2:���
    2ȫ������: ���� ���� �Ե�
     -�����򹥻����Ǹ�����
       1:�Ե�
       2:���� ����
       -������
        1:����
        2:����
    3��ص���: ����
'''
