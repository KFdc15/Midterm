# Kiểm tra xem có phải số nguyên tố hay không
n = int(input("Nhập số muốn kiểm tra: "))
def prime_num(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
if True == prime_num(n):
    print(n, "là số nguyên tố")
else:
    print(n, "không là số nguyên tố")
