def pos(n):
    n -= 1
    while n >= 0:
        print(n, end=' ')
        n -= 1

def neg(n):
    while n<=0:
        print(n, end=' ')
        n += 1

n = int(input("Enter the number: "))
if n<0:
    neg(n)
else:
    pos(n)