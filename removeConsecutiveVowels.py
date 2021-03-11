def is_vowel(ch):
    return (ch == 'a') or (ch == 'e') \
           or (ch == 'i') or (ch == 'o') \
           or (ch == 'u')

def removeConsecutiveVowels(inputString: string) -> string:
    str1 = "" + inputString[0]
    for i in range(1, len(inputString)):
        if (is_vowel(inputString[i - 1])) and (not is_vowel(inputString[i])):
            ch = inputString[i]
            str1 = str1 + ch
        if (not(is_vowel(inputString[i-1]))):
            ch = inputString[i]
            str1 = str1 + ch
    return str1
