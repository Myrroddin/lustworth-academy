#SCREENS
init 1 python:
    scene_defs['policestationcellseast'] = {
        'music': MUSIC_SUSPENSE,
        'altermusic': MUSIC_SUSPENSE,
        'maps': {
            'default': ('prisonmorgueintro', 'prisonmorgueintrohover'),
        },
        'hotspots': [
            ('tocellswest', (0, 203, 206, 873)),
            ('medal', (1285, 323, 89, 133)),
            ('poster', (961, 361, 105, 130)),
            ('tomorgue', (344, 379, 190, 328)),
            ('stairs', (1609, 335, 296, 534)),
            ('clothes', (213, 389, 118, 217)),
            ('map', (1258, 492, 183, 164)),
        ],
        'sprites': [
            # Sprite(key, image, (x, y, w, h), showif)
        ]
    }

#LABELS
label policestationcellseast:
    jump policestationcellseast_loop

label policestationcellseast_loop:
    $ resetscene()
    call screen map('policestationcellseast')
    jump policestationcellseast_loop

#label policestationcellseast_filecabinet:
    #"There is small radio in here."
    #"I think it will work for a minigame in a future update."
    #"...I don't know why I said that."
    #jump policestationcellseast_loop

label policestationcellseast_medal:
    "\"Medal of Honor granted to Dr. Moreau.\""
    jump policestationcellseast_loop

label policestationcellseast_poster:
    "\"Jack Donaguy. A brilliant future for our town.\""
    "Yeah, right."
    jump policestationcellseast_loop

label policestationcellseast_map:
    "Hey, there is a map of Peacock Valley on the screen."
    "Let's see. The academy is in the lower right..."
    "There's a residential area to the west..."
    "The carnival fair is near the coast, by the docks..."
    "And there's an industrial area north of the academy. There's an asylum there. Interesting."
    jump policestationcellseast_loop

label policestationcellseast_tomorgue:
    "The door is locked. Looks like it leads to the morgue."
    jump policestationcellseast_loop

label policestationcellseast_stairs:
    $ gotoscene('policestationfloor1')

label policestationcellseast_clothes:
    "Medic robes, must be from the guy that runs the morgue."
    jump policestationcellseast_loop

label policestationcellseast_tocellswest:
    $ gotoscene('policestationcellswest')
