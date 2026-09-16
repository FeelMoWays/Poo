string  = 'abcdefghijklmnopqrstuvwxyz'
straight_list  = list(string)
reverse_list = straight_list[::-1]

def encode(plain_text):
    encode_text = ""
    for i in plain_text.lower():
        if i.isalpha():
            encode_text += reverse_list[straight_list.index(i)]
        else:
            encode_text += i
    return encode_text

def decode(ciphered_text):
    decode_text = ""
    for i in ciphered_text.lower():
        if i.isaplha():
            decode_text += straight_list[reverse_list.index(i)]
        else:
            decode_text += i
    return decode_text
print(encode("Testing,1 2 3, testing."))