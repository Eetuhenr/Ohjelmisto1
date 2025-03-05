hytti = input("syötä hyttiluokka LUX, A, B, C")
if hytti == "A":
    print("Hyttiluokka on A ikunnallinen hytti autokannen yläpuolella")
elif hytti == "B":
    print("hyttiluokka on B ikkunaton hytti autokannen yläpuolella")
elif hytti == "C":
    print("hyttiluokka on C ikkunaton hytti autokannen alapuolella")
elif hytti == "LUX":
    print("hyttiluokka on LUX parevekkeellinen hytti yläkannella")
else:
    print("hyttiä ei saatavilla")