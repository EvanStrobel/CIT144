def createRandomWord():
    strWord = ""
    import random
    lstWords = ["banjo","azure","absurd","awkward","blitz",
                "espionage","dwarves","galaxy","glyph",
                "lucky","microwave","jumbo","oxygen",
                "puppy","sphinx","strength","quiz",
                "python","voodoo","wyvern","zombie",
                "wizard","pajama","vodka","mnemonic"]
    random.shuffle(lstWords)
    strWord = lstWords[1]
    return(strWord)

def letterGuess(): #Takes strWord as a parameter
    strWord = createRandomWord()
    guessLimit = 0
    while guessLimit < 10: # 10 is a placeholder amount of guesses
        #Repeats this loop an amount of times equal to the guess limit
        guess = input("Guess a letter then press enter: ")
        if guess in strWord:
            print("Your guess was correct!")
            # Here would be code that inserts the correct guess into the
            # appropriate space in the word.
        else:
            print("That letter is not in the word.")
            guessLimit += 1
            # Here would be code that adds another section onto
            # the hangman for incorrectly guessing.
        
letterGuess()
