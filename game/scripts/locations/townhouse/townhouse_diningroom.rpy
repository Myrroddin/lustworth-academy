#SCREENS
init 1 python:
    scene_defs['townhousediningroom'] = {
        'music': MUSIC_TOWNHOUSE,
        'altermusic': MUSIC_TOWNHOUSE,
        'maps': {
            'default': ('jimmyhousediningroom', 'jimmyhousediningroomhover'),
            'night':   ("jimmyhousediningroomnight", "jimmyhousediningroomnighthover")
        },
        'hotspots': [
            ('tolivingroom', (0, 0, 252, 1080)),
            ('tobackyard', (1203, 129, 307, 708)),
        ],
        'sprites': [
            # Sprite(key, image, (x, y, w, h), showif)
        ]
    }

#LABELS
label townhousediningroom:
    jump townhousediningroom_loop

label townhousediningroom_loop:
    $ resetscene()
    call screen map('townhousediningroom')
    jump townhousediningroom_loop

label townhousediningroom_tolivingroom:
    $ gotoscene('townhouselivingroom')

label townhousediningroom_tobackyard:
    $ gotoscene('townhousebackyard')
