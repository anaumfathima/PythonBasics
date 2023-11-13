m1 = int(input("ENTER THE MARKS OF TEST1: "))
m2 = int(input("ENTER THE MARKS OF TEST2: "))
m3 = int(input("ENTER THE MARKS OF TEST3: "))
if m1<=m2 and m1<=m3:
    avg = (m2+m3)/2
elif m2<=m1 and m2<=m3:
     avg = (m1+m3)/2
elif m3<=m1 and m3<=m2:
     avg = (m2+m1)/2
print("The average of best of 2 test marks out of 3 test is ",avg)