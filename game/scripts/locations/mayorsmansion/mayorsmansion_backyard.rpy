#VARIABLES
default mayorsmansionbackyard.wendysLightOn = False
default mayorsmansionbackyard.dogComment = False
default mayorsmansionbackyard.doghouseComment = False
default mayorsmansionbackyard.backDoorComment = False
default dogfoodfound = False
default dogsleeping = False
default mansioninfiltrationrewatch = False

#SCREENS
init 1 python:
    scene_defs['mayorsmansionbackyard'] = {
        'music': MUSIC_SNEAK_THEME,
        'altermusic': MUSIC_SNEAK_THEME,
        'maps': {
            'default': ("mayormansionbackyardnight", "mayormansionbackyardnighthover"),
        },
        'hotspots': [
            ('kitchen', (335, 524, 323, 217)),
            ('pool', (762, 894, 836, 184)),
            ('shed', (1533, 571, 386, 312)),
            ('backdoor', (968, 525, 175, 204)),
            ('wendyroom', (956, 196, 192, 300)),
            ('towerwindow1', (1231, 537, 254, 196)),
            ('towerwindow2', (727, 533, 209, 184)),
            ('dog', (1673, 902, 218, 116)),
        ],
        'sprites': [
            Sprite('wendyswindow', 'wendywindowon', (960, 192, 200, 200), lambda: mayorsmansionbackyard.wendysLightOn),
        ]
    }

#LABELS
label mayorsmansionbackyard:
    jump mayorsmansionbackyard_loop

label mayorsmansionbackyard_loop:
    $ resetscene()
    call screen map('mayorsmansionbackyard')
    jump mayorsmansionbackyard_loop

label mayorsmansionbackyard_kitchen:
    if dogsleeping == False:
        if mayorsmansionbackyard.dogComment == True:
            __("I can see someone in there, but the dog won't let me get close.")
        else:
            __("It's a bit dark. I think someone is in there, let's take a look.")
            __("As [player_name] got closer to the mansion, he felt something bumping against his leg.")
            show rocky happy with vpunch
            play music MUSIC_ROCKY_THEME
            __("The dog which seemed to be sleeping, was looking at him and smelling his clothes.")
            __("After a couple of seconds, he stood in front of [player_name] and tilted his head.")
            Jimmy "Hey, pal..."
            Jimmy "Ummm... You're a good, dog, right?"
            Jimmy "Please, don't bark."
            Jimmy "I'm a friend."
            __("I tried to get closer, but the dog showed his teeth and growled.")
            __("I stepped back and the dog started licking his nose and savoring his mouth.")
            Jimmy "Are you hungry, pal?"
            __("The dog blinked and licked his nose, again.")
            Jimmy "Alright, pal. I'll see what I can do."
            __("Fuck, where the hell am I gonna get food for the dog?")
            __("When [player_name] went back to the pool, the dog did the same thing, laying down on the same spot.")
            $ mayorsmansionbackyard.dogComment = True
    elif not mayorsmansionbackyard.wendysLightOn:
        jump prologue_wendykitchen
    else:
        __("Nothing to see here.")
    jump mayorsmansionbackyard_loop

label mayorsmansionbackyard_wendyroom:
    if dogsleeping == False:
        if mayorsmansionbackyard.dogComment == True:
            __("I think I can climb my way up there.")
        else:
            __("Let's take a look.")
            __("As [player_name] got closer to the mansion, he felt something bumping against his leg.")
            show rocky happy with vpunch
            play music MUSIC_ROCKY_THEME
            __("The dog that seemed to be sleeping, was looking at him and smelling his clothes.")
            __("After a couple of seconds, he stood in front of [player_name] and tilted his head.")
            Jimmy "Hey, pal..."
            Jimmy "Ummm... you're a good, dog, right?"
            Jimmy "Please, don't bark."
            Jimmy "I'm a friend."
            __("I tried to get closer, but the dog showed his teeth and growled.")
            __("I stepped back and the dog started licking his nose and savoring his mouth.")
            Jimmy "Are you hungry, pal?"
            __("The dog blinked and licked his nose, again.")
            Jimmy "Alright, pal. I'll see what I can do."
            __("Fuck, where the hell am I gonna get food for the dog?")
            __("When [player_name] went back to the pool, the dog did the same thing, laying down on the same spot.")
            $ mayorsmansionbackyard.dogComment = True
    elif not mayorsmansionbackyard.wendysLightOn:
        __("I think I can climb my way up there.")
        __("I need to find out if Wendy's room is on the first or second floor, before trying.")
    else:
        "Okay, I'm gonna do it."
        jump prologue_wendyinfiltration
    jump mayorsmansionbackyard_loop

label mayorsmansionbackyard_pool:
    __("Nice pool.")
    __("This place could be great for wild party.")
    jump mayorsmansionbackyard_loop

label mayorsmansionbackyard_dog:
    if dogsleeping == True:
        show rocky sleep aftereat with dissolve
        __("He's snoring, I love this dog.")
    elif dogfoodfound == True:
        play music MUSIC_ROCKY_THEME
        show rocky happy with vpunch
        Jimmy "Alright pal, here's your food."
        $ dogsleeping = True
        __("The dog jumped on the food spreading it everywhere.")
        hide rocky happy with dissolve
        show rocky sleep aftereat with dissolve
        __("With his stomach full, he stumbled a couple of steps away from the bag and went to sleep.")
    else:
        if mayorsmansionbackyard.dogComment == True:
            __("If I find some food, maybe he won't bother me anymore.")
        else:
            __("I should be careful not to wake him up.")
    jump mayorsmansionbackyard_loop

label mayorsmansionbackyard_shed:
    if dogfoodfound == False:
        if mayorsmansionbackyard.dogComment == True:
            __("Maybe I can find something useful in there.")
            show dogfooditem with dissolve
            Jimmy "Jackpot!"
            $ dogfoodfound = True
    else:
        __("Nothing to see there.")
    jump mayorsmansionbackyard_loop

label mayorsmansionbackyard_backdoor:
    if dogsleeping == False:
        if mayorsmansionbackyard.dogComment == True:
            if not mayorsmansionbackyard.backDoorComment:
                __("Maybe I can get in through that door.")
            else:
                __("The back door is locked.")
                $ mayorsmansionbackyard.backDoorComment = True
        else:
            __("Let's take a look.")
            __("As [player_name] got closer to the mansion, he felt something bumping against his leg.")
            show rocky happy with vpunch
            play music MUSIC_ROCKY_THEME
            __("The dog that seemed to be sleeping, was looking at him and smelling his clothes.")
            __("After a couple of seconds, he stood in front of [player_name] and tilted his head.")
            Jimmy "Hey, pal..."
            Jimmy "Ummm... you're a good, dog, right?"
            Jimmy "Please, don't bark."
            Jimmy "I'm a friend."
            __(" [player_name] tried to get closer, but the dog showed his teeth and growled.")
            __(" [player_name] stepped back and the dog started licking his nose and savoring his mouth.")
            Jimmy "Are you hungry, pal?"
            __("The dog blinked and licked his nose, again.")
            Jimmy "Alright, pal. I'll see what I can do."
            __("Fuck, where the hell am I gonna get food for the dog?")
            __("When [player_name] went back to the pool, the dog did the same thing, laying down on the same spot.")
            $ mayorsmansionbackyard.dogComment = True
    elif not mayorsmansionbackyard.backDoorComment:
        __("The back door is locked.")
        $ mayorsmansionbackyard.backDoorComment = True
    else:
        __("It's locked.")
        __("I'll have to find another way.")
    jump mayorsmansionbackyard_loop

label mayorsmansionbackyard_towerwindow1:
    __("I think I see some kind of library, but it's really dark.")
    jump mayorsmansionbackyard_loop

label mayorsmansionbackyard_towerwindow2:
    __("It's too dark to see inside.")
    jump mayorsmansionbackyard_loop

label mayorsmansionbackyard_wendyswindow:
    __("That's Wendy's room.")
    __("Okay, I'm gonna do it.")
    jump prologue_wendyinfiltration
