PRICE = 2700

quantity = int(input("Enter the number of software packages: "))

if quantity >= 100:
    discount = 40
elif quantity >= 50:
    discount = 30
elif quantity >= 20:
    discount = 20
elif quantity >= 10:
    discount = 10
else:
    discount = 0

if discount > 0:
    total = quantity * PRICE * (100 - discount) / 100
else:
    total = quantity * PRICE

print(f"The amount of discount is {discount}%, total amount of the purchase "
      f"after the discount is UAH {total}")
