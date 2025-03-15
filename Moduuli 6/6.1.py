import random
def heita_noppaa():
    return random.randint(1, 6)
while True:
    silmalukku = heita_noppaa()
    print(f"Heiton tulos: {silmalukku}")
    if silmalukku == 6:
        print("Kuutonen tuli! Peli päättyy.")
        break