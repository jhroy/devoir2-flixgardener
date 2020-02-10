# coding : utf-8
import csv, json
import requests
fichier = "lobby.csv"
url = "http://jhroy.ca/uqam/lobby.json"

req = requests.get(url)

# if req.status_code == 200:
    #  print("Oui")
lobby=req.json()
    # # print(registre)
    # print(registre[2][institution])

    # Je sais maintenant que le lien se fait bel et bien avec le fichier json


for lobbyiste in lobby["registre"]:
    info=[]
    fr=lobbyiste[0]["fr_client_org_corp_nm"]
    en=lobbyiste[0]["en_client_org_corp_nm"]
    date=lobbyiste[0]["date_comm"]
    comlog=lobbyiste[0]["client_org_corp_num"]
    sujet=lobbyiste[1][0]["objet"]
    # sujet2=lobbyiste[2][0]["objet_autre"]
    sujet2=lobbyiste[1][0]["objet_autre"]

    info.append(fr)
    info.append(en)
    info.append(date)
    info.append(comlog)
    info.append(sujet)
    info.append(sujet2)
# print(info) Lorsque j'ai fait "print", le script envoyé est tout simplement une ligne aléatoire du registre (['null', 'Bruce Power', '2018-10-31', '5776', 'Energy', 'Energy'])

# f1 = open(fichier)
# lignes = csv.reader(f1)
# print(lignes)

#  if "limat" in sujet:
#      bonneliste=[]
#      bonneliste.append(sujet)
#      bonneliste.append(sujet2)
#      print (bonneliste)
# Cette commande ne fonctionne pas; rien ne sort quand j'entre le script

    n=0 
    if "limat" in sujet or "limat" in sujet2:  
     n+=1  
     print(info)
     cool=open(fichier, "a")
     garcon=csv.writer(cool)
     garcon.writerow(info)





