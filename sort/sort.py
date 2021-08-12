#importlar
from difflib import SequenceMatcher
import os, random

#Değişkenler
numlist = [1,3,2]
numbertoadd = "Python goes brrrr"
numbertoremove = "Python goes brrrr"
command = "Python goes brrrr"
commands = ["help", "?", "quit", "list", "sort", "sortmin", "sortmax", "add", "remove", "clear", "delete", "shuffle","starsortmin","starsortmax","reload"]
commandstart = "<"
commandend = "/>"

#Hebele hübele
print(commandstart+os.path.basename(__file__)+commandend + ' Lütfen yazabileceğiniz komutları görmek için "help" yada "?" yazınız')


#kelimeler arasında benzerlik oranı belirleme (stackoverflow)
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()





#inputlist sıralanacak liste, mm ise minmax (1,2,3) ya da maxmin (3,2,1)
def sort(inputlist, mm):

    listchanged = False #listede birşey değiştimi diye kontrol etmek için, eğer değişmemiş ise "break"
    sortinputlist = inputlist #sıralanacak olan "inputlist" in kopyası

    #loop
    for j in range(len(inputlist)):
        #loop
        for i in range(len(sortinputlist) - 1):
            #ikişer ikişer listenin içinde gidiyor ve eğer 1. sayı 2. den küçükse yerlerini değiştiriyor
            #yani en küçük sayıyı en sonda tutmaya çalışıyor
            if sortinputlist[i] <= sortinputlist[i + 1]:
                sortinputlist[i], sortinputlist[i + 1] = sortinputlist[i + 1], sortinputlist[i]
                listchanged = True
        #Eğer liste değişmemiş ise sıralanmış demektir o yüzden looptan çıkıyor
        if (not (listchanged)):
            break
        listchanged = False

    #Burada mm i kontrol ediyoruz
    #Eğer mm minmax yada maxmin değil ise error veriyor
    if (mm != "minmax" and mm != "maxmin"):
        return "Lütfen minmax ya da maxmin giriniz!"

    #Eğer mm minmax ise şu anki sıralanmış liste büyükten küçüğe olduğu için listeyi tersine çeviriyor
    if (mm == "minmax"):
        sortinputlist.reverse()
    #return
    return sortinputlist



#Komut loopu
while True:
    print()
    commandinput = input(f"{commandstart}{commandend} ")
    command = commandinput.strip().lower()
    print()
    #Boş komut
    if (command == ""):
        pass
    #"help" komutu
    elif command == "help" or command == "?":
        print(commandstart+"help"+'\n    "quit":Programı kapatır\n    "sortmin" veya "sortmax":Listeyi sıralar\n    "list":Şu anki listeyi gösterir\n    "add":Listeye sayı ekler\n    "remove":Listeden sayı çıkarır\n    "delete":Listeyi temizler\n    "clear":Terminali temizler\n    "shuffle":Listeyi karıştırır\n    "starsortmin" veya "starsortmax":Değişik birşey\n    "reload":Programı yeniden başlatır\n'+commandend)
    #"quit" komutu
    elif command == "quit":
        exit()
    #"sort" komutları
    elif command == "sort":
        print(commandstart+"sort"+" Lütfen sortmin veya sortmax yazınız"+commandend)
    elif command == "sortmin":
        print(f"{commandstart+'sortmin'} \n    {sort(numlist, 'minmax')} \n{commandend}")
    elif command == "sortmax":
        print(f"{commandstart+'sortmax'} \n    {sort(numlist, 'maxmin')} \n{commandend}")
    #"list" komutu
    elif command == "list":
        print(f"{commandstart+'list'} \n    {numlist} \n{commandend}")
    #"reload" komutu:
    elif command == "reload":
        os.startfile(os.path.basename(__file__))
        exit()
    #"add" komutu
    elif command == "add":
        print(f"{commandstart}add\n    Bir sayı eklemek istemiyorsanız hiçbirşey yazmadan [Enter] a basın\n    Eklenecek sayıyı/sayıları girin\n{commandend}")
        while True:
            numbertoadd = (input(f"{commandstart}add{commandend} ").strip())
            if (numbertoadd == ""):
                break
            else:
                try:
                    numlist.append(int(numbertoadd))
                except Exception as e:
                    print(f"{commandstart}add Lütfen geçerli bir sayı giriniz{commandend}")
                    continue
    #"remove" komutu
    elif command == "remove":
        print(f"{commandstart}remove\n    Bir sayı silmek istemiyorsanız hiçbirşey yazmadan [Enter] a basın\n    Silinecek sayıyı/sayıları girin\n{commandend}")
        while True:
            numbertoremove = (input(f"{commandstart}remove{commandend} ").strip())
            if (numbertoremove == ""):
                break
            else:
                try:
                    if not (int(numbertoremove) in numlist):
                        print(f"{commandstart}remove Öyle bir sayı listede yok{commandend}")
                    numlist = list(filter((int(numbertoremove)).__ne__, numlist))
                except Exception as e:
                    print(f"{commandstart}remove Lütfen geçerli bir sayı giriniz{commandend}")
                    continue
    #"delete" komutu
    elif command == "delete":
        print(f"{commandstart}delete Liste temizlendi{commandend}")
        numlist = []
    #"clear" komutu
    elif command == "clear":
        for i in range(20):
            print()
    #"shuffle" komutu
    elif command == "shuffle":
        random.shuffle(numlist)
        print(f"{commandstart}shuffle\n    " + str(numlist) + f"\n{commandend}")

    #starsort things
    elif command == "starsortmin":
        numlist = sort(numlist, 'minmax')
        minval = 0
        if (min(numlist) < 0):
            minval = (min(numlist))
        for i in numlist:
            if (i < 0): print(((abs(minval) - abs(i)) * " ") + (abs(i) * '*'))
            else: print(abs(minval) * " " + abs(i) * '*')
    elif command == "starsortmax":
        numlist = sort(numlist, 'maxmin')
        minval = 0
        if (min(numlist) < 0):
            minval = (min(numlist))
        for i in numlist:
            if (i < 0): print(((abs(minval) - abs(i)) * " ") + (abs(i) * '*'))
            else: print(abs(minval) * " " + abs(i) * '*')
    #Eğer geçersiz bir komut girilirse
    else:
        maxprob = 0
        maxprobword = "hello"
        for cmd in commands:
            if (similar(command, cmd)) > maxprob:
                maxprob = similar(command, cmd)
                maxprobword = cmd

        if maxprob >= 0.5:
            print(f"{commandstart + 'Yardım'}\n   Galiba {maxprobword} demeye çalıştınız")
        else:
            print(f'{commandstart + "Yardım"}\n   "{commandinput}" komutu bulunamadı')
        print(f'   Lütfen yazabileceğiniz komutları görmek için "help" yada "?" yazınız \n{commandend}')
