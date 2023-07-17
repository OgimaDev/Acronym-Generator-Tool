# Script Intro Message
print("Acronym Generator Tool\nEnter any combination of words to generate the acronym for them\n")

# Request user to enter multiple word phrase
word_phrase = str(input("Enter multiple words: "))

# Split user input characters and words into single charachter seperated by a space
user_entered_text = word_phrase.split()

# Use to designate seperator
word_seperator = " "

# Run loop of user input and get first character after seperator and capitalize
for i in user_entered_text:
    word_seperator = word_seperator+str(i[0]).upper()

# print the result for user
print("\nThe words you entered created the following acronym:\n> " + word_seperator + "\n")

