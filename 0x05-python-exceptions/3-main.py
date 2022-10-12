test3 = __import__('3-safe_print_division').safe_print_division

a = 12
b = 2
result = test3(a, b)
print("{:d} / {:d} = {}".format(a, b, result))
