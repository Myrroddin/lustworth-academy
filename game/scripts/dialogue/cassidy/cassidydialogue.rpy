#QUESTS
default quests.cassidyFirstFuck = LOCKED

label cassidydialogue:
    hide screen freeroamhud with None
    stop music
    show cassidy neutral
    with dissolve
    jump .dialogmenu

label .dialogmenu:
    menu:
        "Nevermind.":
            pass
    $ gotoscene('townhousehallway')

label cassidyhalloweendialogue:
    hide screen freeroamhud with None
    $ Cassidy.eventMet[HALLOWEEN_EVENT] = True
    jump halloween_cassidycostumecontest
