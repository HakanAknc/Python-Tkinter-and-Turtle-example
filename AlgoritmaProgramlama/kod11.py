a,b,c,d = 0,0,0,0
for a in range(1,6):
    b=b+1
    if(a<3 or b==4):
        c=c+a
    else:
        d=d+c
print(a,b,c,d)

