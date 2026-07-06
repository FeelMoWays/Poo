def rotate(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')

            shifted = (ord(char) - start + key) % 26 + start
            result += chr(shifted)
        else:
            result += char

    return result
print(rotate("H E L L O",10))