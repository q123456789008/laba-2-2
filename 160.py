price = int(input("Enter the price in kopiyky: "))

hryvnias = price // 100
kopiyky = price % 100

if kopiyky == 0:
    print(hryvnias)
else:
    print(hryvnias, kopiyky)
