opakovat = "ano"
while opakovat == "ano":
    cisloJedna = int(input("Zadejte číslo Prvé "))
    operace = input("Jaké bude znaménko ? ")
    cisloDva = int(input("Zadejte číslo Druhé "))
    if operace == "+":
        print(cisloJedna + cisloDva)
    elif operace == "-":
        print(cisloJedna - cisloDva)
    elif operace == "*":
        print(cisloJedna * cisloDva)
    elif operace == "/":
        print(cisloJedna / cisloDva)
    else:
        print("toto není to co bych očekával ...")
    opakovat = input("táži se vás je libo zopakovati akci ? ")
