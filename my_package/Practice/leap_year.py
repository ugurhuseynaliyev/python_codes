def leap_year(year):
    if year % 4 == 0:
        return True
    return False
print(leap_year(2023))