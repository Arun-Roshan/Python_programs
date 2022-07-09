# how many days, weeks, months we have left if we live until 90 years old.
age = input("What is your current age?")

age_int = int(age)
year_remaining = 90 - age_int
days_remaining = year_remaining * 365
weeks_remaining = year_remaining * 52
months_remaining = year_remaining * 12

print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")
