#SCREENS
init 1 python:
    scene_defs['boysdormplaza'] = {
        'music': MUSIC_SCHOOLGROUNDSAMBIENCEDAY_THEME,
        'altermusic': MUSIC_SCHOOLGROUNDSAMBIENCENIGHT_THEME,
        'maps': {
            'morning':   ("boysdormplazafallday", "boysdormplazafalldayhover"),
            'afternoon': ("boysdormplazafallafter", "boysdormplazafallafterhover"),
            'evening':   ("boysdormplazafallevening", "boysdormplazafalleveninghover"),
            'night':     ("boysdormplazafallnight", "boysdormplazafallnighthover")
        },
        'hotspots': [
            ('boysdorm', (508, 579, 189, 375)),
            ('backalley', (1004, 747, 113, 242)),
            ('observatory', (722, 371, 210, 205)),
            ('exit', (1690, 2, 228, 1074)),
        ],
        'sprites': [
            # Sprite(key, image, (x, y, w, h), showif)
        ]
    }

#LABELS
label boysdormplaza:
    $ checkcurfew()
    if quests.fionaHideAndSeek == ACTIVE:
        call boysdormplazacheckderek from _call_boysdormplazacheckderek
    jump boysdormplaza_loop

label boysdormplaza_loop:
    $ resetscene()
    call screen map('boysdormplaza')
    jump boysdormplaza_loop

label boysdormplaza_observatory:
    "The observatory. I think that's where we have astronomy class."
    jump boysdormplaza_loop

label boysdormplaza_backalley:
    if quests.fionaConfrontDerek == ACTIVE:
        if quests.fionaHideAndSeek == LOCKED:
            jump fionaconfrontderekquest.derekfight
    $ gotoscene('boysdormbackalley')

label boysdormplaza_boysdorm:
    if quests.fionaHideAndSeek == ACTIVE:
        Derek "No need to go in there, new guy."
        Derek "Look somewhere else..."
        jump boysdormplaza_loop
    $ gotoscene('boysdormhallway')

label boysdormplaza_exit:
    $ gotoscene('schoolgroundsentrance')

### Various Labels ####

label boysdormplazacheckderek:
    if FionaWineFound == False:
        Derek "Very cold"
        return     
    elif FionaDonutFound == False:
        Derek "Very cold"
        return
    else:
        return