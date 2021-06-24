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
while 0==0:
    print()
    print()
    print()
    print('What do you do next, do you...')
    print('1. Check your pockets for their contents')
    print('2. Attempt to stand up.')
    print('3. Go back to sleep')

    n = int(input('Enter 1, 2, or 3\n'))
    if n == 1:
        print('You check your pockets and find a lighter, and a crumpled a piece of paper.')
    elif n == 2:
        print('You attempt to stand up but to no avail.')
    elif n == 3:
        print('You go back to sleep.')
    else:
        print('You did not enter an integer between 1 and 3.')
    if n == 1:
        print('you unroll the paper to find a simple phrase scribbled on it in what seems to be ink, in the light of your lighter')
        print('Upon reading this you hear an ubrupt noise in the nearby corner of the room and see a sliver of light gleaming through what seems to be a now cracked open door way')
        print('You see a faint shadow through the crack vanish into what waits outside')
        print('Do you go outside?')
        decision = input('y or n')
        if decision == 'y':
            print('you crawl over to the door and peer outside')
            print('outside lies a hallway, dimly lit')
            print('you pry the door back till its fully open and then take it all in')
            print('you find there to be a spiked bat on the floor along side painkillers with a note beside them, reading "xFor your leg %s"' % name)
            print('do you pick up both or just the painkillers?')
            decision = input('a or b')
        if decision == 'n':
            print('*You hear a voice call your name.*')
            print('%s, you must go through the door.' % name)
            print('You do as the voice heads...')
            for i in range(20):
                print('.')
            print('outside lies a hallway, dimly lit')
            print('you pry the door back till its fully open and then take it all in')
            print('you find there to be a spiked bat on the floor along side painkillers with a note beside them, reading "xFor your leg %s"' % name)
            print('do you pick up both or just the painkillers?')
            if decision == 'a':
                print('you pick up the painkillers and down a few and sit around for a little to let them kick in')
                for i in range(20):
                    print('.')
                print('You feel the painkillers set in and now try to stand')
                print('With a little wince of pain you get up reluctantly but alas can stand')
                print('You grab the bat on the ground and look onward towards the hallway')
                print('Do you go down the hallway towards the staircase or turn left to explore the floor?')
                decision = input('a or b')
                if decision == 'a':
                    print('you start to tread down the hallway, firmly grasping the bat')
                    print('as you continue down the hall, you hear a buzz on what seems to be a loudspeaker followed by a slight noise rather similar to breathing, followed by the same silence that accompanied you before')
                    print('')
            if decision == 'b':
                print('You pick up both and you down a few painkillers and sit around for a little to let them kick in.')
                for i in range(20):
                    print('.')
                print('You feel the painkillers set in and now try to stand')
                print('With a little wince of pain you get up reluctantly but alas can stand')
                print('You swing the bat over your shoulder.')
                print('Do you go down the hallway towards the staircase or turn left to explore the floor?')
                decision = input('a or b')
                if decision == 'a':
                    print('you start to tread down the hallway, firmly grasping the bat')
                    print('as you continue down the hall, you hear a buzz on what seems to be a loudspeaker followed by a slight noise rather similar to breathing, followed by the same silence that accompanied you before')
                    print('')

    else:
            continue

