def find_anagrams(word, candidates):
    w = word.lower()
    o = sorted(list(w))
    k = ""
    for i in candidates:
        if w != i:
            u = sorted(list(i))
            if o == u:
                k += i
    return k

