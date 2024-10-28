def get_multiplied_digits(number):
    str_number = str(number)
    result = 1
    while number > 0:
        digit = number % 10
        if digit != 0:
            result *= digit
        number //= 10
    return result
    if len(str_number) > 1:
        first = int(str_number[0])
        return first * get_multiplied_digits(int(str_number[1:]))
    elif len(str_number) < 1:
        com
    else:
        return int(str_number)

result = get_multiplied_digits(40203)
print(result)