# This represents Jimmy's townhouse bedroom the first night he arrives.
# It has its own scene since there is so much unique behavior the first night.
# *THIS IS THE EXCEPTION, NOT THE RULE*

#SCREENS
init 1 python:
    def townhousejimmysroomfirstnight_showif_floorcrack():
        if quests.cassidyDildo != COMPLETE:
            return False
        if townhousehallwayfirstnight.cassidyRoomChecked == True:
            return False
        return True

    scene_defs['townhousejimmysroomnightinfiltration'] = {
        'music': MUSIC_SNEAK_THEME,
        'altermusic': MUSIC_SNEAK_THEME,
        'maps': {
            'default': ("jimmytownbedroomnight", "jimmytownroomemptyhover"),
        },
        'hotspots': [
            ('window', (381, 36, 342, 417)),
            ('pc', (110, 394, 266, 161)),
            ('closet', (748, 391, 389, 248)),
            ('bed', (706, 648, 852, 231)),
            ('underbed', (577, 906, 983, 166)),
            ('floorcrack', (1570, 980, 151, 98)),
            ('tohallway', (0, 888, 574, 192)),
        ],
        'sprites': [
            Sprite('floorcrack', 'floorcrackmoans', (1488, 944, 204, 136), townhousejimmysroomfirstnight_showif_floorcrack, hover='floorcrackmoanhover'),
        ]
    }

#LABELS
label townhousejimmysroomnightinfiltration:
    jump townhousejimmysroomnightinfiltration_loop

label townhousejimmysroomnightinfiltration_loop:
    $ resetscene()
    call screen map('townhousejimmysroomnightinfiltration')
    jump townhousejimmysroomnightinfiltration_loop

label townhousejimmysroomnightinfiltration_window:
    "The night is dark and full of possibilities."
    jump townhousejimmysroomnightinfiltration_loop

label townhousejimmysroomnightinfiltration_pc:
    "Don't have time for that."
    jump townhousejimmysroomnightinfiltration_loop

label townhousejimmysroomnightinfiltration_closet:
    if Jimmy.outfit == JIMMY_STEALTH:
        "I already have what I need."
    else:
        show jimmy neutral with dissolve
        "Let's get some proper clothes for tonight."
        "I think this should work for a stealth mission."
        $ Jimmy.outfit = JIMMY_STEALTH
        show jimmy smug with dissolve
        "Perfect."
    hide jimmy with dissolve
    jump townhousejimmysroomnightinfiltration_loop

label townhousejimmysroomnightinfiltration_bed:
    "I have a plan tonight. I won't sleep 'til it's done."
    jump townhousejimmysroomnightinfiltration_loop

label townhousejimmysroomnightinfiltration_underbed:
    if quests.cassidyDildo == LOCKED:
        "I think there's something in the back. It looks like it's made of rubber."
        "...I'm not gonna touch it."
    elif quests.cassidyDildo == ACTIVE:
        "I think that's Cassidy's dildo back there."
        call item_pickup(ItemCassidyDildo) from _call_item_pickup_13
        "She is so dirty..."
        $ quests.cassidyDildo = SATISFIED
    else:
        "No monsters."
    jump townhousejimmysroomnightinfiltration_loop

label townhousejimmysroomnightinfiltration_floorcrack:
    if quests.cassidyDildo == COMPLETE and not townhousehallwayfirstnight.cassidyRoomChecked:
        jump prologue_cassidypeephole
    else:
        hide screen freeroamhud
        show cassidybedroomnightpeek with dissolve
        if townhousehallwayfirstnight.cassidyRoomChecked == True:
            "I can see Cassidy's bedroom on the other side."
        else:
            "I can see Cassidy's bedroom on the other side."
    jump townhousejimmysroomnightinfiltration_loop

label townhousejimmysroomnightinfiltration_tohallway:
    $ gotoscene('townhousehallwayfirstnight')

#ANIMATIONS
image floorcrackmoans:
    'floorcrackmoan02'
    pause 0.8
    'floorcrackmoan01'
    pause 0.8
    'floorcrackmoan03'
    pause 0.8
    'floorcrackmoan01'
    pause 0.8
    repeat
