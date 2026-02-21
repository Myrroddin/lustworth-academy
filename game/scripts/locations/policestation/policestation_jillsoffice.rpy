#VARIABLES
default policestationjillsoffice.jillChecked = False

#SCREENS
init 1 python:
    scene_defs['policestationjillsoffice'] = {
        'music': MUSIC_SUSPENSE,
        'altermusic': MUSIC_SUSPENSE,
        'maps': {
            'default': ('jillofficeintro', 'jillofficeintrohover'),
        },
        'hotspots': [
            ('door', (0, 35, 166, 1045)),
            ('board', (348, 447, 477, 320)),
            ('certificate', (859, 459, 123, 173)),
            ('jill', (1558, 617, 360, 382)),
        ],
        'sprites': [
            Sprite('hobobag', 'hobobag', (960, 745, 128, 124), lambda: quests.grantHoboBag == ACTIVE),
        ]
    }

#LABELS
label policestationjillsoffice:
    jump policestationjillsoffice_loop

label policestationjillsoffice_loop:
    $ resetscene()
    call screen map('policestationjillsoffice')
    jump policestationjillsoffice_loop

label policestationjillsoffice_board:
    "There are pictures and clues of a case she must be working on."
    "She's investigating a company called \"Zombrella.\""
    "It says they're developing some kind of super virus..."
    "Weird stuff."
    jump policestationjillsoffice_loop

label policestationjillsoffice_certificate:
    "\"This is a certificate in recognition of the hard work of Officer Jillian Valentino.\""
    "\"You make our town better.\""
    "\"Signed: Mayor Jack Donaguy.\""
    "Ha... This guy."
    jump policestationjillsoffice_loop

label policestationjillsoffice_hobobag:
    if quests.grantHoboBag == ACTIVE:
        jump prologue_grantsbagfetch
    jump policestationjillsoffice_loop

label policestationjillsoffice_jill:
    if not policestationjillsoffice.jillChecked:
        "Man, she is really hot."
        "Just look at those huge tits."
        "She's in a deep sleep... Maybe I can give them a little feel."
        menu:
            "Touch":
                hide screen freeroamhud
                play music MUSIC_SEXY_THEME
                scene jilltitgropeanim01 with dissolve
                "Wow, they feel even better than I expected."
                "This is so fucking wrong."
                $ renpy.pause()
                "Alright, that's enough."
                stop music
                $ sexscenes.jillGrope = True
            "Don't touch":
                "On second thought, I shouldn't take advantage of her like this."
                "Let's just grab the bag and get out."
                $ Jimmy.stats['intelligence'] += 1
                $ policestationjillsoffice.jillChecked
    else:
        "I should leave her alone now."
    jump policestationjillsoffice_loop

label policestationjillsoffice_door:
    if quests.grantHoboBag != SATISFIED:
        "I can't leave without Grant's bag."
    else:
        $ gotoscene('policestationfloor2')
    jump policestationjillsoffice_loop

#ANIMATIONS
image jilltitgropeanim01:
    'jillgropeanim01'
    pause 0.3
    'jillgropeanim02'
    pause 0.3
    'jillgropeanim03'
    pause 0.3
    'jillgropeanim04'
    pause 0.2
    'jillgropeanim05'
    pause 0.4
    'jillgropeanim06'
    pause 0.3
    repeat
