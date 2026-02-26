#VARIABLES
default boysdormtvroom.tvChecked = False
default boysdormtvroom.fratBannerChecked = False
default boysdormtvroom.sodaMachineChecked = False
default boysdormtvroom.wallOfPrankmastersChecked = False
default boysdormtvroom.fionaPadlockComment = False

#SCREENS
init 1 python:
    def boysdormtvroom_showif_pete():
        if calendar.when[0] == PROLOGUE:
            return False
        return True

    scene_defs['boysdormtvroom'] = {
        'music': MUSIC_BOYSDORMAMBIENCE02_THEME,
        'altermusic': MUSIC_BOYSDORMAMBIENCENIGHT_THEME,
        'maps': {
            'morning':   ("boysdormtvroomday", "boysdormtvroomdayhover"),
            'afternoon': ("boysdormtvroomafternoon", "boysdormtvroomafternoonhover"),
            'evening':   ("boysdormtvroomevening", "boysdormtvroomeveninghover"),
            'night':     ("boysdormtvroomnight", "boysdormtvroomnighthover")
        },
        'hotspots': [
            ('tv', (0, 413, 308, 374)),
            ('wallofprankmasters', (227, 62, 304, 349)),
            ('fratbanner', (1656, 232, 132, 242)),
            ('sodamachine', (952, 305, 171, 225)),
            ('noticeboard', (653, 203, 218, 165)),
            ('tohallway', (1781, 172, 139, 557)),
        ],
        'sprites': [
            Sprite('pete', 'petekowalskisprite', (1300, 400, 236, 597), boysdormtvroom_showif_pete),
            Sprite('padlock', 'fionapadlock', (240, 821, 100, 100), lambda: quests.fionaPadlock == ACTIVE),
        ]
    }

#LABELS
label boysdormtvroom:
    if quests.algieScroll == COMPLETE:
        if quests.rescueBucky == LOCKED:
            jump buckyrescueintro
    elif quests.beatrixDiary == COMPLETE:
        if quests.garyHalloweenHeist == LOCKED:
            if glob.halloweenEventComplete:
                __("You have already completed the Halloween Event.")
                $ quests.garyHalloweenHeist = COMPLETE
                jump boysdormtvroom_loop
            else:
                jump garyhalloweenheistintro
    jump boysdormtvroom_loop

label boysdormtvroom_loop:
    $ resetscene()
    call screen map('boysdormtvroom')
    jump boysdormtvroom_loop

label boysdormtvroom_tohallway:
    $ gotoscene('boysdormhallway')

label boysdormtvroom_tv:
    if not boysdormtvroom.tvChecked:
        __("There's an XPlayBoy console hooked up, but I have other things to do.")
        $ boysdormtvroom.tvChecked = True
    __("Maybe later.")
    jump boysdormtvroom_loop

label boysdormtvroom_fratbanner:
    __("\"Alpha Legion, the best fraternity in the country.\"")
    if not boysdormtvroom.fratBannerChecked:
        __("\"If you have the balls, try to join us.\"")
        __("\"Pedicabo ego vos et irrumabo.\"")
        __("I wonder what that means.")
        $ boysdormtvroom.fratBannerChecked = True
    jump boysdormtvroom_loop

label boysdormtvroom_noticeboard:
    __("Math classes, a rock concert, and...")
    __("Hey, look at this. The Spanish teacher gives private lessons.")
    if not Punny.met:
        __("I wonder if she's hot.")
    jump boysdormtvroom_loop

label boysdormtvroom_sodamachine:
    if not boysdormtvroom.sodaMachineChecked:
        __("It's a Coca-Pep machine.")
        $ boysdormtvroom.sodaMachineChecked = True
    __("I don't have any money right now.")
    jump boysdormtvroom_loop

label boysdormtvroom_wallofprankmasters:
    if not boysdormtvroom.wallOfPrankmastersChecked:
        __("This must be the Wall of Prankmasters.")
        __("It memorializes the legendary students that funded this dorm.")
        __("Some say they even made a secret tunnel that led right into the girl's dorm.")
        __("Maybe someone knows more about it.")
        $ boysdormtvroom.wallOfPrankmastersChecked = True
    if wallofprankmasters.secretPassage:
        menu: 
            __("Enter the secret passage"):
                jump wallofprankmasters_secretpassage
            __("Admire the Wall of Prankmasters"):
                jump wallofprankmasters
    jump wallofprankmasters

label boysdormtvroom_pete:
    if quests.beatrixDiary == COMPLETE:
        if quests.garyHalloweenHeist == LOCKED:
            jump garyhalloweenheistintro
    hide petekowalskisprite
    jump petedialogue

label boysdormtvroom_padlock:
    __("This must be Fiona's padlock. Nice!")
    hide fionapadlock
    call item_pickup(ItemFionaPadlock) from _call_item_pickup_12
    $ quests.fionaPadlock = SATISFIED
    jump boysdormtvroom_loop
