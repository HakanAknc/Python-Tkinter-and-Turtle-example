"""
1. Başla
2. A, B Oku
3. Sayac = 0, Toplam = 0
4. Toplam = Toplam + A
5. Sayac = Sayac + 1
6. Eğer Sayac < B ise x. adıma Git
7. Toplam Yaz
8. Bitir
"""

# Başlangıç değerlerini al
A = int(input("A değerini girin: "))
B = int(input("B değerini girin: "))

# 1. adım
# Başla

# 2-6. adımlar
Sayac = 0
Toplam = 0
while Sayac < B:
    # 4. adım
    Toplam = Toplam + A
    
    # 5. adım
    Sayac = Sayac + 1

# 7. adım
# Toplamı yazdır
print(Toplam)

# 8. adım
# Bitir
