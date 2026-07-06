import string as st
# def is_pangram(sentence):
#     lst = []
#     sentence = sentence.lower()
#     sentence = sentence.replace(" ","")
#     for i in sentence:
#         if i in st.ascii_lowercase:
#             if i not in lst:
#                 lst.append(i)
#     if len(lst) == 26:
#         return True
#     return False
def is_pangram(sentence):
    letters = {char for char in sentence.lower() if char in st.ascii_lowercase}
    return len(letters) == 26
