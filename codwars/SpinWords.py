def spin_words(sentence):
    split_sentence = sentence.strip().split()
    reversed_list = []
    for i in split_sentence:
        if len(i) >= 5:
            reversed_list.append(i[::-1]) 
        else:
            reversed_string.append(i) 
    return " ".join(reversed_list)
print(spin_words("Welcome"))
