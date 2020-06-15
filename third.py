def get_zeros(n):
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    print(factorial)
    control_sum = 0
    for i in reversed(str(factorial)):
        if str(i) == '0':
            control_sum += 1
        else:
            print(control_sum)
            break
get_zeros(5)
get_zeros(12)





