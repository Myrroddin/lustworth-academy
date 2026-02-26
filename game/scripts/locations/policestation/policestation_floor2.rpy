#VARIABLES
default policestationfloor2.grantBagComment = False

#SCREENS
init 1 python:
    scene_defs['policestationfloor2'] = {
        'music': MUSIC_SUSPENSE,
        'altermusic': MUSIC_SUSPENSE,
        'maps': {
            'default': ('policestationfloor2', 'policestationfloor2hover'),
        },
        'hotspots': [
            ('harrysoffice', (1224, 191, 118, 396)),
            ('jillsoffice', (296, 131, 220, 693)),
            ('interrogationroom', (1564, 51, 268, 944)),
            ('tofloor1', (0, 4, 211, 1061)),
            ('tostafflounge', (835, 199, 233, 253)),
            ('sheriffoffice', (565, 189, 122, 379)),
        ],
        'sprites': [
            # Sprite(key, image, (x, y, w, h), showif)
        ]
    }

#LABELS
label policestationfloor2:
    if quests.grantHoboBag == SATISFIED and not policestationfloor2.grantBagComment:
        __("Man, I thought sneaking into the mayor's mansion was an adrenaline rush.")
        __("But sneaking into a police officer's office WHILE she was in there?")
        __("I thought my heart was gonna burst out of my chest.")
        __("Now I just need to return this to Grant and I can get out of here.")
        $ policestationfloor2.grantBagComment = True
    jump policestationfloor2_loop

label policestationfloor2_loop:
    $ resetscene()
    call screen map('policestationfloor2')
    jump policestationfloor2_loop

label policestationfloor2_interrogationroom:
    __("\"Interrogation.\"")
    __("Locked.")
    jump policestationfloor2_loop

label policestationfloor2_harrysoffice:
    __("\"Harry Callahan - Chief Detective.\"")
    __("Talk about cliché.")
    jump policestationfloor2_loop

label policestationfloor2_sheriffoffice:
    __("\"Sheriff's Office.\"")
    __("Locked.")
    jump policestationfloor2_loop

label policestationfloor2_tostafflounge:
    Jimmy "Wow, there is a huge hall behind that door."
    Jimmy "It's a shame it's locked."
    jump policestationfloor2_loop

label policestationfloor2_jillsoffice:
    if quests.grantHoboBag == ACTIVE:
        __("\"Jillian Valentino - Detective.\"")
        __("This is the one.")
        __("...I hear weird noises from inside.")
        __("What is she doing?")
        call jill_officemasturbation_scene from _call_jill_officemasturbation_scene
        __("Damn, she's out cold.")
        __("I guess now's my chance.")
        $ gotoscene('policestationjillsoffice', transition=fade)
    else:
        __("I already have the bag.")
        __("I should go back and talk to Grant.")
    jump policestationfloor2_loop

label policestationfloor2_tofloor1:
    $ gotoscene('policestationfloor1')
