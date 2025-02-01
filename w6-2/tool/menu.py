import tool.islemler as islem
from tool.task import *



def menu():
    print("-"*40)
    print("ANA MENÜ")
    print("1. Görev Ekle")
    print("2. Görevleri Listele")
    print("3. Görev durum/oncelik Düzenle")
    print("4. Görev Bitiş Tarihi Değiştir")
    print("0. Çıkış")
 


def secim():

    while True:
        menu()
        tm = TaskM()
        tl = TaskL()
        
        id = len(tm.task_list)+1 
        secim = input("Bir İşlem Seçiniz : ")
        if secim =="1":
            islem.gorevekle(id)
        elif secim =="2":
            islem.gorevlistele(tl)
        elif secim =="3":
            islem.gorevduzenle()
        elif secim =="4":
            islem.gorevtduzenle()
        elif secim =="0":
            break
        else:
            print("Lütfen menüdeki gibi seçiniz ...")