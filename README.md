# STONE-PAPER-SCISSORS-GAME

# name ChaitanyaGothwal for hactober fest


Stone paper scissors game developed by CHAITANYA GOTHWAL



#python 3.7.1
import random as rd
import time as tm
com=0
user=0
games=0
sym=42*'—'

print(sym)
print(sym)
print('|| WELCOME TO STONE,PAPER,SCISSOR GAME  ||')
print(sym)
print(sym)

game=int(input('\nEnter Time You Want To Play : '))

while games<game:
    comp=rd.choice(['stone','paper','scissor'])
    print('\nChoose\nstone\npaper\nscissor')
    users=str(input('\nEnter Your Choice : '))

    print('Computer Turn.....')
    tm.sleep(2)
    print(f'\nComputer Choose {comp}')
    tm.sleep(2)
    print(f'{users} v\s {comp}')

    #condition start

    if users==comp:
        print(f'\nThe Match Is Tie\nYour Score Is {user}\nComputer Score Is {com}')
    
    elif users=='stone' and comp=='paper':
        com+=1                                            
        print(f'\nComputer Win The Match\nYour Score Is {user}\nComputer Score Is {com}')           
    elif users=='scissor' and comp=='paper':              
        user+=1                                           
        print(f'\nYou Win The Match\nYour Score Is {user}\nComputer Score Is {com}')

    elif users=='stone' and comp=='scissor':
        user+=1                                           
        print(f'\nYou Win The Match\nYour Score Is {user}\nComputer Score Is {com}')                
    elif users=='paper' and comp=='scissor':
        com+=1                                            
        print(f'\nComputer Win The Match\nYour Score Is {user}\nComputer Score Is {com}')

    elif users=='paper' and comp=='stone':
        user+=1
        print(f'\nYou Win The Match\nYour Score Is {user}\nComputer Score Is {com}')

    elif users=='scissor' and comp=='stone':
        com+=1
        print(f'\nComputer Win The Match\nYour Score Is {user}\nComputer Score Is {com}')

    games=games+1
tm.sleep(1)
print('\nResult Is Coming Soon....')
tm.sleep(2)

if user==com:
    print(f'\nYour Score Is {user}\nComputer Score Is {com}')
    print(f"\n{sym}")
    print(sym)
    print(f'||          The Match Is Tie            ||')
    print(sym)
    print(sym)
    print('plese give me a 🌟')

elif user<=com:
    print(f'\nYour Score Is {user}\nComputer Score Is {com}')
    print(f"\n{sym}")
    print(sym)
    print(f'||        Computer Win The Match        ||')
    print(sym)
    print(sym)
    print('plese give me a 🌟')

elif user>=com:
    print(f'\nYour Score Is {user}\nComputer Score Is {com}')
    print(f"\n{sym}")
    print(sym)
    print(f'||          You Win The Match           ||')
    print(sym)
    print(sym)
    print('plese give me a 🌟')
