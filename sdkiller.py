import requests
from bs4 import BeautifulSoup
import lxml
from colorama import Fore,Style,Back
import os,sys,subprocess
import shutil
import random
from time import sleep

url = 'https://crt.sh/'

ALL_COLORS = [Fore.GREEN, Fore.RED, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
RESET_ALL = Style.RESET_ALL

def get_version():
    try:
        return open("version","r").read().strip()
    except:
        return '2.0'


__VERSION__ = get_version()

def do_zip_update():
    success=False

    # Download Zip from git
    # Unzip and overwrite the current folder

    if success:
        print("SD-KILLER was updated to the latest version")
        print("Please run the script again to load the latest version")
    else:
        print("Unable to update SD-KILLER")
        print("Grab The Latest one From https://github.com/Hackersthakur/SD-Killer.git")

    sys.exit()

def do_git_update():
    success=False
    try:
        os.system("git checkout .")
        os.system("git pull https://github.com/Hackersthakur/SD-Killer HEAD")
        clr()
        print(random.choice(ALL_COLORS) + logo + RESET_ALL)
        print(Fore.RED+"\n  MADE BY HACKERSTHAKUR  "+Fore.CYAN+"       Contact: Hackersthakurindia@gmail.com")
        print(Fore.RED+"\tVersion 1.9\n\n"+RESET_ALL)
        success = True

    except:
        success = False
    print("\n")

    if success:
        print("SD-KILLER was updated to the latest version")
        print("Please run the script again to load the latest version\n")
    else:
        print("Unable to update SD-KILLER")
        print("Make Sure To Install 'git' ")
        print("Then run command:")
        print("git checkout . && git pull https://github.com/Hackersthakur/SD-Killer HEAD")
    sys.exit()

def update():
    if shutil.which('git'):
        do_git_update()
    else:
        do_zip_update()
def check_for_updates():
    print("Checking for updates")
    try:
        fver = requests.get("https://raw.githubusercontent.com/Hackersthakur/SD-Killer/main/version").text.strip()
    except:
        fver = requests.get("https://raw.githubusercontent.com/Hackersthakur/SD-Killer/main/version",timeout=5).text.strip()

    
    if fver != __VERSION__:
        print("An update is available")
        print("Starting update...")
        update()
        
    else:
        print("SD-KILLER is up-to-date")
        print("Starting SD-KILLER\n")
        


def clr():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def sdfinder():
    print(Fore.RED+Style.BRIGHT+"Comming Soon\n"+RESET_ALL)
        

def BruteMode():
    domain = input(Fore.GREEN+Style.BRIGHT+"\n Enter Domain (eg : sthakur.com) : "+RESET_ALL)
    print("\n")
    f = open("Subdomain.txt","r")
    sub = f.read()
    sublist = sub.splitlines()

    for sd in sublist:
        http = "http://"+sd+"."+domain
        https = "https://"+sd+"."+domain
        
        try:
            requests.get(https)
            print(https)
        except requests.ConnectionError:
            try:
                requests.get(http)
                print(http)
            except requests.ConnectionError:
                pass



def defaultMode():
    domain = input(Fore.GREEN+Style.BRIGHT+"\n Enter Domain (eg : sthakur.com) : "+RESET_ALL)
    print("\n")
    #Setting User-Agent
    my_headers = { 
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.8',
        'Accept-Encoding': 'gzip',
     }
    payload = { 'q' : domain }
    r = requests.get( url, params = payload, headers = my_headers ).text
    soup = BeautifulSoup(r, 'lxml')
    #print(soup )
    sdomains = []
    scraped = ""
    d = ""
    for a in soup.select('td'):
        b = str(a)
        scraped = scraped+b
    sc = scraped.split('<')
    for c in sc:
        d = d+str(c)+">"
    f = d.split('>')
    alldom =[]
    for g in f:
        if domain in g and "href" not in g and "Search" not in g:
            if g not in alldom:
                print(g)
                alldom.append(g)


logo="""
    ███████╗██████╗       ██╗  ██╗██╗██╗     ██╗     ███████╗██████╗ 
    ██╔════╝██╔══██╗      ██║ ██╔╝██║██║     ██║     ██╔════╝██╔══██╗
    ███████╗██║  ██║█████╗█████╔╝ ██║██║     ██║     █████╗  ██████╔╝
    ╚════██║██║  ██║╚════╝██╔═██╗ ██║██║     ██║     ██╔══╝  ██╔══██╗
    ███████║██████╔╝      ██║  ██╗██║███████╗███████╗███████╗██║  ██║
    ╚══════╝╚═════╝       ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝"""

def menu():
    clr()
    print(random.choice(ALL_COLORS) + logo + RESET_ALL)
    print(Fore.RED+"\n  MADE BY HACKERSTHAKUR  "+Fore.CYAN+"       Contact: Hackersthakurindia@gmail.com")
    print(Fore.RED+"\tVersion 2.0\n\n"+RESET_ALL)
    print(Fore.YELLOW+Style.BRIGHT+"Options : \n"+RESET_ALL)
    check_for_updates()
    sleep(2)
    clr()
    print(random.choice(ALL_COLORS) + logo + RESET_ALL)
    print(Fore.RED+"\n  MADE BY HACKERSTHAKUR  "+Fore.CYAN+"       Contact: Hackersthakurindia@gmail.com")
    print(Fore.RED+"\tVersion 2.0\n\n"+RESET_ALL)
    print(Fore.YELLOW+Style.BRIGHT+"Options : \n"+RESET_ALL)
    print(Fore.LIGHTWHITE_EX+Style.BRIGHT+"\t[1] Default\n"+RESET_ALL)
    print(Fore.LIGHTWHITE_EX+Style.BRIGHT+"\t[2] SubBrute\n"+RESET_ALL)
    print(Fore.LIGHTWHITE_EX+Style.BRIGHT+"\t[3] Dork\n"+RESET_ALL)

    optsel = int(input(Fore.MAGENTA+Style.NORMAL+"Choose One Option : "+RESET_ALL))



    if optsel == 1:
        defaultMode()
    elif optsel == 2:
        BruteMode()
    elif optsel == 3:
        sdfinder()
    else:
        print(Fore.YELLOW+Style.BRIGHT+"You Selected Invalid Option\n"+RESET_ALL)
        
menu()

