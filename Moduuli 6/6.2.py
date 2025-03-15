import random
def heita_noppaa(tahkot):
    return random.randint(1, tahkot)
maksimi_silmaluku = int(input("Syötä nopan maksimisilmäluku (esim. 6, 20, 21): "))
tahkot = maksimi_silmaluku
while True:
    silmaluku = heita_noppaa(tahkot)
    print(f"Heiton tulos: {silmaluku}")
    if silmaluku == maksimi_silmaluku:
        print(f"Maksimi silmäluvun ({maksimi_silmaluku}) tuli! Peli päättyy.")
        break