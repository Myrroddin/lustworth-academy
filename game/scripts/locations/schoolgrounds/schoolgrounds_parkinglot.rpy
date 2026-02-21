init 1 python:
    def schoolgroundsparkinglot_showif_eunice():
        if quests.euniceGettingtherole == ACTIVE:
            return True
        elif quests.euniceChocolates == COMPLETE:
            if quests.euniceGettingtherole != COMPLETE:
                return True
        return False

#SCREENS
init 1 python:
    scene_defs['schoolgroundsparkinglot'] = {
        'music': MUSIC_SCHOOLGROUNDSAMBIENCEDAY_THEME,
        'altermusic': MUSIC_SCHOOLGROUNDSAMBIENCENIGHT_THEME,
        'maps': {
            'morning':   ("parkinglotfallday", "parkinglotfalldayhover"),
            'afternoon': ("parkinglotfallafter", "parkinglotfallafterhover"),
            'evening':   ("parkinglotfallevening", "parkinglotfalleveninghover"),
            'night':     ("parkinglotfallnight", "parkinglotfallnighthover")
        },
        'hotspots': [
            ('garage', (223, 414, 371, 168)),
            ('shopyard', (605, 450, 159, 127)),
            ('bus', (830, 515, 212, 100)),
            ('togymplaza', (0, 187, 209, 670)),
            ('tosouthplaza', (0, 942, 1920, 123)),
            ('togymplaza2', (1511, 852, 333, 90))
        ],
        'sprites': [
            Sprite('eunice', 'eunicedialog02', (1650, 500, 234, 621), schoolgroundsparkinglot_showif_eunice),
        ]
    }

#LABELS
label schoolgroundsparkinglot:
    if quests.fionaHideAndSeek == ACTIVE:
        call schoolgroundsparkinglotcheckderek from _call_schoolgroundsparkinglotcheckderek
    $ checkcurfew()
    jump schoolgroundsparkinglot_loop

label schoolgroundsparkinglot_loop:
    $ resetscene()
    call screen map('schoolgroundsparkinglot')
    jump schoolgroundsparkinglot_loop

label schoolgroundsparkinglot_garage:
    if quests.fionaHideAndSeek == ACTIVE:
        Derek "No need to go in there, new guy."
        Derek "Look somewhere else..."
        jump schoolgroundsparkinglot_loop
    elif quests.missdawsonAssistant == SATISFIED:
        if quests.missdawsonHalloweenAudrey == LOCKED:
            jump dawsonaudreyhalloween
    $ gotoscene('schoolgarage')

label schoolgroundsparkinglot_shopyard:
    if quests.rescueBucky == SATISFIED:
        jump buckyrescuemission
    $ gotoscene('schoolgroundsjunkyard')

label schoolgroundsparkinglot_bus:
    Developer "{i}Area under construction.{/i}"
    jump schoolgroundsparkinglot_loop

label schoolgroundsparkinglot_tosouthplaza:
    $ gotoscene('schoolgroundssouthplaza')

label schoolgroundsparkinglot_eunice:
    if EuniceDaylimit == True:
        show eunice uniform neutral with dissolve
        Jimmy "*She look busy.*"
        Jimmy "*I already talked to her today.*"
        Jimmy "*I'll see her tomorrow.*"
        jump schoolgroundsparkinglot_loop
    jump eunicedialogue

label schoolgroundsparkinglot_togymplaza:
label schoolgroundsparkinglot_togymplaza2:
    $ gotoscene('schoolgroundspeacockplaza')

label schoolgroundsparkinglotcheckderek:
    if FionaWineFound == False:
        Derek "Ice ice, baby..."
        return     
    elif FionaDonutFound == False:
        Derek "Ice ice, baby..."
        return
    else:
        return