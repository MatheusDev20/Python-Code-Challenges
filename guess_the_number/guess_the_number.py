import random
import time

sorted_number = None

minimo = 1
maximo = 10

get_started = "To get started type Start\n"
guessed = False
question = 'Select a Number\n'
return_question = 'You are wrong, select another Number\n'


print('Welcome to Guessed Number Game \n')
time.sleep(1)
print('You have to guess a number between {} and {} \n'.format(minimo,maximo))
time.sleep(1)

started = input(get_started)

if(started == 'Start' or started == 'start'):
    sorted_number = random.randint(1,10)
    selected_number = int(input(question))
    while(guessed == False):
        selected_number = int(input(return_question))
        if(selected_number == sorted_number):
            guessed = True
    else:
        print('Congratulations you did it')



