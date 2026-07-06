def translate(text):
    vowels = ("a", "e", "i", "o", "u")

    def translate_word(word):
        # Rule 1: starts with vowel, "xr", or "yt"
        if word.startswith(vowels) or word.startswith(("xr", "yt")):
            return word + "ay"

        # Rule 3: starts with zero or more consonants followed by "qu"
        qu_index = word.find("qu")
        if qu_index != -1:
            prefix = word[:qu_index]
            if all(char not in vowels for char in prefix):
                split_index = qu_index + 2
                return word[split_index:] + word[:split_index] + "ay"

        # Rule 4: starts with consonants followed by "y"
        for index, char in enumerate(word):
            if char == "y":
                return word[index:] + word[:index] + "ay"

            if char in vowels:
                # Rule 2: starts with consonants followed by a vowel
                return word[index:] + word[:index] + "ay"

        return word + "ay"

    return " ".join(translate_word(word) for word in text.split())
