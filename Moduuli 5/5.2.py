luvut = []
while True:
    syote = input("Syötä luku (tai paina Enter lopettaaksesi): ")
    if syote == "":
        break
    try:
        luvut.append(int(syote))
    except ValueError:
        print("Virheellinen syöte!")