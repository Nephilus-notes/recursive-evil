cache_dict = {}

def fibb(num):
    if num in cache_dict:
        return cache_dict[num]

    if not isinstance(num, int):
        return "Enter positive Integer"

    result = None
    if num <= 1:
        result = num

    else:
        result = fibb(num-1) + fibb(num-2)

    cache_dict[num] = result
    return result

print(fibb(979))