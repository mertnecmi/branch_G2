import tool.degiskenler as deg
from tool.task import *

def gorevtduzenle():
    while True:
        try:
            id = int(input("Tarihi değiştirilecek ID  (0 Ana Menu): "))
            if id == 0:
                break
            te = TaskE()
            deid = te.gorevgoster(id)
            if not deid:
                print("\033[96mBu ID Bulunamadı\033[0m")
            else:

                while True:
                    bitis = input("Yeni Bitiş Tarihi (gg/aa/yyyy) : " )
                    if bitis=="":
                        break
                    if not (deg.validate_date(bitis)):
                        print("\033[96mGeçerli Bir Tarih Giriniz\033[0m")
                    else:
                        ookmu = te.gorevtarihdegistir(id, bitis)
                    if ookmu:
                        break
                    else:
                        print("hata")
        except ValueError as e:
            print("\033[96m",e,"\033[0m")
def gorevduzenle():
    while True:
        try:
            id = int(input("Durumu veya önceliği değiştirilecek ID  (0 Ana Menu): "))
            if id == 0:
                break
            te = TaskE()
            deid = te.gorevgoster(id)
            if not deid:
                print("\033[96mBu ID Bulunamadı\033[0m")
            else:

                while True:
                    oncelik = input("Öncelik : Yüksek, Orta, Düşük : " )
                    if oncelik=="":
                        break
                    if not (deg.oncelikdegistir(oncelik)):
                        print("\033[96mGeçerli Bir Öncelik Giriniz\033[0m")
                    else:
                        ookmu = te.gorevoncelikdegistir(id, oncelik)
                    if ookmu:
                        break
                    else:
                        print("hata")

                while True:
                    durum = input("Durum : Tamamlandı / Ertelendi : " )
                    if durum=="":
                        break
                    if not (deg.durumdegistir(durum)):
                        print("\033[96mGeçerli Bir Durum Giriniz\033[0m")
                    else:
                        dokmu = te.gorevstatudegistir(id, durum)
                    if dokmu:
                        break
                    else:
                        print("durum hata")

        except ValueError as e:
            print("\033[96m",e,"\033[0m")
def gorevlistele(tl):
    tl.gorevlistele()
    print("-"*120)
    print("SIRALAMA TÜRLERİ")
    print("     1. Bitiş Tarihine Göre")
    print("     2. Önem Sırasına Göre")
    print("     3. Duruma Göre ")
    print("     0. Ana Menu ")

    ssec = input("Sıralama Türü Seçiniz : ")
    if ssec == "1":
        tl.gorevlistele("bitist")
    elif ssec == "2":
        tl.gorevlistele("oncelik")
    elif ssec == "3":
        tl.gorevlistele("statu")

    elif ssec == "0":
       return
    
def gorevekle(id):
    print("-"*40)
    print(id, "Nolu GÖREV EKLE")
    gb = deg.gorevbasliklari()
    task_data = {}
    for k,v in gb.items():
        while True:
            deg.inputmesaj(k)
            user_input = input(v)
            ok = deg.inputkontrol(user_input, k)
            if ok:
                if k =="bitist":
                    task_data[k] = ok
                else:
                    task_data[k] = user_input
                break
            else:
                continue
    renk =  deg.renkler(task_data["oncelik"])       

    gorev = Task(id, task_data["tur"],task_data["isim"], task_data["oncelik"], "Başladı", deg.bugun(), task_data["bitist"], task_data["aciklama"],task_data["kimden"],   task_data["kime"],renk)
    tm = TaskM()
    tm.task_add(gorev)
    tm.task_save()
   