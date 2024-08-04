# Camden
# formatting integers using the F string
i: int = 1000000000
print(f'{i:_}')
print(f'{i:,}')
print(f'{i:e}')
print(f'{i:.2e}')
a = 'Bob'
b = 20
# F = F"My name is {a}, and I am {b} years old"
F = F"My name is {a}, and I am {b} years old"

print(F)

a = 0.1
b = 0.1
print(f"{a*b:.2f}")

c = str(bool(float(a)))
print(c)

