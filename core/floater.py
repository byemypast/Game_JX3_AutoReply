# -*- coding:gbk -*-  
#漂流瓶模块
#不复杂，直接用文件保存读取
import core.game
import core.userinfo
import core.settings
import send.sendcore
from core.debug import *
import random

floater_pool = []
needsending = {}

def floater_readall():
	debug("core.floater.floater_readall : 读取漂流瓶信息")
	dbname = core.settings.floaterdbname
	f = open(dbname)
	floater_pool = f.readlines()
	f.close()
	return floater_pool

def floater_write(player_id,issecret,msg):
	debug("core.floater.floater_write : 漂流瓶写入 用户：" +player_id+" 匿名(0=匿名)："+str(issecret)+" 内容："+msg)
	dbname = core.settings.floaterdbname
	f= open(dbname,'a')
	f.write(player_id+"\t"+str(issecret)+"\t"+msg.replace("\t",",").replace("\n"," ")+"\n")
	f.close()


def APP_floater_main(player_id,state,msg,userdata,PlayerState):
	#state: 300 - 399
	#能用userdata尽量不去访问数据库,userdata为只读数据库
	floater_pool = floater_readall()
	if state==300:
		strcache = ["欢迎~ 【"+core.game.get_usertype(player_id)+ "用户】" + player_id+" 来到漂流瓶模块！",
								"您目前有 " + str(userdata[player_id]['FLOATER_LEFT']) +" 次捞瓶机会，目前池塘共有 " + str(len(floater_pool)) + "条消息。捞瓶次数可以通过向池子里扔瓶子增加~",
								"【1】捞一个；【2】扔一个；【3】返回主菜单"
								]
		send.sendcore.sendlist(player_id,strcache)
		PlayerState[player_id] = 301
	elif state==301:
		#*收核心
		floater_left = userdata[player_id]['FLOATER_LEFT']
		if msg=="1":
			if floater_left<=0:
				send.sendcore.sendstr(player_id,"您的捞瓶次数已用完，请投喂~")
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
					#匿名信息 0:匿名
					floater_author = "一个匿名的小伙伴"
				strcache = [floater_author + "：",floater_msg,"【任意键】返回上一页"]
				send.sendcore.sendlist(player_id,strcache)
				PlayerState[player_id] = 302
		elif msg=="2":
			strcache = ["警告！垃圾信息、广告（含纯帮会/QQ收人无其他内容信息）、诽谤、se情、反don、政zhi","恶意挑起阵营/玩家纷争，或其他任何可能威胁平台生存的话题将导致账号被永久封禁，请珍惜您的账号",
									"请在此输入您的聊天内容："]
			PlayerState[player_id] = 303
			send.sendcore.sendlist(player_id,strcache)
		elif msg=="3":
			PlayerState[player_id] = 1
			send.sendcore.sendstr(player_id,'【任意键】返回主菜单')
	elif state==302:
		strcache = ["您目前有 " + str(userdata[player_id]['FLOATER_LEFT']) +" 次捞瓶机会，目前池塘共有 " + str(len(floater_pool)) + "条消息。捞瓶次数可以通过向池子里扔瓶子增加~",
								"【1】捞一个；【2】扔一个；【3】返回主菜单"]
		send.sendcore.sendlist(player_id,strcache)
		PlayerState[player_id] = 301
	elif state==303:
		#发送确认
		strcache = ["您要发送的内容是：",msg,"【1】确认发送（使用匿名ID）；【2】确认发送（show ID方便联系）；【3】再想想，重新编辑"]
		needsending[player_id] = msg
		PlayerState[player_id] = 304
		send.sendcore.sendlist(player_id,strcache)
	elif state==304:
		#发送核心
		if (msg=="1")or(msg=='2'):
			floater_left = userdata[player_id]['FLOATER_LEFT']
			floater_left += 1
			core.userinfo.database_setvalue("FLOATER_LEFT",floater_left,player_id)
			floater_write(player_id,int(msg)-1,needsending[player_id])
			needsending[player_id] = ""
			send.sendcore.sendstr(player_id,"发送成功！【任意键】返回上一页")
			PlayerState[player_id] = 302
		elif msg=="3":
			needsending[player_id] = ""
			strcache = ["警告！垃圾信息、广告（含纯帮会/QQ收人无其他内容信息）、诽谤、se情、反don、政zhi、恶意挑起阵营/玩家纷争或其他任何可能威胁平台生存的话题将导致账号被永久封禁，请珍惜您的账号",
									"请在此输入您的聊天内容："]
			PlayerState[player_id] = 303
			send.sendcore.sendlist(player_id,strcache)
	return PlayerState