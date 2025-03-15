def gallonat_lyhyt(gallonat):
    return gallonat * 3.785
while True:
    gallonat = float(input("Syötä bensiinin määrä gallonina (negatiivinen luku lopettaa): "))
    if gallonat < 0:
        print("Ohjelma päättyy.")
        break
        litroja = gallonat_lyhyt(gallonat)
        print(f"{gallonat} gallonaa on {litroja:.2f} litraa.")