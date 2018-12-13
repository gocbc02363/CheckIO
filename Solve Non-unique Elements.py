def checkio(list):
    lst = list
    count = {}
    for c in lst:
        if count.get(c) != None:
            count[c] += 1
        else:
            count[c] = 1
    for k in count:
        if count[k] == 1:
            lst.remove(k)

    return lst

# if __name__ == "__main__":
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
#     assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
#     assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
#     assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
#     print("It is all good. Let's check it now")


checkio([1,2,3,1,3])
checkio([1, 2, 3, 4, 5])
checkio([5, 5, 5, 5, 5])
checkio([10, 9, 10, 10, 9, 8])