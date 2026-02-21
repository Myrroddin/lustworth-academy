#SCREENS
init 1 python:
    scene_defs['harrisonhouseentrance'] = {
        'music': MUSIC_HARRISONBARMUFFLE_THEME,
        'altermusic': MUSIC_HARRISONBARMUFFLE_THEME,
        'maps': {
            'default': ('harrisonhouseentrancenight', 'harrisonhouseentrancenighthover'),
        },
        'hotspots': [
            ('tobar', (1522, 264, 314, 558)),
            ('stairs', (690, 11, 558, 654)),
            ('topool', (516, 383, 159, 280)),
            ('tolivingroom', (108, 308, 247, 477))
        ],
        'sprites': [
            Sprite('pete', 'petebunnydialog01', (1114, 410, 165, 437), lambda: quests.fionaBartender != COMPLETE),
        ]
    }

#LABELS
label harrisonhouseentrance:
    $ intownmarker = True
    jump harrisonhouseentrance_loop

label harrisonhouseentrance_loop:
    $ resetscene()
    call screen map('harrisonhouseentrance')
    jump harrisonhouseentrance_loop

label harrisonhouseentrance_tobar:
    $ gotoscene('harrisonhousebar')

label harrisonhouseentrance_stairs:
    $ gotoscene('harrisonhousefloor2')

label harrisonhouseentrance_tolivingroom:
    Developer "{i}Area under construction.{/i}"
    jump harrisonhouseentrance_loop

label harrisonhouseentrance_topool:
    if quests.christyMandyVoltium == COMPLETE:
        Jimmy "Nothing to do at the pool."
    else:
        jump mandyhalloweendialogue
    jump harrisonhouseentrance_loop

label harrisonhouseentrance_pete:
    hide petebunnydialog01
    jump petehalloweendialogue
