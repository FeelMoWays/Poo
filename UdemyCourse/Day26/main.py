import pandas as pd

#TODO 1. Create a dictionary in this format:
data = pd.read_csv(r'D:\Poo\UdemyCourse\Day26\nato_phonetic_alphabet.csv')
data_dict = {}
for (key,value) in data.iterrows():
    data_dict[value.letter.lower()] = value.code
print(data_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def Nato():
    string = input('Enter the word you want to learn the nato alphabet of: ').lower()
    ls = []
    for i in string:
        ls.append(data_dict[i])
    return ls
print(Nato())
