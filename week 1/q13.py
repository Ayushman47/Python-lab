# 13. Check whether a number is in a given range
num = int(input("Enter a number: "))
lower, upper = 10, 50
print("In range" if lower <= num <= upper else "Out of range")
