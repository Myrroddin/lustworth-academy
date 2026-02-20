#VARIABLES
default primordialpathchecked = False

#SCREENS
init 1 python:
    def schoollibrarynerdcliquehq_showif_algie():
        if quests.rescueBucky == ACTIVE or quests.rescueBucky ==  SATISFIED:
            return False
        elif glob.halloweenEventComplete:
            return True
        return False

    scene_defs['schoollibrarynerdcliquehq'] = {
        'music': MUSIC_LIBRARY02,
        'altermusic': MUSIC_LIBRARY02,
        'maps': {
            'morning':   ('librarynerdcliquehq', 'librarynerdcliquehqhover'),
            'afternoon': ('librarynerdcliquehqday', 'librarynerdcliquehqdayhover'),
            'evening':   ('librarynerdcliquehq', 'librarynerdcliquehqhover'),
            'night':     ('librarynerdcliquehq', 'librarynerdcliquehqhover'),
        },
        'hotspots': [
            ('exit', (5, 536, 370, 538)),
            ('dungeonmasterstable', (650, 642, 435, 297)),
            ('decoratedglass', (58, 0, 215, 409)),
            ('templarshield', (1387, 29, 180, 372)),
            ('stickoftruth', (1369, 419, 135, 140)),
            ('cumalotmap', (456, 21, 597, 518)),
        ],
        'sprites': [
            Sprite('algie', 'algiesprite01', (1000, 650, 300, 600), schoollibrarynerdcliquehq_showif_algie),
        ]
    }

#LABELS
label schoollibrarynerdcliquehq:
    if quests.algieScroll == COMPLETE:
        if quests.beatrixHomework == SATISFIED:
            jump melvinherpestalk
    $ checkcurfew()
    jump schoollibrarynerdcliquehq_loop

label schoollibrarynerdcliquehq_loop:
    $ resetscene()
    call screen map('schoollibrarynerdcliquehq')
    jump schoollibrarydungeonmastershq_loop

label schoollibrarynerdcliquehq_exit:
    $ gotoscene('schoollibrarymainhall')

label schoollibrarynerdcliquehq_cumalotmap:
    if futuredeedschecked == True:
        if jilliandearsantasecret == False:
            jump primordialpath
    Jimmy "Looks like a map of something."
    Jimmy "It's very detailed, impressive."
    jump schoollibrarynerdcliquehq_loop

label schoollibrarynerdcliquehq_dungeonmasterstable:
    Jimmy "There are dices and sheets with numbers and strange names."
    Jimmy "It must be one of those tabletop RPG games."
    jump schoollibrarynerdcliquehq_loop

label schoollibrarynerdcliquehq_templarshield:
    Jimmy "It's a cool looking shield."
    jump schoollibrarynerdcliquehq_loop

label schoollibrarynerdcliquehq_stickoftruth:
    Jimmy "It says 'The Stick of Truth'."
    Jimmy "Whoever controls the stick, controls the universe."
    jump schoollibrarynerdcliquehq_loop

label schoollibrarynerdcliquehq_decoratedglass:
    Jimmy "Painted glass. Looks nice."
    jump schoollibrarynerdcliquehq_loop

#SPRITES

label schoollibrarynerdcliquehq_algie:
    hide algiesprite01
    jump algiedialogue


####

label primordialpath:
    hide screen freeroamhud
    scene librarydearsanta with fade
    play music "audio/music/mysterytheme.ogg"
    $ primordialpathchecked = True
    show santashadow with dissolve
    dSanta "Ah! You're so close, servant."
    Jimmy "..."
    dSanta "Umm, let's see."
    dSanta "If the truth you seek, you shall look one last time outside of this world."
    dSanta "The origin of everything lies in the foundations of this family."
    dSanta "The sacred Auditorium where the creators of the universe stand vigilant to see what comes next."
    dSanta "Find the coordinates that will lead you to the language in which the truth has been spoken for centuries."
    dSanta "KLASS is the ending you need to give form to what lies beyond."
    dSanta "If the truth belongs to you, speak to the one that awaits your words and the great prize will be yours."
    dSanta "Look for me once again where it all began, and I shall grant you a reward of my own making."
    hide santashadow with dissolve
    stop music
    jump schoollibrarynerdcliquehq_loop