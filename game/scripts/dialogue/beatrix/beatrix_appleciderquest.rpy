label beatrixappleciderquest:
    if quests.beatrixAppleCider == LOCKED:
        jump .intro
    elif quests.beatrixAppleCider == ACTIVE:
        jump .active
    elif quests.beatrixAppleCider == SATISFIED:
        jump .satisfied

label .intro:
    jump halloween_beatrixappleciderintro

label .active:
    show beatrix neutral mavis with dissolve
    Beatrix "Well? Did you find something to drink?"
    Jimmy "Not yet, still looking."
    Beatrix "Look harder then!"
    $ gotoscene('harrisonhousebar')

label .satisfied:
    jump halloween_beatrixapplecidersatisfied
