# separate each digit of a number and print it on the new line
# reverse number
n = int(input("enter any number"))

#while n > 0:
 #   print(n % 10)
  #  n = n // 10
rev = 0

while n>0:
    rev = rev *10 + n % 10
    n = n // 10

print(rev)    
