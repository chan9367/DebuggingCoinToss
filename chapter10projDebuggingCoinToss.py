import random
import logging
#logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -%(levelname)s - %(message)s')
logging.debug('Start of program')

guess = ''
while guess not in ('heads', 'tails'):
 print('Guess the coin toss! Enter heads or tails:')
 guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads

logging.debug('toss is ' + str(toss))
logging.debug('guess is ' + str(guess))

if toss == guess:
 print('You got it!')
else:
 print('Nope! Guess again!')
 guesss = input()
 logging.debug('toss is ' + str(toss))
 logging.debug('guess is ' + str(guess))
 logging.debug('guesss is ' + str(guesss))
 if toss == guess:
    print('You got it!')

 else:
    print('Nope. You are really bad at this game.')
    

logging.error('toss variable stay as 1 or 0 and never corresponds to heads or tails')
logging.error('guess variable also never gets reassigned after first guess input because the variable is mispelled as guesss')
logging.error('second guess doesn\'t check for heads or tails')
logging.debug('End of program')
