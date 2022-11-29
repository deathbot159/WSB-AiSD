s1 = 'ala ma kota'
s2 = 'aoiuyem'


def magic(str1, str2):
    ile = 0
    chars = list(str1)
    for a in str1:
        for b in str2:
            if a == b:
                ile += 1
    return ile


print(magic(s1, s2))
