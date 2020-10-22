def ft_len(string):
    count = 0
    for _ in string:
        count += 1
    return count


def ft_find_char(char, string):
    if char not in string:
        return False
    for i in range(ft_len(string)):
        if string[i] == char:
            return i


def ft_slice_str(string, start, stop):
    result_string = ''
    for i in range(start, stop):
        result_string += string[i]
    return result_string


def ft_change_str(str1, str2, str3):
    if str2 not in str3:
        return False
    new_string = ft_slice_str(str3, 0, ft_find_char(str2[0], str3)) \
                 + str1 + ft_slice_str(str3, ft_find_char(str2[0], str3)
                                       + ft_len(str2), ft_len(str3))
    return new_string


def ft_remove_str(str1, str2):
    if str2 not in str1:
        return False
    new_string = ft_slice_str(str1, ft_find_char(str2[0], str1), ft_len(str2))
    return new_string


print(ft_remove_str('abck', 'ck'))
