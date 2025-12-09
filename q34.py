#count the frequency of each element list

l = [10,10,10,10,20,200,30,30,30,40,40]
d = {}
for i in l:
    if i in d.keys():
        d[i]+=1

    else:
        d[i] = 1    

print(d)        

