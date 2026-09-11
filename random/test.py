def solution(s):
    if len(s) % 2 != 0:
        s = s + "_"
    n = 2
    out = [(s[i:i+n]) for i in range(0, len(s), n)] 
    return out

o = solution("koi")
print(o)