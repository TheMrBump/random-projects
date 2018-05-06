import random
import sys

#intro doesn't work properly
def intro():
	person = input("Enter your name: ")

	print("Hello " + person + ", would you like to play a friendly game?")
	if input() == "Yes":
		print("Great! Let us begin. The rules goes as follows, I will toss some cards on the table and you will guess which one is the jack.")
		return game()
	else:
		input() != "Yes"
		print("Goodbye!")
		sys.exit()
	

def reply():
	answer = input("Do you want to try again? ")
	if answer == "Yes":
		return game() 
	elif answer != "Yes":
		print("Too bad :(") 
	else:
		sys.exit()

def game():
	card = random.randint(1,3)
	
	for guessesTaken in range(1, 2):
		print("Take a guess.")
	
	guess = int(input())

	if guess == card:
		print("Correct!")
		return reply()
	else:
		print("Wrong!")
		return reply()	

intro()



