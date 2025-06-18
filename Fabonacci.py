a = 0
b = 1
n=int(input("How many Fabonacci series number you want: "))
if n==1:
    print(1)
else:
    print(a)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)