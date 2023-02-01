'''
This is a mini game on a treasure island.
Choose the right option to reach to the treasure!
'''
import mako.filters

print("Welcome to Treasure Island.", end = ' ')
print('Your mission is to find the treasure')
direction_to_take = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\" ").strip()
if direction_to_take == 'left':
	print('You come to a lake. There is an island in the middle of the lake', end = ' ')
	boat_or_swim = input('Type "wait" to wait for a boat. Type "swim" to swim across ').strip()
	if boat_or_swim != 'wait':
		print('You get attacked by an angry trout!',"Game Over.")
		input("Press any key to continue . . .")
	else:
		print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.", end = ' ')
		color_chosen = input("Which colour do you choose? ").strip().capitalize()
		if color_chosen == 'Red':
			print('You got burned by fire!', 'Game Over.')
			input ("Press any key to continue . . .")
		elif color_chosen == 'Blue':
			print('You are eaten by beasts!', 'Game Over.')
			input ("Press any key to continue . . .")
		elif color_chosen == 'Yellow':
			print('You Win!')
			input ("Press any key to continue . . .")
		else:
			print('Game Over.')
			input ("Press any key to continue . . .")
else:
	print('You fell into a hole! Game Over.')
	input ("Press any key to continue . . .")