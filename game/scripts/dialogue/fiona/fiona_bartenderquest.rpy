default fionabartenderquest.introConversation = False

label fionabartenderquest:
    if quests.fionaBartender == LOCKED:
        jump .locked
    elif quests.fionaBartender == ACTIVE:
        jump .active
    elif quests.fionaBartender == SATISFIED:
        jump .satisfied

label .locked:
    Jimmy "Do you want to hang out?"
    Jimmy "Maybe shake our hips to that awful music?"
    Fiona "Ha, ha, ha, ha, ha! Oh, [player_name]."
    Fiona "I would love to, but I'm really busy right now."
    Fiona "If I could find someone to take over for a while, maybe we could hang out."
    Jimmy "Let me see if I can find someone to help."
    Fiona "I know you will, tiger."
    $ quests.fionaBartender = ACTIVE
    jump fionahalloweendialogue.dialogmenu

label .active:
    Fiona "Hey, did you find someone to cover for me?"
    Jimmy "No, not yet."
    Fiona "Oh, well, can I get you something while you're here?"
    jump fionahalloweendialogue.dialogmenu

label .satisfied:
    jump halloween_fionasex
