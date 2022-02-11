# import random
# print('welcome in my game')

# guess = random.randint(1, 10)
# tries = 0
# guess_chances = 10

# while True:
#     tries +=1
#     number = int(input('enter your number 1-10: '))
#     if number < guess:
#         print('this number is too low. Guess number is higher than', number)
#     elif number > guess:
#         print('this number is too high.Guess number is lower than',number)
#     else:
#         print('u Guessed it number of attempts', tries)
#         break

#     guess_chances-=1
#     print(f'{guess_chances}, guesses left')


# print('game over')
# print('your number is', number )
# print('click ENTER to exit')


# list_ = [['we', 'very'], ['loves'], ['Python']]
# print(sum(list_,[]))

list_ = ['Khasan', 'Ali', 'Aidar', 'Daniel', 'Ulan']
for i, name in enumerate(list_):
    print(f'{name}  on {i} place in the list')
