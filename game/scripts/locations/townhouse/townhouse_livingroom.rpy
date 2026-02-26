#VARIABLES
default townhouselivingroom.basementDoorChecked = False

#SCREENS
init 1 python:
    def townhouselivingroom_showif_kassandra():
        if quests.blairUSB == LOCKED:
            return False
        if prologue.awkwardBreakfast:
            return False
        return True

    scene_defs['townhouselivingroom'] = {
        'music': MUSIC_TOWNHOUSE,
        'altermusic': MUSIC_TOWNHOUSE,
        'maps': {
            'morning': ('jimmyhouselivingroomday', 'jimmyhouselivingroomdayhover'),
            'afternoon': ('jimmyhouselivingroomafter', 'jimmyhouselivingroomafterhover'),
            'default': ('jimmyhouselivingroomafter', 'jimmyhouselivingroomafterhover'),
            'night':   ("jimmyhouselivingroomnight", "jimmyhouselivingroomnighthover")
        },
        'hotspots': [
            ('stairs', (1476, 84, 115, 542)),
            ('basementdoor', (1680, 47, 148, 688)),
            ('todiningroom', (894, 20, 564, 549)),
            ('housefront', (0, 5, 348, 1072)),
        ],
        'sprites': [
            Sprite('kassandra', 'kassandrapajama01', (1152, 216, 139, 420), townhouselivingroom_showif_kassandra),
            Sprite('boxes', 'jimmysmovingboxes', (1377, 753, 544, 327), lambda: calendar.when == (PROLOGUE, SATURDAY, MORNING))
        ]
    }

#LABELS
label townhouselivingroom:
    if quests.artProject == ACTIVE:
        if calendar.when[2] == AFTERNOON:
            play sound "audio/sfx/doorknock01.ogg"
            Jimmy "That must be Miku at the door."
    elif quests.bathtubclimax == SATISFIED:
        if calendar.when[2] == NIGHT:
            jump kassandrabathtubclimax
    jump townhouselivingroom_loop

label townhouselivingroom_loop:
    $ resetscene()
    call screen map('townhouselivingroom')
    jump townhouselivingroom_loop

label townhouselivingroom_stairs:
    $ gotoscene('townhousehallway')

label townhouselivingroom_basementdoor:
    if not townhouselivingroom.basementDoorChecked:
        __("This door is locked.")
        __("I think it leads to the basement.")
        $ townhouselivingroom.basementDoorChecked = True
    else:
        __("Locked.")
    jump townhouselivingroom_loop

label townhouselivingroom_boxes:
    if quests.blairUSB == ACTIVE:
        jump prologue_blairusbcollision
    elif quests.blairUSB == SATISFIED:
        __("I already got the USB drive.")
        __("I should go to my room and finish setting up my PC.")
    else:
        __("The boxes are empty.")
    jump townhouselivingroom_loop

label townhouselivingroom_todiningroom:
    if calendar.when[:2] == (PROLOGUE, SATURDAY):
        if calendar.when[2] == EVENING:
            if prologue.dakotaJobOffer == False:
                jump prologue_dakotaantonellaintro
    $ gotoscene('townhousediningroom')

label townhouselivingroom_kassandra:
    hide screen freeroamhud
    hide kassandrapajama01
    show kassandra pajamas with dissolve
    if quests.blairUSB == COMPLETE:
        Kassandra "Hey, honey."
        if alice_breakfastwarning == True:
            Kassandra "We were waiting for you."
            jump prologue_awkwardbreakfast
        else:
            Kassandra "Can you go tell Alice that breakfast is ready, please?"
            $ breakfast_ready = True
            jump townhouselivingroom_loop
    else:
        Kassandra "Have you talked to your [roommate_female]s yet?"
        Kassandra "If you see them, please tell them that breakfast is ready."
        $ breakfast_ready = True
        jump townhouselivingroom_loop

label townhouselivingroom_housefront:
    if prologue.awkwardBreakfast == True:
        $ gotoscene('townhousefront')
    else:
        __("I have things to do before going out.")
        jump townhouselivingroom_loop
