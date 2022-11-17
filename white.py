# smallest number in list

# [50,30,4,2,11,0]
# [40,3,4,2]


# def small(a_list):
#     return min(a_list)

def small(a_list):
    return sorted(a_list)[0]

print(small([50,30,4,2,11,0]))
print(small([40,3,4,2]))


def smaller(a_list):
    smaller = a_list[0]
    for num in a_list:
        if num < smaller:
            smaller = num

    return smaller

def smaller_sqrd(a_list):
    b = set(a_list)
    smaller = 10*100
    for el in b:
        if el < smaller:
            smaller = el
    return smaller

# print(smaller_sqrd([50,30,4,2,11,0]))
# print(smaller_sqrd([40,3,4,2]))

# print(smaller([50,30,4,2,11,0]))
# print(smaller([40,3,4,2]))