def to_freud(sentence):
    result = " ".join("sex" for word in sentence.split())
    return result
u = to_freud("Hello")
print(u)