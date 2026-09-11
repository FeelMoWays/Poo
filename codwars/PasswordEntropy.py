import math
import string as st

def entropy(password):
    pool = 0

    if any(c in st.ascii_lowercase for c in password):
        pool += 26

    if any(c in st.ascii_uppercase for c in password):
        pool += 26

    if any(c in st.digits for c in password):
        pool += 10

    if any(c in st.punctuation for c in password):
        pool += len(st.punctuation)

    E = len(password) * math.log2(pool)

    return E
# ChatGPT Answer Use any to check if any part of the string belongs to the letters
