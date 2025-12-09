year = int(input("tll your year:-"))

if year %100 == 0 and year %400 == 0:
    print("its a leap year")
elif year %100 !=0 and year %4 ==0:
    print("its a leap year")
else:
    print("your year is not leap year")        