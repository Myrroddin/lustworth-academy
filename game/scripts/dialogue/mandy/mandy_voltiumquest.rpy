# Christy and Mandy dialogue
label christyandmandyvoltiumquest:
    hide screen freeroamhud
    if quests.christyMandyVoltium ==  LOCKED:
        jump .locked
    elif quests.christyMandyVoltium == ACTIVE:
        jump .active
    elif quests.christyMandyVoltium == SATISFIED:
        jump .satisfied

label .locked:
    jump halloween_christyandmandypoolintro

label .active:
    scene harrisonhousepool with fade
    show jimmy neutral
    show christy pokemon
    with dissolve
    Christy "[player_name], did you find the pills?"
    Jimmy "I'm still working on it."
    Christy "Well, hurry up, okay? We want to get this party started!"
    $ gotoscene('harrisonhouseentrance', transition=fade)

label .satisfied:
    jump halloween_christyandmandypoolsex
