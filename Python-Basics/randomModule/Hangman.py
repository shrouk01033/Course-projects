import random as r

words = ['orange', 'mango', 'banana', 'watermelon', 'apple']

word = r.choice(words)
Word_length = len(word)

secret = ['-']*Word_length
trials = Word_length+2

print('Hint: fruit')
while trials > 0:
    print(''.join(secret))
    guess = input('Your guess: ')
    
    if guess in word:
        for i , letter in enumerate(word):
            if guess == letter:
                secret[i] = guess
    if '-' not in secret:
        print(''.join(secret))
        print('You win!🎉')
        break           
    else:
        trials-=1
        if trials == 0:
            print(f'Game over! The word was {word} ☑️')
        else:
            print(f'{trials} chances left!⌛')
