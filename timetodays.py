# timetodays.py - tells number of days, hours, minutes and/or seconds from input, # of seconds

i = float(input("Enter seconds:"))

days = i // 86400
rh = i - (days * 86400)
hours = rh // 3600
rm = rh - (hours * 3600)
minutes = rm // 60
rs = rm - (minutes * 60)
seconds = rs / 1


arr = {"Days": days, "Hours": hours, "Minutes": minutes, "Seconds": seconds}

for x in arr:

    print(x, arr[x])


          
