sozcuk=str(input("sozcuk giriniz"))
harf=str(input("harf girin"))
sayac=0
for i in sozcuk:
  if i == harf:
    sayac+=1
    print(sayac)