sozcuk=str(input("sozcuk giriniz"))
sayi= str(input("bir sayı giriniz"))


if sayi<len(sozcuk):
  sonuc=sozcuk[:sayi]+"-"+[sayi:]

print(sonuc)