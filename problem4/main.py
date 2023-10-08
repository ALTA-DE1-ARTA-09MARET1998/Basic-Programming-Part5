def muncul_sekali(angka):
    digit_count = {}

    for i in angka:
        if i in digit_count:
            digit_count[i] += 1
        else:
            digit_count[i] = 1

    result = [int(i) for i, count in digit_count.items() if count == 1]

    return result

if __name__ == '__main__':
    print(muncul_sekali("1234123")) # [4]
    print(muncul_sekali("76523752")) # [6, 3]
    print(muncul_sekali("12345")) # [1, 2, 3, 4, 5]
    print(muncul_sekali("1122334455")) # []
    print(muncul_sekali("0872504")) # [8, 7, 2, 5, 4]