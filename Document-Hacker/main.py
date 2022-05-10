import itertools
from string import digits, punctuation, ascii_letters


symbols = digits + ascii_letters


def brute_word_doc():
    try:
        password_length = input('Длинна пароля: ')
        password_length = [int(item) for item in password_length.split('-')]
    except:
        print('Что-то не так')
    
    print('1: Only digits\t\t\t2: Only letters\n')
    print('3: Only letters and digits\t\t4: All')
    
    try:
        choice = int(input(''))
        if choice == 1:
            possible_symbols = digits
        elif choice == 2:
            possible_symbols = ascii_letters
        elif choice == 3:
            possible_symbols = digits + ascii_letters
        elif choice == 4:
            possible_symbols = digits + ascii_letters + punctuation
        else:
            return 'Nice...'
    except:
        print('Ok')
    
    for pass_length in range(password_length[0], password_length[1] + 1):
        for password in itertools.product(possible_symbols, repeat=pass_length):
            password = ''.join(password)
            print(password)



def main():
    brute_word_doc()


if __name__ == '__main__':
    main()