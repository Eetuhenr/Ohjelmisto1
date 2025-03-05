
kuhanpituus = float(input("syötä Kuhan pituus senttimetreinä"))
if kuhanpituus < 37:
 puuttuvatsentit = kuhanpituus - 37
 print(f"kuha on alamittainen se on {puuttuvatsentit} cm alle pyyntimittainen")
 print("laske kuha järveen")
else:
 print("kuha on sallitun pyyntimitan mukainen")