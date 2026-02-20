#SCREENS
init 1 python:
    scene_defs['mainbuildinginfirmary'] = {
        'music': MUSIC_MAINBUILDINGAMBIENCEDAY_THEME,
        'altermusic': MUSIC_MAINBUILDINGAMBIENCENIGHT_THEME,
        'maps': {
            'morning':   ("infirmarydayfall", "infirmarydayfallhover"),
            'afternoon': ("infirmaryafterfall", "infirmaryafterfallhover"),
            'evening':   ("infirmaryeveningfall", "infirmaryeveningfallhover"),
            'night':     ("infirmarynightfall", "infirmarynightfallhover")
        },
        'hotspots': [
            ('exit', (0, 843, 1916, 233)),
        ],
        'sprites': [
        ]
    }

#LABELS
label mainbuildinginfirmary:
    if quests.beatrixHomework == COMPLETE:
        if quests.beatrixHerpes == ACTIVE:
            jump infirmarynurseintro
    $ checkcurfew()
    jump mainbuildinginfirmary_loop

label mainbuildinginfirmary_loop:
    $ resetscene()
    call screen map('mainbuildinginfirmary')
    jump mainbuildinginfirmary_loop

label mainbuildinginfirmary_exit:
    $ gotoscene('mainbuildingentrance')


########################

label infirmarynurseintro:
    stop music
    hide screen freeroamhud
    Jimmy "Hello?"
    Jimmy "Is there someone in here?"
    play sound "audio/sfx/surprisedhum.ogg"
    Vanessa "Just a moment!"
    "{i}The voice came from behind a door at the back of the infirmary.{/i}"
    "{i}Suddenly, a woman dressed in a specially tight suit came out of the room.{/i}"
    play music "audio/music/funrocktheme01.ogg"
    show vanessa nurse coffee with dissolve
    play sound "audio/sfx/hey04.ogg"
    Vanessa "Good day! Umm, good afternoon or evening, I'm not sure what time of day is."
    Vanessa "Are you feeling something weird in your body?"
    Vanessa "Maybe your stomach, you head, your pen... Uh, your chest..."
    Jimmy "Umm, no."
    Vanessa "Oh, that's great, so why are you here, then?"
    $ Vanessa.met = True
    Vanessa "By the way, I'm Vanessa, the nurse. It's obvious, right?"
    Vanessa "Sorry if I talk too fast, it must be the coffee, or I'm just like this. Who knows, right?"
    play sound "audio/sfx/giggle01.ogg"
    Vanessa "Ha, ha, ha, ha, ha..."
    Vanessa "Uh, well. I can see that you don't talk much, so I'll just wait for you to say something, okay?"
    Jimmy "..."
    Jimmy "Well, it's good to meet you Vanessa. I'm [player_name]."
    Vanessa "Awww, it's a pleasure [player_name]."
    Jimmy "I'm here to ask you something about a friend of mine that has a problem on her face."
    play sound "audio/sfx/hmm02.ogg"
    Vanessa "Uh, okay. What could it be? Humm, let me think about it while you give more information."
    Jimmy "Umm, I think it's called Dermatitis something..."
    Jimmy "It looks like cold sores, but my friend says that it's not."
    Vanessa "Oh, wait! I think I remember who you're talking to."
    Vanessa "The girl with the brackets... Ummm, what's her name?"
    Jimmy "Beat..."
    play sound "audio/sfx/femaleclearthroat.ogg"
    Vanessa "BEATRIX! That's right! That's right. Beatrix has a perioral dermatitis."
    Vanessa "I wonder why she hasn't come to me for a check."
    Jimmy "Well, she's a bit estressed out right now with some homework."
    Vanessa "Of course, I understand. Well, now that her friend came to me, you can take this cream to her and be her hero."
    call item_pickup(ItemDermatitisCream) from _call_item_pickup_41
    Vanessa backpose "How about that? Isn't that romantic?"
    Jimmy "Uhh, sure..."
    Vanessa "Great! Do you need something else?"
    Jimmy "Umm, no."
    play sound "audio/sfx/alright03.ogg"
    Vanessa "Alright, thank you coming! See you later!"
    hide vanessa with vpunch
    "{i}As quickly as she came out, she got back inside the room at the back.{/i}"
    Jimmy "Wow, that caffeine it's doing its work."
    Jimmy "Well, let's see if this cream helps Beatrix."
    $ quests.beatrixHerpes = SATISFIED
    call nexttime from _call_nexttime_52
    $ gotoscene('mainbuildingentrance')
