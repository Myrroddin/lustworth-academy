#SCREENS
init 1 python:
    scene_defs['mainbuildingheadmaster'] = {
        'music': MUSIC_HEADMASTERS_THEME,
        'altermusic': MUSIC_HEADMASTERS_THEME,
        'maps': {
            'morning':   ("headmasterstudyfallday", "headmasterstudyfallday"),
            'afternoon': ("headmasterstudyfallafternoon", "headmasterstudyfallafternoon"),
            'evening':   ("headmasterstudyfallevening", "headmasterstudyfallevening"),
            'night':     ("headmasterstudyfallnight", "headmasterstudyfallnight")
        },
        'hotspots': [
            ('exit', (0, 713, 394, 365)),
        ],
        'sprites': [
            #Sprite('missdawson', 'missdawsondialog01', (730, 264, 213, 310), lambda: quests.headmasterSpy == COMPLETE),
        ]
    }

#LABELS
label mainbuildingheadmaster:
    $ checkcurfew()
    jump mainbuildingheadmaster_loop

label mainbuildingheadmaster_loop:
    $ resetscene()
    call screen map('mainbuildingheadmaster')
    jump mainbuildingheadmaster_loop

label mainbuildingheadmaster_exit:
    $ gotoscene('mainbuildingsecretarysoffice')