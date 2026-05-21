def count_consonants(text):
    lst =[]
    for i in text.lower():
        if i.isalpha() and i not in ["a","e","i","o","u"]:
            if i not in lst:
                lst.append(i)
    return len(lst)
print(count_consonants("jioaeiou!!!!!"))
