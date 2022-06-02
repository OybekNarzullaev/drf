# 95 - bet
# Amaliy topshiriq
# 2 - masala 

# dastlab protsedura(qiymat qaytarmaydigan funksiya tuzamiz)
def chiqarish(n):
    # 0 dan n - 1 gacha bo'lgan solarni olish uchun sikl
    for i in range(n):
        # har bir sikldagi i + 1 ni n ga bo'lishini tekshirib ko'rib chiqaramiz:
        if n % (i + 1) == 0:
            print(i + 1, end=' ')

# funksiyani chaqirish(ishlatish)
chiqarish(6)