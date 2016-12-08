import random

# array-shuffler via built-in random function
def shuffle(array):
    rand_array = []
    rand_array.append(random.shuffle(array))
    print array
    return array

string_array1 = ['how', 'now', 'brown','cow', 'bow', 'plow', 'wow', 'clown']
shuffle(string_array1)

# array-shuffler self-written
def rearrange(array):
    rand_array = []
    for index in range(0, len(array)):
        rand_index = random.randint(0, len(array) - 1)
        rand_array.append(array[rand_index])
        array.pop(rand_index)
    print rand_array
    return rand_array

string_array2 = ['how', 'now', 'brown','cow', 'bow', 'plow', 'wow', 'clown']
rearrange(string_array2)

# string reversal via slicing
def reverse1(string):
    reverse_string = string[::-1]
    print reverse_string
    return reverse_string

string1 = "the quick brown fox jumps over the lazy dog"
reverse1(string1)

#string reversal self-written
def reverse2(string):
    reverse_string = ""
    for index in range(0, len(string)):
        reverse_string += string[len(string)-1-index]
    print reverse_string
    return reverse_string

string2 = "the quick brown fox jumps over the lazy dog"
reverse2(string2)

#madlibs
def madlibs():
    quick = raw_input("Enter verb: ")
    brown = raw_input("Enter color: ")
    jumps = raw_input("Enter verb: ")
    dog = raw_input("Enter animal name: ")
    string = "the " + quick + " " + brown + " fox " + jumps + " over the lazy " + dog
    print string
    return string

madlibs()
