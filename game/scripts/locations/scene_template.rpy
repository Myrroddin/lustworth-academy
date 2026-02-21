#SCREENS
init 1 python:
    scene_defs['templatescene'] = {
        'music': None,
        'maps': {
            'default': ('', ''),
        },
        'hotspots': [
            # (key, (x, y, w, h), showif=None)
            ('', ),
        ],
        'sprites': [
            # Sprite(key, image, (x, y, w, h), showif)
        ]
    }

#LABELS
label templatescene:
    # $ checkcurfew()
    jump templatescene_loop

label templatescene_loop:
    $ resetscene()
    call screen map('templatescene')
    jump templatescene_loop
