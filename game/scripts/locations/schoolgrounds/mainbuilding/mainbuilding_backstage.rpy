#SCREENS
init 1 python:
    scene_defs['mainbuildingbackstage'] = {
        'music': MUSIC_BACKSTAGEAMBIENCEDAY_THEME,
        'altermusic': MUSIC_BACKSTAGEAMBIENCEDAY_THEME,
        'maps': {
            'default':   ("auditoriumbackstage01", "auditoriumbackstage01hover"),
        },
        'hotspots': [
            ('exit', (1622, 1, 297, 1076)),
        ],
        'sprites': [
        ]
    }

#LABELS
label mainbuildingbackstage:
    if quests.bakshiSirlaughsalot == ACTIVE:
        jump sirlaughsalotsearch01
    $ checkcurfew()
    jump mainbuildingbackstage_loop

label mainbuildingbackstage_loop:
    $ resetscene()
    call screen map('mainbuildingbackstage')
    jump mainbuildingbackstage_loop

label mainbuildingbackstage_exit:
    $ gotoscene('mainbuildingauditorium')
