toplam = 0
i = 0

while(True):
    deger=input("Sayı giriniz: ")
    sayi=int(deger)

    if sayi==0:
        break

    toplam = toplam + sayi
    i+=1
    ortalama = toplam/i

    print("Girilen sayıların ortalaması: ",ortalama)