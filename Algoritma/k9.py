"""
1. Başla
2. sn  Oku
3. sa = Tam(sn / 3600)
4. sn = sn – (sa x 3600)
5. dk = sn DIV / 60
6. sn = sn MOD 60
7. sa ‘:’ dk ‘:’ sn Yaz
8. Bitir
"""

# 1. adım
# Başla

# 2. adım
sn = int(input("Saniye değerini girin: "))

# 3. adım
sa = sn // 3600

# 4. adım
sn = sn - (sa * 3600)

# 5. adım
dk = sn // 60

# 6. adım
sn = sn % 60

# 7. adım
# Saat, dakika ve saniyeyi yazdır
print(f"{sa}:{dk}:{sn}")

# 8. adım
# Bitir
