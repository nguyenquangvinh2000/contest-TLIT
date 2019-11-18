number = int(input("Nhap vao mot so: "))
if number <= 1:
    print(number, "0")
else:
    n = 0
for i in range(1, number):
        
    if number % i == 0:
        n = i + n
    
    elif n == number:
        
        print(number, " 1")
    else:
        
        print(number, " 0")
        