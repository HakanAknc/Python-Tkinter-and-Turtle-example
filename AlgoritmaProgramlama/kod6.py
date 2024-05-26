h=int(input("Yüksekliği giriniz: "))
n=int(input("Zıplama sayısını giriniz: "))
i=0
while i<n:
    h=h*60/100
    i+=1
print("Toplam",n,".","zıplamadan sonraki yükseklik",h)