import random
from time import sleep
import time
print('...............Rock Paper Scissor...............'.center(100))
user=input('Enter a choic(rock,paper,scissor Game)')
computer=random.choice(['rock','paper','scissor'])
print(f"\n Your choice : {user} computer choice :{computer}\n")
print('\n\n\n')
time.sleep(2)
print('Processing'.center(50),end='')
for i in range(random.randint(3,10)):
    print('.',end='',flush=True)
    sleep(1)
print('\n\n\n')

if user == computer:
    print(f"Both palyer selected : {user} . Its a tie!".center(100))
elif user == 'rock':
    if computer == "scissor":
        print("Rock smashes Scissor! You win!".center(100))
    else:
        print('Paper Covers Rock! You loss.'.center(100))
elif user == 'paper':
    if computer == 'rock':
        print("Paper covers Rock! You win!".center(100))
    else:
        print('Scissor cuts paper! You loss'.center(100))
elif user == 'scissor':
    if computer == 'papaer':
        print("Scissor cuts paper! You win!".center(100))
    else:
        print('Rock smashes scissor! You loss.'.center(100)) 