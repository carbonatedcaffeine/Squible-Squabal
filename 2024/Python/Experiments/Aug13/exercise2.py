for i in range(10):    
    print(f"before {i = }")
    if i == 5:
        break
    print(f"after {i = }") # If i = 5, it will miss this print statement.

print("-"*20) # spacer

for i in range(10):
    print(f"before {i = }")
    if i % 2 != 0: # skip over odd numbers
        continue    

print(f"after {i = }")
print("-"*20)
for i in range(6):
    i += 2
    print(f"{i = }")