"""
1. Başla
2. A, B, C Oku
3. Eğer B > A ve A > C ise x. adıma Git
4. Eğer C > A ve A > B ise x. adıma Git
5. Eğer A > B ve B > C ise x. adıma Git
6. Eğer C > B ve B > A ise x. adıma Git
7. Eğer A > C ve C > B ise x. adıma Git
8. Eğer B > C ve C > A ise x. adıma Git
9. A Yaz
10. 14. adıma Git
11. B Yaz
12. 14. adıma Git
13. C Yaz
14. Bitir
"""

# Başlangıç değerlerini al
A = int(input("A değerini girin: "))
B = int(input("B değerini girin: "))
C = int(input("C değerini girin: "))

# 1. adım
# Başla

# 2-8. adımlar
if B > A > C:
    result = A
elif C > A > B:
    result = A
elif A > B > C:
    result = B
elif C > B > A:
    result = B
elif A > C > B:
    result = C
elif B > C > A:
    result = C

# 9-13. adımlar
print(result)

# 14. adım
# Bitir
