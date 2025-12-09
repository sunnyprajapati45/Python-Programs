# reverse a string without using in build functiona
a = "sunny"

b = ""

for i in range(len(a)-1,-1,-1):
    b = b + a[i]
print(b)