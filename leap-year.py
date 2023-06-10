DAYS_MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def pick_year():
    year = int(input("Input a year to verify: "))
    return year


def pick_month():
    month = int(input("Input a month to verify: "))
    while month < 1 or month > 12:
        print("NOT a valid number.")
        month = int(input("Input a month to verify: "))
    return month


def calc_leap(year):
    if year % 4 == 0:
        leap_year = True
        return leap_year
    else:
        leap_year = False
        return leap_year


def check_leap(year_tocheck):
    if year_tocheck:
        print("This year is a leap year.")
    else:
        print("This year is NOT a leap year.")


def check_month(month, year_tocheck):
    day_month = DAYS_MONTHS[month - 1]
    if year_tocheck and month == 2:
        day_month += 1
    print(f"This month has {day_month} days.")


year = pick_year()
month = pick_month()
year_tocheck = calc_leap(year)
check_leap(year_tocheck)
check_month(month, year_tocheck)
