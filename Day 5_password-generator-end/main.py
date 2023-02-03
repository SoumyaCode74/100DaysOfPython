'''
Create a strong password using this application based on the following inputs
Number of minimum characters to have? 8
Number of alphabets you want to have? 4
Number of symbols you want to have? 2
Number of digits you want to have? 2
Your password is:  aH%zz71$g
'''
import random

ascii_alphabets = list(range(65,91)) + list(y for y in range(97, 122))
ascii_symbols = list(range(33, 48)) + list(range(58, 65)) + list(range(91, 97)) + list(range(123, 127))
ascii_digits = list(range(48,58))

def add_alphabet() -> int:
	return random.randint(0, ascii_alphabets.__len__() - 1)

def add_symbol() -> int:
	return random.randint(0, ascii_symbols.__len__() - 1)

def add_digit() -> int:
	return random.randint(0, ascii_digits.__len__() - 1)

def create_password(alphabets, symbols, digits) -> str:
	length_of_password_req = alphabets + symbols + digits
	no_of_alphabets_added = 0
	no_of_symbols_added = 0
	no_of_digits_added = 0
	characters_added = 0
	password = ''
	while 1:
		choice = random.randint (0, 2)
		if choice == 0:
			if no_of_alphabets_added == alphabets:
				continue
			else:
				password += chr(ascii_alphabets[add_alphabet()])
				no_of_alphabets_added += 1
		elif choice == 1:
			if no_of_symbols_added == symbols:
				continue
			else:
				password += chr(ascii_symbols[add_symbol()])
				no_of_symbols_added += 1
		else:
			if no_of_digits_added == digits:
				continue
			else:
				password += chr(ascii_digits[add_digit()])
				no_of_digits_added += 1
		characters_added += 1
		if characters_added == length_of_password_req:
			break
	return password

def ask_for_inputs() -> dict:
	no_of_alphabets = abs(int(input("No. of alphabets you want to have? ").strip()))
	no_of_symbols = abs(int(input("No. of symbols you want to have? ").strip()))
	no_of_digits= abs(int(input("No. of digits you want to have? ").strip()))
	return {'alphabets':no_of_alphabets,
	        'symbols':no_of_symbols,
	        'digits':no_of_digits
	        }
	pass

if __name__ == "__main__":
	print("Welcome to the password generator!")
	password = ''
	while 1:
		requirements = ask_for_inputs()
		while 2:
			password = create_password (
			                            alphabets = requirements['alphabets'],
			                            symbols = requirements['symbols'],
			                            digits = requirements['digits']
			                            )
			print(f"Your password {password}")
			choice = input("Like this password? If yes, enter Y, if no, enter N: ").strip().capitalize()
			if choice == 'Y':
				break

		choice = input("Want a different type of password? If yes, enter Y. If no, enter N: ").strip().capitalize()
		if choice != 'Y':
			break
	print('Please find your password in password.txt!',
	      "Please delete the file after use if you're on a public terminal", ':)')
	with open('password.txt','w+') as f:
		f.write(password)
	print('Press any key to continue...')
	input()