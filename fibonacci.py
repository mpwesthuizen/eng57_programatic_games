# create a fibonacci.py calculator

def fib():
    sub2 = 0
    sub1 = 1
    nxt = 1
    num = int(input("How many numbers of the fibonacci.py sequence do you want to see? "))
    for x in range(1, num + 1):
        print(nxt)
        nxt = sub1 + sub2
        sub2 = sub1
        sub1 = nxt

print(fib())