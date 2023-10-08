def pair_sum(arr, target):
    result = []
    if target == arr[-1]:
        for i in range(len(arr)-1):
            if arr[-2] + arr[i] == target:
                result.append(i)
                result.append(len(arr)-2)
    else:
        for i in range(len(arr)-1):
            if arr[i] + arr[i+1] == target:
                result.append(i)
                result.append(i+1)
    return result if result else None

if __name__ == '__main__':
    print(pair_sum([1, 2, 3, 4, 6], 6)) # [1, 3]
    print(pair_sum([2, 5, 9, 11], 11)) # [0, 2]
    print(pair_sum([1, 3, 5, 7], 12)) # [2, 3]
    print(pair_sum([1, 4, 6, 8], 10)) # [1, 2]
    print(pair_sum([1, 5, 6, 7], 6)) # [0, 1]