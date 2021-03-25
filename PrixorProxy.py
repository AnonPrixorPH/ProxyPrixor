##### Proxy Download #####
# Created Date : March 26 2021
# Created Time : 4:30 AM

import os
import sys
import requests
import wget
import time

__Author__ = "AnonPrixor"
__CreatedD__ = "March 26, 2021"
__CreatedT__ = "4:30 AM (PHT)"
__FBACC__ = "https://facebook.com/botnetmaster1337"

##### Logo PrixorProxy #####
def logo():
	print("""
	\033[1;36;40m
    ____       _                 ____                       
   / __ \_____(_)  ______  _____/ __ \_________  _  ____  __
  / /_/ / ___/ / |/_/ __ \/ ___/ /_/ / ___/ __ \| |/_/ / / /
 / ____/ /  / />  </ /_/ / /  / ____/ /  / /_/ />  </ /_/ / 
/_/   /_/  /_/_/|_|\____/_/  /_/   /_/   \____/_/|_|\__, /  
                                         _    _____/____/   
                                        | |  / <  // __ \   
                                        | | / // // / / /   
                                        | |/ // // /_/ /    
                                        |___//_(_)____/  
	""")
	
##### PrixorProxy Menu #####
def PrixorProxy():
	os.system("clear")
	print("""\033[1;33;40m
    ____       _                 ____                       
   / __ \_____(_)  ______  _____/ __ \_________  _  ____  __
  / /_/ / ___/ / |/_/ __ \/ ___/ /_/ / ___/ __ \| |/_/ / / /
 / ____/ /  / />  </ /_/ / /  / ____/ /  / /_/ />  </ /_/ / 
/_/   /_/  /_/_/|_|\____/_/  /_/   /_/   \____/_/|_|\__, /  
                                         _    _____/____/   
                                        | |  / <  // __ \   
                                        | | / // // / / /   
                                        | |/ // // /_/ /    
                                        |___//_(_)____/  
	""")
	print("""
1. PROXY
2. HTTP
3. HTTPS
4. SOCKS4
5. SOCKS5
	""")
	proxymenu = input("Please Choose [1/5]: ")
	if (proxymenu == "1"):
		proxy = requests.get("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt").text
		print(proxy)
		proxyask = input("Do you want to Download PROXY [Y/N]: ")
		if (proxyask == "Y") or (proxyask == "y"):
			proxyd = wget.download("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt")
			time.sleep(2)
			print("[+] Proxy Successfully Downloaded")
		if (proxyask == "N") or (proxyask == "n"):
			os.system("clear")
			PrixorProxy()
	if (proxymenu == "2"):
		http = requests.get("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt").text
		print(http)
		httpask = input("Do you want to Download HTTP [Y/N]: ")
		if (httpask == "Y") or (httpask == "y"):
			httpd = wget.download("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt")
			time.sleep(2)
			print("[+] HTTP Successfully Downloaded")
		if (httpask == "N") or (httpask == "n"):
			os.system("clear")
			PrixorProxy()
	if (proxymenu == "3"):
		https = requests.get("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt").text
		print(https)
		httpask = input("Do you want to Download HTTPS [Y/N]: ")
		if (httpask == "Y") or (httpask == "y"):
			httpsd = wget.download("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt")
			time.sleep(2)
			print("[+] HTTPS Successfully Downloaded")
		if (httpask == "N") or (httpask == "n"):
			os.system("clear")
			PrixorProxy()
	if (proxymenu == "4"):
		socks4 = requests.get("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt").text
		print(socks4)
		socks4ask = input("Do you want to Download SOCKS4 [Y/N]: ")
		if (socks4ask == "Y") or (socks4ask == "y"):
			socks4d = wget.download("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt")
			time.sleep(2)
			print("[+] SOCKS4 Successfully Downloaded")
		if (socks4ask == "N") or (socks4ask == "n"):
			os.system("clear")
			PrixorProxy()
	if (proxymenu == "5"):
		socks5 = requests.get("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt").text
		print(socks5)
		socks5ask = input("Do you want to Download SOCKS5 [Y/N]: ")
		if (socks5ask == "Y") or (socks5ask == "y"):
			socks5d = wget.download("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt")
			time.sleep(2)
			print("[+] SOCKS5 Successfully Downloaded")
		if (socks5ask == "N") or (socks5ask == "n"):
			os.system("clear")
			PrixorProxy()
##### About PrixorProxy #####
def about():
	print("""
    ___    __                __ 
   /   |  / /_  ____  __  __/ /_
  / /| | / __ \/ __ \/ / / / __/
 / ___ |/ /_/ / /_/ / /_/ / /_  
/_/  |_/_.___/\____/\__,_/\__/  
                                
	""")
	print("""
Name : PrixorProxy
Author : AnonPrixor
Created Date : March 26, 2021
Created Time : 4:30 AM

About:

 PrixorProxy is Proxy Downloader\n Easy to use and easy to Download.\nPlease keep the code with Love and Respect.\n\nFrom: AnonPrixor
	""")
	
##### Bug Report #####
def bugreport():
	print("""
    ____                 ____                        __ 
   / __ )__  ______ _   / __ \___  ____  ____  _____/ /_
  / __  / / / / __ `/  / /_/ / _ \/ __ \/ __ \/ ___/ __/
 / /_/ / /_/ / /_/ /  / _, _/  __/ /_/ / /_/ / /  / /_  
/_____/\__,_/\__, /  /_/ |_|\___/ .___/\____/_/   \__/  
            /____/             /_/                      
	""")
	print("""
1. Facebook
2. Email
	""")
	contact = input("Please Choose [1/2]: ")
	if (contact == "1"):
		os.system("xdg-open https://mbasic.facebook.com/botnetmaster1337")
	if (contact == "2"):
		print("Email: anonprixorph@gmail.com")
		print("Email: anonprixorph@yahoo.com")

##### Menu PrixorProxy #####
def menu():
	logo()
	print("""
1. PrixorProxy Menu
2. About
3. Bug Report [ Administrator ]
	""")
	menu = input("Please Choose [1/3]: ")
	if (menu == "1"):
		os.system("clear")
		PrixorProxy()
	if (menu == "2"):
		os.system("clear")
		about()
	if (menu == "3"):
		os.system("clear")
		bugreport()
		
menu()
