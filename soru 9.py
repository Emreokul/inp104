kelime = input("Bir metin girin: ")
sil = input("Silenecek harfleri girin: ")
sonuc = ""
for harf in kelime:
  if harf not in sil:
    sonuc += harf
    print(sonuc)