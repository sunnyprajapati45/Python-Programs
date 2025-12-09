#check palindrom or not
a = "naman"

b = ""

for i in range(len(a)-1,-1,-1):
    b = b + a[i]
if b == a:
    print("palindrom string")
else:
    print("not palindrom")    