#SCREENS
init 1 python:
    def mainbuildingrighthallway_showif_beatrix():
        if calendar.when[0] == PROLOGUE:
            return False
        if quests.beatrixHomework == COMPLETE:
            if quests.beatrixHerpes != COMPLETE:
                return False
        # if quests.beatrixDiary == LOCKED:
        #     return False
        return True

    scene_defs['mainbuildingrighthallway'] = {
        'music': MUSIC_MAINBUILDINGAMBIENCEDAY_THEME,
        'altermusic': MUSIC_MAINBUILDINGAMBIENCENIGHT_THEME,
        'maps': {
            'default': ('firstfloorrighthallway', 'firstfloorrighthallwayhover'),
        },
        'hotspots': [
            ('musicstudio', (1228, 422, 216, 225)),
            ('geographyclass', (1013, 423, 80, 266)),
            ('artclass', (816, 386, 126, 388)),
            ('spanishclass', (516, 342, 174, 533)),
            ('mathclass', (118, 287, 243, 739)),
            ('toentrance', (369, 924, 1549, 156)),
        ],
        'sprites': [
            Sprite('beatrix', 'beatrixdialog01', (1459, 367, 246, 660), mainbuildingrighthallway_showif_beatrix),
        ]
    }

#LABELS
label mainbuildingrighthallway:
    $ checkcurfew()
    jump mainbuildingrighthallway_loop

label mainbuildingrighthallway_loop:
    $ resetscene()
    call screen map('mainbuildingrighthallway')
    jump mainbuildingrighthallway_loop

label mainbuildingrighthallway_musicstudio:
    if calendar.when[1:] == (TUESDAY, AFTERNOON):
        jump musicclass
    else:
        "I don't have Music class right now."
    jump mainbuildingrighthallway_loop

label mainbuildingrighthallway_geographyclass:
    if calendar.when[1:] == (MONDAY, MORNING):
        jump geographyclass
    else:
        "I don't have Geography class right now."
    jump mainbuildingrighthallway_loop

label mainbuildingrighthallway_artclass:
    if calendar.when[1:] == (TUESDAY, MORNING):
        jump artclass
    elif quests.missdawsonAssistant == SATISFIED:
        if quests.missdawsonHalloweenAurora == LOCKED:
            jump dawsonaurorahalloween
        else:
            "I don't have Art class right now."
            jump mainbuildingrighthallway_loop
    elif quests.euniceGettingtherole == ACTIVE:
        if quests.artProject == COMPLETE:
            jump bakshisirlaughsalotquest
        else:
            "I don't have Art class right now."
    elif quests.euniceGettingtherole == COMPLETE:
        if quests.euniceTheaterpractice != COMPLETE:
            call eunicedialogue from _call_eunicedialogue
    else:
        "I don't have Art class right now."
    jump mainbuildingrighthallway_loop

label mainbuildingrighthallway_spanishclass:
    if quests.punnyDatingTeacher == COMPLETE:
        Jimmy "It's not a good time to go back to her."
        Jimmy "Let's give it some time."
        jump mainbuildingrighthallway_loop
    $ gotoscene('spanishclassroom')

label mainbuildingrighthallway_mathclass:
    if calendar.when[1:] == (FRIDAY, MORNING):
        jump mathclass
    elif quests.missdawsonAssistant == SATISFIED:
        if quests.missdawsonHalloweenCamembert == LOCKED:
            jump dawsoncamemberthalloween
        else:
            "I don't have Art class right now."
            jump mainbuildingrighthallway_loop
    else:
        "I don't have Math class right now."
    jump mainbuildingrighthallway_loop

label mainbuildingrighthallway_toentrance:
    $ gotoscene('mainbuildingentrance')

label mainbuildingrighthallway_beatrix:
    hide beatrixdialog01
    jump beatrixdialogue

label dawsonaurorahalloween:
    hide screen freeroamhud
    scene artclassroomfallday with fade
    show aurora jumpsuit neutral with dissolve
    play music MUSIC_AURORA_THEME
    Aurora "Hello, sweetu."
    Aurora "Are you here for art class?"
    Jimmy "Hey, miss. No, the secretary sent me here to ask you about the staff reunion for Halloween."
    Jimmy "She wanted to know if you were coming."
    Aurora crossed "Oh, yes. The reunion, yes. Of course, I vill, sweetu."
    Aurora "By the vay, let me show you my costume!"
    Aurora "I'm so excited, wait here..."
    play sound "audio/sfx/fewmomentslater.ogg"
    show fewmomentslater with fade
    pause 1.0
    hide fewmomentslater with dissolve
    Aurora sari dance "Oh, yes! My chakra is alligned."
    Aurora "Isavasyamidam sarvam..."
    Jimmy "Uh..."
    Aurora "What do you think, sweetu?"
    Jimmy "Very nice, miss."
    Aurora "Oh, thank you so much, sweetu."
    Jimmy "Well, I gotta go. I will tell Miss Dawson that you are ready for the reunion."
    Aurora "Yes, of course, I tink I'll keep dancing for a vhile."
    Jimmy "Alright..."
    $ quests.missdawsonHalloweenAurora = COMPLETE
    $ gotoscene('mainbuildingrighthallway')

label dawsoncamemberthalloween:
    hide screen freeroamhud
    scene mathclassroom01 with fade
    show camembert with dissolve
    play music "audio/music/mathclasstheme.ogg"
    Camembert "And if I catch anyone using a calculator, it's going in the garbage..."
    show beatrix uniform mad left with dissolve
    play sound "audio/sfx/frustratedhum.ogg"
    Beatrix "That's right, Mr. Camembert. If they cannot solve a polinominal equation using planck constant to determine the acceleration of the universe expansion..."
    Beatrix "Then, they don't deserve to be here."
    Camembert "Very well, said. Miss Trudeau."
    Camembert "Good day, young man. Do you need anything?"
    hide beatrix with dissolve
    Jimmy "Oh, yes, sir. Miss Dawson sent me to ask you about the Halloween staff reunion."
    Camembert "Yes, that banal event. Well, you can tell Miss Dawson that I'm trying my best to find a costume."
    Camembert "However, I believe there has been some trouble with the distribution system in the clothing market, because I can't seem to find anything my size anywhere."
    Jimmy "Oh, I wonder why?"
    Camembert "Yes, it's strange indeed. But, I'm a man of my word and I will find something suitable."
    Jimmy "Alright, I'll be on my way, then."
    show beatrix uniform mad left with vpunch
    Beatrix mad arm left "Yeah, and maybe you can take a class on manners before interrupting important conversations."
    Jimmy "Whatever, mophead..."
    Camembert "Oh, ha, ha, ha, that's such a clever joke!"
    Camembert "Ha, ha, ha, ha..."
    play sound "audio/sfx/mad02.ogg"
    $ quests.missdawsonHalloweenCamembert = COMPLETE
    $ gotoscene('mainbuildingrighthallway')
