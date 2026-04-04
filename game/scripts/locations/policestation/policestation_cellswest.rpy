#SCREENS
init 1 python:
    scene_defs['policestationcellswest'] = {
        'music': MUSIC_SUSPENSE,
        'altermusic': MUSIC_SUSPENSE,
        'maps': {
            'default': ("policestationcellblockopen", "policestationcellblockopenhover"),
        },
        'hotspots': [
            ('door', (0, 270, 150, 613)),
            ('keypad', (138, 517, 61, 108)),
            ('trashcan', (1281, 654, 109, 132)),
            ('profilegrant', (1063, 289, 308, 232)),
            ('armscabinet', (1389, 301, 270, 491)),
            ('tocellseast', (1679, 79, 260, 991)),
            ('firealarm', (1111, 19, 118, 90)),
            ('cellgate', (681, 285, 263, 492)),
        ],
        'sprites': [
            Sprite('grant', 'granthobosprite', (750, 400, 148, 360), lambda: True)
        ]
    }

#LABELS
label policestationcellswest:
    jump policestationcellswest_loop

label policestationcellswest_loop:
    $ resetscene()
    call screen map('policestationcellswest')
    jump policestationcellswest_loop

label policestationcellswest_door:
    "Locked tight."
    jump policestationcellswest_loop

label policestationcellswest_keypad:
    "I don't know the code."
    jump policestationcellswest_loop

label policestationcellswest_grant:
    if quests.grantHoboBag != SATISFIED:
        Grant "What are you waiting for, kiddo?"
        Grant "Get my bag so we can get out of here, tonight."
    else:
        jump prologue_grantescape
    jump policestationcellswest_loop

label policestationcellswest_profilegrant:
    "\"Grant, last name unknown. Convicted for fraud, robbing people with a banana, and public disorder.\""
    "\"He claims to be innocent of all charges because he has blue eyes.\""
    Grant "What can I say, my eyes are beautiful!"
    Jimmy "Umm, I have a profile of my own."
    "\"[player_surname], [player_name]. Reported many times for causing public disorder in his home town of San Pestillo.\""
    "\"Student at Trustworth Academy. Possible candidate for the new reformation program.\""
    "Reformation program? I don't like the sound of that."
    jump policestationcellswest_loop

label policestationcellswest_armscabinet:
    Jimmy "Uhh, there is an arsenal here enough to stage a coup."
    jump policestationcellswest_loop

label policestationcellswest_firealarm:
    Jimmy "It's a fire detection system."
    jump policestationcellswest_loop

label policestationcellswest_trashcan:
    Jimmy "Not much here, just a box of matches."
    jump policestationcellswest_loop

label policestationcellswest_cellgate:
    jump policestationcellswest_loop

label policestationcellswest_tocellseast:
    $ gotoscene('policestationcellseast')
