# -*- coding: gbk -*-
#vip1 ��Ϸģʽ
from send.sendcore import *
from core.debug import *
from send.sendapis import * #��Ҫֱ�Ӳ������ֿ�ݼ�
import core.settings
import time
import win32api,win32con

#��Ѽ�λ����Ϊ��
#0������ -��ѡ��Ŀ���Ŀ�� f8:��
def APP_vip1core(player_id,state,msg,PlayerState):
	if state==400:
		sendstr(player_id,'�뿿����ɫ��ظ��������')
		sendstr(player_id,'��1��ѡ���ң���2�����棨��������������3������Ŀ�ꣻ��4���س�����ȷ��ͬ��/���ѵȣ�����5����ͼȷ�ϣ�')
		sendstr(player_id,'��6��ѡ����ѡ�е�Ŀ�ꣻ��7���л���������Ŀ�ꣻ��8����ʼ�������뱣֤�������룩����9��ֹͣ����')
		sendstr(player_id,'��10������ȷ��')
		sendstr(player_id,'�ظ����֡��˳����˳���ģʽ')
		PlayerState[player_id] = 401
	elif state==401:
		if msg=="1":
			debug("��ʼ����ѡ�� "+ player_id)
			sendstr(player_id,'11')
		elif msg=="2":
			debug("��ʼ���Ը���Ŀ�� ָ�����ԣ�"+ player_id)
			key_down(0x1D) #CTRL
			time.sleep(0.4)
			key_down(0x22) #G
			time.sleep(0.4)
			
			key_up(0x1D) #CTRL
			time.sleep(0.4)
			key_up(0x22) #G
			time.sleep(0.4)
		elif msg=="3":
			debug("��ʼ���Ա���Ŀ�� ָ�����ԣ�"+ player_id)
			key_press(0x0B) #0
		elif msg=='4':
			debug("��ʼ���Իس� ָ�����ԣ�"+ player_id)
			key_press(0x1C) #ENTER	
		elif msg=='5':
			sendstr(player_id,'����ɫ������Ȧ�ں�ִ�д�����')
			screen_x = win32api.GetSystemMetrics(0)
			screen_y = win32api.GetSystemMetrics(1)
			midx = int(screen_x/2)
			midy = int(screen_y/2)
			win32api.SetCursorPos((midx,midy))
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,midx,midy,0,0)
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,midx,midy,0,0)
		elif msg=='6':
			debug("��ʼ����ѡ�� "+player_id+" ��Ŀ�� ָ�����ԣ�"+ player_id)
			key_press(0x0C) #-
		elif msg=='7':
			debug("��ʼ����ѡ�и�����Ŀ�� ָ�����ԣ�"+ player_id)
			key_press(0x0F) #tab
		elif msg=='8':
			debug("��ʼ���Թ��� ָ�����ԣ�" +player_id)
			core.settings.set_value("API_VIP1_ATTACK",1)
		elif msg=='9':
			debug("��ʼֹͣ���� ָ�����ԣ�" +player_id)
			core.settings.set_value("API_VIP1_ATTACK",-1)
		elif msg=='10':
			screen_x = win32api.GetSystemMetrics(0)
			screen_y = win32api.GetSystemMetrics(1)
			midx = int(round(0.51927*screen_x))
			midy = int(round(0.39259*screen_y))
			win32api.SetCursorPos((midx,midy))
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,midx,midy,0,0)
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,midx,midy,0,0)
		elif msg=="�˳�":
			PlayerState[player_id] = 1
			sendstr(player_id,'������˳�')
	return PlayerState