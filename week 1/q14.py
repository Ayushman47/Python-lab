# 14. Count uppercase and lowercase letters in a string
text = input("Enter a string: ")
upper_count = sum(1 for c in text if c.isupper())
lower_count = sum(1 for c in text if c.islower())
print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)
