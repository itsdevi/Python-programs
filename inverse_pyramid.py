def print_inverse_pyramid(limit):
    for i in range(limit, 0, -1):
        print(" " * (limit - i) + "*" * (2 * i - 1))

print_inverse_pyramid(5)
