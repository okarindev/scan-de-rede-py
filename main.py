import subprocess
import os
from colorama import Style,Fore,Back,init
from modules import get_mac, scan


init()
ip = input("Digite o ip:")
os.system("cls")
analise = scan.AnaliseRede(ip)
thread = analise.Start()


print(6*" "+"      IPs             |        STATUS          ")
print(6*" "+"                      |                        ")


for text in analise.lista:
    print(text)


content = subprocess.check_output("arp -a")
mac = get_mac.Mac(content)
mac.GetMac()
lista = mac.macs
device = scan.Device()
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
