#SCREENS
init 1 python:
    scene_defs['schoolgroundsjunkyard'] = {
        'music': MUSIC_SCHOOLGROUNDSAMBIENCEDAY_THEME,
        'altermusic': MUSIC_SCHOOLGROUNDSAMBIENCENIGHT_THEME,
        'maps': {
            'morning':   ("junkyardfallday", "junkyardfalldayhover"),
            'afternoon': ("junkyardfallafter", "junkyardfallafterhover"),
            'evening':   ("junkyardfallevening", "junkyardfalleveninghover"),
            'night':     ("junkyardfallnight", "junkyardfallnighthover")
        },
        'hotspots': [
            ('greasercabin', (378, 376, 109, 155)),
            ('watertower', (459, 134, 180, 164)),
            ('toparkinglot', (1163, 215, 486, 455)),
        ],
        'sprites': [
            # Sprite(key, image, (x, y, w, h), showif)
        ]
    }

#LABELS
label schoolgroundsjunkyard:
    $ checkcurfew()
    if quests.fionaHideAndSeek == ACTIVE:
        Derek "Nothing but trash, pal."
        Derek "Look somewhere else."
    elif quests.garyHalloweenHeist == ACTIVE:
        jump tatianaintro
    elif quests.rescueBucky == ACTIVE:
        jump buckyrescuemission
    jump schoolgroundsjunkyard_loop

label schoolgroundsjunkyard_loop:
    $ resetscene()
    call screen map('schoolgroundsjunkyard')
    jump schoolgroundsjunkyard_loop

label schoolgroundsjunkyard_watertower:
    Jimmy "That water tower must belong to the school."
    jump schoolgroundsjunkyard_loop

label schoolgroundsjunkyard_greasercabin:
    Jimmy "It's some kind of cabin. The door is closed and the windows are covered."
    jump schoolgroundsjunkyard_loop

label schoolgroundsjunkyard_toparkinglot:
    $ gotoscene('schoolgroundsparkinglot')
