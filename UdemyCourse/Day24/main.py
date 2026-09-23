#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
with open(r"UdemyCourse\Day24\Input\Letters\starting_letter.txt",mode='r') as starting_file:
    template = starting_file.read()
with open(r'UdemyCourse\Day24\Input\Names\invited_names.txt') as reading_file:
    names = reading_file.readlines()
for i in names:
    i = i.strip('\n')
    replaced_letter = template.replace('[name]',i)
    with open(f"UdemyCourse\Day24\Output\ReadyToSend\{i}.txt",mode='w') as file:
        file.write(replaced_letter)
        