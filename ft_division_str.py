def ft_slice_str(string, start, stop):
    result_string = ''
    for i in range(start, stop):
        result_string += string[i]
    return result_string


def ft_len(string):
    count = 0
    for _ in string:
        count += 1
    return count


def ft_division_str(string):
    if ft_len(string) % 2 == 1:
        return ft_slice_str(string, ft_len(string) // 2 + 1, ft_len(string)) \
               + ft_slice_str(string, 0, ft_len(string) // 2 + 1)

    return ft_slice_str(string, ft_len(string) // 2,
                        ft_len(string)) + ft_slice_str(string, 0, ft_len(string) // 2)
