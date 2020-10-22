def ft_len(string):
    count = 0
    for _ in string:
        count += 1
    return count


def ft_slice_str(string, start, stop):
    result_string = ''
    for i in range(start, stop):
        result_string += string[i]
    return result_string


def ft_even_place(string):
    result_string = str()
    for i in range(ft_len(string)):
        if i % 2 == 1:
            result_string += string[i]
    return result_string


def ft_n_even_place(string):
    result_string = str()
    for i in range(ft_len(string)):
        if i % 2 == 0:
            result_string += string[i]
    return result_string


def ft_analysis(string):
    print(string[2])
    print(string[-2])
    print(ft_slice_str(string, 0, 5))
    print(ft_slice_str(string, 0, ft_len(string) - 2))
    print(ft_even_place(string))
    print(ft_n_even_place(string))
    print(ft_slice_str(string, ft_len(string), 0))
    i = 0
    while i != ft_len(string):
        if i % 2 == 0:
            print(string[ft_len(string) - i - 1], end='')
        i += 1
    print(ft_len(string))

