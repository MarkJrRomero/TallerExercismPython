def leap_year(year):
    return not(bool(year % 4) | (bool(year % 100) ^ bool(year % 400)))
