def is_leap_year(year):
    if year % 4 == 0:
        print("1 - true")
    else:
        print("1 - false")
    if year % 100 == 0:
        print("2 - false")
    else:
        print("2 - true")
    if year % 400 == 0:
        print("3 - true")
    else:
        print("3 - false")

is_leap_year(2100)
print("+-----------------------------------------------------------+")
print("1 - true    2 - true     3 - false   =  it is leap year")
print("1 - true    2 - false    3 - true    =  it is leap year")
print("1 - true    2 - false    3 - false   =  it is not a leap year")