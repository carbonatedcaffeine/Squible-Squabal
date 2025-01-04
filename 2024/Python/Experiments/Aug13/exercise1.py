# Camden, 2024
a = 4
b = 9
c = 5

y = ((a + b) * c) / 2 # Added (a + b)
if y > (a + b + c):
    print("y is more than the sum of a, b and c.")
elif y < ((a + b) + c) / 2: # Add (a + b)
    print("y is less than the sum of a, b and c divided by two.")
print(((a + b)* c)/2)
print(a + b * c /2)
print((a + b)* c / 2)