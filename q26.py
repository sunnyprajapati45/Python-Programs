 #find greatest number
l = [15,56,89,85,4,789,8999,8548]

largest = l[0]
index = 0
for i in range(len(l)):
    if l[i] > largest:
        largest = l[i]
        index = i

print(f"your largest number is {largest} at index {index}")        