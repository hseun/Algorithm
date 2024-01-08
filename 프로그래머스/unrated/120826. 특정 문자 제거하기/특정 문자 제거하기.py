def solution(my_string, letter):
    for i in range(my_string.count(letter)):
        a = my_string.index(letter)
        my_string = my_string[:a] + my_string[a + 1:]
    return my_string