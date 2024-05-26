"""
1. Başla
2. A, B, Op Oku
3. Eğer Op = “+” ise x. adıma Git
4. Eğer Op = “-” ise x. adıma Git
5. Eğer Op = “*” ise x. adıma Git
6. Eğer Op = “/” ise x. adıma Git
7. Sonuc = A + B
8. 14. adıma Git
9. Sonuc = A - B
10. 14. adıma Git
11. Sonuc = A * B
12. 14. adıma Git
13. Sonuc = A / B
14. Sonuc Yaz 
15. Bitir
"""

# Başlangıç değerlerini al
A = float(input("A değerini girin: "))
B = float(input("B değerini girin: "))
Op = input("Operatörü girin (+, -, *, /): ")

# 1. adım
# Başla

# 2-6. adımlar
if Op == "+":
    Sonuc = A + B
elif Op == "-":
    Sonuc = A - B
elif Op == "*":
    Sonuc = A * B
elif Op == "/":
    Sonuc = A / B

# 14. adım
# Sonucu yazdır
print(Sonuc)

# 15. adım
# Bitir
