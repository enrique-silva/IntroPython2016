#the following program will simulate a game of jeopardy. The user will be asked to guess a letter or the complete word.
#As the user guesses words/letters he or she will only be given 10 opportunities, at which time the game will be over.

import random

animals={'giraffe':['long neck'], 'lion':['king of the jungle'], 'cheetah':['has spots and is fast']}

movies= {'sleepless in seattle':["Can't sleep in Seattle"], 'the godfather' : ['al pacino']}

continents= {'africa' :['the sahara'], 'south america': ['brazil'], 'asia' : ['china is here']}

msg="""Welcome to Jeopardy. Please pick a category:

For Animals type: animals

For Movies type: movies

For continents type: continents

To exit please type: x

"""

def main():
	"""This function serves as the jeopardy menu, it will loop infinitely unless the
	contestant decides to exit"""

	reponse=''
	while True:
		print(msg)
		response=input('====> ')
		if response == 'animals':
			print ('x')