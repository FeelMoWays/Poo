alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def encrypt(text, shift):
    encrypted_text = ""
    for i in text.lower():
        if i in alphabets:
            encrypted_text += alphabets[(alphabets.index(i) + shift) % 26]
    return encrypted_text

def decrypt(text,shift):
    decrypted_text = ""
    for i in text.lower():
        if i in alphabets:
            decrypted_text += alphabets[(alphabets.index(i) - shift) % 26]
    return decrypted_text

choice = input("Do You want to encrypt or decrypt: ")
if choice.lower() == "encrypt":
    text_to_be_encrypted = input("Enter Text: ")
    shift_amount = int(input("Enter The Shift Amount: "))
    print(encrypt(text_to_be_encrypted,shift_amount))
else:
    text_to_be_decrypted = input("Enter Text: ")
    shifto = int(input("Enter The Shift Amount: "))
    print(decrypt(text_to_be_decrypted,shifto))
    