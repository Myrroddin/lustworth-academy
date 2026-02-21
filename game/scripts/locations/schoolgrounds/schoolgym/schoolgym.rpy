#SCREENS
init 1 python:
    scene_defs['schoolgym'] = {
        'music': MUSIC_GYMAMBIENCEDAY_THEME,
        'altermusic': MUSIC_GYMAMBIENCENIGHT_THEME,
        'maps': {
            'default': ('gymfall01', 'gymfall01hover'),
        },
        'hotspots': [
            ('storageroom', (972, 239, 130, 187), lambda: calendar.when != (PROLOGUE, THURSDAY, AFTERNOON)),
            ('girlslockers', (1194, 261, 182, 166)),
            ('boyslockers', (1667, 280, 237, 192)),
            ('exit', (1, 529, 555, 547)),
        ],
        'sprites': [
            Sprite('pete', 'petekowalskisprite', (435, 324, 236, 597), lambda: calendar.when == (PROLOGUE, THURSDAY, AFTERNOON)),
            Sprite('casmoans', 'casmoans', (1536, 30, 1920, 1080), lambda: calendar.when == (PROLOGUE, THURSDAY, EVENING), isButton=False),
        ]
    }

#LABELS
label schoolgym:
    if quests.fionaHideAndSeek == ACTIVE:
        call schoolgymcheckderek from _call_schoolgymcheckderek
    elif quests.beatrixDiary == COMPLETE and quests.cassidyTrials == LOCKED:
        call cassidytrialsquestintro from _call_cassidytrialsquestintro
    $ checkcurfew()
    if calendar.when[1:] == (THURSDAY, AFTERNOON) and calendar.when[0] != PROLOGUE:
        jump gymclass
    jump schoolgym_loop

label schoolgym_loop:
    $ resetscene()
    call screen map('schoolgym')
    jump schoolgym_loop

label schoolgym_storageroom:
    if quests.euniceBoobytrap == ACTIVE and time == EVENING:
        jump euniceboobytrap
    $ gotoscene('schoolgymstorageroom')

label schoolgym_girlslockers:
    "I shouldn't just walk into the girl's locker room."
    jump schoolgym_loop

label schoolgym_boyslockers:
    $ gotoscene('schoolgymboyslockers')

label schoolgym_exit:
    $ gotoscene ('schoolgroundsgymplaza')

label schoolgym_pete:
    hide petekowalskisprite
    jump prologue_girlsshowersintro


label schoolgymcheckderek:
    if FionaWineFound == False:
        Derek "Getting hot!"
        return     
    elif FionaDonutFound == False:
        Derek "You're freezing, my guy."
        return
    else:
        return

#ANIMATIONS
image casmoans:
    'casmoans01'
    pause 1.0
    'casmoans02'
    pause 1.0
    'casmoans03'
    pause 1.0
    repeat
