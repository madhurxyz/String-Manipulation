import random

# array-shuffler via built-in random function
def shuffle(array):
    rand_array = []
    rand_array.append(random.shuffle(array))
    print array
    return array

string_array1 = ['how', 'now', 'brown','cow', 'bow', 'plow', 'wow', 'clown']
shuffle(string_array1)
