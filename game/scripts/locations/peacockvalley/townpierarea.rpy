#VARIABLES

#SCREENS
init 1 python:
    scene_defs['townpierarea'] = {
        'music': MUSIC_SEASIDEAMBIENCEDAY_THEME,
        'altermusic': MUSIC_SEASIDEAMBIENCENIGHT_THEME,
        'maps': {
            'morning':   ("townpierareafallday", "townpierareafalldayhover"),
            'afternoon': ("townpierareafallafternoon", "townpierareafallafternoonhover"),
            'evening':   ("townpierareafallevening", "townpierareafalleveninghover"),
            'night':     ("townpierareafallnight", "townpierareafallnighthover")
        },
        'hotspots': [
            ('busstop', (3, 614, 404, 462)),
            ('carnivalfair', (122, 42, 516, 317)),
            ('towncenter', (1403, 51, 516, 295)),
            ('kassandrahouse', (1086, 393, 511, 539)),
            ('antonellahouse', (694, 329, 392, 363)),
            
        ],
        'sprites': [
            # Sprite(key, image, (x, y, w, h), showif)
        ]
    }

#LABELS
label townpierarea:
    jump townpierarea_loop

label townpierarea_loop:
    $ resetscene()
    call screen map('townpierarea')
    jump townpierarea_loop

label townpierarea_carnivalfair:
    Jimmy "The carnival fair."
    jump townpierarea_loop

label townpierarea_towncenter:
    Jimmy "That's the town center."
    jump townpierarea_loop

label townpierarea_antonellahouse:
    Jimmy "Our neighbor's house."
    if quests.punnyDatingTeacher == ACTIVE and calendar.when[2] == NIGHT:
        hide screen freeroamhud
        Jimmy "Alright, this is Lucía's address."
        play sound "audio/sfx/doorknock01.ogg"
        Jimmy "I should have gotten perfume or something..."
        Jimmy "Shit, am I bad at dating."
        Punny "Coming!"
        play sound "audio/sfx/dooropen01.ogg"
        jump punnyromanticdinner
    elif quests.punnyDatingTeacher == ACTIVE:
        hide screen freeroamhud
        Jimmy "This is Miss Punny's address."
        Jimmy "I should get ready for our dinner at night."
    jump townpierarea_loop

label townpierarea_kassandrahouse:
    $ gotoscene('townhousefront')

label townpierarea_busstop:
    __("Where do you want to go?")
    menu:
        __("Beach Area"):
            $ gotoscene('seasideareamap')
        __("Ranch") if prologue.complete:
            if calendar.when[1] == SATURDAY:
                if calendar.when[2] == MORNING:
                    Jimmy "Let's get to work."
                    scene laterthatday with fade
                    $ renpy.pause()
                    $ gotoscene('dakotasranch')
                else:
                    Jimmy "It's too late to go today."
                    Jimmy "Better go in the morning."
                    jump townpierarea_loop
            elif calendar.when[1] == SUNDAY:
                if calendar.when[2] == MORNING:
                    Jimmy "Let's get to work."
                    scene laterthatday with fade
                    $ renpy.pause()
                    $ gotoscene('dakotasranch')
                else:
                    Jimmy "It's too late to go today."
                    Jimmy "Better go in the morning."
                    jump townpierarea_loop
            else:
                Jimmy "It's too late to go today."
                Jimmy "Saturday seems like a good day to work at the ranch."
                jump townpierarea_loop

