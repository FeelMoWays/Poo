def add_prefix_un(word):
    return "".join(["un", word])


def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    words = [prefix]

    for word in vocab_words[1:]:
        words.append("".join([prefix, word]))

    return " :: ".join(words)


def remove_suffix_ness(word):
    word = word.removesuffix("ness")

    if word.endswith("i"):
        return "".join([word[:-1], "y"])

    return word


def adjective_to_verb(sentence, index):
    words = sentence.split()
    adjective = words[index].rstrip(".,!?")
    return "".join([adjective, "en"])