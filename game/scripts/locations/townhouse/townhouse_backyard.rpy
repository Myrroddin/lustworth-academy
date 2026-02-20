#VARIABLES
default pastdeedschecked = False

#SCREENS
init 1 python:
    scene_defs['townhousebackyard'] = {
        'music': MUSIC_TOWNHOUSE,
        'altermusic': MUSIC_TOWNHOUSE,
        'maps': {
            'morning':   ("jimmytownbackyard", "jimmytownbackyardhover"),
            'afternoon': ("jimmytownbackyard", "jimmytownbackyardhover"),
            'evening':   ("jimmytownbackyard", "jimmytownbackyardhover"),
            'night':     ("jimmytownbackyardnight", "jimmytownbackyardnighthover")
        },
        'hotspots': [
            ('exit', (1523, 885, 395, 194)),
            ('treehouse', (3, 85, 275, 437)),
        ],
        'sprites': [
            # Sprite(key, image, (x, y, w, h), showif)
        ]
    }

#LABELS
label townhousebackyard:
    if quests.bathtubclimax == ACTIVE:
        if calendar.when[2] == MORNING:
            jump kassandrabackyardincident
    jump townhousebackyard_loop

label townhousebackyard_loop:
    $ resetscene()
    call screen map('townhousebackyard')
    jump townhousebackyard_loop

label townhousebackyard_exit:
    $ gotoscene('townhousediningroom')

label townhousebackyard_treehouse:
    if dearsantaqueststarted == True:
        if jilliandearsantasecret == False:
            jump pastdeeds
    elif prologue.checkthecliff == True:
        if prologue.findtherope == False:
            hide screen freeroamhud
            show cliffropeitem with dissolve
            "That's it! There is some rope behind the tree I can use."
            play music MUSIC_HEISTPLAN_THEME
            show wendyplan06 with dissolve
            "Let's see..."
            show wendyplan07 with dissolve
            "Nice, now I got a way to fix the stair and climb the cliff."
            show wendyplan08 with dissolve
            "I have everything I need, I should rest for a while and wait 'til midnight."
            $ prologue.findtherope = True
        else:
            Jimmy "An old tree house."
            Jimmy "It's wrecked."
            jump townhousebackyard_loop
    elif prologue.checkthecliff == False:
        Jimmy "An old tree house."
        Jimmy "It's wrecked. There is some rope behind the tree."
    else:
        Jimmy "Maybe one day I can restore it."
    jump townhousebackyard_loop

####

label pastdeeds:
    hide screen freeroamhud
    scene backyardearsanta with fade
    play music "audio/music/mysterytheme.ogg"
    $ pastdeedschecked = True
    show santashadow with dissolve
    dSanta "Ah! You are smarter than I thought, servant."
    Jimmy "..."
    dSanta "Umm, let's see."
    dSanta "Beyond this reality, there is plane of existance that your two-dimensional mind cannot even start to understand."
    dSanta "If the truth you seek, you shall look outside of this world."
    dSanta "There is place where everyone gathers to write and read, a server to find them..."
    dSanta "One server to bring them all, and in the darkness bind them..."
    dSanta "At the basement of it all, in a cold place, you'll find the first three letters for the truth."
    dSanta "Once the knowledge belongs to you, look for me once again where the land meets the deep blue."
    hide santashadow with dissolve
    stop music
    jump townhousebackyard_loop