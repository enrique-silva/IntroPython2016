#the following program will simulate a game of jeopardy. The user will be asked to guess a letter or the complete word.
#As the user guesses words/letters he or she will only be given 10 opportunities, at which time the game will be over.

import random

animals={'giraffe':['long neck'], 'lion':['king of the jungle'], 'cheetah':['has spots and is fast']}

movies= {'sleepless in seattle':["Can't sleep in Seattle"], 'the godfather' : ['al pacino']}

continents= {'africa' :['the sahara'], 'south america': ['brazil'], 'asia' : ['china is here']}

menu="""Welcome to Jeopardy. Please pick a category:

For Animals type: animals

For Movies type: movies

For continents type: continents

To exit please type: x

"""

start_game="""The game has started please enter 1 letter
or the enter a word that is length {}: """

def main(animals,movies, continents):
	"""This function serves as the jeopardy menu, it will loop infinitely unless the
	contestant decides to exit"""

	while True:
		print(menu)
		response=input('====> ')
		if response == 'animals':
			category_choice(animals)
		elif response == 'movies':
			category_choice(movies)
		elif response == 'continents':
			category_choice(continents)
		elif response == 'x':
			break
		else:
			print('Please enter a valid entry')

def category_choice(category):
	list=[key for key in category.keys()]
	word=random.choice(list)
	hint=category[word]
	guessing_game(word,category,hint)


def guessing_game(word, category, hint):
	length_word=len(word)
	print(start_game.format(length_word))
	guess=input('===> ')
	if guess == word:
		print('You won')

	else:
		print('you suck')


main(animals,movies, continents)


