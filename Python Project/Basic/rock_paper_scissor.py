import random
print('Rock Paper Scissor'.center(50))
user=input('Enter a choic(rock,paper,scissor)')
computer=random.choice(['rock','paper','scissor'])
print(f"\n Your choice : '{user},'computer choice : ',{computer}.\n")
if user == computer:
    print(f"Both palyer selected : {user} . Its a tie!")
elif user == 'rock':
    if computer == "scissor":
        print("Rock smashes Scissor! You win!")
    else:
        print('Paper Covers Rock! You loss.')
elif user == 'paper':
    if computer == 'rock':
        print("Paper covers Rock! You win!")
    else:
        print('Scissor cuts paper! You loss')
elif user == 'scissor':
    if computer == 'papaer':
        print("Scissor cuts paper! You win!")
    else:
        print('Rock smashes scissor! You loss.' )                                 