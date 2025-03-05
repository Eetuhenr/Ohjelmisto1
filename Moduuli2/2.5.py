leiviskat= float(input("leiviskät"))
naulat = float(input("naulat"))
luodit = float(input("luodit"))
kokonaisgrammat = (leiviska * 20 * 32 * 13.3) + (naula * 32 * 13.3) + (luoti * 13.3)
kilogrammat = kokonaisgrammat / 1000
grammat = kilogrammat * 1000
print(f"massa nykymittojen mukaan on {grammat} grammaa ja {kilogrammat} kilogrammaa")

