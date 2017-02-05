# -*- coding:gbk -*-  

import datetime
import core.settings
from core.debug import *
from send.sendcore import *


PlayerState = {}
VIPLevel = {"陈洛晨":1,"十里雾中":1,"春风扫残雪":1,"春风寻常在":1,"完颜阿九打":1}
TIEBA_state = {}
TotalServiceTime = 0
#0: 第一次对话介绍+主选单列出
#1：非第一次对话+主选单列出
#2：选择主选单
#100：职业选择APP初始化
def core_input(player_id,talktime,msg):
	if player_id in VIPLevel:
		if VIPLevel[player_id]==-1:
			sendstr(player_id,"您在黑名单中")
			return
	if not player_id in PlayerState:
		PlayerState[player_id] = 0 #init
	response(PlayerState[player_id],player_id,msg)

def APP_working(player_id):
	sendstr(player_id,"正在施工中，敬请期待~回复任意键返回主菜单")
	PlayerState[player_id] = 1

def APP_professiontest(player_id,state,msg):
	if state==100:
		strcache = ['唔，下面我会问你一些问题，请根据提示输入1或2或3',
								'Q1: 你喜欢读条吗？【1】我超喜欢的；【2】去特么的']
		sendlist(player_id,strcache,0,0,0)
		PlayerState[player_id] = 101
	elif state==101:
		if msg=='1':
			#万花 长歌 七秀 五毒 唐门 藏剑 纯阳
			sendstr(player_id,'Q2：那……你希望顺便玩玩治疗吗？【1】当然啦很有成就感；【2】治疗超累总是背锅')
			PlayerState[player_id] = 102
		elif msg=='2':
			#苍云 霸刀 少林 天策 丐帮 纯阳 明教
			sendstr(player_id,'Q2：你觉得当阵眼怎么样？【1】老子就要当小队VIP；【2】阵眼都是要饭的')
			PlayerState[player_id] = 103
		else:
			pass #随机输入不回答
	elif state==102:
		if msg=='1':
			#万花 长歌 七秀 五毒
			sendstr(player_id,'Q3：一个人在午夜，寂寞吗？【1】当然有人陪最好了；【2】老子无所畏惧')
			PlayerState[player_id] = 104
		elif msg=='2':
			#唐门 藏剑 纯阳
			sendstr(player_id,'Q3：一个人在午夜，有安全感吗？【1】吓得我开始熟悉技能了；【2】老子无所畏惧')
			PlayerState[player_id] = 105
		else:
			pass #随机输入不回答
	elif state==103:
		if msg=='1':
			#少林 丐帮
			sendstr(player_id,'Q3：遇到危险更喜欢明哲保身还是舍己为人？【1】死道友不死贫道；【2】艺高人胆大当然两肋插刀在所不辞')
			PlayerState[player_id] = 106
		elif msg=='2':
			#霸刀 苍云 天策 纯阳 明教
			sendstr(player_id,'Q3：遇到危险，你更希望以攻为守还是全身而退？【1】以攻为守；【2】全身而退；【3】钻地底下')
			PlayerState[player_id] = 107
		else:
			pass #随机输入不回答
	elif state==104:
		if msg=='1':
			#长歌 五毒
			sendstr(player_id,'Q4：你真的很希望试试治疗吗？【1】当然了；【2】打个酱油就好')
			PlayerState[player_id] = 108
		elif msg=='2':
			#万花 七秀
			sendstr(player_id,'Q4：在你理想中，你是个什么样的人？【1】知书达理的；【2】能歌善舞的')
			PlayerState[player_id] = 109
	elif state==105:
		if msg=='1':
			#唐门 纯阳
			sendstr(player_id,'Q4：喜欢移位吗？【1】那是我不仅自己跑跑跳跳，也要让别人跑跑跳跳；【2】老子就缩在这儿来打我啊')
			PlayerState[player_id] = 110
		elif msg=='2':
			sendstr(player_id,'嘿嘿嘿，你最适合的职业大概是：藏剑~【仅供娱乐】希望再试一次吗？【1】我不服！再来！【2】玩腻了回主菜单')
			PlayerState[player_id] = 111
	elif state==106:
		if msg=='1':
			sendstr(player_id,'嘿嘿嘿，你最适合的职业大概是：丐帮~【仅供娱乐】希望再试一次吗？【1】我不服！再来！【2】玩腻了回主菜单')
			PlayerState[player_id] = 111
		elif msg=='2':
			sendstr(player_id,'嘿嘿嘿，你最适合的职业大概是：少林~【仅供娱乐】希望再试一次吗？【1】我不服！再来！【2】玩腻了回主菜单')
			PlayerState[player_id] = 111
	elif state==107:
		if msg=='1':
			#苍云 天策
			sendstr(player_id,'Q4：当你放大招被打断的时候，一点都忍不了吗？【1】气得手抖【2】被打断是常事儿早就习惯了')
			PlayerState[player_id] = 112
		elif msg=='2':
			#明教 纯阳 霸刀
			sendstr(player_id,'Q4：相权和皇权你觉得哪个更有翻云覆雨的潜力？【1】皇权【2】相权')
			PlayerState[player_id] = 113
		elif msg=='3':
			sendstr(player_id,'嘿嘿嘿，你最适合的职业大概是：明教~【仅供娱乐】希望再试一次吗？【1】我不服！再来！【2】玩腻了回主菜单')
			PlayerState[player_id] = 111
	elif state==108:
		if msg=='1':
			sendstr(player_id,'嘿嘿嘿，你最适合的职业大概是：五毒~【仅供娱乐】希望再试一次吗？【1】我不服！再来！【2】玩腻了回主菜单')
			PlayerState[player_id] = 111
		elif msg=='2':
			sendstr(player_id,'嘿嘿嘿，你最适合的职业大概是：长歌~【仅供娱乐】希望再试一次吗？【1】我不服！再来！【2】玩腻了回主菜单')
			PlayerState[player_id] = 111
	elif state==109:
		if msg=='1':
			sendstr(player_id,'嘿嘿嘿，你最适合的职业大概是：万花~【仅供娱乐】希望再试一次吗？【1】我不服！再来！【2】玩腻了回主菜单')
			PlayerState[player_id] = 111
		elif msg=='2':
			sendstr(player_id,'嘿嘿嘿，你最适合的职业大概是：七秀~【仅供娱乐】希望再试一次吗？【1】我不服！再来！【2】玩腻了回主菜单')
			PlayerState[player_id] = 111
	elif state==110:
		if msg=='1':
			sendstr(player_id,'嘿嘿嘿，你最适合的职业大概是：唐门~【仅供娱乐】希望再试一次吗？【1】我不服！再来！【2】玩腻了回主菜单')
			PlayerState[player_id] = 111
		elif msg=='2':
			sendstr(player_id,'嘿嘿嘿，你最适合的职业大概是：纯阳~【仅供娱乐】希望再试一次吗？【1】我不服！再来！【2】玩腻了回主菜单')
			PlayerState[player_id] = 111
	elif state==111:
		#1 再来；2回主菜单
		if msg=='1':
			PlayerState[player_id] = 100
			APP_professiontest(player_id,100,"from state 111")
		elif msg=='2':
			PlayerState[player_id] = 1
			response(1,player_id,"from state 111")
	elif state==112:
		if msg=='1':
			sendstr(player_id,'嘿嘿嘿，你最适合的职业大概是：苍云~【仅供娱乐】希望再试一次吗？【1】我不服！再来！【2】玩腻了回主菜单')
			PlayerState[player_id] = 111
		elif msg=='2':
			sendstr(player_id,'嘿嘿嘿，你最适合的职业大概是：天策~【仅供娱乐】希望再试一次吗？【1】我不服！再来！【2】玩腻了回主菜单')
			PlayerState[player_id] = 111
	elif state==113:
		if msg=='1':
			sendstr(player_id,'嘿嘿嘿，你最适合的职业大概是：霸刀~【仅供娱乐】希望再试一次吗？【1】我不服！再来！【2】玩腻了回主菜单')
			PlayerState[player_id] = 111
		elif msg=='2':
			sendstr(player_id,'Q5：恋家吗？【1】志在四方【2】常回家看看')
			PlayerState[player_id] = 114
	elif state==114:
		if msg=='1':
			sendstr(player_id,'嘿嘿嘿，你最适合的职业大概是：明教~【仅供娱乐】希望再试一次吗？【1】我不服！再来！【2】玩腻了回主菜单')
			PlayerState[player_id] = 111
		elif msg=='2':
			sendstr(player_id,'嘿嘿嘿，你最适合的职业大概是：纯阳~【仅供娱乐】希望再试一次吗？【1】我不服！再来！【2】玩腻了回主菜单')
			PlayerState[player_id] = 111


def APP_ToTUTU(player_id):
	if (player_id =='十里雾中')or(player_id =='陈洛晨')or(player_id =='春风寻常在'):
		dnow = datetime.datetime.now()
		d0 = datetime.datetime(2017,2,14)
		d1 = datetime.datetime(2016,5,21)
		d2 = datetime.datetime(2016,11,13)
		d3 = datetime.datetime(2016,8,10)
		d4 = datetime.datetime(2016,5,21)
		strcache = [
		'秃秃~嘿嘿嘿你喜欢吗~这个程序是特意做给你的~',
		'平时咱俩都很忙的，本来见面次数就不多。再加上这个寒假各种贪睡，上线的次数也少了……',
		'我好内疚啊 #欣喜 所以一天夜里突发奇想开始码了这个程序，不知不觉已经几千行了',
		'当我在睡觉的时候，忙的时候，不能陪你的时候，希望你看到这个程序就能想起我_(:з」∠)_嘿嘿嘿~',
		'玩着玩着说不定就会忘了时间，我会很快赶来陪秃秃的~'
		'——以此纪念我们2017年2月14日，我们过的第一个情人节 ^_^',
		'#欣喜 #欣喜 我爱你！'
		'表白纪念日：       2016年12月10日 距离此日已经：' + str((dnow-d1).days),
		'见面纪念日：       2016年11月13日 距离此日已经：' + str((dnow-d2).days),
		'情缘纪念日：       2016年 8月10日 距离此日已经：' + str((dnow-d3).days),
		'认识纪念日：       2016年 5月21日 距离此日已经：' + str((dnow-d4).days),
		'程序上线日：       2017年 2月14日 距离此日已经：' + str((dnow-d0).days),
		'·回复任意键返回主菜单'
		]
		sendlist(player_id,strcache,1,0.1,0.5)
	else:
		strcache = [
		'有一个姑娘~她有一些任性她还有一些~~嚣张~~ #笨猪',
		'有一个姑娘~她有一些叛逆她还有一些~~疯狂~~ #欣喜',
		'哦~~是哪个姑娘啊~~哦~~ #噢',
		'哦~~~~那就是蠢秃秃啊~ #笨猪'
		'·回复任意键返回主菜单']
		sendlist(player_id,strcache,1,0.1,0.5)
	PlayerState[player_id] = 1 #主菜单

def APP_TIEBA_TOP10(player_id,state,msg):
	debug("进入应用：贴吧十大 "+player_id+" state:"+str(state)+" msg:"+msg)
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
		#非VIP
		strcache = [
		"今日（"+TIEBA_SHIDA_UPDATE+"）十大：",
		"(*您目前的权限为 普通用户，可浏览TOP 10)",
		"标题--回复数--作者--发帖时间--贴吧地址(kz)"]
		sendlist(player_id,strcache,0,0,0)
		sendlist(player_id,TIEBA_SHIDA,0,0,0)
		sendstr(player_id,"本程序约于每晚六点自动更新，届时系统会卡住一段时间，请您耐心等待")
		PlayerState[player_id] = 1
	else:
		if state == 200:
			sendstr(player_id,"嘿嘿嘿~你好呀~VIP用户 "+player_id+", 请选择您想查询的类别：【1】今日百大（今日内发帖）；【2】全部百大（今日内回复）")
			PlayerState[player_id] = 201
			TIEBA_state[player_id] = (0,0) #(文件名序号,页数--页数*10)
		elif state == 201:
			if msg =='1':
				strcache = [
				"今日（"+TIEBA_SHIDA_UPDATE+"）百大：",
				"(*您目前的权限为 VIP用户，可浏览TOP 100)",
				"标题--回复数--作者--发帖时间--贴吧地址(kz)"]
				sendlist(player_id,strcache,0,0,0)
				sendlist(player_id,top100_2[0:10],0,0,0)
				sendstr(player_id,"第 1 / 10 页 【-1】上一页 【1】下一页 【x】退出")
				PlayerState[player_id] = 202
				TIEBA_state[player_id] = (2,0)
			else:
				strcache = [
				"全部（"+TIEBA_SHIDA_UPDATE+"）百大：",
				"(*您目前的权限为 VIP用户，可浏览TOP 100)",
				"标题--回复数--作者--发帖时间--贴吧地址(kz)"]
				sendlist(player_id,strcache,0,0,0)
				sendlist(player_id,top100_1[0:10],0,0,0)
				sendstr(player_id,"第 1 / 10 页 【-1】上一页 【1】下一页 【x】退出")
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
			sendstr(player_id,"标题--回复数--作者--发帖时间--贴吧地址(kz)")
			if fname_id == 1:
				sendlist(player_id,top100_1[page*10:(page+1)*10],0,0,0)
			else:
				sendlist(player_id,top100_2[page*10:(page+1)*10],0,0,0)
			sendstr(player_id,"第 "+ str(page+1)+" / 10 页 【-1】上一页 【1】下一页 【x】退出")
			
			
			

def response(state,player_id,msg):
	debug("response received. state: "+str(state)+" "+player_id+" "+msg,1)
	global TotalServiceTime 
	TotalServiceTime += 1
	if state == 0: #第一次对话，应介绍本程序，并列出所有的application msg:随机内容
		strcache = [
		'嘿嘿嘿你好啊~ ' + player_id+'，抓到我啦~',
		'我是秃秃聊天机器人，目前版本 '+ str(core.settings.VERSION),
		'希望能给在无聊的日日日日常中给你一点乐趣和惊喜 #欣喜',
		'1: 查看给蠢秃秃的特别消息',
		'2: 剑网3 贴吧 今日热门(每晚六点更新)',
		'3: 我真的适合玩这个鬼职业吗',
		'4: 漂流瓶(暂未开放，敬请期待)',
		'5: 小和尚奇侠传(暂未开放，敬请期待)',
		'6: 入帮/给作者提意见添加更多功能',
		'7: 本次开机统计']
		sendlist(player_id,strcache,1,0.1,0.5)
		PlayerState[player_id] = 2
	elif state == 1: #非第一次对话，主选单，msg:随机内容
		strcache = [
		'嘿嘿嘿~ ' + player_id+'，欢迎回来~ #欣喜',
		'1: 查看给蠢秃秃的特别消息',
		'2: 剑网3 贴吧 今日热门(每晚六点更新)',
		'3: 我真的适合玩这个鬼职业吗',
		'4: 漂流瓶(暂未开放，敬请期待)',
		'5: 小和尚奇侠传(暂未开放，敬请期待)',
		'6: 入帮/给作者提意见添加更多功能',
		'7: 本次开机统计']
		sendlist(player_id,strcache,1,0.1,0.5)
		PlayerState[player_id] = 2
	elif state == 2: # 选择进入不同应用程序 msg:主选单选择
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
			sendstr(player_id,'嘿嘿嘿欢迎加入中恶六级帮会【北京大学】~入帮直接申请就好~')
			sendstr(player_id,'如果有什么建议，欢迎写信给ID【北京大学】，或者直接在这儿私聊就好。一会儿会自动回到主菜单，我会看到的~蟹蟹大佬！')
			PlayerState[player_id] = 1
		elif msg=="7":
			dnow = datetime.datetime.now()
			strcache = '本次程序开始至今，共运行：' + str((dnow-core.settings.STARTTIME).seconds) + "秒，收到查询 " + str(TotalServiceTime) +" 次，共有用户： "+ str(len(PlayerState))+" 个。这是程序的第 "+ str(core.settings.get_value("RESTARTTIME"))+" 次启动。任意键返回主菜单"
			sendstr(player_id,strcache)
			PlayerState[player_id] = 1
		else:
			sendstr(player_id,'请输入正确的选项！')
			PlayerState[player_id] = 1
			response(1,player_id,"")
	elif (int(state)>=100)and(int(state)<200):
		APP_professiontest(player_id,state,msg)
	elif (int(state>=200)and(int(state)<300)):
		APP_TIEBA_TOP10(player_id,state,msg)
		
		
		
'''

万花 长歌 苍云 霸刀 少林 七秀 五毒 唐门 藏剑 天策 丐帮 纯阳 明教

-愿意读条吗
1: 万花 长歌 七秀 五毒 唐门 藏剑 纯阳
 -希望至少顺便玩奶吗
  1: 万花 长歌 七秀 五毒
   -一个人的时候寂寞吗
    1: 长歌 五毒
    -你真的很想玩奶吗
     1:五毒
     2:长歌
    2: 万花 七秀
    -更希望大家子弟还是轻歌曼舞
     1:万花
     2:七秀
  
  2: 唐门 藏剑 纯阳
   -一个人的时候有安全感吗
     1:唐门 纯阳
     -喜欢跑来跑去吗
      1：唐门
      2: 纯阳
     2:藏剑

2: 苍云 霸刀 少林 天策 丐帮 纯阳 明教
 -觉得阵眼怎么样
  1: 少林 丐帮
   -更倾向舍己为人还是明哲保身
    1:少林 2:丐帮
  2: 霸刀 苍云 天策 纯阳 明教
   -遇到危险的时候，你更希望
    1以攻为守: 苍云 天策
     -放大招被打断很烦躁一点也不能忍吗
      1:苍云
      2:天策
    2全身以退: 明教 纯阳 霸刀
     -更倾向攻击还是辅助？
       1:霸刀
       2:明教 纯阳
       -恋家吗
        1:纯阳
        2:明教
    3钻地底下: 明教
'''
