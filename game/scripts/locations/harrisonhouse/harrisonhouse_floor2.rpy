#SCREENS
init 1 python:
    scene_defs['harrisonhousefloor2'] = {
        'music': MUSIC_HARRISONBARMUFFLE_THEME,
        'altermusic': MUSIC_HARRISONBARMUFFLE_THEME,
        'maps': {
            'default': ('harrisonhouse2ndfloor', 'harrisonhouse2ndfloorhover'),
        },
        'hotspots': [
            ('downstairs', (382, 554, 177, 243)),
            ('upstairs', (498, 272, 207, 270)),
            ('bedroom1', (0, 420, 256, 513)),
            ('bedroom2', (1536, 429, 118, 333)),
            ('office', (1200, 456, 121, 99)),
        ],
        'sprites': [
            Sprite('miku', 'mikupotterdialog01', (1267, 432, 309, 601), lambda: quests.mikuJacuzzi != COMPLETE),
        ]
    }

#LABELS
label harrisonhousefloor2:
    jump harrisonhousefloor2_loop

label harrisonhousefloor2_loop:
    $ resetscene()
    call screen map('harrisonhousefloor2')
    jump harrisonhousefloor2_loop

label harrisonhousefloor2_downstairs:
    $ gotoscene('harrisonhouseentrance')

label harrisonhousefloor2_upstairs:
    if quests.halloweenFakeFlag == COMPLETE:
        $ gotoscene('harrisonhouseroofflag')
    else:
        $ gotoscene('harrisonhouseroof')
    jump harrisonhousefloor2_loop

label harrisonhousefloor2_bedroom1:
    Jimmy "I hear voices inside, but it's closed."
    jump harrisonhousefloor2_loop

label harrisonhousefloor2_bedroom2:
    if quests.christyMandyVoltium == ACTIVE:
        jump halloween_voltiumfound
    jump harrisonhousefloor2_loop

label harrisonhousefloor2_office:
    if quests.beatrixHalloweenGrinding == COMPLETE:
        "The door won't open."
        "Beatrix must've locked it."
    else:
        $ gotoscene('harrisonhouseoffice')
    jump harrisonhousefloor2_loop

label harrisonhousefloor2_miku:
    hide mikupotterdialog01
    jump mikuhalloweendialogue
