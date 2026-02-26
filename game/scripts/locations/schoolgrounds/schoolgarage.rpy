#SCREENS
init 1 python:
    scene_defs['schoolgarage'] = {
        'music': MUSIC_SCHOOLGROUNDSAMBIENCEDAY_THEME,
        'altermusic': MUSIC_SCHOOLGROUNDSAMBIENCENIGHT_THEME,
        'maps': {
            'morning':   ("shopclassroomfallday", "shopclassroomfalldayhover"),
            'afternoon': ("shopclassroomfallafternoon", "shopclassroomfallafternoonhover"),
            'evening':   ("shopclassroomfallevening", "shopclassroomfalleveninghover"),
            'night':     ("shopclassroomfallnight", "shopclassroomfallnighthover")
        },
        'hotspots': [
            ('exit', (1, 23, 571, 1054)),
        ],
        'sprites': [
            # Sprite(key, image, (x, y, w, h), showif)
        ]
    }

#LABELS
label schoolgarage:
    $ checkcurfew()
    if calendar.when[1:] == (FRIDAY, AFTERNOON):
        jump shopclass
    elif quests.slingshotcraft == ACTIVE:
        jump rubberbandscene
    elif quests.slingshotcraft == SATISFIED:
        if Jimmy.hasItem(ItemRubberBand):
            jump schoolgarage_loop
        else:
            jump rubberbandscene
    jump schoolgarage_loop

label schoolgarage_loop:
    $ resetscene()
    call screen map('schoolgarage')
    jump schoolgarage_loop

label schoolgarage_exit:
    $ gotoscene('schoolgroundsparkinglot')

label dawsonaudreyhalloween:
    hide screen freeroamhud
    $ showscene('schoolgarage', transition=fade)
    play music MUSIC_AUDREY_THEME
    Jimmy "Good day! Is anyone there?"
    Audrey "Yes! I'm back here!"
    scene audreysexymechanicdawson with fade
    play sound SOUND_SEXY_INTRO
    Audrey "Sup, dude. Need anything?"
    Jimmy "Umm... Yeah, I came to ask you about the Halloween staff reunion."
    Jimmy "The secretary wants to know if you will assist."
    Audrey "The party! Fuck yeah, I will."
    Audrey "Oh, sorry. I shouldn't speak like that in school."
    Audrey "Can I ask you something, though?"
    Jimmy "Yeah."
    Audrey "Will there be any booze?"
    Audrey "I mean, it's a party, right?"
    Audrey "There has to be some."
    Jimmy "Maybe? I'm not sure."
    Audrey "Well, that's better than no."
    Audrey "See you there, dude!"
    Jimmy "Right..."
    $ quests.missdawsonHalloweenAudrey = COMPLETE
    $ gotoscene('schoolgroundsparkinglot')
