def ft_count_words(string):
    count = 0
    for char in string.split():
        if char != '':
            count += 1
    return count
