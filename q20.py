a = "sdfso123@54#@&%tmn897"

char = 0
dig = 0
spchar = 0

for i in a:
    if i.isdigit():
        dig +=1
    elif i.isalpha():
        char +=1
    else:
        spchar +=1

print(f"your digits are {dig}\n your spchar{spchar}\n your alphabets are {char}")            
