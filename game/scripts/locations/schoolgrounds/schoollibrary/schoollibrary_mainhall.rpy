#SCREENS
init 1 python:
    def schoollibrarymainhall_showif_clarissa():
        if calendar.when[0] == PROLOGUE:
            return False
        else:
            return True
 
    scene_defs['schoollibrarymainhall'] = {
        'music': MUSIC_LIBRARY,
        'altermusic': MUSIC_LIBRARY,
        'maps': {
            'morning':   ("librarymainhallfallday", "librarymainhallfalldayhover"),
            'afternoon': ("librarymainhallfallafternoon", "librarymainhallfallafternoonhover"),
            'evening':   ("librarymainhallfallevening", "librarymainhallfalleveninghover"),
            'night':     ("librarymainhallfallnight", "librarymainhallfallnighthover")
        },
        'hotspots': [
            ('exit', (0, 893, 1023, 185)),
            ('toarchive', (252, 233, 222, 469)),
            ('nerdhq', (1509, 1, 349, 291)),
            ('reception', (1093, 789, 528, 257)),
            ('shelves', (1221, 248, 264, 381)),
        ],
        'sprites': [
            Sprite('clarissa', 'clarissalibrarysprite', (1320, 752, 284, 1096), schoollibrarymainhall_showif_clarissa),
            
            
        ]
    }

#LABELS
label schoollibrarymainhall:
    if quests.fionaHideAndSeek == ACTIVE:
        call schoollibrarymainhallcheckderek from _call_schoollibrarymainhallcheckderek
    elif not Miku.met:
        if prologue.complete:
            jump libraryintroscene
    $ checkcurfew()
    jump schoollibrarymainhall_loop

label schoollibrarymainhall_loop:
    $ resetscene()
    call screen map('schoollibrarymainhall')
    jump schoollibrarymainhall_loop

label schoollibrarymainhall_exit:
    $ gotoscene('schoollibraryplaza')

label schoollibrarymainhall_toarchive:
    if quests.fionaHideAndSeek == ACTIVE:
        __("The door is closed.")
        jump schoollibrarymainhall_loop
    $ gotoscene('schoollibraryarchives')

label schoollibrarymainhall_nerdhq:
    if glob.halloweenEventComplete:
        if quests.algieScroll == LOCKED:
            jump welcometothekingdom
        else:
            $ gotoscene('schoollibrarynerdcliquehq')
    elif quests.fionaHideAndSeek == ACTIVE:
        __("The door is closed.")
        jump schoollibrarymainhall_loop
    elif prologue.complete:
        $ gotoscene('schoollibrarynerdcliquehq')
    else:
        __("There is a closed door at the end of the passage.")
        jump schoollibrarymainhall_loop

label schoollibrarymainhall_shelves:
    $ gotoscene('schoollibraryshelves')
    jump schoollibrarymainhall_loop

label schoollibrarymainhall_reception:
    hide clarissalibrarysprite
    if prologue.complete:
        jump clarissadialogue
    else:
        __("There is no one at the reception.")
        jump schoollibrarymainhall_loop


label schoollibrarymainhall_clarissa:
    hide clarissalibrarysprite
    if prologue.complete:
        jump clarissadialogue
    else:
        __("There is no one at the reception.")
        jump schoollibrarymainhall_loop

label schoollibrarymainhallcheckderek:
    if FionaDonutFound == False:
        Derek "Getting hot!"
        return
    elif FionaWineFound == False:
        Derek "You're freezing, my guy."
        return
    else:
        return
