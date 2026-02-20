#SCREENS
init 1 python:
    def mainbuildingcafeteria_showif_eunice():
        if calendar.when[0] == PROLOGUE:
            return False
        if not chapter1.introCutscene:
            return False
        if quests.euniceChocolates == COMPLETE:
            if quests.euniceGettingtherole != COMPLETE:
                return False
        if quests.euniceGettingtherole == COMPLETE:
            if quests.euniceTheaterpractice != COMPLETE:
                return False
        # if calendar.when[2] in [EVENING, NIGHT]:
        #     return False
        return True

    scene_defs['mainbuildingcafeteria'] = {
        'music': MUSIC_CAFETERIAAMBIENCEDAY_THEME,
        'altermusic': MUSIC_MAINBUILDINGAMBIENCENIGHT_THEME,
        'maps': {
            'default': ("cafeteriafallday", "cafeteriafalldayhover"),
        },
        'hotspots': [
            ('kitchen', (1750, 302, 171, 353)),
            ('exit', (0, 881, 1918, 199)),
        ],
        'sprites': [
            Sprite('eunice', 'eunicedialog01', (1344, 432, 234, 621), mainbuildingcafeteria_showif_eunice),
        ]
    }

#LABELS
label mainbuildingcafeteria:
    $ checkcurfew()
    jump mainbuildingcafeteria_loop

label mainbuildingcafeteria_loop:
    $ resetscene()
    call screen map('mainbuildingcafeteria')
    jump mainbuildingcafeteria_loop

label mainbuildingcafeteria_exit:
    $ gotoscene('mainbuildinglefthallway')

label mainbuildingcafeteria_eunice:
    hide eunicedialog01
    if EuniceDaylimit == True:
        show eunice uniform neutral with dissolve
        Jimmy "*She look busy today.*"
        Jimmy "*Let's talk another time.*"
        jump mainbuildingcafeteria_loop
    jump eunicedialogue

label mainbuildingcafeteria_kitchen:
    if quests.missdawsonAssistant == ACTIVE:
        if quests.missdawsonAssistantEdna == LOCKED:
            jump ednathecookintro
    "That's the kitchen, it's smells awful in there."
    jump mainbuildingcafeteria_loop

label ednathecookintro:
    hide screen freeroamhud
    play music MUSIC_KITCHENAMBIENCEDAY_THEME
    scene schoolkitchendayfall with fade
    Jimmy "What the hell is that smell? Ugh..."
    play music MUSIC_EDNA_THEME
    show edna cook neutral with dissolve
    $ Edna.met = True
    Edna "That, boy! Is the smell of Edna's culinary art."
    Edna "You know, some chicken legs that have been resting for days in a broken fridge."
    play sound "audio/sfx/ednalaugh.ogg"
    Edna "But! Don't worry, fire will make it edible, ha ha ha ha!"
    Jimmy "Well, I don't wanna know the rest."
    Jimmy "Miss Dawson asked me to deliver this memo to you, Miss."
    if quests.missdawsonAssistantMarlon == COMPLETE:
        $ Jimmy.inventory.remove(ItemMemos02)
    else:
        $ Jimmy.inventory.remove(ItemMemos01)
        call item_pickup(ItemMemos02) from _call_item_pickup_23
    hide edna with dissolve
    show edna cook daring with dissolve
    Edna "Ahh! That uptight bitch! What does she want now!?"
    Edna reading memo "Fuck me in the ass! I have to work extra hours on Halloween!?"
    Edna cook daring "What the fuck is this shit!?"
    Edna "Go back to that bitch, kiddo."
    Edna "And tell her that if she wants food for that stupid reunion, she can make it herself."
    Edna "I'm gonna be off to the beach that weekend."
    play sound "audio/sfx/ednaahgorgeous.ogg"
    Jimmy "Whatever..."
    $ quests.missdawsonAssistantEdna = COMPLETE
    $ gotoscene('mainbuildingcafeteria')
    