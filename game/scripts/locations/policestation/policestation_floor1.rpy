#SCREENS
init 1 python:
    scene_defs['policestationfloor1'] = {
        'music': MUSIC_SUSPENSE,
        'altermusic': MUSIC_SUSPENSE,
        'maps': {
            'default': ('policestationreception', 'policestationreceptionhover'),
        },
        'hotspots': [
            ('receptionexit', (783, 909, 952, 159)),
            ('mayorphoto', (985, 256, 197, 261)),
            ('recordsdoor', (426, 208, 283, 593)),
            ('messageboard', (1362, 223, 120, 151)),
            ('tocells', (1818, 51, 119, 901)),
            ('tofloor2', (0, 3, 255, 938)),
            ('filescabinet', (1586, 496, 223, 385)),
        ],
        'sprites': [
            # Sprite(key, image, (x, y, w, h), showif)
        ]
    }

#LABELS
label policestationfloor1:
    jump policestationfloor1_loop

label policestationfloor1_loop:
    $ resetscene()
    call screen map('policestationfloor1')
    jump policestationfloor1_loop

label policestationfloor1_filescabinet:
    "There is small radio in here."
    "I think it will work for a minigame in a future update."
    "...I don't know why I said that."
    jump policestationfloor1_loop

label policestationfloor1_mayorphoto:
    "This guy is everywhere..."
    jump policestationfloor1_loop

#label policestationfloor1_receptionwindow:
    #"There seems to be no one in there."
    #"Where are all the cops?"
    #jump policestationfloor1_loop

label policestationfloor1_receptionexit:
    "The main gate is locked."
    jump policestationfloor1_loop

label policestationfloor1_recordsdoor:
    "\"Evidence Room.\""
    "It's locked."
    jump policestationfloor1_loop

label policestationfloor1_messageboard:
    "\"Party at Manny's house at 10 o'clock.\""
    "\"Night shifts: Officer Valentino and Officer Kalinski.\""
    "\"Sorry guys, I'll bring you cake tomorrow.\""
    jump policestationfloor1_loop

label policestationfloor1_tocells:
    $ gotoscene('policestationcellseast')

label policestationfloor1_tofloor2:
    $ gotoscene('policestationfloor2')
