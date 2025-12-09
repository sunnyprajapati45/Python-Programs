#palinrom number
n = int(input("enter any number"))
copy = n

rev = 0

while n>0:
    rev = rev * 10 + n % 10
    n = n // 10

if copy == rev :
    print("its palindrom number") 

else:
    print("not palindrom")      