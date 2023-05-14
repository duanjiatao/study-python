import re


def tt_re():
    pattern = r'\bm\w*\b'
    s = 'psoencg markting abc mark xiansge marvel'
    result = re.match(pattern, s, re.I)
    print(result)
    result = re.findall(pattern, s, re.I)
    print(result)


if __name__ == '__main__':
    tt_re()
