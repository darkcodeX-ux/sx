# SX ReverseIp, by Nopebee7
# Jangan recode atau di perjualbelikan. Hargai hak cipta

import urllib3, re, time, random, sys, os, socket
color = ["\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m", "\033[37m", "\033[39m"]
try: import requests; s = requests.Session()
except: print("{w}Require {g}requests {w}module\n{y}pip install {g}requests".format(w=color[6], y=color[2], g=color[1]));exit()
try: from multiprocessing.dummy import Pool as tpool
except:print("{w}Require {g}multiprocessing {w}module\n{y}pip install {g}multiprocessing".format(w=color[6], y=color[2], g=color[1]));exit()


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
thread = 100
outputFile = open("sr_sites.txt", "a")
tmpSites = []
ipsList = []
retSo = []
retSe = []


def logo():
    os.system(["clear", "cls"][os.name == 'nt'])
    Logo = '''
        ______  __      ____            ____
       / ___/ |/ /     / __ \___ _   __/  _/___
       \__ \|   /_____/ /_/ / _ \ | / // // __ \\
      ___/ /   /_____/ _, _/  __/ |/ // // /_/ /
     /____/_/|_|    /_/ |_|\___/|___/___/ .___/ 
     {y}nopebee7 {w}[{g}@{w}] {y}skullxploit          /_/ {w}v1.2\n'''.format(g=color[1], w=color[7], m=color[4], y=color[2], r=color[0])
    for Line in Logo.split('\n'):
        print(random.choice(color)+Line)
        time.sleep(0.1)


def opt():
    siteList = []
    fileName = input(
        " {w}[{g}+{w}] {y}the list {w}> ".format(w=color[6], g=color[1], y=color[2]))
    if os.path.exists(fileName):
        siteList = open(fileName, "r+").readlines()
    else:
        print(" {A}[{B}x{A}] {B}The list not found in current dir".format(
            A=color[6], B=color[5]))
        exit()
    theThread = input(
        " {w}[{g}+{w}] {y}thread {w}({y}default{w}:{y}100{w}) {w}> ".format(w=color[6], g=color[1], y=color[2]))
    if theThread == "":
        theThread = 100
    if siteList == []:
        print(" {A}[{B}x{A}] {B}Empty list".format(A=color[6], B=color[5]))
        exit()
    else:
        if len(siteList) < int(theThread):
            theThread = len(siteList)
        return siteList, int(theThread)


def revSo(ip):
    global retSo
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}
    api = "https://sonar.omnisint.io/reverse/"
    try:
        r = s.get(api+ip, headers=headers)
    except:
        if ip not in retSo:
            revSo(ip)
        return "error"
    if (r.text == "null"):
        return "error"
    else:
        r = r.json()
        res = []
        for site in r:
            site = site.replace("www.", "").replace('cpanel.', '').replace('webmail.', '').replace('webdisk.', '').replace('ftp.', '').replace(
                'cpcalendars.', '').replace('cpcontacts.', '').replace('mail.', '').replace('ns1.', '').replace('ns2.', '').replace('autodiscover.', '')
            res.append(site)
        return res


def rev(url):
    global tmpSites, outputFile, ipsList
    if url.startswith("http://"):
        url = url.replace("http://", "")
    elif url.startswith("https://"):
        url = url.replace("https://", "")
    url = url.replace("\n", "").replace("\r", "").replace("/", "")
    try:
        ip = socket.gethostbyname(url)
        if ip in ipsList:
            print(" \033[41;1m -- SAME IP -- \033[0m "+url)
            return
        ipsList.append(ip)
        so = revSo(ip)
    except Exception as e:
        print(" \033[41;1m -- ERROR -- \033[0m "+url)
        return
    st = []
    if so != "error":
        for s in so:
            if s not in st:
                st.append(s)
    resultSite = []
    for site in st:
        if site != "":
            if site not in tmpSites:
                outputFile.write(site+"\n")
                tmpSites.append(site)
                resultSite.append(site)
    print(" \033[42;1m -- "+str(len(resultSite))+" SITES -- \033[0m "+url)


if __name__ == "__main__":
    try:
        logo()
        sx = opt()
        print("\n")
        pool = tpool(sx[1])
        pool.map(rev, sx[0])
        pool.close()
        pool.join()
        print("\n {A}[{B}+{A}] {Y}Done {A}: {Y}{S} sites".format(Y=color[2],
                                                                 A=color[6], B=color[5], S=(str(len(tmpSites)))))
    except KeyboardInterrupt:
        print(
            "\n {w}[{r}-{w}] {b}Goodbye >//< ".format(w=color[6], r=color[0], b=color[3]))
