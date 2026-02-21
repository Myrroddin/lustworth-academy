#VARIABLES
default boysdormhallway.petesRoomChecked = False
default boysdormhallway.garysRoomChecked = False
default boysdormhallway.rastamansRoomChecked = False

#SCREENS
init 1 python:
    scene_defs['boysdormhallway'] = {
        'music': MUSIC_BOYSDORMAMBIENCE02_THEME,
        'altermusic': MUSIC_BOYSDORMAMBIENCENIGHT_THEME,
        'maps': {
            'morning':   ("boysdormhallwayday", "boysdormhallwaydayhover"),
            'afternoon': ("boysdormhallwayafternoon", "boysdormhallwayafternoonhover"),
            'evening':   ("boysdormhallwayevening", "boysdormhallwayeveninghover"),
            'night':     ("boysdormhallwaynight", "boysdormhallwaynighthover")
        },
        'hotspots': [
            ('jimmysroom', (621, 445, 84, 293)),
            ('petesroom', (742, 495, 50, 160)),
            ('garysroom', (1118, 496, 50, 176)),
            ('rastamansroom', (1204, 444, 85, 294)),
            ('tvroom', (0, 116, 278, 935)),
            ('toplaza', (1682, 0, 238, 1077)),
        ],
        'sprites': [
            # Sprite(key, image, (x, y, w, h), showif)
        ]
    }

#LABELS
label boysdormhallway:
    jump boysdormhallway_loop

label boysdormhallway_loop:
    $ resetscene()
    call screen map('boysdormhallway')
    jump boysdormhallway_loop

label boysdormhallway_jimmysroom:
    if not prologue.findJimmysRoom:
        jump prologue_jimmysroomintro
    $ gotoscene('boysdormjimmysroom')

label boysdormhallway_petesroom:
    if not boysdormhallway.petesRoomChecked:
        "\"P. Kowalski.\""
        if not Pete.met:
            "Funny name."
        else:
            "This must be Pete's room."
        $ boysdormhallway.petesRoomChecked = True
    elif not Pete.met:
        "Locked."
    else:
        "Pete's room. It's locked. Guess he's not here right now."
    jump boysdormhallway_loop

label boysdormhallway_garysroom:
    if not boysdormhallway.garysRoomChecked:
        "\"Gary.\" No last name."
        "Some sort of twisted swastika has been carved into the door."
        $ boysdormhallway.garysRoomChecked = True
    elif not Gary.met:
        "Locked."
    else:
        "Gary's room. Don't want to talk him right now."
    jump boysdormhallway_loop

label boysdormhallway_rastamansroom:
    if not boysdormhallway.rastamansRoomChecked:
        "\"Rastaman.\""
        "Cool name."
        $ boysdormhallway.rastamansRoomChecked = True
    else:
        "I can hear reggae music playing from behind the door."
    jump boysdormhallway_loop

label boysdormhallway_tvroom:
    $ gotoscene('boysdormtvroom')

label boysdormhallway_toplaza:
    if calendar.when[2] == NIGHT:
        if prefectpass == True:
            $ gotoscene('boysdormplaza')
        else:
            show camembert with vpunch
            Camembert "Where do you think you're going, young man!"
            Camembert "You should go to bed if you don't want to get in trouble."
            jump boysdormhallway_loop
    else:
        $ gotoscene('boysdormplaza')
