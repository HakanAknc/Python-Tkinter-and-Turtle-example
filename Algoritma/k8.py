"""
1. Başla
2. n Oku
3. i = 0, tekToplam = 0, ciftToplam = 0
4. Sayi Oku
5. i = i + 1
6. Eğer Sayi MOD 2 = 0 ise x. adıma Git
7. tekToplam = tekToplam + Sayi
8. 10. adıma Git
9. ciftToplam = ciftToplam + Sayi
10. Eğer i < n ise x. adıma Git
11. tekToplam, ciftToplam Yaz
12. Bitir
"""

# 1. adım
# Başla

# 2. adım
n = int(input("n değerini girin: "))

# 3. adım
i = 0
tekToplam = 0
ciftToplam = 0

# 4-10. adımlar
while i < n:
    # 4. adım
    Sayi = int(input("Bir sayı girin: "))
    
    # 5. adım
    i = i + 1

    # 6. adım
    if Sayi % 2 == 0:
        continue  # x. adıma Git

    # 7. adım
    tekToplam = tekToplam + Sayi

    # 9. adım
    ciftToplam = ciftToplam + Sayi

    # 10. adım
    if i < n:
        continue  # x. adıma Git

# 11. adım
# Toplamları yazdır
print("Tek Toplam:", tekToplam)
print("Çift Toplam:", ciftToplam)

# 12. adım
# Bitir
