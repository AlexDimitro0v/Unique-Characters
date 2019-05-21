"""
_______________________________________________________________________________
Implement an algorithm to determine if a string has all unique characters.
_______________________________________________________________________________
Notes:
1. with hash map
2. nxn
3. sort and compare
time complexity, memory
O(n^2)
_______________________________________________________________________________
"""


def all_unique_characters(string):
    alphabet = {}
    for char in string:
        if char in alphabet:
            alphabet[char] += 1
        else:
            alphabet[char] = 1

        for x in alphabet.values():
            if x > 1:
                return False
    return True


def all_unique_characters2(string):
    for char in string:
        if string.count(char) > 1:      # count is O(n)
            return False
    return True


def all_unique_characters3(string):
    string = ''.join(sorted(string))
    for i, char in enumerate(string[:-1]):
        if char == string[i + 1]:
            return False
    return True


if __name__ == '__main__':
    strings = ['I love playing rugby',
               'superb',
               'How are you?',
               'uniQ',
               'not unique'
               ]
    print(strings)

    print('\n 1. with hash map')
    print([*map(all_unique_characters, strings)])   # the star is used for unpacking
    print('\n 2. nxn')
    print([*map(all_unique_characters2, strings)])
    print('\n 3. sort and compare')
    print([*map(all_unique_characters3, strings)])
