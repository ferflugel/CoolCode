''' Print out all permutations '''

def permutations(string):

    if len(string) == 0:
        return ['']

    perm = []
    for char in string:
        for subper in permutations(string.replace(char, "")):
            perm.append(char + subper)
    return perm

# print(permutations("abc"))


''' Print out all combinations '''

def combinations(lst):
    if len(lst) == 1:
        return [[], lst]
    return combinations(lst[1:]) + elementwise_addition(combinations(lst[1:]), lst[0])

def elementwise_addition(lst, elem):
    for sublst in lst:
        sublst += [elem]
    return lst

#print(combinations([1, 2, 3]))