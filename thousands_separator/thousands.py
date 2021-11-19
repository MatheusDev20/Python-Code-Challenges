def group(number):
    p = str(number)
    s = '%d' % number
    print(p)
    print(s)
    groups = []
    while s and s[-1].isdigit():
        print(s[-3:])
        groups.append(s[-3:])
        s = s[:-3]

    return s + ','.join(reversed(groups))

print(group(-23432432434.34))
