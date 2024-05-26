n = int(input("bir sayı giriniz: "))
i=1
toplam=0
while i<=n:
    toplam = toplam + i
    i=i+1
print("1'den n'e kadar olan sayıların toplamı: ",toplam)
# print(f"1'den {n}'e kadar olan sayıların toplamı: ",toplam)
# print("1'den {}'e kadar olan sayıların toplamı: ".format(n),toplam)