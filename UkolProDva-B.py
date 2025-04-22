#Brejcha
try:
    běh = int(input("Jak dlouho jsi běhal?"))
    chuze = int(input("Jak dlouho jsi šel?"))
except ValueError:
    print("Zadejte prosím číslo který dává smysl")
    exit()

celkovy_vydej = (běh * 5) + (chuze * 5)
print(f"Celkem spálené kalorie: {celkovy_vydej:.1f} kcal")
