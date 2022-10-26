def sum_in_array(ar: list, S):
    i = 0
    j = len(ar) - 1
    while True:
        s = ar[i] + ar[j]
        if s == S:
            return ar[i], ar[j]
        elif s > S:
            j -= 1
        elif s < S:
            i += 1
        if i == j:
            return [-1]


if __name__ == '__main__':
    print(
        sum_in_array(ar=[-3, 1, 4, 6], S=7),
        sum_in_array(ar=[-3, 1, 4, 6], S=8)
    )


