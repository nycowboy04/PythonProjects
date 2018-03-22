###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
import random

# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!

def findMatch(lsans,lsgue):
    '''Compare each number in both lists to determine where there's a match, if any.'''

    clues=[]
    for ind, num in enumerate(lsgue):
        if num==lsans[ind]:
            clues.append('Match')
        elif num in lsans:
            clues.append('Close')

        if clues==[]:
            return ['Nope']
        else:
            return clues
def isMatch(a,g):
    '''determines if the two lists are exact matches'''
    result = []
    if a==g:
        result =["correct!"]
        return result
    else:
        return result

def shuffleNumbers():
    '''creates a random list of three digits'''
    digits=list(range(10))
    random.shuffle(digits)
    return digits[:3]

def getGuess():
    '''prompts user for data entry'''
    Nu=list(input("what is your guess? Enter a 3-digit number. "))
    print("The Number you entered was: "+ "".join(Nu))
    return Nu

def main():
    answer=shuffleNumbers()
    guess=getGuess()
    goal=isMatch(answer,guess)
    while goal != "correct!":
        result=findMatch(answer,guess)
        print("Here is the result of your guess: ")
        for clue in result:
            print(clue)
        guess=getGuess()
        goal=isMatch(answer,guess)

main()
