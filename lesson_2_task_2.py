is_year_leap = [2008, 2007,2020]
for year in is_year_leap:
    if (year % 4 == 0):
        print("True", year)
    else:
        if (year % 3 == 0):
            print("False", year)

is_year_leap =int(input())
if (is_year_leap % 4 == 0):
    print("год", is_year_leap, True)
else:
    print("год", is_year_leap, False)