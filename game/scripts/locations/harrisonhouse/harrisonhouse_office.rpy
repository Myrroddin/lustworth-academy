#SCREENS
init 1 python:
    scene_defs['harrisonhouseoffice'] = {
        'music': MUSIC_HARRISONBARMUFFLE_THEME,
        'altermusic': MUSIC_HARRISONBARMUFFLE_THEME,
        'maps': {
            'default': ('mansionofficebackground', 'mansionofficebackgroundhover'),
        },
        'hotspots': [
            ('exit', (0, 960, 1918, 120)),
        ],
        'sprites': [
            Sprite('applecider1', 'applecider2x', (1300, 680, 190, 190), lambda: quests.beatrixAppleCider < SATISFIED),
            Sprite('applecider2', 'applecider1x', (1300, 680, 190, 190), lambda: quests.beatrixAppleCider >= SATISFIED),
        ]
    }

#LABELS
label harrisonhouseoffice:
    jump harrisonhouseoffice_loop

label harrisonhouseoffice_loop:
    $ resetscene()
    call screen map('harrisonhouseoffice')
    jump harrisonhouseoffice_loop

label harrisonhouseoffice_exit:
    $ gotoscene('harrisonhousefloor2')

label harrisonhouseoffice_applecider1:
label harrisonhouseoffice_applecider2:
    if quests.beatrixAppleCider == ACTIVE:
        __("What is this?")
        __("Seems like apple juice to me.")
        call item_pickup(ItemAppleCider) from _call_item_pickup_11
        $ quests.beatrixAppleCider = SATISFIED
    elif quests.beatrixAppleCider == SATISFIED:
        __("I already got some apple juice. I should give it to Beatrix.")
    elif quests.beatrixAppleCider == COMPLETE:
        jump halloween_beatrixgrinding
    else:
        __("Looks like some sort of apple juice.")
    jump harrisonhouseoffice_loop
