default quests.christyMandyVoltium = LOCKED

label mandydialogue:
    hide screen freeroamhud with None
    # stop music
    # show jimmy neutral
    # show mandy neutral
    # with dissolve
    # jump .dialogmenu

# label .dialogmenu:
#     menu:
#         "Nevermind.":
#             pass
#     $ gotoscene('mainbuildingentrance')

label mandyhalloweendialogue:
    hide screen freeroamhud with None
    jump christyandmandyvoltiumquest
