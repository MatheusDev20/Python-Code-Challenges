import random
import time
x = 0

finalPoints = 0
parcialPoints = 0
while( x < 5):
    result = None

    minimo = 1

    maximo = 4

    question = 'Please select a number between 1 and 4 '
    string_input = input(question)
    if(string_input.isalpha()): 
        print('Please type a number value')
    while(string_input.isalpha()):
        string_input = input(question)
        print('Please type a number value')

    number_input = int(string_input)

    result = random.randint(minimo,maximo)

    if(result == number_input):
        parcialPoints += 10
        finalPoints += parcialPoints
        print('Congratulations youre a lucky guy and the dice ends on {}'.format(result))
        time.sleep(1)
        print('Parcial Points: {}'.format(parcialPoints))
    else : 
        print('Oh no the gods arent on your favor the dice ends on {}'.format(result))

    x+=1
    
else : 
    print('Final Points: {}'.format(finalPoints))







