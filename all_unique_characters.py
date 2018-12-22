'''
_______________________________________________________________________________
Implement an algorithm to determine if a string has all unique characters.
What if you can not use additional data structures?
_______________________________________________________________________________
Notes:
1. with hash map
2. nxn
3. sort and compare
time complexity, memory
O(n) =
_______________________________________________________________________________
 '''


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
        if string.count(char) > 1:
            return False
    return True


def all_unique_characters3(string):
    string = ''.join(sorted(string))
    alex = string[:-1]
    for i, char in enumerate(string[:-1]):
        if char == string[i + 1]:
            return False
    return True


if __name__ == '__main__':
    strings = ['az obicham mach i boza',
               'superb',
               'Kakv0 st@va?',
               'уникат',
               'уникатт'
               ]
    print(strings)

    print('\n 1. with hash map')
    print([*map(all_unique_characters, strings)])
    print('\n 2. nxn')
    print([*map(all_unique_characters2, strings)])
    print('\n 3. sort and copmare')
    print([*map(all_unique_characters3, strings)])
