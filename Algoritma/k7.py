"""
1. Başla
2. A Oku
3. Say = 1
4. Eğer A MOD Say = 0 ise x. adıma Git
5. 7. adıma Git
6. Say Yaz
7. Say = Say + 1
8. Eğer Say < = A ise x. adıma Git
9. Bitir
"""

# 1. adım
# Başla

# 2. adım
A = int(input("Bir sayı girin: "))

# 3. adım
Say = 1

# 4-8. adımlar
while True:
    # 4. adım
    if A % Say == 0:
        continue  # x. adıma Git

    # 6. adım
    print(Say)

    # 7. adım
    Say = Say + 1

    # 8. adım
    if Say <= A:
        continue  # x. adıma Git

    # 9. adım
    break  # Bitir
