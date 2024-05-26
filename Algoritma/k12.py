"""
1. Başla
2. n Oku
3. i=3
4. A = 1, B = 1
5. A, B Yaz
6. C=A+B 
7. C Yaz
8. A = B
9. B = C
10. i=i+1
11. Eğer i <= n ise x. adıma Git
12. Bitir
"""

# 1. adım
# Başla

# 2. adım
n = int(input("n değerini girin: "))

# 3. adım
i = 3

# 4. adım
A, B = 1, 1

# 5. adım
print("A:", A)
print("B:", B)

# 6-11. adımlar
while i <= n:
    # 7. adım
    C = A + B
    print("C:", C)

    # 8. adım
    A = B

    # 9. adım
    B = C

    # 10. adım
    i = i + 1

    # 11. adım
    if i <= n:
        continue  # x. adıma Git

# 12. adım
# Bitir
