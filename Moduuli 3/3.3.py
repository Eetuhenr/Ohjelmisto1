sukupuoli = input("mies/nainen")
hemoglobiini = float(input("hemoglobiini arvo"))
if sukupuoli == "mies":
    print("sukupuoli on mies")
if sukupuoli == "nainen":
    print("sukupuoli on nainen")
if hemoglobiini < 167:
    print("hemoglobiini taso on alhainen")
elif hemoglobiini == 167:
    print("hemoglobiini taso on normaali")
else:
    print("hemoglobiini taso on korkea")
