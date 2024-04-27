def last_digit_of_fibonacci(n):
    """Finds the last digit of the nth Fibonacci number efficiently."""

    # Precompute the last digits of the first 60 Fibonacci numbers
    fib_last_digits = [0, 1] + [0] * 58
    for i in range(2, 60):
        fib_last_digits[i] = (fib_last_digits[i - 1] + fib_last_digits[i - 2]) % 10

    # Use the Pisano period to efficiently find the last digit
    return fib_last_digits[n % 60]

if __name__ == '__main__':
    input_number = int(input())
    print(last_digit_of_fibonacci(input_number))

