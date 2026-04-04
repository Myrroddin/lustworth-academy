#VARIABLES

#SCREENS
init 1 python:
    scene_defs['seasideareamap'] = {
        'music': MUSIC_SEASIDEAMBIENCEDAY_THEME,
        'altermusic': MUSIC_SEASIDEAMBIENCENIGHT_THEME,
        'maps': {
            'morning':   ("seasideneighborhoodfallday", "seasideneighborhoodfalldayhover"),
            'afternoon': ("seasideneighborhoodfallafternoon", "seasideneighborhoodfallafternoonhover"),
            'evening':   ("seasideneighborhoodfallevening", "seasideneighborhoodfalleveninghover"),
            'night':     ("seasideneighborhoodfallnight", "seasideneighborhoodfallnighthover")
        },
        'hotspots': [
            ('tikibar', (844, 499, 308, 247)),
            ('mansioncliff', (436, 0, 748, 345)),
            ('beachhorizon', (1, 3, 392, 1074)),
            ('suburbanarea', (1330, 74, 590, 464)),
            ('beachkiosk', (573, 865, 242, 155)),
            ('beachhouse', (540, 371, 274, 152)),
            ('tanyahouse', (1492, 681, 426, 395)),
        ],
        'sprites': [
            # Sprite(key, image, (x, y, w, h), showif)
        ]
    }

#LABELS
label seasideareamap:
    if prologue.visitthebeach == False:
        "Man, I love the beach."
        "I have a feeling I'm gonna spend a lot of time here."
        "Alright, let's see."
        "The mansion is up there, near the cliff."
        "Maybe I can find a way to climb to it."
        $ prologue.visitthebeach = True
    jump seasideareamap_loop

label seasideareamap_loop:
    $ resetscene()
    call screen map('seasideareamap')
    jump seasideareamap_loop

label seasideareamap_tikibar:
    if quests.fionaNightDate == ACTIVE:
        jump tikibarintro
    "There is a tiki bar on the beach."
    "Looks like a cool place to hang out."
    jump seasideareamap_loop

label seasideareamap_mansioncliff:
    "The Mayor's mansion."
    if prologue.checkthecliff == False:
        jump cliffcheckfionaintro
    elif prologue.findtherope == False:
        "I have to find something to fix the stairs, maybe a rope."
    jump seasideareamap_loop

label seasideareamap_beachhorizon:
    if prologue.checkthecliff == False:
        jump cliffcheckfionaintro
    elif quests.fionaNightDate == ACTIVE:
        Jimmy "I should get some ice at the bar."
        jump seasideareamap_loop
    $ gotoscene('seasidecliff')

label seasideareamap_suburbanarea:
    if quests.fionaNightDate == ACTIVE:
        Jimmy "Can't leave Fiona like that."
        Jimmy "I should get back to her."
        jump seasideareamap_loop
    $ gotoscene('townpierarea')

label seasideareamap_beachkiosk:
    "A small kiosk."
    jump seasideareamap_loop

label seasideareamap_beachhouse:
    "Must be nice to have a house that close to the beach."
    "It's on sale. I bet the price is really high."
    jump seasideareamap_loop

label seasideareamap_tanyahouse:
    jump seasideareamap_loop


#### SCENES ####

label tikibarintro:
    hide screen freeroamhud
    play music "audio/music/beachukelele.ogg"
    scene tikibarbackground with fade
    show matunga tiki neutral with dissolve
    Matunga "Hey, dude! Welcome to Matunga's Paradise"
    Matunga "First time I see you around, but you look like a cool dude, dude."
    Matunga "I got anything you need to have the best time around here, dude."
    Jimmy "Wow, this bar looks really nice."
    Matunga "Oh, thank you so much, dude."
    Matunga "You know, my house, your house, dude."
    Matunga "You're welcome anytime, dude."
    Jimmy "Thanks, dude."
    Matunga "Ha! That's right... I'm your dude now, dude."
    Jimmy "Ummm, I need some ice, can you sell me some?"
    Matunga "OF COURSE, DUDE!"
    call item_pickup(ItemIceBag) from _call_item_pickup_26
    Matunga "Here you go!"
    Jimmy "Wow, that was fast."
    Matunga "Told you, dude. This is the best place to hang out."
    Jimmy "How much for that?"
    Matunga "Oh, no, dude. At Matunga's Paradise, the ice is on the house, dude."
    Jimmy "Oh, wow, that's great."
    Jimmy "Thank you... dude."
    Matunga "No problem, dude. Please, come back anytime you need something."
    Jimmy "I sure will, bye."
    $ quests.fionaNightDate = SATISFIED
    stop music
    jump chapterone_fionasurfinglesson
