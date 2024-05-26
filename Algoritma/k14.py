"""
1. Başla
2. n Oku
3. t = 0, i = 1
4. t = t + i
5. i = i + 2
6. Eğer i < = n ise x. adıma Git
7. ‘Toplam =’, t Yaz
8. Bitir
"""

# 1. adım
# Başla

# 2. adım
n = int(input("n değerini girin: "))

# 3. adım
t = 0
i = 1

# 4-6. adımlar
while i <= n:
    # 4. adım
    t = t + i

    # 5. adım
    i = i + 2

    # 6. adım
    if i <= n:
        continue  # x. adıma Git

# 7. adım
# Toplamı yazdır
print("Toplam =", t)

# 8. adım
# Bitir
