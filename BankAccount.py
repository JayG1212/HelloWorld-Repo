#Written By Jay Gunderson
#05/15/2023

#Sets total
total = 1000

#Sets amount withdrawn
withdrawn = int(input("How much will you withdraw from your balance of 1000: "))

#Sets output if nothing is withdrawn
if withdrawn < 0:
    while withdrawn < 0:
     withdrawn = int(input("Error give a positive number: "))
if withdrawn == 0:
    print("Your total remains the same: $" + total )
else:
    total = total - withdrawn
    print("Your new total:" + total)