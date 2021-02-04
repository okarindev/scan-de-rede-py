import subprocess
import threading
import os
import get_mac
import requests as r
from colorama import Style,Fore,Back,init
from time import sleep
from requests.api import head
from requests.exceptions import RetryError
from bs4 import BeautifulSoup

init()
class Device():

    def __init__(self):
        self.lista_msg = []

    def GetDevice(self,mac,ip):
        try:
            headerss = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
            req = r.get(f"https://hwaddress.com/?q={mac}",params=headerss)
            html = req.content
            soup = BeautifulSoup(html,"html.parser")
            tr = soup.find_all("tr")
            device = tr[0].text
            self.lista_msg.append(str(6*" "+Fore.WHITE+f"Host: {ip}"+(18-len(ip)-3)*" "+f" | Dispositivo: {device}"))
        except:
            pass

class AnaliseRede:

    def __init__(self,ip):
        self.lista = []
        self.ip = ip

    def MarkName(self):
            print(Style.BRIGHT+Fore.CYAN+"   _____                       _        _____          _      \n  / ____|                     | |      |  __ \        | |     \n | (___   ___ __ _ _ __     __| | ___  | |__) |___  __| | ___ \n  \___ \ / __/ _` | '_ \   / _` |/ _ \ |  _  // _ \/ _` |/ _ \ \n  ____) | (_| (_| | | | | | (_| |  __/ | | \ \  __/ (_| |  __/\n |_____/ \___\__,_|_| |_|  \__,_|\___| |_|  \_\___|\__,_|\___|\n | |                                                          \n | |__  _   _                                                 \n | '_ \| | | |                                                \n | |_) | |_| |                                                \n |_.__/ \__, |                                                \n         __/ |                                                \n   ____ |___/           _       _____                         \n  / __ \| |            (_)     |  __ \                        \n | |  | | | ____ _ _ __ _ _ __ | |  | | _____   __            \n | |  | | |/ / _` | '__| | '_ \| |  | |/ _ \ \ / /            \n | |__| |   < (_| | |  | | | | | |__| |  __/\ V /             \n  \____/|_|\_\__,_|_|  |_|_| |_|_____/ \___| \_/              \n                                                                                                                            ")
            print(Style.BRIGHT+Fore.LIGHTWHITE_EX+f"\n Conexões[...]\n")

    def Ping(self,i):
        try:
            content = subprocess.check_output(f"ping {self.ip}.{i} -n 4").decode("cp1252").split("\n")
            tam = 15 - len(f"{self.ip}.{i}")
            if content[2].find("destino") == -1:
                self.lista.insert(i,Style.BRIGHT+Fore.GREEN+6*" "+f"Host: {self.ip}.{i}"+tam*" "+" | Conexão Acessível   [+]")
            '''else:
                self.lista.insert(i,Style.BRIGHT+Fore.RED+f"Host: {self.ip}.{i}"+tam*" "+" | Conexão Inacessível [X]")'''
        except Exception as error:
            tam = 15 - len(f"{self.ip}.{i}")
            self.lista.insert(i,Style.BRIGHT+Fore.YELLOW+6*" "+f"Host: {self.ip}.{i}"+tam*" "+" | Conexão Indefinida  [-]")

    def Start(self):
        self.MarkName()
        for i in range(1,256):
            self.thread = threading.Thread(target=self.Ping,args=(i,))
            self.thread.start()
        while self.thread.is_alive():
            continue
        return
#ALTERADO
ip = input("Digite o ip:")
analise = AnaliseRede(ip)
thread = analise.Start()
print(6*" "+"      IPs             |        STATUS          ")
print(6*" "+"                      |                        ")
for text in analise.lista:
    print(text)


content = subprocess.check_output("arp -a")
mac = get_mac.Mac(content)
mac.GetMac()
lista = mac.macs
device = Device()

print(Style.BRIGHT+Fore.WHITE+"\nDispositivos[...]\n")

for i in range(0,len(lista)):
    ip = mac.ips[i]
    device.GetDevice(mac.macs[i],ip)

for text in device.lista_msg:
    try:
        content = text.replace("Company","")
        print(content)
    except:
        content = text
        print(content)

    
while True:
    continue
