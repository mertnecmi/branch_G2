import json
import pandas as pd
from tool.degiskenler import renkler


class Task:

    def __init__(self,id, tur,isim, oncelik, statu,baslamat,bitist,aciklama,kimden,kime,renk="\033[91m"):
        self.id     = id
        self.tur    = tur
        self.isim   = isim
        self.oncelik= oncelik
        self.statu  = statu
        self.baslamat=baslamat
        self.bitist = bitist
        self.aciklama=aciklama
        self.kimden =kimden
        self.kime = kime
        self.renk = renk
     
    def __str__(self):
        return f"{self.renk}{self.id}--{self.isim} (Başlangıç: {self.baslamat}, Bitiş: {self.bitist})"

    

class TaskM:
    def __init__(self):
        self.task_list = []
        self.task_load()

    def task_load(self):
        try:
            with open("gorevler.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            for d in data:
                self.task_list.append(d)
        except Exception as e:
            print(e)
            self.task_list=[]

    def task_add(self,task: Task):
        data ={
        "id" : task.id,
        "tur": task.tur.upper(),
        "isim": task.isim.capitalize(),
        "oncelik": task.oncelik.capitalize(),
        "statu": task.statu.capitalize(),
        "baslamat":task.baslamat,
        "bitist":task.bitist,
        "aciklama": task.aciklama.capitalize(),
        "kimden": task.kimden.capitalize(),
        "kime": task.kime.capitalize(),
        "renk" : task.renk
        }        
        self.task_list.append(data)

    def task_save(self):
        try:
            with open ("gorevler.json", "w", encoding="utf-8") as f:
                json.dump(self.task_list, f, ensure_ascii=False, indent=4)
            print("\033[96m Görevler Başarıyla Eklendi.... \033[0m]")
        except Exception as e:
            print(e)

class TaskL(TaskM):
    def __init__(self):
        super().__init__()

    def print_colored_row(self,row):
    
        color = row['renk'] if 'renk' in row and row['renk'] else ''
        # Her satır için renkli formatlama
        row_str = f"{color}{row['id']:<3} | {row['tur']:<3} | {row['isim']:15} | {row['oncelik']:<8} | {row['statu']:<10} | {row['baslamat']:<11} | {row['bitist']:<11} | {row['aciklama'][:19]:<20} | {row['kimden']:<12} | {row['kime']:<12}\033[0m"
        print(row_str)


    def gorevlistele(self,siralama="isim"):
        self.task_list.sort(key=lambda x: x[siralama])
        df = pd.DataFrame(self.task_list)
        for _, row in df.iterrows():
            self.print_colored_row(row)
    
        
class TaskE(TaskM):
    def __init__(self):
        super().__init__()
    
    def gorevgoster(self,id):
        gorev = next((gorev for gorev in self.task_list if gorev["id"] == id), False)
        if not gorev:
            return False
        else:
            print("\033[96mGörev Türü    : \033[33m", gorev["tur"])
            print("\033[96mGörev Adı     : \033[33m", gorev["isim"])
            print("\033[96mGörev Öncelik : \033[33m", gorev["oncelik"])
            print("\033[96mBitiş Tarihi : \033[33m", gorev["bitist"])
            print("\033[96mGörev Durumu  : \033[33m", gorev["statu"],"\033[0m")
            return True

    def gorevstatudegistir(self,id,durum):
        okmu=False
        for gorev in self.task_list :
            if gorev["id"] == id:
                gorev["statu"] = durum.capitalize()
                gorev["renk"] = renkler(durum)
                okmu = True
                break
        if okmu:
            self.task_save()
            return True
        else:
            return False
    def gorevoncelikdegistir(self,id,oncelik):
        okmu=False
        for gorev in self.task_list :
            if gorev["id"] == id:
                gorev["oncelik"] = oncelik.capitalize()
                gorev["renk"] = renkler(oncelik)
                okmu = True
                break
        if okmu:
            self.task_save()
            return True
        else:
            return False
    def gorevtarihdegistir(self,id,bitist):
        okmu=False
        for gorev in self.task_list :
            if gorev["id"] == id:
                gorev["bitist"] =bitist
                okmu = True
                break
        if okmu:
            self.task_save()
            return True
        else:
            return False