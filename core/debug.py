from send.sendcore import *
import core.settings
DEBUGLEVEL = 3
DEBUGF = open(core.settings.debugname,'a')

def debug(strs,level = 2):
	if DEBUGLEVEL>=level:
		try:
			DEBUGF.write(str(time.ctime())+" : "+strs+"\n")
		except:
			pass
	if level!=3:
		print(str(time.ctime())+" : "+strs)