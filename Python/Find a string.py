def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        ss = string[i:i + len(sub_string)]
        if ss == sub_string:
            count += 1
    return count
