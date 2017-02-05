# -*- coding:gbk -*- 
#用户信息模块
#表结构：(userdata)
#--------------------------------------------------------------------------------
#NAME | FLOATER_LEFT  |  VIP_LEVEL  |   SCORE    |     JOB      |  REGTIME      |
#--------------------------------------------------------------------------------

import time
import sqlite3
import shutil
import tempfile
from core.debug import *
dbname = "userdb.db"
tempdir = tempfile.mkdtemp()

def database_getall(name):
	return database_query("SELECT * from userdata where NAME = '"+name+"'")

def database_query(query_str):
	debug("数据库查询："+ str(query_str))
	try:
		conn = sqlite3.connect(dbname)
		retstr = conn.execute(query_str).fetchall()
		conn.commit()
		conn.close()
	except Exception as err:
		debug("***database_query error: " +str(err)+", 使用代替方式(userinfo.py)",1)
		filename = str(random.randint(0,99999999))
		shutil.copyfile(dbname,tempdir+"\\"+filename)
		connnew = sqlite3.connect(tempdir+"\\"+filename)
		retstr = connnew.execute(query_str).fetchall()
		connnew.close()
		os.remove(tempdir+"\\"+filename)
	debug("数据库查询结束，返回值："+str(retstr))
	return retstr

def database_buildup():
	debug("收到建库指令")
	database_query("CREATE TABLE userdata(NAME TEXT PRIMARY KEY, FLOATER_LEFT INT, VIP_LEVEL INT, SCORE REAL, JOB TEXT, REGTIME TEXT);")
	debug("建库成功")

def database_newuser(player_id):
	#player_id is impossible to inject
	#给予2次漂流瓶机会
	database_query("INSERT INTO userdata(NAME,FLOATER_LEFT,VIP_LEVEL,SCORE,JOB,REGTIME) VALUES ('"+player_id+"',2,3,0,'未知','"+time.ctime()+"')")

def database_getvalue(key,name):
	debug("数据库访问:"+key+" "+name)
	retstr = database_query("SELECT "+key+" from userdata where NAME = '"+name+"'").fetchall()
	debug("数据库访问结果:"+retstr[0][0])
	return retstr[0][0]

def database_setvalue(key,keyto,name):
	#no try
	conn = sqlite3.connect(dbname)
	retstr = conn.execute("UPDATE userdata SET "+ key +" = "+str(keyto)+"where NAME = "+ name)
	conn.commit()
	conn.close()
	

