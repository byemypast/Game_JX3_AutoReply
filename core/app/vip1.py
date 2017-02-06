# -*- coding: gbk -*-
#vip1 调戏模式
from send.sendcore import *
from core.debug import *
from send.sendapis import * #需要直接操作各种快捷键
import core.settings
import time
import win32api,win32con

#请把键位设置为：
#0：抱抱 -：选中目标的目标 f8:宏
def APP_vip1core(player_id,state,msg,PlayerState):
	if state==400:
		sendstr(player_id,'请靠近角色后回复下列命令：')
		sendstr(player_id,'【1】选中我；【2】跟随（仅限绿名）；【3】抱抱目标；【4】回车（如确认同乘/好友等）；【5】过图确认；')
		sendstr(player_id,'【6】选中我选中的目标；【7】切换附近红名目标；【8】开始攻击（请保证攻击距离）；【9】停止攻击')
		sendstr(player_id,'【10】进组确认')
		sendstr(player_id,'回复汉字【退出】退出该模式')
		PlayerState[player_id] = 401
	elif state==401:
		if msg=="1":
			debug("开始尝试选中 "+ player_id)
			sendstr(player_id,'11')
		elif msg=="2":
			debug("开始尝试跟随目标 指令来自："+ player_id)
			key_down(0x1D) #CTRL
			time.sleep(0.4)
			key_down(0x22) #G
			time.sleep(0.4)
			
			key_up(0x1D) #CTRL
			time.sleep(0.4)
			key_up(0x22) #G
			time.sleep(0.4)
		elif msg=="3":
			debug("开始尝试抱抱目标 指令来自："+ player_id)
			key_press(0x0B) #0
		elif msg=='4':
			debug("开始尝试回车 指令来自："+ player_id)
			key_press(0x1C) #ENTER	
		elif msg=='5':
			sendstr(player_id,'将角色带到光圈口后执行此命令')
			screen_x = win32api.GetSystemMetrics(0)
			screen_y = win32api.GetSystemMetrics(1)
			midx = int(screen_x/2)
			midy = int(screen_y/2)
			win32api.SetCursorPos((midx,midy))
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,midx,midy,0,0)
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,midx,midy,0,0)
		elif msg=='6':
			debug("开始尝试选中 "+player_id+" 的目标 指令来自："+ player_id)
			key_press(0x0C) #-
		elif msg=='7':
			debug("开始尝试选中附近的目标 指令来自："+ player_id)
			key_press(0x0F) #tab
		elif msg=='8':
			debug("开始尝试攻击 指令来自：" +player_id)
			core.settings.set_value("API_VIP1_ATTACK",1)
		elif msg=='9':
			debug("开始停止攻击 指令来自：" +player_id)
			core.settings.set_value("API_VIP1_ATTACK",-1)
		elif msg=='10':
			screen_x = win32api.GetSystemMetrics(0)
			screen_y = win32api.GetSystemMetrics(1)
			midx = int(round(0.51927*screen_x))
			midy = int(round(0.39259*screen_y))
			win32api.SetCursorPos((midx,midy))
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,midx,midy,0,0)
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,midx,midy,0,0)
		elif msg=="退出":
			PlayerState[player_id] = 1
			sendstr(player_id,'任意键退出')
	return PlayerState