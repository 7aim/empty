import requests

from collections import Counter
from io import BytesIO
from PIL import Image


#ornek1
class SucRaporu():
    def __init__(self,category,date,force):
        self.category = category
        self.date = date
        self.force = force
        self.suclar = self.suclar_rapor()

    def suclar_rapor(self):
        url = "https://data.police.uk/api/crimes-no-location"
        payload = {"category": self.category,"date": self.date,"force": self.force}

        response = requests.get(url,payload)
 
        if response.status_code == 200:
            return response.json()
        else:
            print("Basarisiz")

    def ayikla(self):
        suclar_listesi = []
        for suc in self.suclar:
            suclar_listesi.append(suc["category"])
        return Counter(suclar_listesi)


sr = SucRaporu("all-crime","2024-01","leicestershire")

#print(sr.suclar_rapor())

#print(sr.ayikla())



#ornek2
class Futbolcu():
    def __init__(self,isim,pac,sho,pas,dri,deff,phy):
        self.isim = isim
        self.pac = pac
        self.sho = sho
        self.pas = pas
        self.dri = dri
        self.deff = deff
        self.phy = phy

    def yetenekler(self):
        x = ",".join([
        str(self.pac),
        str(self.sho),
        str(self.pas),
        str(self.dri),
        str(self.deff),
        str(self.phy)
        ])
        return x

    def futbolcu_charti(self):
        url = "https://image-charts.com/chart"
        payload = {
            "chco":"3092de,027182",
            "chdlp":"b",
            "chdl":self.isim,
            "chs":"480x480",
            "cht":"r" ,
            "chd":"t:" + self.yetenekler(),
            "chtt":"Futbolcu ozellikleri",
            "chxl":"0:|0|20|40|60|80|100",
            "chxt":"x",
            "chxr":"0,0.0,100.0",
            "chm": "B,AAAAAABB,0,0,0"
        }
        response = requests.post(url,params=payload)
        image = Image.open(BytesIO(response.content))
        image.show()

    def karsilastir(self,rakip):

        url = "https://image-charts.com/chart"
        payload = {
            "chco":"3092de",
            "chdlp":"b",
            "chdl":self.isim + "|" + rakip.isim,
            "chs":"480x480",
            "cht":"r" ,
            "chd":"t:" + self.yetenekler() + "|" + rakip.yetenekler(),
            "chtt":"Futbolcu ozellikleri",
            "chxl":"0:|0|20|40|60|80|100",
            "chxt":"x",
            "chxr":"0,0.0,100.0",
            "chm": "B,AAAAAABB,0,0,0|B,0073CFBB,1,0,0"
        }
        response = requests.post(url,params=payload)
        image = Image.open(BytesIO(response.content))
        image.show()



ronaldo = Futbolcu("Ronaldo",50,70,50,50,90,50)
messi = Futbolcu("Messi",70,10,50,90,90,50)


ronaldo.karsilastir(messi)




