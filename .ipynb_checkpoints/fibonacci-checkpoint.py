def fib(n, memo={}):
    if n <= 1:
        return n
    
    if n not in memo:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    
    return memo[n]
        
if __name__ == '__main__':
    input_number = int(input())
    print(fib(input_number, memo ={}))