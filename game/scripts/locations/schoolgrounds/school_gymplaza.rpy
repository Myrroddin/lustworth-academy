#SCREENS
init 1 python:
    scene_defs['schoolgroundsgymplaza'] = {
        'music': MUSIC_SCHOOLGROUNDSAMBIENCEDAY_THEME,
        'altermusic': MUSIC_SCHOOLGROUNDSAMBIENCENIGHT_THEME,
        'maps': {
            'morning':   ("gymplazafallday", "gymplazafalldayhover"),
            'afternoon': ("gymplazafallafternoon", "gymplazafallafternoonhover"),
            'evening':   ("gymplazafallevening", "gymplazafalleveninghover"),
            'night':     ("sgymplazafallnight", "gymplazafallnighthover")
        },
        'hotspots': [
            ('topool', (421, 438, 192, 226)),
            ('tosoccerfield', (995, 365, 199, 253)),
            ('toparkinglot', (964, 865, 955, 213)),
            ('togym', (1364, 360, 341, 241))
        ],
        'sprites': [
            # Sprite(key, image, (x, y, w, h), showif)
        ]
    }

#LABELS
label schoolgroundsgymplaza:
    if quests.fionaHideAndSeek == ACTIVE:
        call schoolgroundsgymplazacheckderek from _call_schoolgroundsgymplazacheckderek
    $ checkcurfew()
    jump schoolgroundsgymplaza_loop

label schoolgroundsgymplaza_loop:
    $ resetscene()
    call screen map('schoolgroundsgymplaza')
    jump schoolgroundsgymplaza_loop

label schoolgroundsgymplaza_tosoccerfield:
    Developer "{i}Area under construction.{/i}"
    jump schoolgroundsgymplaza_loop

label schoolgroundsgymplaza_topool:
    Developer "{i}Area under construction.{/i}"
    jump schoolgroundsgymplaza_loop

label schoolgroundsgymplaza_toparkinglot:
    $ gotoscene('schoolgroundspeacockplaza')

label schoolgroundsgymplaza_togym:
    $ gotoscene('schoolgym')


label schoolgroundsgymplazacheckderek:
    if FionaWineFound == False:
        Derek "Warm..."
        return
    elif FionaDonutFound == False:
        Derek "Very cold."
        return
    else:
        return
