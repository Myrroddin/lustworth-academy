#SCREENS
init 1 python:
    scene_defs['observatoryhillexterior'] = {
        'music': MUSIC_OBSERVATORYHILLAMBIENCEDAY_THEME,
        'altermusic': MUSIC_SCHOOLGROUNDSAMBIENCENIGHT_THEME,
        'maps': {
            'morning':   ("observatoryhillfallday", "observatoryhillfalldayhover"),
            'afternoon': ("observatoryhillfallafter", "observatoryhillfallafterhover"),
            'evening':   ("observatoryhillfallevening", "observatoryhillfalleveninghover"),
            'night':     ("observatoryhillfallnight", "observatoryhillfallnighthover")
        },
        'hotspots': [
            ('observatory', (915, 21, 643, 551)),
            ('mountaintop', (0, 0, 775, 618)),
            ('exit', (0, 853, 1156, 223)),
        ],
        'sprites': [
            # Sprite(key, image, (x, y, w, h), showif)
        ]
    }

#LABELS
label observatoryhillexterior:
    $ checkcurfew()
    jump observatoryhillexterior_loop

label observatoryhillexterior_loop:
    $ resetscene()
    call screen map('observatoryhillexterior')
    jump observatoryhillexterior_loop

label observatoryhillexterior_observatory:
    #if calendar.when[1:] == (WEDNESDAY, AFTERNOON):
        #jump astronomyclass
    "There is a note in the entrance."
    show observatorynote with dissolve
    "..."
    hide observatorynote with dissolve
    jump observatoryhillexterior_loop

label observatoryhillexterior_mountaintop:
    "It's a long way to the top..."
    jump observatoryhillexterior_loop

label observatoryhillexterior_exit:
    $ gotoscene('harrisonhouseexterior')