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

# Another hint:
guess = input("What is your guess? ")
print(guess)

# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!

def findMatch(lsans,lsgue):

    if lsans[0]==lsgue[0] or lsans[1]==lsgue[1] or lsans[2]==lsgue:
        return "Match"
    elif lsans[0]==lsgue[1] or lsans[0]=lsgue[2] or lsans[1]==lsgue[2]:
        return "Close"
    else:
        return "nope"
def isMatch(a,g):
    return a==g
def main():
    digits = list(range(10))
    random.shuffle(digits)
    answer=(digits[:3])
    while not isMatch(answer, guess):
        lsans=list(answer)
        lsgue=list(guess)
        result=findMatch(lsans,lsgue)
        print(result)
        guess=input("What is your guess? ")
        int(answer)
