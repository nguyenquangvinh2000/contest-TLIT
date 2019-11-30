def ktnt(x):
    kt = True
    for i in range(2,x):
        if x % i == 0:
            break 
    return kt 

#su dung ham de kiem tra so nguyen to
for i in range(2,100):
    if ktnt(i) == True:
        print(i)
