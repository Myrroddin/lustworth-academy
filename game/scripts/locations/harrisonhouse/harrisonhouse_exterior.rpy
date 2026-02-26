#SCREENS
init 1 python:
    scene_defs['harrisonhouseexterior'] = {
        'music': MUSIC_SCHOOLGROUNDSAMBIENCEDAY_THEME,
        'altermusic': MUSIC_SCHOOLGROUNDSAMBIENCENIGHT_THEME,
        'maps': {
            'morning': ('harrisonhouseexteriorday', 'harrisonhouseexteriordayhover'),
            'afternoon': ('harrisonhouseexteriorday', 'harrisonhouseexteriordayhover'),
            'evening':   ('harrisonhouseexteriorday', 'harrisonhouseexteriordayhover'),
            'night':     ("harrisonhouseexteriornight", "harrisonhouseexteriornighthover")
        },
        'hotspots': [
            ('observatoryhill', (0, 60, 409, 594)),
            ('harrisonhouse', (1155, 453, 259, 255)),
            ('exit', (560, 936, 1080, 139))
        ],
        'sprites': [
        ]
    }

#LABELS
label harrisonhouseexterior:
    jump harrisonhouseexterior_loop

label harrisonhouseexterior_loop:
    $ resetscene()
    call screen map('harrisonhouseexterior')
    jump harrisonhouseexterior_loop

label harrisonhouseexterior_observatoryhill:
    $ gotoscene('observatoryhillexterior')

label harrisonhouseexterior_harrisonhouse:
    __("It's closed.")
    jump harrisonhouseexterior_loop

label harrisonhouseexterior_exit:
    $ gotoscene('schoolgroundspeacockplaza')
