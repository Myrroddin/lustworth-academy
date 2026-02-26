#VARIABLES

#SCREENS
init 1 python:
    scene_defs['boysdormbackalley'] = {
        'music': MUSIC_SCHOOLGROUNDSAMBIENCEDAY_THEME,
        'altermusic': MUSIC_SCHOOLGROUNDSAMBIENCENIGHT_THEME,
        'maps': {
            'morning':   ("boysdormbackalleyday", "boysdormbackalleydayhover"),
            'afternoon': ("boysdormbackalleyafter", "boysdormbackalleyafterhover"),
            'evening':   ("boysdormbackalleyevening", "boysdormbackalleyeveninghover"),
            'night':     ("boysdormbackalleynight", "boysdormbackalleynighthover")
        },
        'hotspots': [
            ('graffiti', (1203, 296, 278, 313)),
            ('bedroomwindow', (276, 17, 193, 333)),
            ('trashcan', (431, 621, 350, 312)),
            ('toplaza', (12, 955, 1902, 119)),
        ],
        'sprites': [
            # Sprite(key, image, (x, y, w, h), showif)
        ]
    }

#LABELS
label boysdormbackalley:
    if quests.fionaHideAndSeek == COMPLETE:
        if quests.fionaConfrontDerek != COMPLETE:
            jump chapterone_fionaderekconfrontation
    elif quests.fionaHideAndSeek == ACTIVE:
        call boysdormbackalleycheckderek from _call_boysdormbackalleycheckderek
    elif quests.fionaConfrontDerek == ACTIVE:
        if quests.fionaHideAndSeek == LOCKED:
            jump chapterone_derekhideandseekintro
    jump boysdormbackalley_loop

label boysdormbackalley_loop:
    $ resetscene()
    call screen map('boysdormbackalley')
    jump boysdormbackalley_loop

label boysdormbackalley_graffiti:
    Jimmy "Weirdly shaped graffiti."
    Jimmy "Cool, though."
    jump boysdormbackalley_loop

label boysdormbackalley_bedroomwindow:
    Jimmy "That's my room."
    jump boysdormbackalley_loop

label boysdormbackalley_trashcan:
    Jimmy "It smells awful."
    jump boysdormbackalley_loop

label boysdormbackalley_toplaza:
    $ gotoscene('boysdormplaza')


label boysdormbackalleycheckderek:
    if FionaWineFound == False:
        Derek "Very cold"
        return     
    elif FionaDonutFound == False:
        Derek "Very cold"
        return
    else:
        return
