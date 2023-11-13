val = int(input("ENTER A VALUE: "))
str_val = str(val)
if str_val == str_val[::-1]:
    print("IT IS A PALLINDROME!!")
else:
    print("IT IS NOT A APALLINDROME")
for i in range(10):
    if str_val.count(str(i))>0:
        print(str(i)," appears",str_val.count(str(i))," times");