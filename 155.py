PI = 3.14

radius = float(input("Enter the radius: "))
service = int(input("Enter the service number (1-4): "))

if service == 1:
    print(round(2 * PI * radius, 2))
elif service == 2:
    print(round(PI * radius ** 2, 2))
elif service == 3:
    print(round(4 / 3 * PI * radius ** 3, 2))
elif service == 4:
    print(round(4 * PI * radius ** 2, 2))
else:
    print("Invalid service number")
