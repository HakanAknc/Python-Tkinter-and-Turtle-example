A = int(input("1. Sayıyı giriniz: "))
B = int(input("2. Sayıyı giriniz: "))
C = int(input("3. Sayıyı giriniz: "))
if (B>A and A>C):
    orta = A
elif (C>A and A>B):
    orta = A
elif (A>B and B>C):
    orta = B
elif (C>B and B>A):
    orta = B
elif (B>C and C>A):
    orta = C
else:
    orta = C

print(A,",",B,",",C, "İçinde ortada olan sayı: ", orta)