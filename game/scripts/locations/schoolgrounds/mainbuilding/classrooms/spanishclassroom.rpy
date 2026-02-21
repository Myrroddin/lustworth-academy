init 1 python:
    def spanishclassroom_showif_misspunny():
        if quests.punnyPrivateLessons == ACTIVE:
            return True
        if quests.punnyPrivateLessons == COMPLETE:
            if not quests.punnyDatingTeacher == COMPLETE:
                return True
        return False

    scene_defs['spanishclassroom'] = {
        'music': MUSIC_CLASSROOMAMBIENCEDAY_THEME,
        'altermusic': MUSIC_CLASSROOMAMBIENCEDAY_THEME,
        'maps': {
            'morning':   ("spanishclassroomfallday", "spanishclassroomfalldayhover"),
            'afternoon': ("spanishclassroomfallafternoon", "spanishclassroomfallafternoonhover"),
            'evening':   ("spanishclassroomfallevening", "spanishclassroomfalleveninghover"),
            'night':     ("spanishclassroomfallnight", "spanishclassroomfallnighthover")
        },
        'hotspots': [
            ('exit', (1578, 8, 341, 1070)),
        ],
        'sprites': [
            Sprite('misspunny', 'misspunnysprite01', (1000, 430, 234, 621), spanishclassroom_showif_misspunny),
            # Sprite(key, image, (x, y, w, h), showif)
        ]
    }

#LABELS
label spanishclassroom:
    $ checkcurfew()
    if calendar.when[1:] == (THURSDAY, MORNING):
        jump spanishclass
    jump spanishclassroom_loop

label spanishclassroom_loop:
    $ resetscene()
    call screen map('spanishclassroom')
    jump spanishclassroom_loop

label spanishclassroom_misspunny:
    hide misspunnysprite01
    jump misspunnydialog

label spanishclassroom_exit:
    $ gotoscene('mainbuildingrighthallway')
