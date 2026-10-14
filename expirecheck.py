
from datetime import date

month = int(input("Enter expiry month (1-12): "))
year = int(input("Enter expiry year: "))

today = date.today()
current_month = today.month
current_year = today.year

if year < current_year or (year == current_year and month < current_month):
    print("Medicine is expired")
else:
    print("Medicine is still valid")