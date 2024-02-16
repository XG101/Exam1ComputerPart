###############################################################################
# DONE: 1. (3 pts)
#
#   In this module, we are going to create a program that will allow a user to
#   do a simple mad lib.
#
#   If you have never heard of a mad lib before, it is a little game were one
#   person has a little short story where random words are taken out and
#   replaced with blanks and which part of speech (noun, verb, etc.) the word
#   is supposed to be. They then ask their friend for a random word that
#   matches the part of speech for each blank, they fill in the word for each
#   blank, and then they read the story with the random words filled in. Feel
#   free to look up examples of this if you wish.
#
#   First, we need a function that will ask the user for a word that is a
#   particular part of speech.
#
#   Write a function called get_word() that takes one parameter:
#       - part_of_speech    <-- str
#
#   It should prompt the user to enter a word that is the given part of speech
#   like so:
#
#       "Please enter a(n) <PART_OF_SPEECH>: "
#
#   It should then return the word that the user enters.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

def get_word(part_of_speech):
    speech = input(f"Please enter a(n) {part_of_speech}: ")
    return speech


###############################################################################
# DONE: 2. (3 pts)
#
#   Now, write a function called name() that simply asks the user to enter
#   their name and return the name they enter.
#
#   The function should prompt them lik so:
#
#       "Please enter your name: "
#
#   It should return the name that the user enters.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def name():
    user_name = input("Please enter your name: ")
    return user_name

###############################################################################
# DONE: 3. (9 pts)
#
#   Now, let's put it all together.
#
#   Write a function called main() that does these things in order (make sure
#   you use the functions you defined above and use f-strings in your
#   solution):
#
#       1. Prints "Let's play Mad Libs!"
#       2. Promps the user to enter their name and saves it to a variable.
#       3. Prints "Welcome, <USER'S_NAME>!"
#       4. Asks the user for a "noun" and saves it to a variable
#       5. Asks the user for a "verb ending in -ing" and saves it to a variable
#       6. Asks the user for an "adjective" and saves it to a variable.
#       7. Prints the mad lib below but with the words filled in that the user
#          gave.
#
#          "This semester, I hope to join the __noun__ club and go __verb 
#          ending in -ing__. It is going to be a(n) __adjective__ semester!"
#   
#   Make sure you call your main() function after you define it.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

def main():
    print("Let's play Mad Libs!")
    name()
    noun = get_word("Noun")
    verb = get_word("Verb ending in -ing")
    adjective = get_word("Adjective")
    print(f"This semester, I hope to join the {noun} club and go {verb}. It is going to be a(n) {adjective} semester!")
main()
