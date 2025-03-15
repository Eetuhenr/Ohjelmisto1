import random
kuutioiden_lukumaara = int(input("kuinka monta arpakuutiota haluat heittää"))
summa = 0
for i in range(kuutioiden_lukumaara):
    heitto = random.randint(1,6)
    summa += heitto
print("silmälukujen summa on", summa)

