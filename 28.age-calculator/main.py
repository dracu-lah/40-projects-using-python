import datetime

y, m, d = [int(i) for i in input("Enter dob [ yyyy mm dd ] : ").split()]

today = datetime.datetime.now().date()
dob = datetime.date(y, m, d)
age = int((today-dob).days/365.25)

print(f"Your age is {age}")
