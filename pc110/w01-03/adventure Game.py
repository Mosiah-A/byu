#Author: Mosiah Andrade

#Pourpose: Adventure Game

#adds: I add a loop to alway the user input a worng answere return to the prompt again


valid = False # check the answere


while valid == False:
    #scenarie 1.1
    choice = input("You are walking through a dark street, in the end you can Tun the RIGHT or LEFT, what is your choice? \n")

    if choice.lower() == 'right':
        while not valid:
            #scenarie 2.1
            print('')
            choice = input('You Turn the right. In this side of street, you see a bandit, do you want RUN or FIGHT? \n')

            if choice.lower() == 'run':
                while not valid:
                    #scenarie 3.1
                    print('')
                    choice = input('You run. This bandit runs behind you. In front of you, have a fence, you JUMP the fence or STOP running?\n')

                    if choice.lower() == 'jump':
                        print('')
                        print('You try to jump the fence, but you fell on the ground. when you look at to the bandit, you not see him. maybe was a ghost.\n')
                        valid = True

                    elif choice.lower() == 'stop':
                        print('')
                        print('You stop running, and you turn around and look at the bandit and he stops to running too, when he be closer, you recognize him, he is your friend Mike. you were just scarry.\n')
                        valid = True

                    else:
                        print('YOUR ANSWERE IS INVALID')
                        print('')
            elif choice.lower() == 'fight':
                #scnenarie 3.2
                print('')
                print('You fight with him. he is more strong than you and you faints.')
                choice = input('You return to consciousness. you are stuck in a room, you see a window and a door. you wans to see the WINDOW, or check the DOOR or WAIT?\n')

                if choice.lower() == 'window':
                    #scenarie 4.1
                    print('')
                    print('You are shouting at the people outside, and one cop listen you. Congretulation. you are free. ')
                    valid = True

                elif choice.lower() == 'door':
                    #scenarie 4
                    print('')
                    print('You check the door. Surprise, it is open! you are Free')
                    valid = True

                elif choice.lower() == 'wait':
                    print('')
                    print('After some minuter the door open, it is your friend Mike he will save you.')
                else:
                    print('YOUR ANSWERE IS INVALID')
                    print('')

            else:
                print('YOUR ANSWERE IS INVALID')
                print('')

    elif choice.lower() == 'left':
         while not valid:
            print('')
            choice = input('You turn the left, this side of street has a large camp of flower and a big gold house. you want to SMELL one flower or ENTER the bis gold house? \n')

            if choice.lower() == 'smell':
                print('')
                print('You smell one flower. and you sneezed, you are alergic.')
                valid = True

            elif choice.lower() == 'enter':
                print('')
                print('You enter the big gold house. it is a genius house, congratulation you have three Wishes')
                valid = True

            else:
                 print('YOUR ANSWERE IS INVALID')
                 print('')

    else:
        print('YOUR ANSWERE IS INVALID')

