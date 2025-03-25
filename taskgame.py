import random
data=random.randint(0,9)
guess_number=(input('please enter your guess number: '))
if guess_number.isdigit():
    guess_number=int(guess_number)
    if guess_number >=0 and guess_number <=9:
        if data == guess_number:
            print('Congratuations! You are the winner.',)
            print('')
        else:
            print('Indixpert is the winner.',guess_number)  
            print(data)
        
    else:
        print('invalid number enter 0 to 9!')    
else:
    print('please enter you only digit!')

