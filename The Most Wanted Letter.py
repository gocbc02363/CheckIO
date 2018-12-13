def checkio(str):

    count = {}
    stri = ''.join(e for e in str if e.isalnum())
    strii = ''.join(e for e in stri if not e.isdigit())

    for c in strii.lower():
        if count.get(c) != None:
            count[c] += 1
        else:
            count[c] = 1

    mac = [k for k, v in count.items() if v == max(count.values())]
    return print(min(mac))



# Example:
#
# checkio("Hello World!") == "l"
# checkio("How do you do?") == "o"
# checkio("One") == "e"
# checkio("Oops!") == "o"
# checkio("AAaooo!!!!") == "a"
# checkio("abe") == "a"


checkio("Hello World!")
checkio("How do you do?")
checkio("One")
checkio("Oops!")
checkio("AAaooo!!!!")
checkio("abe")
checkio('one')
checkio('Lorem ipsum dolor sit amet 0000000000000000000')