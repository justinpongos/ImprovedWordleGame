import string
WORD_LENGTH = 5
#code for functions

def read_dictionary(file_name):
    stinky = []
    dictionary = open (file_name)
    new_dictionary_list = dictionary.read()
    new_dictionary_list = new_dictionary_list.split('\n')
    new_dictionary_list.pop()
    for i in new_dictionary_list:
        i = i.lower()
        f = [i]
        stinky = stinky + f
    dictionary.close()
    return stinky

def enter_a_word (word_type, num_letters): 
    a_word = input(f'Enter the {num_letters}-letter {word_type} word: ') 
    a_word = a_word.lower()
    return a_word #A string with lower case letters

def is_it_a_word (input_word, word_list):
    is_word = False
    for i in word_list:
        if input_word == i:
            is_word = True
            break
    return is_word #Boolean variable

def enter_and_check(word_type, word_list):
    length = 0
    in_word = enter_a_word(word_type, 5)
    in_dict = is_it_a_word(in_word, word_list)
    length = len(in_word)
    while in_dict!= True or length != 5:           
        if is_it_a_word(in_word, word_list) == False:
            print(f'You entered a {length}-letter word that is not in the dictionary. Please try again!')
            in_word = enter_a_word(word_type, 5)
            length = len(in_word)
            in_dict = is_it_a_word(in_word, word_list)
        elif length != 5:
            print(f'You entered a {length}-letter word that is in the dictionary. Please try again!')
            in_word = enter_a_word(word_type, 5)
            length = len(in_word)
            in_dict = is_it_a_word(in_word, word_list)
    return in_word #a string - valid input word

def compare_words (player, secret): 
    global remaining_alphabet
    global in_secret_word_correct_spot
    global in_secret_word_somewhere
    global not_in_secret_word
    final = '_____'
    final_list = list(final)
    x = 0
    in_correct_spot = 0
    p_list = list(player)
    s_list = list(secret)
    index = 0
    finalfinal = ''

    for p in p_list:
        if p == s_list[x]:
            in_correct_spot += 1
            final_list[x] = p
            if p in remaining_alphabet:
                remaining_alphabet.remove(p)
                in_secret_word_correct_spot.append(p)

        elif p in s_list:
            final_list[x] = f'({p})'
            if p in remaining_alphabet:
                remaining_alphabet.remove(p)
                in_secret_word_somewhere.append(p)
        else:
            if p in remaining_alphabet:
                remaining_alphabet.remove(p)
                not_in_secret_word.append(p)
        x += 1
        
    for f in in_secret_word_correct_spot:
        if f in in_secret_word_somewhere:
            index = in_secret_word_somewhere.index(f)
            in_secret_word_somewhere.remove(index)
    for f in final_list:
        finalfinal = finalfinal + f
    return finalfinal, in_correct_spot # returns a string and an integer

# program code
print('Welcome to new and improved Wordle - CECS 174 edition!')
alphabet_string = string.ascii_lowercase #Create a string of all lowercase letters
remaining_alphabet = list(alphabet_string) #Create a list of all lowercase letters

in_secret_word_correct_spot = [] 
in_secret_word_somewhere = []
not_in_secret_word = []
words_list = read_dictionary('project4_dictionary.txt')
N = 0 
attempts = 1
guess = ''
bruh = ''
win = False

secret_word = enter_and_check('secret', words_list)
N = int(input('Input allowed number of attempts: '))

while attempts <= N:
    print(f'Enter your attempt #{attempts}')
    guess = enter_and_check('player', words_list)
    bruh = compare_words(guess, secret_word)
    print (f'letter in the right spot: {bruh[1]}')
    print (f'You guessed letters of the secret_word: {bruh[0]}')
    print (f'Previously attempted letters that are in the correct spot of secret_word:')
    print (f'{in_secret_word_correct_spot}')
    print (f'Previously attempted letters that are in some spot of secret_word:')
    print (f'{in_secret_word_somewhere}')
    print (f'Previously attempted letters that are not in the secret_word:')
    print (f'{not_in_secret_word}')
    print (f'Remaining letters of the alphabet that have not been tried:')
    print (f'{remaining_alphabet}')

    if guess == secret_word:
        print(f'Congrats you won using {attempts} attempt(s)')
        win = True
        break
    attempts += 1
    
if win == False and N != 0:
    print (f'You already used #{N} attempts. Better luck tomorrow!')
