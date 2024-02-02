# timetodays.py - tells number of days, hours, minutes and/or seconds from input, # of seconds

days = float(input("Enter # of days:"))
hours = float(input("Enter # of hours:"))
minutes = float(input("Enter # of minutes:"))

print(f"You entered {days} days, {hours} hours, and {minutes} minutes.")

seconds = (days * 86400) + (hours * 3600) + (minutes * 60)

print (f"{days} days, {hours} hours, and {minutes} minutes, are {seconds} seconds.")

