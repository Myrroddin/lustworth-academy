default headmasterbathroomsprite = False

#SCREENS
init 1 python:

    def headmasterbathroomsprite_showif():
        if DawsonDaylimit == True:
            return False
        elif headmasterbathroomsprite == True:
            return True
        return False

    scene_defs['mainbuildinglefthallway'] = {
        'music': MUSIC_MAINBUILDINGAMBIENCEDAY_THEME,
        'altermusic': MUSIC_MAINBUILDINGAMBIENCENIGHT_THEME,
        'maps': {
            'morning':   ("main1lefthallday", "main1lefthalldayhover"),
            'afternoon': ("main1lefthallafter", "main1lefthallafterhover"),
            'evening':   ("main1lefthallevening", "main1lefthalleveninghover"),
            'night':     ("main1lefthallnight", "main1lefthallnighthover"),
        },
        'hotspots': [
            ('cafeteria', (425, 371, 304, 260)),
            ('boysbathroom', (831, 386, 60, 276)),
            ('girlsbathroom', (930, 351, 83, 353)),
            ('labs', (1068, 164, 351, 575)),
            ('halloweenposter', (1671, 248, 110, 189)),
            ('campaignposter', (1667, 443, 116, 146)),
            ('lockers', (196, 354, 195, 488)),
            ('toentrance', (0, 903, 1920, 174)),
        ],
        'sprites': [
            Sprite('headmasterbath', 'headmasterdialog01', (730, 400, 128, 350), headmasterbathroomsprite_showif)
        ]
    }

#LABELS
label mainbuildinglefthallway:
    if mainbuildingentrance_showif_headmastersdoor and quests.headmasterSpy == COMPLETE:
        if quests.missdawsonBathroomIncident == LOCKED:
            $ headmasterbathroomsprite = True
        else:
            $ headmasterbathroomsprite = False
    $ checkcurfew()
    jump mainbuildinglefthallway_loop

label mainbuildinglefthallway_loop:
    $ resetscene()
    call screen map('mainbuildinglefthallway')
    jump mainbuildinglefthallway_loop

label mainbuildinglefthallway_cafeteria:
    $ gotoscene('mainbuildingcafeteria')

label mainbuildinglefthallway_boysbathroom:
    if quests.algieScroll == ACTIVE:
        jump algiescrollfound
    else:
        "No need to go in there."
        jump mainbuildinglefthallway_loop

label mainbuildinglefthallway_girlsbathroom:
    "No need to go in there."
    jump mainbuildinglefthallway_loop

label mainbuildinglefthallway_halloweenposter:
    if quests.halloweenCostume == LOCKED:
        "\"Trustworth's annual Halloween Party!\""
        "\"Wear your best costume and win the prize!\""
        "Huh, sounds interesting."
    elif quests.halloweenCostume == ACTIVE:
        "The Halloween party is this Friday."
        "I still need a costume. Fiona said she was selling some, I wonder if she still has any."
    elif quests.halloweenCostume != COMPLETE:
        if calendar.when[1] != FRIDAY:
            "The Halloween party is this Friday."
        else:
            "The Halloween party is tonight."
        "I'll need to be sure to wear my costume."
    jump mainbuildinglefthallway_loop

label mainbuildinglefthallway_campaignposter:
    "\"Don't be a nerd. Be cool and vote for Ted!\""
    "\"Ted for prez!\""
    "..."
    "He looks like an idiot."
    jump mainbuildinglefthallway_loop

label mainbuildinglefthallway_labs:
    if calendar.when[1:] == (MONDAY, AFTERNOON):
        jump biologyclass
    elif calendar.when[1:] == (WEDNESDAY, MORNING):
        jump chemistryclass
    elif quests.beatrixHomework == COMPLETE:
        if quests.beatrixHerpes == LOCKED:
            jump beatrixbiologyessay02
        if quests.beatrixHerpes == SATISFIED:
            jump beatrixbiologyessay03
    else:
        "I don't have Biology or Chemistry right now."
    jump mainbuildinglefthallway_loop

label mainbuildinglefthallway_toentrance:
    $ gotoscene('mainbuildingentrance')

label mainbuildinglefthallway_headmasterbath:
    jump headmasterbathroomincident

label mainbuildinglefthallway_lockers:
    if quests.slingshotcraft == ACTIVE:
        jump shapedbranchscene
    elif quests.slingshotcraft == SATISFIED:
        if Jimmy.hasItem(ItemShapedBranch):
            Jimmy "The lockers. Why I don't have one? Nobody knows..."
            jump mainbuildinglefthallway_loop
        else:
            jump shapedbranchscene
    Jimmy "The lockers. Why I don't have one? Nobody knows..."
    jump mainbuildinglefthallway_loop


#LOCATIONSCENES

label headmasterbathroomincident:
    hide screen freeroamhud
    hide headmasterdialog01 with dissolve
    play sound "audio/sfx/clearthroat01.ogg"
    play music MUSIC_HEADMASTERS_THEME
    show stapleneck stern with dissolve
    Stapleneck "Move along, student. There is nothing to see here."
    Stapleneck stern talk "Oh, it's you Mr. [player_surname]."
    Stapleneck "Are you making yourself comfortable around here, my boy?"
    Jimmy "Just trying to fit in, sir."
    Stapleneck arm "That's right, don't make a nuisance of yourself, that's not the Trustworth way, boy."
    Jimmy "Yeah, you could have fooled me..."
    Stapleneck smug talk "What?"
    Jimmy "I said you could have fooled me."
    Jimmy "This place is full maniacs."
    Stapleneck sarcasm "Nonsense, that's just school spirit!"
    play sound SOUND_RECORD_SCRATCH
    stop music
    Ruby "Sir! I cannot stand this anymore!"
    show ruby uniform stern with dissolve
    play sound "audio/sfx/mad01.ogg"
    Ruby "That thing is getting everywhere, I can't stop scratching my butt!"
    show rubyscratchbutt with fade
    play sound SOUND_SEXY_INTRO
    Ruby "Look! It was all over the toilet's seat."
    Ruby "It's itching everywhere!"
    play sound "audio/sfx/clearthroat01.ogg"
    Stapleneck neutral "Miss Matthews, that is completely unnecessary, please stop showing yourself like this."
    hide rubyscratchbutt with dissolve
    play sound "audio/sfx/hmm01.ogg"
    play music MUSIC_FUNNY_MOMENT
    Ruby "My daddy will hear about this."
    Ruby "I will never, ever, use this bathroom again."
    Ruby "I should have known that this kind of places used by the common people would do me no good."
    Stapleneck arm "The matter with be dealed with at once, Miss Matthews, there is no need to cause any disturbance beyond this."
    play sound "audio/sfx/mad01.ogg"
    Ruby "Ughh... What are you looking at, poor guy?"
    Ruby "I can't stand this people, I'm gone."
    hide ruby with vpunch
    stop music
    play sound "audio/sfx/clearthroat01.ogg"
    Stapleneck "Well, that what I call some high jinks."
    Stapleneck smug talk "I need to deal with this now."
    Stapleneck "Please, Mr. [player_surname], go and tell Miss Dawson that I will be very busy the rest of the evening."
    Stapleneck "Tell her that our meeting today has to be posponed, sadly."
    Jimmy "Alright."
    Stapleneck stern talk "Alright, what?"
    Jimmy "Alright, sir..."
    $ quests.missdawsonBathroomIncident = ACTIVE
    $ gotoscene('mainbuildinglefthallway')