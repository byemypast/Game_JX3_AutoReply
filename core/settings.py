import datetime
#�汾��
VERSION = 0.4
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

var = {}
var["TIEBA_UPDATE_TO"] = ""
var['TIEBA_SHIDA'] = []
var['TIEBA_SHIDA_UPDATE'] = ""
var['TIEBA_UPDATETIME'] = "18-00"

def set_value(svar,value):
	var[svar] = value

def get_value(svar):
	return var[svar]