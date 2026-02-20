label petedialogue:
    hide screen freeroamhud with None
    #stop music
    show jimmy neutral
    show pete uniform neutral
    with dissolve
    Pete "Hey [player_name], what's up?"
    jump .dialogmenu

label .dialogmenu:
    menu:
        "Ask about Derek" if quests.fionaConfrontDerek == ACTIVE:
            Jimmy talk "Have you seen Derek?"
            Pete "Derek? You mean the bully who's always harassing the girls on campus?"
            if Derek.met:
                Jimmy "Yeah, that's the one."
            else:
                Jimmy "I guess so, he fits the description."
            Pete "Why would you want to talk to him?"
            Jimmy smug "Let's just say, I've got an important message to give him."
            Pete "Actually, I think I saw him loitering around in the back alley."
            Jimmy "Alright, thanks Pete."
            jump .dialogmenu
        "Ask about the Halloween Plan" if quests.garyHalloweenHeist == ACTIVE:
            Jimmy "Hey, can you remind me where to find the spray paint?"
            Pete "Oh, yeah, look in the garage's junkyard."
            Pete "The greasers should have some used cans of spray paint tossed around."
            Jimmy "Right, thanks Pete."
            jump .dialogmenu
        "Ask about the Halloween Plan" if quests.garyHalloweenHeist == SATISFIED:
            Jimmy "Hey, Pete. Where can I find an invitation to the Halloween party?"
            Pete "I heard the headmaster's secretary has one decomissioned in her office."
            Pete "If you can find a way to get it, that'd be great."
            Jimmy "Alright, thanks Pete."
            jump .dialogmenu
        "How can I go to Town during the weekend?" if not calendar.event == HALLOWEEN_EVENT:
            Jimmy "Pete, can you remind me how can I go to Town during the weekend?"
            Pete "Well, right now students only have permission to go to town during the weekend."
            Pete "The bus comes every Friday evening, but monitors won't let you take the bus if you're wearing your uniform."
            Pete "So, change your clothes and take the bus on Friday evening and you'll be able to spend the weekend in town."
            Jimmy "Right, thanks, pal."
            Pete "Anytime."
            jump .dialogmenu
        "Nevermind":
            pass
    $ gotoscene('boysdormtvroom')

label petehalloweendialogue:
    hide screen freeroamhud with None
    show pete bunny salute with dissolve
    play sound "audio/sfx/heypete01.ogg"
    Pete "Hey [player_name], what's up?"
    jump .dialogmenu

label .dialogmenu:
    $ isBartender = (quests.fionaBartender == COMPLETE)
    menu:
        "Ask about the graffiti message" if quests.halloweenGraffitiMessage == ACTIVE:
            Jimmy "Hey Pete. Can you remind me what I should do with the spray paint?"
            Pete neutral "You need to leave a message of some kind in a room that the preps frequently visit."
            Pete "The bar seems like the perfect place, but there is too much people in there."
            Pete "Maybe you can find another place."
            jump .dialogmenu
        "Ask about the laxative plan" if quests.halloweenFruitPunch == ACTIVE:
            Jimmy "Hey Pete, what are we going to do with the laxative?"
            Pete neutral "I need to get close to the bar."
            Pete "I suspect the preps like drinking cocktails like fruit punch, so maybe we can use the laxative on those drinks."
            Pete shy "Obviously, the bartender won't let me even smell it."
            Pete neutral "So, if you can help me get rid of the bartender for a while, that'd be great."
            jump .dialogmenu
        "Ask about the flag" if quests.halloweenFakeFlag == ACTIVE:
            Jimmy "Hey Pete, what's up with the flag?"
            Pete shy "Don't ask Gary where he got it."
            Pete neutral "Just go to the roof and change the flags."
            Jimmy "Alright, thanks Pete."
            jump .dialogmenu
        "Ask for a drink for Beatrix" if isBartender:
            Jimmy "Do you have anything non-alcoholic back there?"
            Pete "Nope, it's alcohol everywhere."
            Jimmy "Alright. Thanks anyway."
            jump .dialogmenu
        "Mention the bartender search" if quests.fionaBartender == ACTIVE:
            Jimmy "Pete, this is our lucky night. The bartender is looking for someone to help serve drinks at the bar while she takes a break."
            Jimmy "It might be a way to get you closer to the drinks."
            Pete "Great idea, [player_name]."
            Pete "I mean, I don't really like to deal with people, but..."
            Pete "Ughh... I just want to get done with this."
            Jimmy "Let's do it, pal."
            $ quests.fionaBartender = SATISFIED
            $ quests.halloweenFruitPunch = COMPLETE
            jump fionabartenderquest
        "Nevermind":
            pass
    if isBartender:
        $ gotoscene('harrisonhousebar')
    $ gotoscene('harrisonhouseentrance')
