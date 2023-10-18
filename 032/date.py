import date as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.weekday()

print(year, type(year))
print(month, type(month))
print(day, type(day))

# We can test year, month and day because it's integer
if year == 2023:
    print("It's 2023")

# Create a date with default valuie for time
day_of_birth = dt.datetime(year=2023, month=10, day=18)
print("With default time",day_of_birth)
day_of_birth = dt.datetime(year=2023, month=10, day=18, hour=16, minute=46)
print(day_of_birth)