"""
1. Başla
2. h, n Oku
3. s = 0
4. s = s + 1
5. h = h * 60 / 100
6. Eğer s < n ise x. adıma Git 
7. h Yaz
8. Bitir
"""

# 1. adım
# Başla

# 2. adım
h = int(input("Başlangıç değerini girin (h): "))
n = int(input("n değerini girin: "))

# 3. adım
s = 0

# 4-6. adımlar
while s < n:
    # 4. adım
    s = s + 1

    # 5. adım
    h = h * 60 / 100

    # 6. adım
    if s < n:
        continue  # x. adıma Git

# 7. adım
# Sonuç yazdır
print("Sonuç:", h)

# 8. adım
# Bitir
