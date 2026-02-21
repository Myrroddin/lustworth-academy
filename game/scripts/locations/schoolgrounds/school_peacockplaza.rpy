#SCREENS
init 1 python:
    scene_defs['schoolgroundspeacockplaza'] = {
        'music': MUSIC_SCHOOLGROUNDSAMBIENCEDAY_THEME,
        'altermusic': MUSIC_SCHOOLGROUNDSAMBIENCENIGHT_THEME,
        'maps': {
            'morning':   ("peacockplazafallday", "peacockplazafalldayhover"),
            'afternoon': ("peacockplazafallafternoon", "peacockplazafallafternoonhover"),
            'evening':   ("peacockplazafallevening", "peacockplazafalleveninghover"),
            'night':     ("peacockplazafallnight", "peacockplazafallnighthover")
        },
        'hotspots': [
            ('togymplaza', (1285, 477, 341, 229)),
            ('toparkinglot', (1637, 522, 302, 553)),
            ('tolibraryplaza', (2, 227, 293, 848)),
            ('toharrisonhouse', (353, 358, 422, 292)),
            ('peacockstatue', (811, 249, 338, 508)),
        ],
        'sprites': [
        ]
    }

#LABELS
label schoolgroundspeacockplaza:
    jump schoolgroundspeacockplaza_loop

label schoolgroundspeacockplaza_loop:
    $ resetscene()
    call screen map('schoolgroundspeacockplaza')
    jump schoolgroundspeacockplaza_loop

label schoolgroundspeacockplaza_togymplaza:
    $ gotoscene('schoolgroundsgymplaza')

label schoolgroundspeacockplaza_toparkinglot:
    $ gotoscene('schoolgroundsparkinglot')
    
label schoolgroundspeacockplaza_tolibraryplaza:
    $ gotoscene('schoollibraryplaza')

label schoolgroundspeacockplaza_toharrisonhouse:
    $ gotoscene('harrisonhouseexterior')

label schoolgroundspeacockplaza_peacockstatue:
    "That statue is impressive."
    "Is it made of gold?"
    jump schoolgroundspeacockplaza_loop