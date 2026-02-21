#SCREENS
init 1 python:
    scene_defs['schoollibraryarchives'] = {
        'music': MUSIC_LIBRARY02,
        'altermusic': MUSIC_LIBRARY02,
        'maps': {
            'default': ('libraryarchivefallday', 'libraryarchivefalldayhover'),
        },
        'hotspots': [
            ('exit', (0, 909, 1918, 171)),
            ('archivepc', (0, 417, 232, 252)),
        ],
        'sprites': [
            # Sprite(key, image, (x, y, w, h), showif)
        ]
    }

#LABELS
label schoollibraryarchives:
    $ checkcurfew()
    if calendar.when[2] == EVENING:
        if quests.mikuPhotoShoot == COMPLETE and quests.mikuStorypartone != COMPLETE:
            if MikuDaylimit == False:
                jump mikuprivatephotoshootscene
            else:
                Jimmy "I should come back tomorrow for Miku."
    jump schoollibraryarchives_loop

label schoollibraryarchives_loop:
    $ resetscene()
    call screen map('schoollibraryarchives')
    jump schoollibraryarchives_loop

label schoollibraryarchives_exit:
    $ gotoscene('schoollibrarymainhall')

label schoollibraryarchives_archivepc:
    if chapter1_freeroam_iscomplete:
        call jimmyspc from _call_jimmyspc_1
    else:
        "I'll have time to use my computer later."
        "Right now I need to do something else."
    jump schoollibraryarchives_loop
