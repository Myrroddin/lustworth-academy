label dormwardrobe_costume(costume, narration, oldOutfit=None):
    $ halloween = (calendar.when == (CHAPTER_1, FRIDAY, NIGHT))
    if oldOutfit is None:
        $ oldOutfit = JIMMY_UNIFORM
    $ Jimmy.outfit = costume
    show jimmy smug with dissolve
    __(narration)
    if glob.halloweenEventComplete:
        menu:
            __("Replay the Halloween event?")
            __("Yes"):
                jump skip_to_halloween
            __("No"):
                $ Jimmy.outfit = oldOutfit
                jump boysdormjimmysroom_closet
    elif not halloween:
        __("But I should wait until the night of the Halloween party to change into my costume.")
        menu:
            __("Skip ahead to Friday night?")
            __("Yes"):
                jump skip_to_halloween
            __("No"):
                $ Jimmy.outfit = oldOutfit
                jump boysdormjimmysroom_closet

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
    __("I like this jacket, makes me look buff.")
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
    __("Alright, it fits pretty well.")
    $ gotoscene('boysdormjimmysroom', transition=fade)

label dormwardrobe_shaggycostume:
    call dormwardrobe_costume(JIMMY_SHAGGY, "Looks good...")

label dormwardrobe_piratecostume:
    $ oldOutfit = Jimmy.outfit
    call dormwardrobe_costume(JIMMY_PIRATE, "Looks good.", oldOutfit)

label dormwardrobe_homelandercostume:
    $ oldOutfit = Jimmy.outfit
    call dormwardrobe_costume(JIMMY_HOMELANDER, "Looks good.", oldOutfit)

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
