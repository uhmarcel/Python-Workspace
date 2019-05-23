# Example of functions

def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2) 

print ('Fibonacci sequence:')
x = input()

print ('fib(' + x + ') = ' + str(fib(int(x))))
