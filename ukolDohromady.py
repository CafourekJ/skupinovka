#Cafourek#Brejcha
#toto nám napíše uživatel

jidloJedna = str(input("Napište jídlo č. 1: "))
KalorieJedna = int(input("Kolik mělo kalorií: "))
jidloDva = str(input("Napište jídlo č. 2: "))
KalorieDva = int(input("Kolik mělo kalorií: "))
jidloTri = str(input("Napište jídlo č. 3: "))
KalorieTri = int(input("Kolik mělo kalorií: "))

#tady nám náš prográmek vypočítá celkový počet kalorií

celkove_kalorie = (KalorieJedna + KalorieDva + KalorieTri)
print(f"Celkový počet kalorií je:",celkove_kalorie)

#zde jsme vypsali dvě aktivity
try:
    běh = int(input("Jak dlouho jsi běhal?"))
    chuze = int(input("Jak dlouho jsi šel?"))
except ValueError:
    print("Zadejte prosím číslo který dává smysl")
    exit()
#výpočet výdeje kalorií

celkovy_vydej = (běh * 5) + (chuze * 5)
print(f"Celkem spálené kalorie: {celkovy_vydej:.1f} kcal")

#vypočítáme si přebytek

přebytek_a_nadbytek = celkove_kalorie - celkovy_vydej
if přebytek_a_nadbytek > 0:
    print(f"Sněd jsi {celkove_kalorie:.1f} kcal a spálil {celkovy_vydej:.1f} kcal, To jest přebytek: {přebytek_a_nadbytek:.1f} kcal")
elif přebytek_a_nadbytek < 0:
    print(f"Sněd jsi {celkove_kalorie:.1f} kcal a spálil {celkovy_vydej:.1f} kcal, To jest málo příteli: {abs(přebytek_a_nadbytek):.1f} kcal")
else:
    print(f"Sněd jsi {celkove_kalorie:.1f} kcal a spálil {celkovy_vydej:.1f} kcal, Perfektně vyvážený")