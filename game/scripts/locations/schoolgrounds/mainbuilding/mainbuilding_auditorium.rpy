#SCREENS
init 1 python:
    scene_defs['mainbuildingauditorium'] = {
        'music': MUSIC_MAINBUILDINGAMBIENCEDAY_THEME,
        'altermusic': MUSIC_MAINBUILDINGAMBIENCENIGHT_THEME,
        'maps': {
            'morning':   ("auditoriumhallfallday", "auditoriumhallfalldayhover"),
            'afternoon': ("auditoriumhallfallafternoon", "auditoriumhallfallafternoonhover"),
            'evening':   ("auditoriumhallfallevening", "auditoriumhallfalleveninghover"),
            'night':     ("auditoriumhallfallnight", "auditoriumhallfallnighthover")
        },
        'hotspots': [
            ('infoboard', (1459, 498, 131, 163)),
            ('mainstage', (575, 77, 819, 584)),
            ('posters', (0, 251, 319, 323)),
            ('backstage', (314, 566, 166, 180)),
            ('exit', (0, 843, 1916, 233)),
        ],
        'sprites': [
        ]
    }

#LABELS
label mainbuildingauditorium:
    if calendar.when[1:] == (FRIDAY, EVENING):
        if quests.punnyPrivateLessons == SATISFIED:
            jump misspunnydancinglesson
    $ checkcurfew()
    jump mainbuildingauditorium_loop

label mainbuildingauditorium_loop:
    $ resetscene()
    call screen map('mainbuildingauditorium')
    jump mainbuildingauditorium_loop

label mainbuildingauditorium_infoboard:
    "Trustworth's has talent! festival will be celebrated during the holydays."
    "It's a competition, I think. A talent competition."
    jump mainbuildingauditorium_loop

label mainbuildingauditorium_exit:
    $ gotoscene('mainbuildingentrance')

label mainbuildingauditorium_mainstage:
    "Being up there has to make you feel all powerful or frightened, depends on the pussy meter."
    jump mainbuildingauditorium_loop

label mainbuildingauditorium_posters:
    "Vote for your Class President! The nerds and the preps are fighting for this one."
    jump mainbuildingauditorium_loop

label mainbuildingauditorium_backstage:
    $ gotoscene('mainbuildingbackstage')
