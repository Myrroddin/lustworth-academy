#VARIABLES
default boysdormjimmysroom.nightstandChecked = False
default boysdormjimmysroom.alwaysSunnyComment = False
default boysdormjimmysroom.pantiesChecked = False
default dearsantaqueststarted = False

#SCREENS
init 1 python:
    scene_defs['boysdormjimmysroom'] = {
        'music': MUSIC_BOYSDORMAMBIENCE02_THEME,
        'altermusic': MUSIC_BOYSDORMAMBIENCENIGHT_THEME,
        'maps': {
            'morning':   ("jimmybedroomfallday", "jimmybedroomfalldayhover"),
            'afternoon': ("jimmybedroomfallafternoon", "jimmybedroomfallafternoonhover"),
            'evening':   ("jimmybedroomfallevening", "jimmybedroomfalleveninghover"),
            'night':     ("jimmybedroomfallmidnight", "jimmybedroomfallmidnighthover")
        },
        'hotspots': [
            ('bed', (852, 485, 564, 174)),
            ('door', (862, 183, 248, 298)),
            # Disable most hotspots the first night
            ('window', (-20, 143, 91, 338), lambda: calendar.when != (PROLOGUE, WEDNESDAY, NIGHT)),
            ('nightstand', (1424, 575, 107, 140), lambda: calendar.when != (PROLOGUE, WEDNESDAY, NIGHT)),
            ('closet', (274, 180, 339, 336), lambda: calendar.when != (PROLOGUE, WEDNESDAY, NIGHT))
        ],
        'sprites': [
            Sprite('angiesnote', 'angiesnoteidle', (165, 750, 173, 133), lambda: sexscenes.angiesNote),
            Sprite('derbylaptop', 'derbylaptopaccess', (50, 900, 400, 200), lambda: glob.halloweenEventComplete),
            Sprite('dearsantamark', 'dearsantamark', (1300, 250, 400, 200), lambda: glob.halloweenEventComplete),
        ]
    }

#LABELS
label boysdormjimmysroom:
    $ intownmarker = False
    jump boysdormjimmysroom_loop

label boysdormjimmysroom_loop:
    $ resetscene()
    call screen map('boysdormjimmysroom')
    jump boysdormjimmysroom_loop

label boysdormjimmysroom_window:
    if quests.goodbyeWendy == ACTIVE:
        if calendar.when[2] in [NIGHT]:
            __("Someone is coming...")
            jump wendygoodbyescene
    elif quests.fionaNightDate == ACTIVE:
        if calendar.when[1] != TUESDAY:
            __("Fiona isn't coming until Tuesday.")
        elif calendar.when[2] != NIGHT:
            __("Fiona won't be here until midnight.")
        else:
            jump chapterone_fionanightdate
    elif calendar.when[2] in [MORNING, AFTERNOON]:
        if not boysdormjimmysroom.alwaysSunnyComment:
                __("You know what they say - it's always sunny in Philadelphia.")
            $ boysdormjimmysroom.alwaysSunnyComment = True
        else:
            else:
                __("Sunny day.")
    elif calendar.when[2] == EVENING:
        elif calendar.when[2] == EVENING:
            __("It's getting dark out.")
    else:
        else:
            __("It's pitch black outside.")
    jump boysdormjimmysroom_loop

label boysdormjimmysroom_nightstand:
    if not boysdormjimmysroom.nightstandChecked:
            __("What the?")
            __("It's locked.")
            __("I guess I need a key or something.")
        $ boysdormjimmysroom.nightstandChecked = True
    else:
        else:
            __("It's locked.")
    jump boysdormjimmysroom_loop

label boysdormjimmysroom_closet:
    $ gotoscene('dormwardrobe')

label boysdormjimmysroom_bed:
    $ time = calendar.when[2]
    if calendar.when[0] == PROLOGUE and time != NIGHT:
        __("I'm not in the mood to sleep this early.")
        jump boysdormjimmysroom_loop
    $ night1 = (calendar.when == (PROLOGUE, WEDNESDAY, NIGHT))
    $ night2 = (calendar.when == (PROLOGUE, THURSDAY, NIGHT))
    menu:
        __("Take a nap") if time < NIGHT:
            jump nap_menu
        __("Go to sleep"):
            if night1:
                jump prologue_mysterygirlnight1
            elif night2:
                jump prologue_mysterygirlnight2
            # TODO: actually implement weekends
            elif calendar.when[1] == FRIDAY:
                menu:
                    __("Skip the weekend?"):
                        hide screen freeroamhud
                        stop music
                        scene black with fade
                        # skip to Monday
                        # (ugly but Ren'Py doesn't really have for-loops)
                        call nextday from _call_nextday_2
                        call nextday from _call_nextday_3
                        call sleep from _call_sleep_1
                    __("Go to town for the weekend"):
                        $ Jimmy.outfit = JIMMY_DEFAULT
                        hide screen freeroamhud
                        $ intownmarker = True
                        if calendar.when[2] in [MORNING, AFTERNOON]:
                            show jimmytownhouseday with fade
                            if quests.bathtubclimax == LOCKED:
                                $ quests.bathtubclimax = ACTIVE
                            if quests.drunkblair == LOCKED:
                                $ quests.drunkblair = SATISFIED
                        else:
                            show jimmytownhousenight with fade
                            if quests.bathtubclimax == LOCKED:
                                $ quests.bathtubclimax = ACTIVE
                            if quests.drunkblair == LOCKED:
                                $ quests.drunkblair = SATISFIED
                        pause 0.8
                        $ gotoscene('townhouselivingroom', transition=fade)
                    __("Nevermind"):
                        jump boysdormjimmysroom_loop
            else:
                call sleep from _call_sleep_5
        __("Nevermind"):
            jump boysdormjimmysroom_loop
    $ gotoscene('boysdormjimmysroom', transition=fade)

label boysdormjimmysroom_panties:
    if not boysdormjimmysroom.pantiesChecked:
        __("She sure left in a hurry...")
        __("Judging by the stain, she got really wet down there before taking them off.")
        $ boysdormjimmysroom.pantiesChecked = True
        jump boysdormjimmysroom_loop
    else:
        __("These are Wendy's panties.")
        jump boysdormjimmysroom_loop

label boysdormjimmysroom_angiesnote:
    hide screen freeroamhud
    show angiesnote
    $ renpy.pause()
    jump boysdormjimmysroom_loop

label boysdormjimmysroom_derbylaptop:
    if chapter1_freeroam_iscomplete:
        call jimmyspc from _call_jimmyspc
    else:
        __("I'll have time to use my computer later.")
        __("Right now I need to do something else.")
        jump boysdormjimmysroom_loop

label boysdormjimmysroom_dearsantamark:
    if primordialpathchecked == True:
        if jilliandearsantasecret == False:
            jump finaltruth
        else:
            menu:
                __("Jillian Secret Scene"):
                    hide screen freeroamhud
                    call jillian_secretcowgirl_scene from _call_jillian_secretcowgirl_scene
                    jump boysdormjimmysroom_loop
                __("Nevermind"):
                    __("Nevermind"):
                    jump boysdormjimmysroom_loop
    else:
        call firstomen from _call_firstomen
    jump boysdormjimmysroom_loop

label boysdormjimmysroom_door:
    $ gotoscene('boysdormhallway')


####

label firstomen:
    hide screen freeroamhud
    scene jimmybedroomdearsanta with fade
    play music "audio/music/mysterytheme.ogg"
    if dearsantaqueststarted == True:
        Jimmy "What the hell is that?"
        Jimmy "I haven't eaten any mushrooms, haven't I?"
    $ dearsantaqueststarted = True
    show santashadow with dissolve
    dSanta "Who summons me?"
    Jimmy "..."
    dSanta "Speak now, servant..."
    Jimmy "..."
    dSanta "Umm, a hard headed one I see."
    dSanta "Fear not, I'm but a messenger of the truth."
    dSanta "If the truth you seek, you shall look in the past."
    dSanta "A past built in rotten wood and broken nails."
    dSanta "Don't you remember the castle that was built for you to reach the clouds?"
    dSanta "Of course, not... You didn't even know how to read back then."
    hide santashadow with dissolve
    stop music
    jump boysdormjimmysroom_loop

label finaltruth:
    hide screen freeroamhud
    scene jimmybedroomdearsanta with fade
    play music "audio/music/mysterytheme.ogg"
    show santashadow with dissolve
    dSanta "Finally, you've tried to reach enlightment, my servant."
    Jimmy "..."
    dSanta "I know it's been though, but here's a consolation prize if you couldn't have the truth in time."
    dSanta "I can see through your mind..."
    dSanta "Let me take you far away, to a place where everything is possible, even your deepest desires..."
    call jillian_secretcowgirl_scene from _call_jillian_secretcowgirl_scene_1
    scene jimmybedroomdearsanta with fade
    play music "audio/music/mysterytheme.ogg"
    show santashadow with dissolve
    dSanta "Satisfied?"
    dSanta "I hope you don't sell your soul for a woman."
    dSanta "Even the devil is cautious with them..."
    dSanta "Anyways, good job, servant."
    dSanta "I'll never see you again."
    $ jilliandearsantasecret = True
    hide santashadow with dissolve
    stop music
    jump boysdormjimmysroom_loop
