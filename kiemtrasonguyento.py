number = int(input("nhap vao so nguyen: "))
if number < 2:
    print("so nhap vao phai lon hon 2")
    exit()

is_prime = True

for i in range(2, int(number / 2) + 1):
    if number % 1 == 0:
        is_prime = False
        break
if is_prime:
    print("so %d la so nguyen to" % number)
else:
    print("so %d khong phai la so nguyen to" % number)