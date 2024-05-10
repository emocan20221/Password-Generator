import random
why = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

soru = int(input("rastgele porolanın kaç harfli omasını isterseniz"))

parola = ""

for i in range(soru):
    parola += random.choice(why)

print(parola)