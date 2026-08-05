count = 0
def analyze_recursive_iterative(n):
    def rec_factorial(n):
        if n==0 or n==1:
            return n
        else:
            return n *rec_factorial(n-1)
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    global count
    count=0
    def rec_fibonacci(n):
        global count
        count+=1
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return rec_fibonacci(n-1) + rec_fibonacci(n-2)
    rec_fib = rec_fibonacci(n)
    if n==0:
        iter_fib = 0
    elif n==1:
        iter_fib = 1
    else:
        a, b = 0,1
        for i in range(2,n+1):
            a, b = b, a+b
        iter_fib = b
    return ['Computation Analysis Report',
            f'Recursive Factorial: {rec_factorial (n)}',
            f'Iterative Factorial: {fact}',
            f'Recursive Fibonacci: {rec_fib}', 
            f'Iterative Fibonacci: {iter_fib}', 
            'Operation Count Comparison', 
            f'Recursive Factorial Count: {n+1}', 
            f'Iterative Factorial Count: {n}', 
            f'Recursive Fibonacci Count: {count}', 
            f'Iterartive Fibonacci Count: {n}']
n = 5