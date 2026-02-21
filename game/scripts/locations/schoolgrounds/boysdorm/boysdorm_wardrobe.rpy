#SCREENS
init 1 python:
    scene_defs['dormwardrobe'] = {
        'music': MUSIC_ELEVATOR_THEME,
        'altermusic': MUSIC_ELEVATOR_THEME,
        'maps': {
            'default':   ("clothesinterfacebase", "clothesinterfacebasehover"),
        },
        'hotspots': [
            ('exit', (1, 2, 160, 1076)),
        ],
        'sprites': [
            Sprite('yellowjacket', 'yellowjacketsprite', (1242, 36, 156, 504), lambda: prologue.firstNight == True),
            Sprite('uniform01', 'uniformsprite01', (1128, 36, 174, 504), lambda: prologue.firstNight == True),
            Sprite('homelandercostume', 'homelandercostumesprite', (504, 18, 132, 204), lambda: ItemHeroCostume in Jimmy.inventory),
            Sprite('piratecostume', 'piratecostumesprite', (569, 36, 200, 204), lambda: ItemPirateCostume in Jimmy.inventory),
            Sprite('shaggycostume', 'shaggycostumesprite', (665, 138, 132, 204), lambda: ItemShaggyCostume in Jimmy.inventory),
        ]
    }

#LABELS
label dormwardrobe:
    jump dormwardrobe_loop

label dormwardrobe_loop:
    $ resetscene()
    call screen map('dormwardrobe')
    jump dormwardrobe_loop

label dormwardrobe_yellowjacket:
    $ Jimmy.outfit = JIMMY_DEFAULT
    show jimmy smug with dissolve
    "I like this jacket, makes me look buff."
    $ gotoscene('boysdormjimmysroom', transition=fade)

label dormwardrobe_uniform01:
    if jimmynewuniform == False:
        show jimmy uniform intro with dissolve
        Jimmy "Well, I look like an idiot."
        Jimmy "Let's see..."
        show jimmy uniform fix with dissolve
        Jimmy "Now, that's better."
        $ jimmynewuniform = True
    $ Jimmy.outfit = JIMMY_UNIFORM
    show jimmy smug with dissolve
    "Alright, it fits pretty well."
    $ gotoscene('boysdormjimmysroom', transition=fade)

label dormwardrobe_shaggycostume:
    $ halloween = (calendar.when == (CHAPTER_1, FRIDAY, NIGHT))
    $ Jimmy.outfit = JIMMY_SHAGGY
    show jimmy smug with dissolve
    "Looks good..."
    if glob.halloweenEventComplete:
        menu:
            "{i}Replay the Halloween event?{/i}"

            "Yes":
                jump skip_to_halloween
            "No":
                $ Jimmy.outfit = JIMMY_UNIFORM
                jump boysdormjimmysroom_closet
    elif not halloween:
        "I should wait until the night of Halloween to change into my costume."
        menu:
            "{i}Skip ahead to Friday night?{/i}"

            "Yes":
                jump skip_to_halloween
            "No":
                $ Jimmy.outfit = JIMMY_UNIFORM
                jump boysdormjimmysroom_closet

label dormwardrobe_piratecostume:
    $ halloween = (calendar.when == (CHAPTER_1, FRIDAY, NIGHT))
    $ oldOutfit = Jimmy.outfit
    $ Jimmy.outfit = JIMMY_PIRATE
    show jimmy smug with dissolve
    "Looks good."
    if glob.halloweenEventComplete:
        menu:
            "{i}Replay the Halloween event?{/i}"

            "Yes":
                jump skip_to_halloween
            "No":
                $ Jimmy.outfit = oldOutfit
                jump boysdormjimmysroom_closet
    elif not halloween:
        "But I should wait until the night of the Halloween party to change into my costume."
        menu:
            "{i}Skip ahead to Friday night?{/i}"

            "Yes":
                jump skip_to_halloween
            "No":
                $ Jimmy.outfit = oldOutfit
                jump boysdormjimmysroom_closet

label dormwardrobe_homelandercostume:
    $ halloween = (calendar.when == (CHAPTER_1, FRIDAY, NIGHT))
    $ oldOutfit = Jimmy.outfit
    $ Jimmy.outfit = JIMMY_HOMELANDER
    show jimmy smug with dissolve
    "Looks good."
    if glob.halloweenEventComplete:
        menu:
            "{i}Replay the Halloween event?{/i}"

            "Yes":
                jump skip_to_halloween
            "No":
                $ Jimmy.outfit = oldOutfit
                jump boysdormjimmysroom_closet
    elif not halloween:
        "But I should wait until the night of the Halloween party to change into my costume."
        menu:
            "{i}Skip ahead to Friday night?{/i}"

            "Yes":
                jump skip_to_halloween
            "No":
                $ Jimmy.outfit = oldOutfit
                jump boysdormjimmysroom_closet

label skip_to_halloween:
    $ halloween = (calendar.when == (CHAPTER_1, FRIDAY, NIGHT))
    if not halloween:
        hide screen freeroamhud
        scene black with fade
        # TODO: update the day counter
        $ calendar.when = (CHAPTER_1, FRIDAY, NIGHT)
        $ showscene('boysdormjimmysroom', transition=fade)
        show jimmy smug with dissolve
    jump chapterone_garyhalloweenintro

label dormwardrobe_exit:
    $ gotoscene('boysdormjimmysroom', transition=fade)
