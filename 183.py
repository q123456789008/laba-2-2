day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

if day > 1:
    day -= 1
elif month == 1:
    day = 31
    month = 12
    year -= 1
else:
    month -= 1
    if month in (1, 3, 5, 7, 8, 10, 12):
        day = 31
    elif month in (4, 6, 9, 11):
        day = 30
    elif (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        day = 29
    else:
        day = 28

print(f"{day}.{month}.{year}")
