#SCREENS
init 1 python:
    scene_defs['schoollibraryplaza'] = {
        'music': MUSIC_SCHOOLGROUNDSAMBIENCEDAY_THEME,
        'altermusic': MUSIC_SCHOOLGROUNDSAMBIENCENIGHT_THEME,
        'maps': {
            'morning':   ("libraryplazafallday", "libraryplazafalldayhover"),
            'afternoon': ("libraryplazafallafter", "libraryplazafallafterhover"),
            'evening':   ("libraryplazafallevening", "libraryplazafalleveninghover"),
            'night':     ("libraryplazafallnight", "libraryplazafallnighthover")
        },
        'hotspots': [
            ('library', (788, 173, 275, 571)),
            ('bed', (1703, 765, 212, 312)),
            ('hopscotch', (391, 823, 576, 127)),
            ('tosouthplaza', (24, 676, 282, 68)),
            ('tosouthplaza2', (0, 968, 1672, 109)),
            ('topeacockplaza', (1673, 0, 246, 745)),
            ('topeacockplaza2', (21, 744, 286, 67)),
        ],
        'sprites': [
            Sprite('wildcrowd', 'wildcrowd01', (400, 580, 499, 271), lambda: quests.cassidyTrials == ACTIVE),
        ]
    }

#LABELS
label schoollibraryplaza:
    if quests.fionaHideAndSeek == ACTIVE:
        call schoollibraryplazacheckderek from _call_schoollibraryplazacheckderek
    $ checkcurfew()
    jump schoollibraryplaza_loop

label schoollibraryplaza_loop:
    $ resetscene()
    call screen map('schoollibraryplaza')
    jump schoollibraryplaza_loop

label schoollibraryplaza_library:
    $ gotoscene('schoollibrarymainhall')

label schoollibraryplaza_bed:
    $ time = calendar.when[2]
    menu:
        "Rest for a while" if time < NIGHT:
            jump nap_menu
        "Nevermind":
            jump schoollibraryplaza_loop
    $ gotoscene('schoollibraryplaza', transition=fade)

label schoollibraryplaza_hopscotch:
    Jimmy "Umm... Don't have time to play hopscotch."
    jump schoollibraryplaza_loop

label schoollibraryplaza_tosouthplaza:
    $ gotoscene('schoolgroundssouthplaza')

label schoollibraryplaza_tosouthplaza2:
    $ gotoscene('schoolgroundssouthplaza')

label schoollibraryplaza_topeacockplaza:
    $ gotoscene('schoolgroundspeacockplaza')

label schoollibraryplaza_topeacockplaza2:
    $ gotoscene('schoolgroundspeacockplaza')

label schoollibraryplaza_wildcrowd:
    Jimmy "Umm... What's all the fuss about?"
    call cassidytrialsbanana from _call_cassidytrialsbanana
    jump schoollibraryplaza_loop

label schoollibraryplazacheckderek:
    if FionaDonutFound == False:
        Derek "Warm..."
        return     
    elif FionaWineFound == False:
        Derek "Very cold."
        return
    else:
        return