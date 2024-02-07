# evennumber.py - tells if input number is even or odd

i = int(input("Enter Number:"))

# use modolu operator %, that calculates if fractional result of divisin is zero or otherwise; othersie is odd, zero is even

if (i % 2) ==0:
    print(f"{i} is Even")
else:
    print(f"{i} is Odd")