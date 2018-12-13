def is_ascii(s):
    return all(ord(c) < 128 for c in s)


def checkio(pw):
    if is_ascii(pw) == True:
        if 9 < len(pw) <= 64:
            upper = 0
            lower = 0
            num = 0

            for c in pw:
                if c.isupper():
                    upper += 1
                elif c.islower():
                    lower += 1
                elif c.isdigit():
                    num += 1

            if upper != 0 and lower != 0 and num != 0:
                print( True)

            else:
                print( False)

        else:
            print( False)
    else:
        print( False)



# Testing
# checkio('A1213pokl') == False
# checkio('bAse730onE') == True
# checkio('asasasasasasasaas') == False
# checkio('QWERTYqwerty') == False
# checkio('123456123456') == False
# checkio('QwErTy911poqqqq') == True


checkio('A1213pokl')
checkio('bAse730onE')
checkio('asasasasasasasaas')
checkio('QWERTYqwerty')
checkio('123456123456')
checkio('QwErTy911poqqqq')