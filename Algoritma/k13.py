"""
1. Başla
2. n Oku
3. X = 1
4. X * X Yaz
5. X = X+1
6. Eğer X < = n ise x. adıma Git
7. Bitir
"""

# 1. adım
# Başla

# 2. adım
n = int(input("n değerini girin: "))

# 3. adım
X = 1

# 4-6. adımlar
while X <= n:
    # 4. adım
    print(X * X)

    # 5. adım
    X = X + 1

    # 6. adım
    if X <= n:
        continue  # x. adıma Git

# 7. adım
# Bitir
