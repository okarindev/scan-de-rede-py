import subprocess
from time import sleep


class Mac():

    def __init__(self,content):
        self.ips = 0
        self.macs = 0
        self.lista = 0
        self.ips = []
        self.macs = []
        self.words = "abcdefghijklmnopqrstuvwxz"
        self.content = content
        self.content = self.content.decode("cp1252")

    def GetMac(self):
        
        for example_mac in self.content.split("\n"):
            valor = 0
            space = example_mac[2:].find(" ")
            self.ip = example_mac[2:space+2]
            for w in self.words:
                check = self.ip.find(w)
                if check != -1:
                    valor = 1
                    break
            if valor == 0 and len(self.ip) > 5:
                self.ips.append(str(self.ip))
     
        for example_mac in self.content.split("\n"):
            index_1 = example_mac.find("-")-2
            mac_adress = example_mac[index_1:index_1+17]
            if len(mac_adress) == 17:
                self.macs.append(str(mac_adress))

