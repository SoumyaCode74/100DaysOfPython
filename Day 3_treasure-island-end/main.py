'''
This is a mini game on a treasure island.
Choose the right option to reach to the treasure!
'''

def play_game() -> bool:
	print("Welcome to Treasure Island.", end = ' ')
	print('Your mission is to find the treasure')
	direction_to_take = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\" ").strip()
	if direction_to_take == 'left':
		print('You come to a lake. There is an island in the middle of the lake', end = ' ')
		boat_or_swim = input('Type "wait" to wait for a boat. Type "swim" to swim across ').strip()
		if boat_or_swim != 'wait':
			print('You get attacked by an angry trout!',"Game Over.")
			return False
		else:
			print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.", end = ' ')
			color_chosen = input("Which colour do you choose? ").strip().capitalize()
			if color_chosen == 'Red':
				print('You got burned by fire!', 'Game Over.')
				return False
			elif color_chosen == 'Blue':
				print('You are eaten by beasts!', 'Game Over.')
				return False
			elif color_chosen == 'Yellow':
				print('You Win!')
				return True
			else:
				print('Game Over.')
				return False
	else:
		print('You fell into a hole! Game Over.')
		return False

if __name__ == "__main__":
	while (1):
		result = play_game()
		check_to_replay = input('Want to play again? Press Y. To exit, press any other key . . .').strip().capitalize()
		if check_to_replay != 'Y' :
				print('Have a nice day!')
				break

