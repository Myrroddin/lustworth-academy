#SCREENS
init 1 python:
    def schoollibraryshelves_showif_miku():
        if calendar.when[0] == PROLOGUE:
            return False
        elif quests.euniceGettingtherole == COMPLETE:
            if quests.mikuStorypartone != COMPLETE:
                return True
            elif quests.euniceTheaterpractice != COMPLETE:
                return False
        elif Miku.met:
            return True
    def fionahideandseek_showif_donutbox():
        if quests.fionaHideAndSeek == ACTIVE:
            if FionaDonutFound == False:
                return True
        return False

    scene_defs['schoollibraryshelves'] = {
        'music': MUSIC_LIBRARY,
        'altermusic': MUSIC_LIBRARY,
        'maps': {
            'morning':   ("libraryshelvespacefallday", "libraryshelvespacefalldayhover"),
            'afternoon': ("libraryshelvespacefallafternoon", "libraryshelvespacefallafternoonhover"),
            'evening':   ("libraryshelvespacefallevening", "libraryshelvespacefalleveninghover"),
            'night':     ("libraryshelvespacefallnight", "libraryshelvespacefallnighthover")
        },
        'hotspots': [
            ('exit', (1, 0, 344, 1059)),

        ],
        'sprites': [
            Sprite('miku', 'mikusprite01', (1000, 200, 284, 1096), schoollibraryshelves_showif_miku),
            Sprite('donutbox', 'donutbox_sprite', (720, 670, 180, 180), fionahideandseek_showif_donutbox),
        ]
    }

#LABELS
label schoollibraryshelves:
    if quests.fionaHideAndSeek == ACTIVE:
        call schoollibraryshelvescheckderek from _call_schoollibraryshelvescheckderek
    $ checkcurfew()
    jump schoollibraryshelves_loop

label schoollibraryshelves_loop:
    $ resetscene()
    call screen map('schoollibraryshelves')
    jump schoollibraryshelves_loop

label schoollibraryshelves_exit:
    # TODO: change to west plaza once implemented
    $ gotoscene('schoollibrarymainhall')

label schoollibraryshelves_miku:
    hide mikusprite01
    jump mikudialogue

label schoollibraryshelves_donutbox:
    hide screen freeroamhud
    hide donutbox_sprite
    call item_pickup(ItemDonutBox) from _call_item_pickup_28
    $ FionaDonutFound = True
    Jimmy "Found Fiona's donuts."
    if FionaWineFound == True:
        Jimmy "There is a note here..."
        show dereknote01 with dissolve
        Jimmy "..."
        Jimmy "Motherfucker..."
        Jimmy "Better get back to the kiosk now."
        $ quests.FionaHideAndSeek = SATISFIED
        jump chapterone_dereknote02
    else:
        Derek "Good job, new guy! Only one left, let's go..."
    jump schoollibraryshelves_loop

label schoollibraryshelvescheckderek:
    if FionaDonutFound == True:
        hide donutbox
        return