def print_pyramid(limit):
    for i in range(1, limit + 1):
        print(" " * (limit - i) + "*" * (2 * i - 1))

print_pyramid(5)
