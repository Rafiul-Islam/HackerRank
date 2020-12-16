s = list(s)
count = 0
while count < len(s) - 1:
    if s[count] == s[count + 1]:
        del s[count]
        del s[count]
        if count != 0:
            count -= 1
    else:
        count += 1
if len(s) == 0:
    return 'Empty String'
else:
    return "".join(s)
