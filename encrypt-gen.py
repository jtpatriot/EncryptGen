# Password Generator of Random Text
# Version 0.0.2-2
# Changes: in security_chars function, changed line 60 from range(1,6) to
# range(1,7) to encompass the 6 correctly, didn't allow option 6 before.
#
#
import random


def main():
    

    def security_level():
        global security_level_choice
        security_level_loop = 1
        security_level_choice = raw_input('What is your preferred level of \
security, in number of characters?\
\nEnter a number: ')
        while security_level_loop == 1:
            try:
                int(security_level_choice)
                security_level_choice = int(security_level_choice)
                security_level_loop = 0
            except ValueError:
                security_level_choice = raw_input('You must specify a number!\
\nEnter a number: ')
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
        
        security_chars_choice = raw_input('What kind of password would you like?\
\n1) Hexadecimal. (0-9,a-f)\
\n2) Lowercase alphabet. (a-z)\
\n3) Uppercase alphabet. (A-Z)\
\n4) Upper and lowercase alphabet. (A-Z,a-z)\
\n5) Lowercase alphabet with digits. (a-z,0-9)\
\n6) Digits. (0-9)\
\nEnter selection (1-6):')
        
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

        print '\n \
Passphrase with ', str(security_level_choice), 'characters: ', pass_string, '\
\n'
        






    again_or_not_loop = 1
    while again_or_not_loop == 1:

        security_level()
        security_chars()
        generate_passphrase(pass_chars, security_level_choice)

        again_or_not = raw_input('Would you like to do it again? (Y/n): ')

        if again_or_not in ('y','ye','yes','Y','YES'):
            again_or_not_loop = 1
            print '\n\nRestarting...\n'

        elif again_or_not in ('n','no','nope','N','NO'):
            again_or_not_loop = 0
            print '\n\nExiting...\n'

        else:
            print 'Please select yes or no answer.'










if __name__ == "__main__":
    main() 





