from datetime import *



def oncelikdegistir(durum):
    if durum.capitalize() in ("Yüksek","Orta","Düşük"):
        return True
    

def durumdegistir(durum):
    if durum.capitalize() in ("Tamamlandı","Ertelendi"):
        return True
    

def renkler(durum):
    if durum.capitalize() == "Yüksek":
        renk ="\033[91m"
    elif durum.capitalize() == "Orta":
        renk ="\033[33m"
    elif durum.capitalize() == "Tamamlandı":
        renk ="\033[09m"
    elif durum.capitalize() == "Düşük":
        renk ="\033[32m"
    else:
        renk ="\033[32m"    
    return renk


def inputmesaj(b):
    if b == "tur":
        print("Kişisel İçin : K ... İş İçin : W giriniz ")
    if b == "oncelik":
        print("yüksek, orta, düşük giriniz ")
    
    if b == "bitist":
        print("Yarın için :1, Bir hafta sonrası için 2, veya (gün/ay/yıl) giriniz")
    
def inputkontrol(a,b):
    if b == "tur":
        if a.upper() == "K" or a.upper()=="W":
            return True
        else:
            return False
    elif b == "oncelik":
        if a.upper() in ("YÜKSEK","ORTA","DÜŞÜK"):
            return True
        else:
            return False    
    elif b == "bitist":
        if a == "1":
            return yarin()
        elif a=="2":
            return ghafta()
        else:
           if validate_date(a):
               return a
           else:
               return False
    else:
        return True
    

def validate_date(date_str):
    try:
        # Girilen tarihin "DD/MM/YYYY" formatında olduğunu kontrol et
        datetime.strptime(date_str, "%d/%m/%Y")
        return True  # Geçerli bir tarih
    except ValueError:
        return False  # Geçersiz tarih

def gorevbasliklari():
    return {
        "tur"       : "Görev Türü   : ",
        "isim"      : "Görev Adı    : ",
        "oncelik"   : "Öncelik      : ",
        "bitist"    : "Bitis Tarihi : ",
        "aciklama"  : "Açiklama     : ",
        "kimden"    : "Kimden       : ",
        "kime"      : "Kime         : "
        } 

def ghafta():
    bugun = date.today()
    ghafta = (bugun+timedelta(weeks=1)).strftime("%d/%m/%Y")
    return ghafta

def yarin():
    bugun = date.today()
    yarin = (bugun+timedelta(days=1)).strftime("%d/%m/%Y")
    return yarin

def bugun():
    bugun = date.today()
    bugun = bugun.strftime("%d/%m/%Y")
    return bugun
def saat():
    saat = datetime.now()
    saat = saat.strftime("%H:%M")
    return saat