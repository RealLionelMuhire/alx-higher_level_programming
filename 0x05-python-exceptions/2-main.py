safe_print_list_integers = __import__('2-safe_print_list_integers').safe_print_list_integers
my_list = [1, 2, 2, 4,"hello", 5, 5]
rar = safe_print_list_integers(my_list, 7)
print("{}".format(rar))
