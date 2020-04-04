#!/usr/bin/env python3

import random, os, sys

cardName = { 1: 'As', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'Joto', 12: 'Qüina', 13: 'Rey' }
cardSuit = { 'c': 'Treboles', 'h': 'Corazones', 's': 'Espadas', 'd': 'Diamantes' }

class Card:

	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit

	def __str__(self):
		return(cardName[self.rank]+" De "+cardSuit[self.suit])

	def getRank(self):
		return(self.rank)

	def getSuit(self):
		return(self.suit)

	def BJValue(self):
		if self.rank > 9:
			return(10)
		else:
			return(self.rank)

def showHand(hand):
	for card in hand:
		print(card)

def showCount(hand):
	print("Puntos: "+str(handCount(hand)))

def handCount(hand):
	handCount=0
	for card in hand:
		handCount += card.BJValue()
	return(handCount)

def gameEnd(score):
	print("Jack Black!! *Puntaje Final* IA: "+str(score['computer'])+" Tu: "+str(score['human']))
	sys.exit(0)

deck	= []
suits = [ 'c','h','d','s' ]
score = { 'computer': 0, 'human': 0 }
hand	= { 'computer': [],'human': [] }

for suit in suits:
	for rank in range(1,14):
		deck.append(Card(rank,suit))

keepPlaying = True

while keepPlaying:

	random.shuffle(deck)
	random.shuffle(deck)
	random.shuffle(deck)

	hand['human'].append(deck.pop(0))
	hand['computer'].append(deck.pop(0))

	hand['human'].append(deck.pop(0))
	hand['computer'].append(deck.pop(0))

	playHuman = True
	bustedHuman = False

	while playHuman:
		os.system('clear')
		print("Blackjack! IA: "+str(score['computer'])+" Tú: "+str(score['human']))

		print()

		print('Mano de IA: '+ str(hand['computer'][-1]))
		print()

		print('Tú mano:')

		showHand(hand['human'])

		showCount(hand['human'])

		print()

		inputCycle = True
		userInput = ''

		while inputCycle:
			userInput = input("(P)edir Otra, (Q)uedarse, o (S)alir: ").upper()
			if userInput == 'P' or 'Q' or 'S':
				inputCycle = False

		if userInput == 'P':
			hand['human'].append(deck.pop(0))
			if handCount(hand['human']) > 21:
				playHuman = False
				bustedHuman = True
		elif userInput == 'Q':
			playHuman = False
		else:
			gameEnd(score)

	playComputer = True
	bustedComputer = False

	while not bustedHuman and playComputer:
		print(handCount(hand['computer']))
		if handCount(hand['computer'])<17:
			hand['computer'].append(deck.pop(0))
		else:
			playComputer = False

		if handCount(hand['computer'])>21:
			playComputer = False
			bustedComputer = True

	if bustedHuman:
		print('Te pasaste')
		score['computer'] += 1
	elif bustedComputer:
		print('Se pasó la IA')
		score['human'] += 1
	elif handCount(hand['human']) > handCount(hand['computer']):
		print('Gano el Jugador')
		score['human'] += 1
	elif handCount(hand['human']) == handCount(hand['computer']):
		print('Empate')
		score['computer'] += 1
		score['human'] += 1
	else:
		print('Gano la PC')
		score['computer'] += 1

	print()
	print('Mano de Computadora:')
	showHand(hand['computer'])
	showCount(hand['computer'])

	print()
	print('Mano de Jugador:')
	showHand(hand['human'])
	showCount(hand['human'])
	print()
	if input("(S)alir o enter para jugar otra ronda: ").upper() == 'S':
		gameEnd(score)

	deck.extend(hand['computer'])
	deck.extend(hand['human'])

	del hand['computer'][:]
	del hand['human'][:]
