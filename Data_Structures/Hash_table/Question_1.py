# Return the first recurring character

def rec_char(array):
    values = {}
    for i in range(len(array)):
        if array[i] in values:
            return array[i]
        else:
            values[array[i]] = i

    print(values)
    return 0
        



print(rec_char([1,3,5,4,7,8,0]))