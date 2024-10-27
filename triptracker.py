import Moneyleft as ML
import SA
import time

def check_end():
    while True:
        tf = input('end? y/n\n')
        if tf == 'y':
            print('bye')
            return False
        elif tf == 'n':
            print('restarting.')
            time.sleep(2.5)
            print('restarting..')
            time.sleep(2.5)
            print('restarting...\n')
            time.sleep(2.5)
            return True
        else:
            print('that is not an option\n')

# Main loop
rd = True

while rd:
    try:
        c = int(input('1) money left \n2) check cost of each item\n3) end\n4) dishes done\n5) rake leaves\n6) weed the garden\n7) lawn mowed\n8) trash collected and taken out\n'))
    except ValueError:
        print("Please enter a valid number.\n")
        continue
    
    if c == 1:
        print(ML.Owes)
        rd = check_end()
    
    elif c == 2:
        print('mowed lawn = 20\ntrash collected and taken out = 5\ndishes done = 5\nrake leaves = 15\nweed the garden = 5')
        rd = check_end()


    elif c == 3:
        print('okay bye')
        rd = False

    elif c == 4:
        SA.sa(5)
        rd = check_end()

    elif c == 5:
        SA.sa(15)
        rd = check_end()

    elif c == 6:
        SA.sa(5)
        rd = check_end()
    
    elif c == 7:
        SA.sa(20)
        rd = check_end()

    elif c == 8:
        SA.sa(5)
        rd = check_end()

    else:
        print('that is not an option\n')
