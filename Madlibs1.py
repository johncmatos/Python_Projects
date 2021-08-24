import random   # Allows the program to pick a element randomly.
namesList = ['Davy Jones', 'Spongebob', 'Obama', 'Mr.pickles', 'Beyonce', 'Naruto', 'Goku', 'Elon Muskratt',
            'Elon Musk',
            'Morty', 'Rick']    # List of names.
while True:
    nameIndex = random.choice(namesList)    # Creates a variable so that a randomly picked element from the list,
    # can be used.
    name = nameIndex    # A variable to hold the element that was randomly chosen by the program.
    verb = input('Enter a verb -->')    # User enters a verb.
    adjective = input('Enter an adjective -->')     # User enters an adjective.
    noun = input('Enter a noun -->')    # User enters a noun.

    sentence = name + ' ' + verb + ' through the city, hoping to escape the ' + adjective + ' ' + noun + '.'
    print()     # Spacing between texts.
    print(sentence)     # The program presents the output.
    print()     # Spacing between texts.

    answer = input('Type "q" to quit, or anything else to continue: ')      # User has a choice to continue,
    # or quit program.
    if answer == 'q':
        break   # If user hits the q key, the program will exit the loop ending the program.

print('Bye.')
