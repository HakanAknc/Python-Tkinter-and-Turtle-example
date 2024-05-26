"""
1. Başla
2. T = 0, S = 0, Ort = 0
3. X Oku
4. Eğer X = 0 ise x. adıma Git
5. T = T + X
6. S = S + 1 
7. 3. adıma Git
8. Ort = T / S
9. Ort Yaz
10. Bitir
"""

# 1. adım
# Başla

# 2. adım
T = 0
S = 0
Ort = 0

while True:
    # 3. adım
    X = float(input("Bir sayı girin (0 girerek sonlandırın): "))

    # 4. adım
    if X == 0:
        break  # 0 girildiğinde döngüden çık

    # 5. adım
    T = T + X

    # 6. adım
    S = S + 1

    # 7. adım
    continue  # Döngüye devam et

# 8. adım
# Ortalama hesapla
if S != 0:
    Ort = T / S

# 9. adım
# Ortalamayı yazdır
print("Ortalama:", Ort)

# 10. adım
# Bitir
