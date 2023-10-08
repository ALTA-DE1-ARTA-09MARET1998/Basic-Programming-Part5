def join_array_remove_duplicate(arrayA, arrayB):
    # your code here
    result = []

    for elem in arrayA:
        if elem not in result:
            result.append(elem)

    for elem in arrayB:
        if elem not in result:
            result.append(elem)

    return result

if __name__ == '__main__':
    # Test cases
    print(join_array_remove_duplicate(["apel", "anggur"], ["lemon", "leci", "nanas"]))
    # ["apel", "anggur", "lemon", "leci", "nanas"]


    print(join_array_remove_duplicate(["samsung", "apple"], ["apple", "sony", "xiaomi"]))
    # ["samsung", "apple", "sony", "xiaomi"]


    print(join_array_remove_duplicate(["football", "basketball"], ["basketball", "football"]))
    # ["football", "basketball"]
