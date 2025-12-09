#print all the sum of all even number and odd number in range separetly
n = int(input("tell your number"))
even = 0
odd = 0
for i in range(1,n+1,):
    if i%2 == 0:
        even = even + i
    else:
        odd = odd +i

print(f"the sum of even and odd number is {even} , {odd}")            