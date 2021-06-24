# Project Title: (Adventure Game (Non Linear)) "ESCAPE ROOM"
# Creators: Pierce Chaffin and Mauricio Litvak
# Created for CMPSC 121 Spring 2017 PSU UP

print('This game was made for CMPSC 121 Spring 2017')
print('Coded by Mauricio Litvak and Pierce Chaffin')
print('...Game starts in...')
for i in range(6,0,-1):
    print(i)
name = input('Enter your name: ')
print()
print()
print()
print()
for i in range(4):
    print('Drip...')
print('*A drop of water rolls down your face and you wake with a dull pain in your head*')
wake_count = 0
while 0 == 0:
    wake_condition = input('Wake up? *yes or no*')
    if wake_condition == 'yes':
        wake_count += 1
        if wake_count == 3:
            break
        else:
            print('*you pass out again*')
            continue
    else:
        print('You fall into deep sleep again\n *hours pass*')
        continue
print('*you finally awake to complete darkness*')
while 0==0:
    option1 = input('*Try to get up or take in your surroundings* (Enter A or B)')
    if option1 == 'A':
        print('*You try to get up but upon getting up you face severe pain in your leg and realize that its completely broken and pass out in pain*')
        print()
        print()
        print()
        print('*you awake a little later*')
        break
    else:
        print('You attempt to take in your surroundings but you are stopped by you cannot due to the insurmountable pain in your leg.')
print()
print()
print()
print('What do you do next, do you...')
print('1. Check your pockets for there contents')
print('2. Attempt to stand up.')
print('3. Go back to sleep')
n = input('Enter 1, 2, or 3\n')
if n == 1:
    print('You check your pockets and find a lighter, and a crumpled a piece of paper.')
if n == 2:
    print('You attempt to stand up but to no avail.')
if n == 3:
    print('You go back to sleep.')
else:
    print('You did not enter an integer between 1 and 3.')
    
