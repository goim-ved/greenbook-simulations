def count_trailing_zeros(n):
    count = 0
    divisor = 5

    while divisor <= n:
        count += n // divisor
        divisor *= 5

    return count


n = int(input("Enter a number: "))
result = count_trailing_zeros(n)
print(f"Number of trailing zeros in {n}! is: {result}")
