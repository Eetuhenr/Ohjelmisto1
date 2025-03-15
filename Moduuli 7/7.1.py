vuodenajat = ()
("talvi", 12, 1, 2)
("kevät", 3, 4, 5)
("kesä", 6, 7, 8)
("syksy", 9, 10, 11)
kuukausi = int(input("Syötä kuukauden numero (1-12): "))
for vuodenaika in vuodenajat:
    if kuukausi in vuodenaika[1:]:
        print(f"Kuukauden {kuukausi} vuodenajan nimi on {vuodenaika[0]}.")
        break