print("""███████████████████████████
███████▀▀▀░░░░░░░▀▀▀███████
████▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░░░▄███████
██████████▄▄▄▄▄▄▄██████████
███████████████████████████""")


print("""\n\nWELCOME TO KODI'S ADVENTURE GAME!
    
    Let's start the action! 💀😈💀
     
    You wake up, sweating, scared and unsure of where you are but its dark. Looking down you're in bed and you can see the palpitations of fear through your shirt.
    You're in an unrecognizable childs room. Slowly you begin to get up with, no phone, no weapon and no idea of whats going on. 
    Suddenly you hear a rustling from what barely appears to be a closet in the thick darkness. You see a door in the corner and run for it. as you open the door you see three options. 
    The stairs to the left, a door directly in front of you or down the dark hallway to the right.
""")

answer1 = input("Type your choice: left, right or straight?\n")

if(answer1.upper()=="RIGHT"):
    print("\nYou take off down the dark hallway as the lack of light envelopes you. The darkness is thick and heavy. After a minute you try to go back the way you came. You run for what feels like hours.\nIt's black there are no more walls, forever you'll be lost here, game over.\n")

elif(answer1.upper()=="LEFT"):
    print("\n You run down the stairs and fall towards the end. Landing on your butt you slide down the last three steps. Stand up, it's time to get out of here.\n")
    answer2 = input(" You hear rustling in the livingroom to your left and you see a light on in the kitchen to your right. Which way should you go to get out of this nightmare?\n")
    if(answer2.upper()=="LEFT"):
        print("\n    You walk into the room, slip on a banana peel and fall to your death.🍌\n")
    elif(answer2.upper()=="RIGHT"):
        print("""\n    Entering the kitchen you see a little girl sitting on the floor. you dont recognize her and she does not speak. Her hair is long and dark brown as she faces the opposite direction.
    To your left theres a door, it's open and you can see the outside. as you stand there for a moment, about to walk out the door, you notice the little girl is choking.
    you hear her sputtering for air weakly.\n""")
       
        finalAnswer = input("your choices are: run or help\n")
        if(finalAnswer.upper()=="RUN"):
            print("\n    You run out the door and as you look back you see a large black monster stepping out of what appears to be the little girls chest. You wake up in your bed, \nyou have survived my game.🎖️\n\n")
        elif(finalAnswer.upper()=="HELP"):
            print("""\n    You run over to the little girl 'Are you ok?' you ask. As you turn her around a large black hand reaches out of her throat and mouth, to grab you by the bottom of your jaw.
    the arms pulls you into the girls mouth by your jaw. It's dark, you never wake up, game over.\n\n""")
        else:
            print("thats not a correct input")
    else:
        print("thats not a correct input")     
elif(answer1.upper()=="STRAIGHT"):
    print("\n    You open the door and run into the room. Before you realize what is happening youre falling. Two minutes go past, 5 minutes, 10 and then 20. forever you will fall here, game over.\n")

else:
    print("thats not a correct input")

