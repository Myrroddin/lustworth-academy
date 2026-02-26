#SCREENS
init 1 python:
    def fionahideandseek_showif_grapewine():
        if quests.fionaHideAndSeek == ACTIVE:
            if FionaWineFound == False:
                return True
        return False

    scene_defs['schoolgymstorageroom'] = {
        'music': MUSIC_STORAGEROOMAMBIENCEDAY_THEME,
        'altermusic': MUSIC_GYMAMBIENCENIGHT_THEME,
        'maps': {
            'default': ('gymstorageroom', 'gymstorageroomhover'),
        },
        'hotspots': [
            ('poster', (627, 77, 264, 412)),
            ('exit', (130, 939, 1366, 141)),
        ],
        'sprites': [
            Sprite('grapewine', 'grapewine_sprite', (280, 620, 180, 180), fionahideandseek_showif_grapewine),
        ]
    }

#LABELS
label schoolgymstorageroom:
    if quests.fionaHideAndSeek == ACTIVE:
        call schoolgymstorageroomcheckderek from _call_schoolgymstorageroomcheckderek
    $ checkcurfew()
    jump schoolgymstorageroom_loop

label schoolgymstorageroom_loop:
    $ resetscene()
    call screen map('schoolgymstorageroom')
    jump schoolgymstorageroom_loop

label schoolgymstorageroom_poster:
    if Christy.met == False:
        Jimmy "That poster is barely holding on to the wall."
    else:
        hide screen freeroamhud
        show girlshowerhole with dissolve
        __("No one's there.")
        hide girlshowerhole with dissolve
    jump schoolgymstorageroom_loop

label schoolgymstorageroom_grapewine:
    hide screen freeroamhud
    hide grapewine_sprite
    call item_pickup(ItemGrapeWine) from _call_item_pickup_27
    $ quests.FionaWineFound = True
    Jimmy "Found Fiona's wine."
    if FionaDonutFound == True:
        Jimmy "There is a note here..."
        show dereknote01 with dissolve
        Jimmy "..."
        Jimmy "Motherfucker..."
        Jimmy "Better get back to the kiosk now."
        $ quests.fionaHideAndSeek = SATISFIED
        jump chapterone_dereknote02
    else:
        Derek "Great job, new guy! Only one left, let's go..."
    jump schoolgymstorageroom_loop

label schoolgymstorageroom_exit:
    $ gotoscene('schoolgym')

label schoolgymstorageroomcheckderek:
    if FionaDonutFound == False:
        Derek "You're freezing, my guy."
        return
    else:
        return
