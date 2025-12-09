def palindrom(str):
    rev = ""
    for i in range(len(str)-1,-1,-1):
        rev = rev + str[i]

    if rev == str:
        print("its palindrom")

    else:
        print("not palindrom") 

palindrom("naman")
palindrom("sunny")       



