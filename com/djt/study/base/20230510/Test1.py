def calc_error(a, b):
    quotient = a // b
    product = quotient * b
    error = product - a
    return error


if __name__ == '__main__':
    print(calc_error(101, 10))
