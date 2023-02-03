'''
This is a mini game on a treasure island.
Choose the right option to reach to the treasure!
'''
import time

def play_game() -> bool:
	print("Welcome to Treasure Island.", end = ' ')
	print('Your mission is to find the treasure')
	print("You're at a cross road. Where do you want to go? ", end = ' ')
	while 1:
		direction_to_take = input("Type \"left\" or \"right\" ").strip().lower()
		if direction_to_take == 'left':
			print('You come to a lake. There is an island in the middle of the lake', end = ' ')
			while 2:
				boat_or_swim = input('Type "wait" to wait for a boat. Type "swim" to swim across ').strip().lower()
				if boat_or_swim == 'swim':
					print('You get attacked by an angry trout!',"Game Over.")
					return False
				elif boat_or_swim == 'wait':
					print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.", end = ' ')
					while 3:
						color_chosen = input("Which colour do you choose? ").strip().lower().capitalize()
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
							print('Wrong choice! Please try again!')
							continue
				else:
					print('Wrong choice! Please try again!')
					continue
		elif direction_to_take == 'right':
			print('You fell into a hole! Game Over.')
			return False
		else:
			print('Wrong choice! Please try again!')
			continue

if __name__ == "__main__":
	while (1):
		result = play_game()
		check_to_replay = input('Want to play again? Press Y. To exit, press any other key . . .').strip().capitalize()
		if check_to_replay != 'Y' :
				print('Have a nice day!')
				time.sleep(0.8)
				break

