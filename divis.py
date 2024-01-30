# divis.py - tells if N is divisble by M or not

i = int(input("Enter N:"))
j = int(input("Enter M:"))

if (i % j) == 0:
    print(f"N  {i} is divisibly by M {j} ")
else:
    print(f"N  {i} is NOT  divisibly by M {j} ")