#SCREENS
init 1 python:
    scene_defs['schoolgroundssouthplaza'] = {
        'music': MUSIC_SCHOOLGROUNDSAMBIENCEDAY_THEME,
        'altermusic': MUSIC_SCHOOLGROUNDSAMBIENCENIGHT_THEME,
        'maps': {
            'morning':   ("mainplazafallday", "mainplazafalldayhover"),
            'afternoon': ("mainplazafallafter", "mainplazafallafterhover"),
            'evening':   ("mainplazafallevening", "mainplazafalleveninghover"),
            'night':     ("mainplazafallmidnight", "mainplazafallmidnighthover")
        },
        'hotspots': [
            ('libraryplaza', (0, 100, 441, 786)),
            ('parkinglot', (1491, 122, 428, 787)),
            ('mainbuilding', (696, 445, 517, 312)),
            ('toentrance', (0, 891, 1919, 187)),
        ],
        'sprites': [
            # Sprite(key, image, (x, y, w, h), showif)
        ]
    }

#LABELS
label schoolgroundssouthplaza:
    if quests.fionaHideAndSeek == ACTIVE:
        call schoolgroundssouthplazacheckderek from _call_schoolgroundssouthplazacheckderek
    $ checkcurfew()
    jump schoolgroundssouthplaza_loop

label schoolgroundssouthplaza_loop:
    $ resetscene()
    call screen map('schoolgroundssouthplaza')
    jump schoolgroundssouthplaza_loop

label schoolgroundssouthplaza_libraryplaza:
    $ gotoscene('schoollibraryplaza')

label schoolgroundssouthplaza_parkinglot:
    $ gotoscene('schoolgroundsparkinglot')

label schoolgroundssouthplaza_mainbuilding:
    if quests.fionaHideAndSeek == ACTIVE:
        Derek "No need to go inside, new guy."
        Derek "Look somewhere else..."
        jump schoolgroundssouthplaza_loop
    elif mainbuildingentrance.camembertCaught and Jimmy.outfit != JIMMY_UNIFORM:
        "I can't go in there without my uniform, not unless I want detention."
        jump schoolgroundssouthplaza_loop
    $ gotoscene('mainbuildingentrance')

label schoolgroundssouthplaza_toentrance:
    $ gotoscene('schoolgroundsentrance')

label mainbuildingplazadayfallmap:
    if mapclick == "gotoparkinglot":
        hide screen freeroammainhud
        jump schoolparkinglotfalldaymap
    elif mapclick == "gotoparkinglot02":
        hide screen freeroammainhud
        jump schoolparkinglotfalldaymap

label schoolgroundssouthplazacheckderek:
    if FionaDonutFound == False:
        Derek "Cold..."
        return     
    elif FionaWineFound == False:
        Derek "Very cold."
        return
    else:
        return