def fibonacci(n):
    if n <= 1:
        return 1
    else:
        a = fibonacci(n-2) + fibonacci(n - 1)
        return a
        
if __name__ == '__main__':
    input_number = int(input())
    print(fibonacci(input_number))