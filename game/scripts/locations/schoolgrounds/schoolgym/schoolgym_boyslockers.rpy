#SCREENS
init 1 python:
    scene_defs['schoolgymboyslockers'] = {
        'music': MUSIC_BOYSLOCKERAMBIENCEDAY_THEME,
        'altermusic': MUSIC_GYMAMBIENCENIGHT_THEME,
        'maps': {
            'default': ('boysgymbathfall', 'boysgymbathfallhover'),
        },
        'hotspots': [
            ('exit', (400, 872, 785, 208)),
        ],
        'sprites': [
            # Sprite(key, image, (x, y, w, h), showif)
        ]
    }

#LABELS
label schoolgymboyslockers:
    if quests.christyPlan == ACTIVE:
        jump christysinisterplanintro
    if quests.fionaHideAndSeek == ACTIVE:
        call schoolgymboyslockerscheckderek from _call_schoolgymboyslockerscheckderek
    if quests.euniceChocolates == ACTIVE:
        jump eunicechocolatesquest.derekfight
    $ checkcurfew()
    jump schoolgymboyslockers_loop

label schoolgymboyslockers_loop:
    $ resetscene()
    call screen map('schoolgymboyslockers')
    jump schoolgymboyslockers_loop

label schoolgymboyslockers_exit:
    $ gotoscene('schoolgym')

label schoolgymboyslockerscheckderek:
    if FionaWineFound == False:
        Derek "Warm..."
        return
    elif FionaDonutFound == False:
        Derek "You're freezing, my guy."
        return
    else:
        return