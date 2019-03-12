import os
TRIES = 10
OFFER_NEXT_GAME = 'Would you like to have another try? (y/n)\n'
GAME_WON_PHRASE = 'Congratulations!'
GAME_LOST_PHRASE = 'GAME OVER'
LETTERS_LEFT = 'Letters left:'
INPUT_PROMPT = 'Guess a letter:\n'
INVALID_INPUT = 'Invalid input, try again'
REMAINING_TRIES = 'Tries left:'

INPUT_CHARS = []
clear = lambda: os.system('clear')


# MAKE SURE YOU MODIFY THE initialize function
def initialize(gameRounds):
    i = 0
    while i < len(gameRounds):
        start_new_game(gameRounds[i])
        i += 1

    print(OFFER_NEXT_GAME)
    userInput = input()
    if (userInput.lower()[0] == "y"):
        initialize(rounds)
    else:
        exit


def obfuscate(word):
    result = list(word)
    for idx, val in enumerate(word):
        if (val == '-'):
            result[idx] = '-'
        elif any(val.lower() in s for s in INPUT_CHARS):
            result[idx] = val.upper()
        else:
            result[idx] = '_'

    return ''.join(result)

redrawTitle = lambda theme, tries : print('Welcome to Hangman. The theme for this round is - ' + theme + '. Amount of tries before we chop your head off:', tries)

def start_new_game(gameRound):
    clear()
    redrawTitle(gameRound.theme, TRIES)
    previousResult = obfuscate(gameRound.word)
    currentTries = TRIES
    while currentTries > 0:
        userInput = input()
        clear()
        if userInput.isalpha() and not any(userInput in s for s in INPUT_CHARS):
            INPUT_CHARS.append(userInput[0].lower())
            currentResult = obfuscate(gameRound.word)
            if (currentResult == gameRound.word.upper().replace(' ', '_')):
                break
            elif (previousResult == currentResult):
                currentTries -= 1
            else:
                previousResult = currentResult
            redrawTitle(gameRound.theme, currentTries)
            print(currentResult)
        else:
            redrawTitle(gameRound.theme, currentTries)
            print(previousResult)

    clear()
    if currentTries > 0:
        print(GAME_WON_PHRASE)
    else:
        print(GAME_LOST_PHRASE)

    INPUT_CHARS.clear()



class GameRound:
  def __init__(self, word, theme):
    self.word = word
    self.theme = theme

rounds = [GameRound('Obi-Wan Kenobi', "Star Wars"), GameRound('Fuzz Universe', 'Paul Gilbert')]

initialize(rounds)