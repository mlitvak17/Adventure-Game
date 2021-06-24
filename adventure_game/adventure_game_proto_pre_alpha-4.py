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
print('1. Check your pockets for their contents')
print('2. Attempt to stand up.')
print('3. Go back to sleep')
n = int(input('Enter 1, 2, or 3\n'))
while 0 == 0:
    if n == 1:
        print('You check your pockets and find a lighter, and a crumpled a piece of paper.')
        break
    elif n == 2:
        print('You attempt to stand up but to no avail.')
    elif n == 3:
        print('You go back to sleep.')
    else:
        print('You did not enter an integer between 1 and 3.')
if (n == 1) or (n == 2) or (n == 3):
    print('you unroll the paper to find a simple phrase scribbled on it in what seems to be ink, in the light of your lighter\n*Trust the Process*')
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
        if decision == 'a':
            print('you pick up the painkillers and down a few and sit around for a little to let them kick in')
            print('the loudspeaker kicks on and in a scratchy voice you hear "a fighter...interesting"')
            for i in range(20):
                print('.')
            print('You feel the painkillers set in and now try to stand')
            print('With a little wince of pain you get up reluctantly but alas can stand')
            print('You grab the bat on the ground and look onward towards the hallway')
            print('do you go down the hallway towards the staircase or turn left to explore the floor')
            decision = input('a or b')
            if decision == 'a':
                print('you start to tread down the hallway, firmly grasping the bat')
                print('as you continue down the hall, you hear a buzz on what seems to be a loudspeaker followed by a slight noise rather similar to breathing, followed by the same silence that accompanied you before')
                print('you hear a sharp fizzing noise followed by a pop')
                print('The hallway lights fizz out and you are left to the pitch black of before')
                print('Do you pull out your lighter or do you trust you remember where the stair door was')
                decision = input('a or b')
                if decision == 'a':
                    print('You reach for your lighter but feel nothing left in your pocket but the scrap of paper with\n*Trust the process*\nscrawled on it')
                    print('The all but familiar static of the loud speaker is heard again')
                    print('The voice speaks again saying in a rather raspy older bodied voice \n"Ahhhhh Do you not Trust %s?"' % name)
                    print('You stand in the darkness trembling, feeling light headed, with pain bolting down your leg with every step you do and dont take')
                    print('Do you respond to the voice?')
                    decsion = input('a or b')
                    if decision == 'a':
                        print('What do you say?')
                        speech = input()
                        print('%s...interesting...you must trust %s, its the only way' % (speech, name))
                        print('you scream "WHAT DO YOU MEAN???"')
                        print('the loudspeaker fizzes out and the voice never responds')
                        print('you decide to sit down a regroup')
                        for i in range(60):
                            print('.')
                        print('You look up and notice that two strips of purple light are turning on dully on the ceiling')
                        print('Upon futher evaluation you notice the walls are slightly glowing but not fully, only in some sort of distinct shape')
                        print('They seem to resemble a path with the phrase \n*Trust*\n scrawled on the wall in blood and the logo of a corporation that looks somewhat familiar')
                        print('You get up and decide to follow the path on the wall and it leads you to the stairway door')
                        print('You open the door and find not a staricase but an elongated roo, with what seems to be a figure sitting down, staring out a window')
                        print('You move closer into the room and pause for a second')
                        print('A great metal clap is heard from behind you and you find that the door that you entered through is no longer existant')
                        print('Do you approach the figure or call to them at a distance?')
                        decision = input('a or b')
                        if decision == 'a':
                            print('You slowly approach the figure masked in shadow')
                            print('In the faint light coming from the window you find the figure to have a bag over head and be tied at both hand and foot')
                            print('In the corner of the room a television monitor comes to life showing a screen of static, with the static noise filling your ears')
                            print('Attached to the monitor is a note not unlike the one you found earlier in your pocket')
                            print('*Choose from the three')
                            print('You ask what the note means and the television comes into focus revealing a woman not unlike that of the man presented before you, tied and gagged')
                            print('Do you ask who the third is or choose from the two?')
                            decision = input('a or b')
                            if decision == 'a':
                                print('The sizzle and static of the loudspeaker can be heard yet again')
                                print('"are there not three individuals in your presence"')
                                print('You ask as to who the two indivduals are')
                                print('"The man sitting before your eyes is an indivdual that resides in deaths row"')
                                print('"The woman before you...you know her"')
                                print('You ask who the third individual is and you recieve silence in response as the loudspeaker comes to a halt, replacing the voice again with static')
                            else:
                                pass                               
                    else:
                        pass
                else:
                    pass
            else:
                pass
        
