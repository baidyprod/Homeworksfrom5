def your_zip(*iterables):
    res = []  #Result list
    list_not_final = []  #List which will be fullfilled with n-indexed elements from each iterable
    b = [*iterables]  #Variable b is a list of different iterables of different types
    a = tuple([list(word) for word in b])  #Variable "a" becomes a tuple of iterables converted to lists
    e = tuple([list(word) for word in b])  #Variable "e" is the same as "a" but has different id (e = a[:] and e = a.copy() don't work idk why :/)
    for item in e:  #Next three lines convert each digit in "e" list of list to a string. We need to do this because function min (3 lines lower) doesn't work without this.
        for digit in item:
            item[item.index(digit)] = str(digit)
    list_of_length = []  #Next 4 lines we need to count the shortest iterable which was input
    for item in e:
        list_of_length.append(len(item))
    minimum = min(list_of_length)
    for i in range(minimum):  #"i" takes the index of item in iterable
        for o in range(len(a)):  #"o" takes the index of iterable
            list_not_final.append((a[o][i]))  #List_not_final is being appended by items of same index in different iterables
        res.append(tuple(list_not_final))  #Result list is being appended by the previous list, converted into tuple
        list_not_final = []  #List_not_final is being cleared before the next repeat of main loop
    return res  #After all iterations our function returns the result list