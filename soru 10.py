kelime = str(input("bir sözcük girin"))

sesli_harfler="aeıioöuüAEIİOÖUÜ"

sayac = 0
for harf in kelime :
  if harf in sesli_harfler:
    sayac+=1
    
    print("sesli harf sayısı",sayac)