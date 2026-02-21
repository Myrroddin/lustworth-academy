#SCREENS
init 1 python:
    scene_defs['mainbuildingsecretarysoffice'] = {
        'music': MUSIC_HEADMASTERS_THEME,
        'altermusic': MUSIC_HEADMASTERS_THEME,
        'maps': {
            'default': ('secretaryoffice01', 'secretaryoffice01hover'),
        },
        'hotspots': [
            ('headmastersoffice', (1284, 25, 595, 753)),
            ('exit', (0, 713, 394, 365)),
        ],
        'sprites': [
            Sprite('missdawson', 'missdawsondialog01', (730, 264, 213, 310), lambda: quests.headmasterSpy == COMPLETE),
        ]
    }

#LABELS
label mainbuildingsecretarysoffice:
    $ checkcurfew()
    jump mainbuildingsecretarysoffice_loop

label mainbuildingsecretarysoffice_loop:
    $ resetscene()
    call screen map('mainbuildingsecretarysoffice')
    jump mainbuildingsecretarysoffice_loop

label mainbuildingsecretarysoffice_headmastersoffice:
    if calendar.when[0] != PROLOGUE and quests.headmasterSpy != COMPLETE:
        jump missdawsondialogue.headmasterspy
    jump mainbuildingsecretarysoffice_loop

label mainbuildingsecretarysoffice_exit:
    $ gotoscene('mainbuildingentrance')

label mainbuildingsecretarysoffice_missdawson:
    hide missdawsondialog01
    jump missdawsondialogue
