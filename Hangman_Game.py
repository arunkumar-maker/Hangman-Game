import random
def hangman():
    list_of_words=['arun','tharun','apple','banana']
    word=random.choice(list_of_words)
    turns=10
    guessmade=''
    valid_entry=set('abcdefghijklmnopqrstuvwxyz')
# this loop will run when we define some valid word which is more than a letter
    while len(word)>0:
        main_word=""

        for letter in word:
            if letter in guessmade:
                main_word=main_word+letter
            else:
                main_word=main_word+'_  '     # to print dashes("_") for not yet guessed word

# main_word is the word which we are guessing right now

        if main_word == word:
            print("so the final word is ",main_word)
            print("Hurrah!!!")
            print("You Won!!!!")
            break
        print("Guess the word ",main_word)

# to make sure that the user is entering a valid letter to hunt the word
        guess=input()
        if guess in valid_entry:
            guessmade=guessmade+guess
        else:
            print("Enter valid character")
            guess = input()
        # hangman starts from here
        if guess not in word:
            turns=turns-1

            if turns==9:
                print("You are left with 9 turns !!!")
                print("-------------")
            if turns==8:
                print("You are left with 8 turns !!!")
                print("-------------")
                print("      o      ")
            if turns==7:
                print("You are left with 7 turns !!!")
                print("-------------")
                print("      o      ")
                print("      |      ")
            if turns==6:
                print("You are left with 6 turns !!!")
                print("-------------")
                print("      o      ")
                print("      |      ")
                print("     /       ")
            if turns==5:
                print("You are left with 5 turns !!!")
                print("-------------")
                print("      o      ")
                print("      |      ")
                print("     / \     ")
            if turns==4:
                print("You are left with 4 turns !!!")
                print("-------------")
                print("     \o      ")
                print("      |      ")
                print("     / \     ")
            if turns==3:
                print("You are left with 3 turns !!!")
                print("-------------")
                print("     \o/     ")
                print("      |      ")
                print("     / \     ")
            if turns==2:
                print("You are left with 2 turns !!!")
                print("-------------")
                print("     \o/ |    ")
                print("      |      ")
                print("     / \     ")
            if turns==1:
                print("You are left with 1 turn !!!")
                print("Hangman is on last breath")
                print("Please don't kill him")
                print("-------------")
                print("         |    ")
                print("      o _|    ")
                print("     /|\      ")
                print("     / \     ")
            if turns==0:
                print("You lost the game")
                print("you let a good man die")
                break                

name=input("Enter your name :")
print("Welcome",name,"!!!")
print("------------------------")
print("Try to guess the word in lessthan 10 chances")
hangman()
