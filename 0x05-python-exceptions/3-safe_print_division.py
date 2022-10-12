def safe_print_division(a, b):
    try:
        div = a/b
    except (ZeroDivisionError, TypeError):
        none
    finally:
        print("Inside result: {}".format(div))
    return div
