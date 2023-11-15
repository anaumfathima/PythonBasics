def oct2hex(val):
    rev=val[::-1]
    dec=0
    i=0
    for dig in rev:
        dec+= int(dig)*8**i
        i+=1
    list=[]
    while dec!=0:
        list.append(dec%16)
        dec=dec//16
    n1=[]
    for elem in list[::-1]:
        if elem<=9:
            n1.append(str(elem))
        else:
            n1.append(chr(ord('A')+(elem-10)))
    hex= "".join(n1)
    return hex

num2 = input("ENTER A OCTAL NUMBER: ")
print(oct2hex(num2))