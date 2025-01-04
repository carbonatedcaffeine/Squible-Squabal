# Camden
print("Exception handling test")

try:
    x = 1/0
except:
    print("YEOUCH")

print("Finished")

def BadFunc():
    x = 1/0

try:
    BadFunc()
except Exception as e:
    print(f"{e = }")
print("All is good")

print("--"*10)
s = "a111"
try:
    num = int(s)
except:
    num = 0
print(f"{num = }")