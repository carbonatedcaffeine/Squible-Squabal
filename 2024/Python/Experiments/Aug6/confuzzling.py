aT:bool = True
bT:bool = True
cF:bool = False
dF:bool = False

a = 10
b = 20
# a % 2 is false. 
# It's false because the remainder is 0, so 
# the answer ends up being false.

# not false = true
# not true = false


print(bool(a))
print(bool(a % 2))
if not a % 2:
    print(f"{a % 2 = }")

print((aT and a) < b)
print(aT and a)
print(aT + a)
print(cF + a)
print(cF and a)