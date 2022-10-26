import re


def lucky(sting: str):
    l = re.findall(r'[56]+', sting)
    l.sort(key=lambda x: len(x), reverse=True)
    for i in l:
        if '5' in i and '6' in i:
            return i
    return 0


if __name__ == '__main__':
    print(
        lucky('4556432455665334'),
        lucky('5656556565'),
    )
