init 1 python:
    scene_defs['harrisonhouseroofflag'] = {
        'music': MUSIC_HARRISONPARTYROOF_THEME,
        'altermusic': MUSIC_HARRISONPARTYROOF_THEME,
        'maps': {
            'default': ('harrisonhouseroofflag', 'harrisonhouseroofflaghover'),
        },
        'hotspots': [
            ('jacuzzidoor', (136, 222, 129, 530)),
            ('backdown', (58, 899, 1203, 181)),
            ('flagpole', (1641, 0, 277, 1080)),
        ],
        'sprites': [
        ]
    }

#LABELS
label harrisonhouseroofflag:
    jump harrisonhouseroofflag_loop

label harrisonhouseroofflag_loop:
    $ resetscene()
    call screen map('harrisonhouseroofflag')
    jump harrisonhouseroofflag_loop

label harrisonhouseroofflag_jacuzzidoor:
    Jimmy "I think there is a jacuzzi inside."
    Jimmy "But it's closed."
    jump harrisonhouseroofflag_loop

label harrisonhouseroofflag_backdown:
    $ gotoscene('harrisonhousefloor2')

label harrisonhouseroofflag_flagpole:
    Jimmy "Gary has a really fucked-up sense of humor."
    jump harrisonhouseroofflag_loop
