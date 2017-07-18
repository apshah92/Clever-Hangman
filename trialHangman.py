'''
Created on Nov 27, 2016

@author: Arpan Shah
'''
import random

DEBUG=False

def fileToStringList(filename):
    """
    filename is a file of strings, 
    returns a list of strings, each string represents
    one line from filename
    """
    wordlist = []
    f = open(filename)
    for line in f:
        line = line.strip()
        wordlist.append(line)
    f.close()
    return wordlist
    
     
def getPossibleWords(wordlist,length):
    """
    returns a list of words from wordlist having a 
    specified length 
    """
    fixed_length_words=[]
    for word in wordlist:
        if len(word)==length:
            fixed_length_words.append(word)
    return fixed_length_words

def displayGuess(wordList):
    '''
    wordList is a list of characters with letters correctly
    guessed and '_' for letters not quessed yet
    returns the list as a String
    '''
    return ' '.join(wordList)

def guessStart(word):
    '''
    returns a list of single characters '_' the
    same size as word
    '''
    return ['_']*len(word)

def updateLetter(guessList,wordToGuess, letter):
    '''
    wordToGuess is the word the user is trying to guess.
    guessList is the word to guess as a list of characters, but
    only including the letters the user has guessed and showing
    the character '_' if a letter hasn't been guessed yet.
    letter is the current letter the user has guessed. 
    
    Modify guessList to include letter in its proper locations if 
    letter is in wordToGuess.
    
    For example, if the wordToGuess is "baloney" and so far only a and
    e have been guessed, then guessList is ['_','a','_','_','_','e','_']
    If letter is 'o', then guessList is modified to now be:
    ['_','a','_','o','_','e','_']
    
    '''
    letter=letter.lower()
    count=wordToGuess.count(letter)
    start_index=0

    while count!=0:
            index=wordToGuess.find(letter,start_index)
            guessList[index]=letter
            start_index=index+1
            count=count-1           
                
    
            
def playGame(words):
    '''
    Play the game. Let the user know if they won or not.
    '''
    #setup for game

    print "Welcome to hangman"
    while True:
            guessLength = int(raw_input("how many letters in word to guess? "))
            if guessLength < 3:
                print "length word must be greater than 2,please enter again"
            else:
                break

        
    misses_left=int(raw_input("how many wrong letter guesses? "))
    
    possibleWords = getPossibleWords(words,guessLength)    
    wordToGuess = random.choice(possibleWords)
    guessList = guessStart(wordToGuess)


    
    
    alphabet='abcdefghijklmnopqrstuvwxyz'
    lettersguessed = ""

    Winner=False

    
    # start the guessing
    while True:
        print wordToGuess
        if guessList.count('_') == 0 or misses_left==0:        # all letters guessed or ran out of guesses
            break
        print "guessed so far: ", displayGuess(guessList)
        
        
        letter = raw_input("guess a letter or press + to guess word: ")    # Arpan....To Do add condition for single letter input only if needed

        if letter=='+':
            user_word=raw_input("enter word: ")
            if user_word==wordToGuess:
                Winner=True
                break
            else:
                Winner=False
                break

        
        else:    
            dictionary_of_templates={}
            for word in possibleWords:
                key=""
                for character in word:
                    if character==letter or character in lettersguessed:
                        key=key+character
                        lettersguessed += letter
                    if character not in lettersguessed:
                        key=key+"_"
                        

                if key not in dictionary_of_templates.keys():
                    dictionary_of_templates[key]=[word]
                else:
                    dictionary_of_templates[key].append(word)                   

            max_category_words=0
            
            
            same_number_words_key = []
            no_of_letters=[]
            
            for key in dictionary_of_templates.keys():
                if len(dictionary_of_templates[key])>max_category_words:                    
                    max_category_words=len(dictionary_of_templates[key])
            
            for key in dictionary_of_templates.keys():
                if len(dictionary_of_templates[key])==max_category_words:
                    same_number_words_key.append(key)

            
            for each in same_number_words_key:
                    count=each.count(letter)
                    no_of_letters.append(count)
            min_letters=min(no_of_letters)
            index_of_key=no_of_letters.index(min_letters)
            
            key=same_number_words_key[index_of_key]
            possibleWords=dictionary_of_templates[key]
            
            
                    

            wordToGuess=random.choice(possibleWords)

            if DEBUG==True:
                print "Dictionary of categories and # of words:"
                for key in dictionary_of_templates.keys():
                    print key,len(dictionary_of_templates[key])
                print "(secret word:",wordToGuess,") # words possible ",len(possibleWords)
            
            if letter in wordToGuess:
                    print "You guessed a letter"
                    alphabet=alphabet.replace(letter,'')
                    updateLetter(guessList, wordToGuess, letter)
                    

                    
            else:
                    print "That's a miss"
                    misses_left=misses_left-1
                    alphabet=alphabet.replace(letter,'')
        
        
        print "You have this many guesses left: ",misses_left
        print "Letters not guessed: ",alphabet

     
    # game over
    if guessList.count('_') == 0 or Winner==True:
        print "You win. You guessed the word", wordToGuess
    else:
        print "You lost, word was", wordToGuess


if __name__ == '__main__':
    words = fileToStringList('lowerwords.txt')
    print "game (g) or testing(t) mode?"
    mode=raw_input("g or t? ")
    if mode=='t':
        DEBUG=True
        
    playGame(words)
    




