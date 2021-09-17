import json
import urllib.request
import http_pyynto




# 1. malliratkaisusta lainattu funktio "ryhmittele_toimipaikoittain"----------------------------
# palauttaa kaikki toimipaikat ja postinumerot ryhmiteltynä
def ryhmittele_toimipaikoittain (numero_sanakirja):
    paikat = {}
    for numero, nimi in numero_sanakirja.items():
        if nimi not in paikat:
            paikat[nimi] = []

        paikat[nimi].append(numero)

    return paikat


# 2. listaa toimipaikan postinumerot ---------------------------------- 
def listaa_postitoimipaikan_postinumerot(toimipaikka, numero_sanakirja):
    
    toimipaikan_postinumerot = []
    obj = ryhmittele_toimipaikoittain(numero_sanakirja) 
  
    if toimipaikka in obj.keys():
     for key, value in obj.items(): 

       if key == toimipaikka:
 
        toimipaikan_postinumerot.append(value)

     print("Postitoimipaikan_postinumerot: "+ ', '.join(toimipaikan_postinumerot[0]))

     return toimipaikan_postinumerot[0]

    else:
     print ("postinumeroa ei löytynyt")      


  
def kasittele_bugi(numero_sanakirja):
    smartpost_postinumerot = []
    obj = ryhmittele_toimipaikoittain(numero_sanakirja) 
  
    if "SMARTPOST" or "SMART POST" or "SMARTPSOT" in obj.keys():
     for key, value in obj.items(): 

       if key == "SMARTPOST" or key== "SMART POST" or key =="SMARTPSOT" :
 
        smartpost_postinumerot.append(value)

     print("bugi: "+ ', '.join(smartpost_postinumerot[0]))

     return smartpost_postinumerot[0]

    else:
     print ("Jokin meni vikaan")    




def main():
    postinumerot = http_pyynto.hae_postinumerot() 
    postitoimipaikka = input('Kirjoita postitoimipaikka: ').upper() 
    
    if postitoimipaikka == 'SMARTPOST' or postitoimipaikka =='SMART POST' or postitoimipaikka =='SMARTPSOT' or postitoimipaikka =='SMART-POST':
        print('bugi:' + postitoimipaikka)
        kasittele_bugi(postinumerot)

    else:
    
     listaa_postitoimipaikan_postinumerot(postitoimipaikka, postinumerot)
    
    

    
if __name__ == '__main__':
    main()
