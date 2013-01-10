# Password Generator of Random Text
# Version 0.0.2-4
# Changes:
# 
#
#
import random


def main():


	def printBlankLine(amount):
		while amount >> 0:
			print ''
			amount = amount - 1


	def replacerDict():
		global replacers
		replacers = {' ':'', 'a':'@', 'e':'3', '':'', 'o':'0', 's':'5', 't':'7'}


	def welcomeMessage():
		print """         -Welcome to EncryptGen-"""
		print """Let us help make your passwords more secure!"""


	def passwordType():
		print """What kind of password do you want?"""
		print """1) Generate a random character password."""
		print """2) Randomize a specific word or phrase."""
		print """3) Combination of 1 and 2."""
		password_type_choice = raw_input("Enter a number selection: ")
		
		password_type_loop = 1
		while password_type_loop == 1:
			try:
				int(password_type_choice)
				while int(password_type_choice) not in range(1,4):
					password_type_choice = raw_input('Invalid number choice! \
Valid range is 1-3: ')
				break
				password_type_loop = 0
			except ValueError:
				password_type_choice = raw_input('You must specify a number! \
Valid range is 1-3: ')
				
		if password_type_choice == '1':
			print ''
			
		elif password_type_choice == '2':
			print ''
			
			
		elif password_type_choice == '3':
			print ''

		return password_type_choice
	


	def stringInput():
		global inputStringText
		inputStringTextLoop = 1
		print 'What is the word you want to be turned into a password?'
		inputStringText = raw_input('Input word or phrase: ')


	def charReplace(text, dic):
		for i, j in dic.iteritems():
			text = text.replace(i, j)
		return text


	def printResults(results):
		print 'The secured string is:', results
	

	def security_level():
		global security_level_choice
		print 'How many characters should the password have?'
		print 'More characters means more secure. Suggested range is'
		print 'between 10 and 30.'
		security_level_choice = raw_input('Enter a number: ')
		
		security_level_loop = 1
		while security_level_loop == 1:
			try:
				int(security_level_choice)
				while int(security_level_choice) not in range(1,10001):
					print 'Invalid number choice! Valid range is 1-10,000.'
					security_level_choice = raw_input('Enter a number: ')
				security_level_choice = int(security_level_choice)
				security_level_loop = 0
			except ValueError:
				print 'You must specify a number!'
				security_level_choice = raw_input('Enter a number: ')
		return security_level_choice
			

	def security_chars():
		# Character Strings
		global pass_chars
		pass_chars = '0'
		hex_string_low = '0123456789abcdef'
		alphabet_string_low = 'abcdefghijklmnopqrstuvwxyz'
		alphabet_string_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		alphabet_string_low_up = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
		digit_string = '0123456789'
		symbol_string = """!@#$%^&*()"""
		at_pound_string = """@#"""
		# Messages
		hex_true_str = 'Password will be hexidecimal. '
		alph_low_true_str = 'Password will include lowercase alphabet. '
		alph_up_true_str = 'Password will include uppercase alphabet. '
		digit_true_str = 'Password will have digits. '
		
		print 'What kind of characters would you like in your password?'
		print '1) Hexadecimal. (0-9,a-f)'
		print '2) Lowercase alphabet. (a-z)'
		print '3) Uppercase alphabet. (A-Z)'
		print '4) Upper and lowercase alphabet. (A-Z,a-z)'
		print '5) Lowercase alphabet with digits. (a-z,0-9)'
		print '6) Digits. (0-9)'
		security_chars_choice = raw_input('Enter selection (1-6): ')
		
		security_chars_loop = 1
		while security_chars_loop == 1:
			try:
				int(security_chars_choice)
				while int(security_chars_choice) not in range(1,7):
					security_chars_choice = raw_input('Invalid number choice! \
Valid range is 1-6: ')
				break
				security_chars_loop = 0
			except ValueError:
				security_chars_choice = raw_input('You must specify a number! \
Valid range is 1-6: ')
				
		if security_chars_choice == '1':
			pass_chars = hex_string_low
			print hex_true_str
			
		elif security_chars_choice == '2':
			pass_chars = alphabet_string_low
			print alph_low_true_str
			
		elif security_chars_choice == '3':
			pass_chars = alphabet_string_up
			print alph_up_true_str
			
		elif security_chars_choice == '4':
			pass_chars = alphabet_string_low_up
			print alph_low_true_str,alph_up_true_str
			
		elif security_chars_choice == '5':
			pass_chars = alphabet_string_low + digit_string
			print alph_low_true_str,digit_true_str
			
		elif security_chars_choice == '6':
			pass_chars = digit_string
			print digit_true_str

		return pass_chars


# Ask for symbols eventually

	def generate_passphrase(pass_chars, security_level_choice):

		list_of_chars = [random.choice(pass_chars) for n in xrange(security_level_choice)]
		pass_string = "".join(list_of_chars)

		print \
'Passphrase with ', str(security_level_choice), 'characters: ', pass_string, ''
		





	welcomeMessage()
	printBlankLine(2)
	program_loop = 1
	while program_loop == 1:

		passwordType_selection = passwordType()
		if passwordType_selection in ('1'):
			security_chars()
			printBlankLine(1)
			security_level()
			printBlankLine(1)
			generate_passphrase(pass_chars, security_level_choice)
			printBlankLine(1)
		elif passwordType_selection in ('2'):
			stringInput()
			replacerDict()
			results = charReplace(inputStringText, replacers)
			printBlankLine(1)
			printResults(results)
			printBlankLine(1)
		elif passwordType_selection in ('3'):
			print 'This feature is still being worked on.'
			
		
		
		
		
		repeat_question = 1
		while repeat_question == 1:
			again_or_not = raw_input('Would you like to do it again? (Y/n): ')

			if again_or_not in ('y','ye','yes','Y','YES'):
				program_loop = 1
				repeat_question = 0
				print '\n\nRestarting...\n'

			elif again_or_not in ('n','no','nope','N','NO'):
				program_loop = 0
				repeat_question = 0
				print '\n\nExiting...\n'

			else:
				print 'Please select yes or no answer.'
				repeat_question = 1










if __name__ == "__main__":
	main() 





