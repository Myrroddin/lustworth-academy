#VARIABLES

#SCREENS
init 1 python:
    scene_defs['schoolgroundsentrance'] = {
        'music': MUSIC_SCHOOLGROUNDSAMBIENCEDAY_THEME,
        'altermusic': MUSIC_SCHOOLGROUNDSAMBIENCENIGHT_THEME,
        'maps': {
            'morning':   ("entranceplazafallday", "entranceplazafalldayhover"),
            'afternoon': ("entranceplazafallafternoon", "entranceplazafallafternoonhover"),
            'evening':   ("entranceplazafallevening", "entranceplazafalleveninghover"),
            'night':     ("entranceplazafallnight", "entranceplazafallnighthover")
        },
        'hotspots': [
            ('boysdorm', (0, 326, 289, 752)),
            ('girlsdorm', (1618, 401, 301, 676)),
            ('tosouthplaza', (717, 269, 475, 572)),
            ('frontgate', (373, 869, 1179, 209)),
        ],
        'sprites': [
            # Sprite(key, image, (x, y, w, h), showif)
        ]
    }

#LABELS
label schoolgroundsentrance:
    if quests.fionaHideAndSeek == ACTIVE:
        call schoolgroundsentrancecheckderek from _call_schoolgroundsentrancecheckderek
    $ checkcurfew()
    jump schoolgroundsentrance_loop

label schoolgroundsentrance_loop:
    $ resetscene()
    call screen map('schoolgroundsentrance')
    jump schoolgroundsentrance_loop

label schoolgroundsentrance_boysdorm:
    $ gotoscene('boysdormplaza')

label schoolgroundsentrance_girlsdorm:
    $ gotoscene('girlsdormfrontgate')

label schoolgroundsentrance_tosouthplaza:
    $ gotoscene('schoolgroundssouthplaza')

label schoolgroundsentrance_frontgate:
    if quests.fionaHideAndSeek == ACTIVE:
        Derek "No need to go outside the campus, new guy."
        Derek "Look somewhere else..."
        jump schoolgroundsentrance_loop
    $ gotoscene('schoolgroundsmaingate')

label schoolgroundsentrancecheckderek:
    if FionaDonutFound == False:
        Derek "Ice ice, baby..."
        return     
    elif FionaWineFound == False:
        Derek "Very cold."
        return
    else:
        return