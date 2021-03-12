# hangman game by Anandakrishnan

from words import words
import random

word_taken = random.choice(words)

# for printing the word for testing
# print(word_taken)

difficulty = str(input("Select the difficulty , e for easy , m for medium , h for hard \n"))
if difficulty.lower() == 'e':
    lives = 10
elif difficulty.lower() == 'm':
    lives = 7
else:
    lives = 5

guess = "-" * len(word_taken)
index_set = {''}
res = 0
number = 1

used_letters = []

while (word_taken != guess) & (lives > 0):

    user = str(input("Enter the letter : "))

    if (word_taken.count(user) != 0) & (len(user) == 1):
        i = word_taken.index(user)

        if i in index_set:

            while number > 0:
                res = i
                number = number - 1

            try:
                new_index = word_taken[res + 1:].index(user) + 1
                index_set.add(new_index + i)
                # print(new_index + i)
                res += new_index

                if user in word_taken:
                    guess = guess[:res] + guess[res:].replace('-', user, 1)
                    print(guess)
                    used_letters.append(user)
                    print(f'You have used the following letters : {used_letters}')
                    print(f'You have {lives} lives left')

            except ValueError:
                print("You have already used the letter .No more instances of the letter present")
                lives = lives - 1
                print(guess)
                print(f'You have {lives} lives left')

        else:
            index_set.add(i)
            if user in word_taken:
                guess = guess[:i] + guess[i:].replace('-', user, 1)
                print(guess)
                used_letters.append(user)
                print(f'You have used the following letters : {used_letters}')
                print(f'You have {lives} lives left')

        # print(index_set)

    else:
        print("Oops! entered letter not present in the word!. Input a valid letter")
        lives = lives - 1
        print(guess)
        print(f'You have {lives} lives left')

if word_taken == guess:
    print(f"Yay! guessed it right. The correct word was {word_taken}")
else:
    print(f"Oops! try again.The correct word was {word_taken}")
