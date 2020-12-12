def swap_case(s):
    newStr = ''
    for i in s:
        if(i.islower()):
            newStr += i.upper()
        else:
            newStr += i.lower()
    return newStr
