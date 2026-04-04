# This represents the townhouse hallway the first night Jimmy arrives.
# It has its own scene since there is so much special behavior the first night.
# *THIS IS THE EXCEPTION, NOT THE RULE*

#VARIABLES
default townhousehallwayfirstnight.alicesRoomChecked = False
default townhousehallwayfirstnight.blairsRoomChecked = False
default townhousehallwayfirstnight.cassidyRoomChecked = False

#SCREENS
init 1 python:
    scene_defs['townhousehallwayfirstnight'] = {
        'music': MUSIC_SNEAK_THEME,
        'altermusic': MUSIC_SNEAK_THEME,
        'maps': {
            'default': ("townhousehallwayfallnight", "townhousehallwayfallnighthover"),
        },
        'hotspots': [
            ('window', (0, 146, 126, 633)),
            ('jimmysroom', (387, 1, 414, 205)),
            ('blairsroom', (240, 411, 177, 353)),
            ('cassidysroom', (705, 256, 163, 586)),
            ('alicesroom', (1021, 81, 237, 859)),
            ('bathroom', (509, 352, 124, 433)),
            ('stairs', (1484, 0, 435, 1077)),
        ],
        'sprites': [
            # Sprite(key, image, (x, y, w, h), showif)
        ]
    }

#LABELS
label townhousehallwayfirstnight:
    jump townhousehallwayfirstnight_loop

label townhousehallwayfirstnight_loop:
    $ resetscene()
    call screen map('townhousehallwayfirstnight')
    jump townhousehallwayfirstnight_loop

label townhousehallwayfirstnight_window:
    if Jimmy.outfit != JIMMY_STEALTH:
        "I need to change into something lighter for a stealth mission."
    elif quests.cassidyDildo == LOCKED:
        jump prologue_cassidycaught
    elif quests.cassidyDildo == ACTIVE:
        show cassidy pajama neutral with dissolve
        Cassidy "I'm watching you, [player_name]."
        Cassidy "Get me my toy, now."
    elif quests.cassidyDildo == SATISFIED:
        "I should give Cassidy her dildo."
    elif townhousehallwayfirstnight.cassidyRoomChecked == True:
        "Alright, Cassidy is asleep."
        "Let's roll to the mayor's mansion."
        jump prologue_mayorsmansion
    else:
        "I, uh, should make sure Cassidy is asleep. Right."
        "I just need to find a way to see into her room."
    jump townhousehallwayfirstnight_loop

label townhousehallwayfirstnight_jimmysroom:
    $ gotoscene('townhousejimmysroomnightinfiltration')

label townhousehallwayfirstnight_blairsroom:
    if not townhousehallwayfirstnight.blairsRoomChecked:
        "Blair's room"
        scene blairsleepingpeek01 with fade
        "The door's open, that's weird."
    hide screen freeroamhud
    scene blairsleepingpeek02 with fade
    if not townhousehallwayfirstnight.blairsRoomChecked:
        "Oh, that's Blair."
        "Wow, she sleeps almost naked."
        $ townhousehallwayfirstnight.blairsRoomChecked = True
    $ renpy.pause()
    "I better go before I wake her up."
    jump townhousehallwayfirstnight_loop

label townhousehallwayfirstnight_cassidysroom:
    if quests.cassidyDildo == LOCKED:
        "I hear noises from behind, but the door is locked."
    elif quests.cassidyDildo == ACTIVE:
        "I need to find her toy."
        "She said it should be somewhere in my room."
    elif quests.cassidyDildo == SATISFIED:
        jump prologue_cassidydildo
    elif not townhousehallwayfirstnight.cassidyRoomChecked == True:
        "I can hear noises coming from Cassidy's room."
    else:
        "She's asleep. The coast is clear."
    jump townhousehallwayfirstnight_loop

label townhousehallwayfirstnight_alicesroom:
    if not townhousehallwayfirstnight.alicesRoomChecked:
        "This seems to be Alice's room."
        $ townhousehallwayfirstnight.alicesRoomChecked = True
    "It's locked."
    jump townhousehallwayfirstnight_loop

label townhousehallwayfirstnight_bathroom:
    "Looks like a bathroom. I don't need to go."
    jump townhousehallwayfirstnight_loop

label townhousehallwayfirstnight_stairs:
    "That's not a good idea. I don't want to get caught by Kassandra."
    "I need to find another way out."
    jump townhousehallwayfirstnight_loop
