#VARIABLES
default intownmarker = False

#SCREENS
init 1 python:
    scene_defs['schoolgroundsmaingate'] = {
        'music': MUSIC_SCHOOLGROUNDSAMBIENCEDAY_THEME,
        'altermusic': MUSIC_SCHOOLGROUNDSAMBIENCENIGHT_THEME,
        'maps': {
            'morning':   ("academygatefallday", "academygatefalldayhover"),
            'afternoon': ("academygatefallafternoon", "academygatefallafternoonhover"),
            'evening':   ("academygatefallevening", "academygatefalleveninghover"),
            'night':     ("academygatefallmidnight", "academygatefallmidnighthover")
        },
        'hotspots': [
            ('toentranceplaza', (649, 357, 590, 639)),
            ('busstop', (0, 598, 227, 479)),
        ],
        'sprites': [
            # Sprite(key, image, (x, y, w, h), showif)
        ]
    }

#LABELS
label schoolgroundsmaingate:
    $ checkcurfew()
    $ intownmarker = False
    jump schoolgroundsmaingate_loop

label schoolgroundsmaingate_loop:
    $ resetscene()
    call screen map('schoolgroundsmaingate')
    jump schoolgroundsmaingate_loop

label schoolgroundsmaingate_toentranceplaza:
    $ gotoscene('schoolgroundsentrance')

label schoolgroundsmaingate_busstop:
    $ gateIsOpen = (calendar.when[1:] == (FRIDAY, EVENING) or (calendar.when[1] in [SATURDAY, SUNDAY] and calendar.when[2] != NIGHT))
    if gateIsOpen:
        if Jimmy.outfit == JIMMY_UNIFORM:
            __("I better change out of my uniform before I leave.")
        elif calendar.when == (PROLOGUE, FRIDAY, EVENING):
            jump prologue_kassandraintro
        else:
            menu:
                __("{i}Visit Kassandra's house?{/i}")

                __("Yes"):
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
                __("No"):
                    jump schoolgroundsmaingate_loop
    else:
        __("Can't take the bus until the weekend.")
    jump schoolgroundsentrance_loop
