'''
This is a mini-game between the user and the computer.
The user will be asked 10 times to choose between rock, paper, scissors
The computer will make its own choice.
Below is the rule table for the points:
-----------------------------------------------
|   You    |   Computer    |   Who wins?   |
-----------------------------------------------
|   Rock    |   Rock             |   None            |
|   Rock    |   Paper           |   You             |
|   Rock    |   Scissors       |   You             |
|   Paper   |   Rock            |   Computer     |
|   Paper   |   Paper          |    None            |
|   Paper   |   Scissors       |    Computer    |
|   Scissors |  Rock            |   Computer    |
|   Scissors |  Paper          |    You            |
|   Scissors  | Scissors       |    None            |
------------------------------------------------
The total points earnt by user and computer will be calculated and displayed after each round
After the tenth round, the final result will be declared and the user will be prompted for new game
If user declines, terminate the application
'''
import random
from random import randint

def play_game():
	# Display the rules first
	print ('Please check below the rules of the game before you start')
	display_rules()
	user_pts = 0
	computer_pts = 0
	choices = ['Rock', 'Paper', 'Scissors']
	user_chose = [f'You chose {x}' for x  in choices]
	computer_chose = [f'Computer chose {x}' for x in choices]
	user_state = 'You win!'
	computer_state = 'Computer wins!'
	for i in range(10):
		print(f"Round {i+1}")
		print('What do you choose? Rock: 0, Paper: 1,  Scissors: 2', end = ': ')
		user = int(input().strip())
		while user not in (0, 1, 2):
			print('Wrong choice. Please try again! ')
			print ('What do you choose? Rock: 0, Paper: 1,  Scissors: 2', end = ': ')
			user = int (input ())
		computer = randint(0,2)
		#0: Rock, 1: Paper, 2: Scissors
		if user == computer:
			print(user_chose[user], ',', computer_chose[computer], ',', 'It\'s a Draw!')
		elif user == 0 and computer == 1:
			print(user_chose[user], ',', computer_chose[computer], ',', computer_state)
			computer_pts += 1
		elif user == 0 and computer == 2:
			print(user_chose[user], ',', computer_chose[computer], ',', user_state)
			user_pts += 1
		elif user == 1 and computer == 0:
			print(user_chose[user], ',', computer_chose[computer], ',', user_state)
			user_pts += 1
		elif user == 1 and computer == 2:
			print(user_chose[user], ',', computer_chose[computer], ',', computer_state)
			computer_pts += 1
		elif  user == 2 and computer == 0:
			print(user_chose[user], ',', computer_chose[computer], ',', computer_state)
			computer_pts += 1
		else:
			print(user_chose[user], ',', computer_chose[computer], ',', user_state)
			user_pts += 1
		print(f"Round {i+1} result: Your points: {user_pts}, Computer's points: {computer_pts}")
		if i < 9:
			print(f"Get ready for Round {i+2}!")
		else:
			print (f"Get ready for final result!")
		print ('=' * 60)
	declare_result(user_pts, computer_pts)


def declare_result(user_pts, computer_pts):
	if user_pts > computer_pts:
		print("Congratulations! You won the game! :) :) :)")
	elif user_pts < computer_pts:
		print("Sorry! You lose the game! Better luck next time! :( :( :(")
	else:
		print("Ahaaa!! You both are equal!!")

def display_rules():
	print ('---------------------------------------------')
	line = ['(\t','You\t',',','\tComputer\t',',','\tWho Wins?\t',')']
	print(''.join(line))
	print ('---------------------------------------------')
	line = ['(\t','Rock',',','\tRock\t\t',',','\tNone\t','\t)']
	print(''.join(line))
	print ('---------------------------------------------')
	line = ['(\t','Rock',',','\tPaper\t\t',',','\tComputer\t',')']
	print(''.join(line))
	print ('---------------------------------------------')
	line = ['(\t','Rock',',','\tScissors\t',',','\tYou\t\t\t',')']
	print(''.join(line))
	print ('---------------------------------------------')
	line = ['(\t','Paper',',','\tRock\t','\t,','\tYou','\t\t\t)']
	print(''.join(line))
	print ('---------------------------------------------')
	line = ['(\t','Paper',',','\tPaper\t','\t,','\tNone','\t\t)']
	print(''.join(line))
	print ('---------------------------------------------')
	line = ['(\t','Paper',',','\tScissors','\t,','\tComputer','\t)']
	print(''.join(line))
	print ('---------------------------------------------')
	line = ['(\t','Scissors',',','\tRock','\t,','\tComputer','\t)']
	print(''.join(line))
	print ('---------------------------------------------')
	line = ['(\t','Scissors',',','\tPaper','\t,','\tYou','\t\t\t)']
	print(''.join(line))
	print ('---------------------------------------------')
	line = ['(\t','Scissors',',','\tScissors',',','\tNone','\t\t)']
	print(''.join(line))
	print ('---------------------------------------------')


if __name__ == '__main__':
	while 1:
		print('Welcome to the popular Rock-Paper-Scissors game!')
		play_game()
		choice = input("Wanna play again?? Press Y to confirm, N to exit the game ").strip().capitalize()
		if choice != 'Y':
			break





