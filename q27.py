#find second largest number
l = [15,48,10,79,45,55]

largest = 0
sec_largest = 0
largestindex = 0
sec_largestindex = 0
for i in l:
    if i > largest:
        sec_largest = largest
        largest = i
      

    elif i > sec_largest:
        sec_largest = i 
      

print(f" largest value is {largest} and index {largestindex} second largest value is {sec_largest} and index {sec_largestindex}")        