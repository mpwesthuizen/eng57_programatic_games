# How to remove list duplicates using sets
def no_dup(old_list):
    new_list = []
    for arg in old_list:
        new_list.append(arg)
    return list(set(new_list))

def no_dupe_alt(list1):
    list2 = []
    for item in list1:

        if item not in list2:
            list2.append(item)

    return list2

test = [1, 1, 1, 1, 2, 3, 3, 1, 1]
str_test = ['a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'e']

print(no_dupe_alt(test))
print(no_dupe_alt(str_test))
