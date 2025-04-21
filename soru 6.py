sozcuk=str(input("sozcuk giriniz"))
sayi= int(input("bir sayı giriniz"))
harf=str(input("harf girin"))

if sayi < len(sozcuk):
  sonuc = sozcuk[:sayi-1]+harf+sozcuk[sayi:]

print(sonuc)