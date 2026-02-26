#VARIABLES
default mainbuildingentrance.camembertCaught = False

#SCREENS
init 1 python:
    def mainbuildingentrance_showif_headmastersdoor():
        if calendar.when[1] not in [TUESDAY, THURSDAY]:
            return True
        if calendar.when[2] != EVENING:
            return True
        return False

    scene_defs['mainbuildingentrance'] = {
        'music': MUSIC_MAINBUILDINGAMBIENCEDAY_THEME,
        'altermusic': MUSIC_MAINBUILDINGAMBIENCEDAY_THEME,
        'maps': {
            'morning':   ("schoolhallfallday", "schoolhallfalldayhover"),
            'afternoon': ("schoolhallfallafter", "schoolhallfallafterhover"),
            'evening':   ("schoolhallfallevening", "schoolhallfalleveninghover"),
            'night':     ("schoolhallfallnight", "schoolhallfallnighthover")
        },
        'hotspots': [
            ('lefthallway', (191, 406, 171, 255)),
            ('righthallway', (1448, 427, 197, 233)),
            ('leftstairs', (472, 431, 280, 236)),
            ('rightstairs', (1045, 422, 237, 238)),
            ('auditorium', (1433, 139, 142, 183)),
            ('yearbook', (785, 427, 237, 244)),
            ('secretaryoffice', (500, 237, 223, 135)),
            ('exit', (0, 834, 1920, 231)),
            ('conciergeroom', (1076, 242, 135, 130)),
            ('2ndfloorleft', (194, 76, 151, 216)),
        ],
        'sprites': [
        ]
    }

#LABELS
label mainbuildingentrance:
    $ checkcurfew()
    if Jimmy.outfit != JIMMY_UNIFORM:
        jump mainbuildingentrance_camembertcaught
    jump mainbuildingentrance_loop

label mainbuildingentrance_loop:
    $ resetscene()
    call screen map('mainbuildingentrance')
    jump mainbuildingentrance_loop

label mainbuildingentrance_lefthallway:
    $ gotoscene('mainbuildinglefthallway')

label mainbuildingentrance_righthallway:
    $ gotoscene('mainbuildingrighthallway')

label mainbuildingentrance_leftstairs:
    $ gotoscene('mainbuildingsecretarysoffice')

label mainbuildingentrance_rightstairs:
    if calendar.when[2] in [EVENING]:
        if quests.euniceTheaterpractice == SATISFIED:
            if MikuDaylimit == False:
                jump queenletticiarescueintro
    $ gotoscene('mainbuildingauditorium')

label mainbuildingentrance_auditorium:
    if calendar.when[2] in [EVENING]:
        if quests.euniceTheaterpractice == SATISFIED:
            if MikuDaylimit == False:
                jump queenletticiarescueintro
    $ gotoscene('mainbuildingauditorium')

label mainbuildingentrance_2ndfloorleft:
    $ gotoscene('mainbuildinginfirmary')

label mainbuildingentrance_yearbook:
    jump yearbook

label mainbuildingentrance_secretaryoffice:
    $ gotoscene('mainbuildingsecretarysoffice')

label mainbuildingentrance_exit:
    $ gotoscene('schoolgroundssouthplaza')

label mainbuildingentrance_headmastersdoor:
    __("Office hours: Tuesday and Thursday evenings.")
    jump mainbuildingentrance_loop

label mainbuildingentrance_conciergeroom:
    if quests.missdawsonAssistant == ACTIVE:
        if quests.missdawsonAssistantMarlon == LOCKED:
            jump marlontheconciergeintro
    __("The concierge room. It's locked.")
    jump mainbuildingentrance_loop

label mainbuildingentrance_camembertcaught:
    hide screen freeroamhud
    show jimmy neutral with dissolve
    show camembert with vpunch
    Camembert "What do you think you're doing, young man!"
    Camembert "Why aren't you wearing your uniform?"
    Camembert "Go get changed now, or you'll get detention."
    Jimmy talk "Yeah, whatever..."
    $ mainbuildingentrance.camembertCaught = True
    $ gotoscene('boysdormplaza')

label marlontheconciergeintro:
    hide screen freeroamhud
    Jimmy "This is the concierge room. Let's see..."
    __("*Knock* *Knock*.")
    Marlon "Come in!"
    play sound "audio/sfx/dooropen01.ogg"
    scene conciergestorageroom with fade
    show marlonconciergeintro with dissolve
    play music MUSIC_MARLONS_THEME
    __("When [player_name] entered the room, he saw an old man sitting in a chair while petting a golden cat.")
    Jimmy "Good day, sir."
    Jimmy "Miss Dawson asked me to deliver this memo to you."
    if quests.missdawsonAssistantEdna == COMPLETE:
        $ Jimmy.inventory.remove(ItemMemos02)
    else:
        $ Jimmy.inventory.remove(ItemMemos01)
        call item_pickup(ItemMemos02) from _call_item_pickup_24
    Marlon "Good day to you, my lad."
    Marlon "Please, make an old man a favor and read it for me, will ya?"
    Marlon "I'm not sure where I left my glasses."
    Jimmy "No problem, sir."
    Jimmy "It says: 'Mr. Shelby, the Halloween festivities are getting close and a reunion for the staff and teachers of the academy will be held at the Cafeteria..."
    Jimmy "It would be appreciated if you help us with the preparations regarding the maintenance of the place.'"
    Marlon "Oh, orders from above I see..."
    $ Marlon.met = True
    Marlon "Thank you, lad. My name is Marlon, by the way."
    Jimmy "[player_name], sir. It's a pleasure."
    Marlon "The pleasure is mine, lad."
    __("'I like this guy', thought [player_name].")
    $ quests.missdawsonAssistantMarlon = COMPLETE
    $ gotoscene('mainbuildingentrance')
