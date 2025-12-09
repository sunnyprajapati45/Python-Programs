#calculate factor
n = int(input("tell your number"))

for i in range(1,n+1):
    if n%i == 0:
        print(i)