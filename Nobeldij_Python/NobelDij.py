print("OKJ vizsga: Nobeldíj")
print("\n--------------------------------------\n")
print("2.Feladat: Adatok beolvasása")
NobelDijAdatok_List=[]
beolvasasDB=0
fajl=open("nobel.csv", encoding="utf-8")
#év;típus;keresztnév;vezetéknév
for egySor in fajl:
    egySor=egySor.strip()
    dbok=egySor.split(";")
    Nobel={
        "Ev":int(dbok[0]),
        "Tipus":dbok[1],
        "Keresztnev":dbok[2],
        "Vezeteknev":dbok[3],
        "Nev":dbok[2]+" "+dbok[3]
        }
    NobelDijAdatok_List.append(Nobel)
    beolvasasDB+=1
fajl.close()
if(beolvasasDB>0):
    print("\tBeolvasás sikeres, beolvasorr sorok száma: ",beolvasasDB)
else:
    print("\tSikertelen beolvasás, kezd újra")
print("\n------------------------------------------\n")
print("3.Feladat: Arthur B. McDonald milyen Nóbeldíjat kapott?")
for Nobel in NobelDijAdatok_List:
    if(Nobel["Nev"]=="Arthur B. McDonald"):
        print("\tArthur B, McDonald Nobeldíja: "+Nobel["Tipus"])
print("\n------------------------------------------\n")
print("4.Feladat: Ki kapott 2017-ben irodalmi Nobeldíjat?")
for Nobel in NobelDijAdatok_List:
    if( Nobel["Ev"]==2017 and Nobel["Tipus"]=="irodalmi" ):
        print("\t"+Nobel["Nev"]+"\t:"+Nobel["Ev"].__str__())
print("\n-------------------------------------------\n")
print("5.Feladat: béke Nobeldíjas szervezetek 1990-től napjainkig")
for Nobel in NobelDijAdatok_List:
    if(Nobel["Tipus"]=="béke" and Nobel["Ev"]>1989 and Nobel["Vezeteknev"]==""):
        print("\t"+Nobel["Ev"].__str__() +" : "+Nobel["Nev"]+" "+Nobel["Tipus"]+" ")
print("\n--------------------------------------------\n")
print("6.Feladat: Curie család Nobeldíjasai ")
for Nobel in NobelDijAdatok_List:
    if(Nobel["Vezeteknev"].__contains__("Curie")):
        print("\t"+Nobel["Ev"].__str__()+" : "+Nobel["Nev"]+" -> "+Nobel["Tipus"])
print("\n--------------------------------------------\n")
print("7.Feladat: statisztika ")
Tipusok_List=[]
for Nobel in NobelDijAdatok_List:
    if not Tipusok_List.__contains__(Nobel["Tipus"]):
        Tipusok_List.append(Nobel["Tipus"])
#for i in range(len(Tipusok_List)):
#   print("\t"+Tipusok_List[i])
Statisztika_List=[]
for i in range(len(Tipusok_List)):
    db=0
    for Nobel in NobelDijAdatok_List:
        if Nobel["Tipus"]==Tipusok_List[i]:
            db+=1
    statisztika = {
        "mod": Tipusok_List[i],
        "db": db
    }
    Statisztika_List.append(statisztika)
    print("\t"+Tipusok_List[i]+" : "+db.__str__()+" db")
print("\n----------------------------------------")
for i in range(len(Statisztika_List)):
    print(Statisztika_List[i])