label rubydialogue:
    hide screen freeroamhud with None
    # stop music
    # show jimmy neutral
    # show ruby neutral
    # with dissolve
    # jump .dialogmenu

# label .dialogmenu:
#     menu:
#         "Nevermind.":
#             pass
#     $ gotoscene('mainbuildingentrance')

label rubyhalloweendialogue:
    hide screen freeroamhud with None
    $ Ruby.eventMet[HALLOWEEN_EVENT] = True
    jump halloween_rubycostumecontest
