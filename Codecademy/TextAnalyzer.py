def text(sentence):
    vowels = ['a','e','i','o','u']
    vowel_count = 0
    consonant_count = 0
    word_count = 0
    reversed_string = ""
    print(f"The total number of characters in the given sentence are {len(sentence)}")
    print(f"The total number of words in the given sentence are {len(sentence.strip().split())}")

    for i in sentence:
        if i.isalpha():
            if i in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    print(f"The number of vowels in the given sentence are {vowel_count}")
    print(f"The number of consonants in the given sentence are {consonant_count}")

    reversed_string = sentence[::-1]
    print(f"The reversed string is {reversed_string}")

    if sentence == reversed_string:
        print("The given sentence is a Palindrome")
    else:
        print("The given sentence is not a Palindrome")

choice = input("Do you want to use our Text Analyzer 3000: ").lower()
if choice == 'yes':
    sentence_input  = input("Enter you sentence which you want to be analyzed: ")
    text(sentence=sentence_input)
else:
    print("Thank you for coming by") 