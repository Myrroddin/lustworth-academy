#VARIABLES
default futuredeedschecked = False

#SCREENS
init 1 python:
    scene_defs['seasidecliff'] = {
        'music': MUSIC_SEASIDEAMBIENCEDAY_THEME,
        'altermusic': MUSIC_SEASIDEAMBIENCENIGHT_THEME,
        'maps': {
            'morning':   ("seasidecliffday", "seasidecliffdayhover"),
            'afternoon': ("seasidecliffafter", "seasidecliffafterhover"),
            'evening':   ("seasidecliffevening", "seasidecliffeveninghover"),
            'night':     ("seasidecliffnight", "seasidecliffnighthover")
        },
        'hotspots': [
            ('seaview', (0, 0, 774, 556)),
            ('stairs', (1247, 0, 567, 994)),
            ('exit', (0, 869, 1238, 205)),
        ],
        'sprites': [
            # Sprite(key, image, (x, y, w, h), showif)
        ]
    }

#LABELS
label seasidecliff:
    if calendar.when[1:] == (SATURDAY, EVENING):
        if quests.fionaConfrontDerek == COMPLETE:
            if quests.fionaNightDate == SATISFIED:
                jump chapterone_fionasurfinglesson
            elif quests.fionaNightDate == LOCKED:
                jump chapterone_fionanightdateintro
    jump seasidecliff_loop

label seasidecliff_loop:
    $ resetscene()
    call screen map('seasidecliff')
    jump seasidecliff_loop

label seasidecliff_seaview:
    __("That's a nice view.")
    jump seasidecliff_loop

label seasidecliff_stairs:
    if pastdeedschecked == True:
        if jilliandearsantasecret == False:
            jump futuredeeds
    elif prologue.complete:
        Jimmy "The broken stair. It's a stair and is broken."
    jump seasidecliff_loop

label seasidecliff_exit:
    $ gotoscene('seasideareamap')

####

label futuredeeds:
    hide screen freeroamhud
    scene seasidedearsanta with fade
    play music "audio/music/mysterytheme.ogg"
    $ futuredeedschecked = True
    show santashadow with dissolve
    dSanta "Oh! You're getting far, servant."
    Jimmy "..."
    dSanta "Umm, let's see."
    dSanta "If the truth you seek, you shall look outside of this world, once again."
    dSanta "The X marks the place, or so they say..."
    dSanta "Careful, the place is known to be hostile, even your words are limited in order to speak."
    dSanta "If you manage to step over the rocks, you'll find three more letters for the truth."
    dSanta "Once the knowledge belongs to you, look for me once again in a place where epic stories are told and fought on paper and imagination."
    hide santashadow with dissolve
    stop music
    jump seasidecliff_loop
