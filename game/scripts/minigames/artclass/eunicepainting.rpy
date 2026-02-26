#VARIABLES
default euniceline1_2 = False
default euniceline2_3 = False
default euniceline3_4 = False
default euniceline4_5 = False
default euniceline5_6 = False
default euniceline6_3 = False
default euniceline3_7 = False
default euniceline7_8 = False
default euniceline8_9 = False
default euniceline9_10 = False
default euniceline10_11 = False
default euniceline11_12 = False
default euniceline12_13 = False
default euniceline13_14 = False
default euniceline14_15 = False
default euniceline14_12 = False
default euniceline12_15 = False
default euniceline12_16 = False
default euniceline16_17 = False
default euniceline17_18 = False
default euniceline18_19 = False
default euniceline19_1 = False

#VARIABLESDOT
default eunicedot.active = 0
default euniceartpoints = 0

#VARIABLESPLUS


label eunice_painting_game:
    scene artclassroomfallday with fade
    $ gotoscene('eunicepaintinggame')

init 1 python:
    def showif_euniceline1_2():
        if euniceline1_2 == True:
            return True
        else:
            return False
    
    def showif_euniceline2_3():
        if euniceline2_3 == True:
            return True
        else:
            return False

    def showif_euniceline3_4():
        if euniceline3_4 == True:
            return True
        else:
            return False
    
    def showif_euniceline4_5():
        if euniceline4_5 == True:
            return True
        else:
            return False

    def showif_euniceline5_6():
        if euniceline5_6 == True:
            return True
        else:
            return False
    
    def showif_euniceline6_3():
        if euniceline6_3 == True:
            return True
        else:
            return False
    
    def showif_euniceline3_7():
        if euniceline3_7 == True:
            return True
        else:
            return False
    
    def showif_euniceline7_8():
        if euniceline7_8 == True:
            return True
        else:
            return False
    
    def showif_euniceline8_9():
        if euniceline8_9 == True:
            return True
        else:
            return False
    
    def showif_euniceline9_10():
        if euniceline9_10 == True:
            return True
        else:
            return False

    def showif_euniceline10_11():
        if euniceline10_11 == True:
            return True
        else:
            return False

    def showif_euniceline11_12():
        if euniceline11_12 == True:
            return True
        else:
            return False
    
    def showif_euniceline12_13():
        if euniceline12_13 == True:
            return True
        else:
            return False
    
    def showif_euniceline13_14():
        if euniceline13_14 == True:
            return True
        else:
            return False
    
    def showif_euniceline14_15():
        if euniceline14_15 == True:
            return True
        else:
            return False
    
    def showif_euniceline12_15():
        if euniceline12_15 == True:
            return True
        else:
            return False

    def showif_euniceline12_16():
        if euniceline12_16 == True:
            return True
        else:
            return False
    
    def showif_euniceline16_17():
        if euniceline16_17 == True:
            return True
        else:
            return False
    
    def showif_euniceline17_18():
        if euniceline17_18 == True:
            return True
        else:
            return False
    
    def showif_euniceline18_19():
        if euniceline18_19 == True:
            return True
        else:
            return False
    
    def showif_euniceline19_1():
        if euniceline19_1 == True:
            return True
        else:
            return False

    def showif_euniceartbutton3():
        if euniceline2_3 == True:
            return True
        elif euniceline3_4 == True:
            return True
        elif euniceline6_3 == True:
            return True
        elif euniceline3_7 == True:
            return True
        else:
            return False

    def showif_euniceartbutton12():
        if euniceline11_12 == True:
            return True
        elif euniceline12_13 == True:
            return True
        elif euniceline12_15 == True:
            return True
        elif euniceline12_16 == True:
            return True
        else:
            return False
    
    scene_defs['eunicepaintinggame'] = {
        'music': MUSIC_ART_CLASS,
        'altermusic': MUSIC_ART_CLASS,
        'maps': {
            'default':   ("eunicepaint01", "eunicepaint01hover"),
        },
        'hotspots': [
            ('dot01', (737, 270, 30, 28)),
            ('dot02', (812, 168, 28, 27)),
            ('dot03', (937, 250, 29, 29)),
            ('dot04', (908, 355, 30, 27)),
            ('dot05', (980, 421, 27, 32)),
            ('dot06', (998, 343, 32, 27)),
            ('dot07', (1044, 187, 31, 28)),
            ('dot08', (1138, 333, 30, 28)),
            ('dot09', (1179, 534, 27, 32)),
            ('dot10', (1466, 721, 30, 30)),
            ('dot11', (1279, 798, 26, 26)),
            ('dot12', (1015, 868, 28, 26)),
            ('dot13', (1072, 765, 29, 27)),
            ('dot14', (1010, 723, 29, 29)),
            ('dot15', (948, 770, 29, 28)),
            ('dot16', (707, 801, 29, 31)),
            ('dot17', (472, 796, 28, 28)),
            ('dot18', (767, 581, 30, 29)),
            ('dot19', (780, 419, 27, 27)),
            ('restart', (983, 946, 196, 129)),
            ('giveup', (770, 945, 187, 128)),
        ],
        'sprites': [
            Sprite('euniceartline1', 'euniceartline01', (0, 0, 0, 0), showif_euniceline1_2),# Sprite(key, image, (x, y, w, h), showif)
            Sprite('euniceartline2', 'euniceartline02', (0, 0, 0, 0), showif_euniceline2_3),
            Sprite('euniceartline3', 'euniceartline03', (0, 0, 0, 0), showif_euniceline3_4),
            Sprite('euniceartline4', 'euniceartline04', (0, 0, 0, 0), showif_euniceline4_5),
            Sprite('euniceartline5', 'euniceartline05', (0, 0, 0, 0), showif_euniceline5_6),
            Sprite('euniceartline6', 'euniceartline06', (0, 0, 0, 0), showif_euniceline6_3),
            Sprite('euniceartline7', 'euniceartline07', (0, 0, 0, 0), showif_euniceline3_7),
            Sprite('euniceartline8', 'euniceartline08', (0, 0, 0, 0), showif_euniceline7_8),
            Sprite('euniceartline9', 'euniceartline09', (0, 0, 0, 0), showif_euniceline8_9),
            Sprite('euniceartline10', 'euniceartline10', (0, 0, 0, 0), showif_euniceline9_10),
            Sprite('euniceartline11', 'euniceartline11', (0, 0, 0, 0), showif_euniceline10_11),
            Sprite('euniceartline12', 'euniceartline12', (0, 0, 0, 0), showif_euniceline11_12),
            Sprite('euniceartline13', 'euniceartline13', (0, 0, 0, 0), showif_euniceline12_13),
            Sprite('euniceartline14', 'euniceartline14', (0, 0, 0, 0), showif_euniceline13_14),
            Sprite('euniceartline15', 'euniceartline15', (0, 0, 0, 0), showif_euniceline14_15),
            Sprite('euniceartline16', 'euniceartline16', (0, 0, 0, 0), showif_euniceline12_15),
            Sprite('euniceartline17', 'euniceartline17', (0, 0, 0, 0), showif_euniceline12_16),
            Sprite('euniceartline18', 'euniceartline18', (0, 0, 0, 0), showif_euniceline16_17),
            Sprite('euniceartline19', 'euniceartline19', (0, 0, 0, 0), showif_euniceline17_18),
            Sprite('euniceartline20', 'euniceartline20', (0, 0, 0, 0), showif_euniceline18_19),
            Sprite('euniceartline21', 'euniceartline21', (0, 0, 0, 0), showif_euniceline19_1),
            Sprite('euniceartbutton3', 'art1button', (937, 250, 29, 29), showif_euniceartbutton3),
            Sprite('euniceartbutton12', 'art1button', (1015, 868, 28, 26), showif_euniceartbutton12),
            

        ]
    }

    
#LABELS

label restarteunicegame:
    $ euniceartpoints = 0
    $ eunicedot.active = 0
    $ euniceline1_2 = False
    $ euniceline2_3 = False
    $ euniceline3_4 = False
    $ euniceline4_5 = False
    $ euniceline5_6 = False
    $ euniceline6_3 = False
    $ euniceline3_7 = False
    $ euniceline7_8 = False
    $ euniceline8_9 = False
    $ euniceline9_10 = False
    $ euniceline10_11 = False
    $ euniceline11_12 = False
    $ euniceline12_13 = False
    $ euniceline13_14 = False
    $ euniceline14_15 = False
    $ euniceline12_15 = False
    $ euniceline12_16 = False
    $ euniceline16_17 = False
    $ euniceline17_18 = False
    $ euniceline18_19 = False
    $ euniceline19_1 = False
    $ gotoscene('eunicepaintinggame')

label eunicepaintinggame:
    hide screen freeroamhud
    jump eunicepaintinggame_loop

label eunicepaintinggame_loop:
    hide screen freeroamhud
    if euniceartpoints == 21:
        play sound "audio/sfx/missioncomplete.ogg"
        show eunicepaintsuccess with dissolve
        $ renpy.pause()
        jump eunicepaintingsuccess
    $ resetscene()
    call screen map('eunicepaintinggame')
    jump eunicepaintinggame_loop

label eunicepaintinggame_dot01:
    if eunicedot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ eunicedot.active = 1
        jump eunicepaintinggame_loop
    elif eunicedot.active == 2:
        if euniceline1_2 == False:
            show euniceartline01
            $ eunicedot.active = 1
            $ euniceline1_2 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame
            jump eunicepaintinggame_loop
    elif eunicedot.active == 19:
        if euniceline19_1 == False:
            show euniceartline21
            $ eunicedot.active = 1
            $ euniceline19_1 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_1
            jump eunicepaintinggame_loop
    else:
        play sound SOUND_INCORRECT
        jump eunicepaintinggame_loop

label eunicepaintinggame_dot02: 
    if eunicedot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ eunicedot.active = 2
        jump eunicepaintinggame_loop
    elif eunicedot.active == 1:
        if euniceline1_2 == False:
            $ eunicedot.active = 2
            $ euniceline1_2 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_2
            jump eunicepaintinggame_loop
    elif eunicedot.active == 3:
        if euniceline2_3 == False:
            show euniceartline02
            $ eunicedot.active = 2
            $ euniceline2_3 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_3
            jump eunicepaintinggame_loop
    else:
        play sound SOUND_INCORRECT
        jump eunicepaintinggame_loop

label eunicepaintinggame_dot03:
    if eunicedot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ eunicedot.active = 3
        jump eunicepaintinggame_loop
    elif eunicedot.active == 2:
        if euniceline2_3 == False:
            show euniceartline02
            $ eunicedot.active = 3
            $ euniceline2_3 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_4
            jump eunicepaintinggame_loop
    elif eunicedot.active == 4:
        if euniceline3_4 == False:
            show euniceartline03
            $ eunicedot.active = 3
            $ euniceline3_4 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_5
            jump eunicepaintinggame_loop
    elif eunicedot.active == 6:
        if euniceline6_3 == False:
            show euniceartline06
            $ eunicedot.active = 3
            $ euniceline6_3 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_6
            jump eunicepaintinggame_loop
    elif eunicedot.active == 7:
        if euniceline3_7 == False:
            show euniceartline07
            $ eunicedot.active = 3
            $ euniceline3_7 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_7
            jump eunicepaintinggame_loop
    else:
        play sound SOUND_INCORRECT
        jump eunicepaintinggame_loop

label eunicepaintinggame_dot04:
    if eunicedot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ eunicedot.active = 4
        jump eunicepaintinggame_loop
    elif eunicedot.active == 3:
        if euniceline3_4 == False:
            show euniceartline03
            $ eunicedot.active = 4
            $ euniceline3_4 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_8
            jump eunicepaintinggame_loop
    elif eunicedot.active == 5:
        if euniceline4_5 == False:
            show euniceartline04
            $ eunicedot.active = 4
            $ euniceline4_5 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_9
            jump eunicepaintinggame_loop
    else:
        play sound SOUND_INCORRECT
        jump eunicepaintinggame_loop

label eunicepaintinggame_dot05:
    if eunicedot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ eunicedot.active = 5
        jump eunicepaintinggame_loop
    elif eunicedot.active == 4:
        if euniceline4_5 == False:
            show euniceartline04
            $ eunicedot.active = 5
            $ euniceline4_5 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_10
            jump eunicepaintinggame_loop
    elif eunicedot.active == 6:
        if euniceline5_6 == False:
            show euniceartline05
            $ eunicedot.active = 5
            $ euniceline5_6 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_11
            jump eunicepaintinggame_loop
    else:
        play sound SOUND_INCORRECT
        jump eunicepaintinggame_loop

label eunicepaintinggame_dot06:
    if eunicedot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ eunicedot.active = 6
        jump eunicepaintinggame_loop
    elif eunicedot.active == 3:
        if euniceline6_3 == False:
            show euniceartline06
            $ eunicedot.active = 6
            $ euniceline6_3 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_12
            jump eunicepaintinggame_loop
    elif eunicedot.active == 5:
        if euniceline5_6 == False:
            show euniceartline05
            $ eunicedot.active = 6
            $ euniceline5_6 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_13
            jump eunicepaintinggame_loop
    else:
        play sound SOUND_INCORRECT
        jump eunicepaintinggame_loop

label eunicepaintinggame_dot07:
    if eunicedot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ eunicedot.active = 7
        jump eunicepaintinggame_loop
    elif eunicedot.active == 3:
        if euniceline3_7 == False:
            show euniceartline07
            $ eunicedot.active = 7
            $ euniceline3_7 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_14
            jump eunicepaintinggame_loop
    elif eunicedot.active == 8:
        if euniceline7_8 == False:
            show euniceartline08
            $ eunicedot.active = 7
            $ euniceline7_8 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_15
            jump eunicepaintinggame_loop
    else:
        play sound SOUND_INCORRECT
        jump eunicepaintinggame_loop

label eunicepaintinggame_dot08:
    if eunicedot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ eunicedot.active = 8
        jump eunicepaintinggame_loop
    elif eunicedot.active == 7:
        if euniceline7_8 == False:
            show euniceartline08
            $ eunicedot.active = 8
            $ euniceline7_8 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_16
            jump eunicepaintinggame_loop
    elif eunicedot.active == 9:
        if euniceline8_9 == False:
            show euniceartline09
            $ eunicedot.active = 8
            $ euniceline8_9 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_17
            jump eunicepaintinggame_loop
    else:
        play sound SOUND_INCORRECT
        jump eunicepaintinggame_loop

label eunicepaintinggame_dot09:
    if eunicedot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ eunicedot.active = 9
        jump eunicepaintinggame_loop
    elif eunicedot.active == 8:
        if euniceline8_9 == False:
            show euniceartline09
            $ eunicedot.active = 9
            $ euniceline8_9 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_18
            jump eunicepaintinggame_loop
    elif eunicedot.active == 10:
        if euniceline9_10 == False:
            show euniceartline10
            $ eunicedot.active = 9
            $ euniceline9_10 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_19
            jump eunicepaintinggame_loop
    else:
        play sound SOUND_INCORRECT
        jump eunicepaintinggame_loop

label eunicepaintinggame_dot10:
    if eunicedot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ eunicedot.active = 10
        jump eunicepaintinggame_loop
    elif eunicedot.active == 9:
        if euniceline9_10 == False:
            show euniceartline10
            $ eunicedot.active = 10
            $ euniceline9_10 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_20
            jump eunicepaintinggame_loop
    elif eunicedot.active == 11:
        if euniceline10_11 == False:
            show euniceartline11
            $ eunicedot.active = 10
            $ euniceline10_11 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_21
            jump eunicepaintinggame_loop
    else:
        play sound SOUND_INCORRECT
        jump eunicepaintinggame_loop

label eunicepaintinggame_dot11:
    if eunicedot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ eunicedot.active = 11
        jump eunicepaintinggame_loop
    elif eunicedot.active == 10:
        if euniceline10_11 == False:
            show euniceartline11
            $ eunicedot.active = 11
            $ euniceline10_11 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_22
            jump eunicepaintinggame_loop
    elif eunicedot.active == 12:
        if euniceline11_12 == False:
            show euniceartline12
            $ eunicedot.active = 11
            $ euniceline11_12 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_23
            jump eunicepaintinggame_loop
    else:
        play sound SOUND_INCORRECT
        jump eunicepaintinggame_loop

label eunicepaintinggame_dot12:
    if eunicedot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ eunicedot.active = 12
        jump eunicepaintinggame_loop
    elif eunicedot.active == 11:
        if euniceline11_12 == False:
            show euniceartline12
            $ eunicedot.active = 12
            $ euniceline11_12 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_24
            jump eunicepaintinggame_loop
    elif eunicedot.active == 13:
        if euniceline12_13 == False:
            show euniceartline13
            $ eunicedot.active = 12
            $ euniceline12_13 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_25
            jump eunicepaintinggame_loop
    elif eunicedot.active == 15:
        if euniceline12_15 == False:
            show euniceartline16
            $ eunicedot.active = 12
            $ euniceline12_15 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_26
            jump eunicepaintinggame_loop
    elif eunicedot.active == 16:
        if euniceline12_16 == False:
            show euniceartline17
            $ eunicedot.active = 12
            $ euniceline12_16 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_27
            jump eunicepaintinggame_loop
    else:
        play sound SOUND_INCORRECT
        jump eunicepaintinggame_loop

label eunicepaintinggame_dot13:
    if eunicedot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ eunicedot.active = 13
        jump eunicepaintinggame_loop
    elif eunicedot.active == 12:
        if euniceline12_13 == False:
            show euniceartline13
            $ eunicedot.active = 13
            $ euniceline12_13 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_28
            jump eunicepaintinggame_loop
    elif eunicedot.active == 14:
        if euniceline13_14 == False:
            show euniceartline14
            $ eunicedot.active = 13
            $ euniceline13_14 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_29
            jump eunicepaintinggame_loop
    else:
        play sound SOUND_INCORRECT
        jump eunicepaintinggame_loop

label eunicepaintinggame_dot14:
    if eunicedot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ eunicedot.active = 14
        jump eunicepaintinggame_loop
    elif eunicedot.active == 13:
        if euniceline13_14 == False:
            show euniceartline14
            $ eunicedot.active = 14
            $ euniceline13_14 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_30
            jump eunicepaintinggame_loop
    elif eunicedot.active == 15:
        if euniceline14_15 == False:
            show euniceartline15
            $ eunicedot.active = 14
            $ euniceline14_15 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_31
            jump eunicepaintinggame_loop
    else:
        play sound SOUND_INCORRECT
        jump eunicepaintinggame_loop

label eunicepaintinggame_dot15:
    if eunicedot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ eunicedot.active = 15
        jump eunicepaintinggame_loop
    elif eunicedot.active == 12:
        if euniceline12_15 == False:
            show euniceartline16
            $ eunicedot.active = 15
            $ euniceline12_15 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_32
            jump eunicepaintinggame_loop
    elif eunicedot.active == 14:
        if euniceline14_15 == False:
            show euniceartline15
            $ eunicedot.active = 15
            $ euniceline14_15 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_33
            jump eunicepaintinggame_loop
    else:
        play sound SOUND_INCORRECT
        jump eunicepaintinggame_loop

label eunicepaintinggame_dot16:
    if eunicedot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ eunicedot.active = 16
        jump eunicepaintinggame_loop
    elif eunicedot.active == 12:
        if euniceline12_16 == False:
            show euniceartline17
            $ eunicedot.active = 16
            $ euniceline12_16 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_34
            jump eunicepaintinggame_loop
    elif eunicedot.active == 17:
        if euniceline16_17 == False:
            show euniceartline18
            $ eunicedot.active = 16
            $ euniceline16_17 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_35
            jump eunicepaintinggame_loop
    else:
        play sound SOUND_INCORRECT
        jump eunicepaintinggame_loop

label eunicepaintinggame_dot17:
    if eunicedot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ eunicedot.active = 17
        jump eunicepaintinggame_loop
    elif eunicedot.active == 16:
        if euniceline16_17 == False:
            show euniceartline18
            $ eunicedot.active = 17
            $ euniceline16_17 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_36
            jump eunicepaintinggame_loop
    elif eunicedot.active == 18:
        if euniceline17_18 == False:
            show euniceartline19
            $ eunicedot.active = 17
            $ euniceline17_18 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_37
            jump eunicepaintinggame_loop
    else:
        play sound SOUND_INCORRECT
        jump eunicepaintinggame_loop

label eunicepaintinggame_dot18:
    if eunicedot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ eunicedot.active = 18
        jump eunicepaintinggame_loop
    elif eunicedot.active == 17:
        if euniceline17_18 == False:
            show euniceartline19
            $ eunicedot.active = 18
            $ euniceline17_18 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_38
            jump eunicepaintinggame_loop
    elif eunicedot.active == 19:
        if euniceline18_19 == False:
            show euniceartline20
            $ eunicedot.active = 18
            $ euniceline18_19 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_39
            jump eunicepaintinggame_loop
    else:
        play sound SOUND_INCORRECT
        jump eunicepaintinggame_loop

label eunicepaintinggame_dot19:
    if eunicedot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ eunicedot.active = 19
        jump eunicepaintinggame_loop
    elif eunicedot.active == 18:
        if euniceline18_19 == False:
            show euniceartline20
            $ eunicedot.active = 19
            $ euniceline18_19 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_40
            jump eunicepaintinggame_loop
    elif eunicedot.active == 1:
        if euniceline19_1 == False:
            show euniceartline20
            $ eunicedot.active = 19
            $ euniceline19_1 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_41
            jump eunicepaintinggame_loop
    else:
        play sound SOUND_INCORRECT
        jump eunicepaintinggame_loop

label eunicepaintinggame_euniceartline1:
    jump eunicepaintinggame_loop

label eunicepaintinggame_euniceartline2:
    jump eunicepaintinggame_loop

label eunicepaintinggame_euniceartline3:
    jump eunicepaintinggame_loop

label eunicepaintinggame_euniceartline4:
    jump eunicepaintinggame_loop

label eunicepaintinggame_euniceartline5:
    jump eunicepaintinggame_loop

label eunicepaintinggame_euniceartline6:
    jump eunicepaintinggame_loop

label eunicepaintinggame_euniceartline7:
    jump eunicepaintinggame_loop

label eunicepaintinggame_euniceartline8:
    jump eunicepaintinggame_loop

label eunicepaintinggame_euniceartline9:
    jump eunicepaintinggame_loop

label eunicepaintinggame_euniceartline10:
    jump eunicepaintinggame_loop

label eunicepaintinggame_euniceartline11:
    jump eunicepaintinggame_loop

label eunicepaintinggame_euniceartline12:
    jump eunicepaintinggame_loop

label eunicepaintinggame_euniceartline13:
    jump eunicepaintinggame_loop

label eunicepaintinggame_euniceartline14:
    jump eunicepaintinggame_loop

label eunicepaintinggame_euniceartline15:
    jump eunicepaintinggame_loop

label eunicepaintinggame_euniceartline16:
    jump eunicepaintinggame_loop

label eunicepaintinggame_euniceartline17:
    jump eunicepaintinggame_loop

label eunicepaintinggame_euniceartline18:
    jump eunicepaintinggame_loop

label eunicepaintinggame_euniceartline19:
    jump eunicepaintinggame_loop

label eunicepaintinggame_euniceartline20:
    jump eunicepaintinggame_loop

label eunicepaintinggame_euniceartline21:
    jump eunicepaintinggame_loop

label eunicepaintinggame_euniceartbutton3:
    if eunicedot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ eunicedot.active = 3
        jump eunicepaintinggame_loop
    elif eunicedot.active == 2:
        if euniceline2_3 == False:
            show euniceartline02
            $ eunicedot.active = 3
            $ euniceline2_3 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_42
            jump eunicepaintinggame_loop
    elif eunicedot.active == 4:
        if euniceline3_4 == False:
            show euniceartline03
            $ eunicedot.active = 3
            $ euniceline3_4 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_43
            jump eunicepaintinggame_loop
    elif eunicedot.active == 6:
        if euniceline6_3 == False:
            show euniceartline06
            $ eunicedot.active = 3
            $ euniceline6_3 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_44
            jump eunicepaintinggame_loop
    elif eunicedot.active == 7:
        if euniceline3_7 == False:
            show euniceartline07
            $ eunicedot.active = 3
            $ euniceline3_7 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_45
            jump eunicepaintinggame_loop
    else:
        play sound SOUND_INCORRECT
        jump eunicepaintinggame_loop

label eunicepaintinggame_euniceartbutton12:
    if eunicedot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ eunicedot.active = 12
        jump eunicepaintinggame_loop
    elif eunicedot.active == 11:
        if euniceline11_12 == False:
            show euniceartline12
            $ eunicedot.active = 12
            $ euniceline11_12 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_46
            jump eunicepaintinggame_loop
    elif eunicedot.active == 13:
        if euniceline12_13 == False:
            show euniceartline13
            $ eunicedot.active = 12
            $ euniceline12_13 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_47
            jump eunicepaintinggame_loop
    elif eunicedot.active == 15:
        if euniceline12_15 == False:
            show euniceartline16
            $ eunicedot.active = 12
            $ euniceline12_15 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_48
            jump eunicepaintinggame_loop
    elif eunicedot.active == 16:
        if euniceline12_16 == False:
            show euniceartline17
            $ eunicedot.active = 12
            $ euniceline12_16 = True
            play sound SOUND_PAINTSTROKE
            $ euniceartpoints += 1
            jump eunicepaintinggame_loop
        else:
            play sound SOUND_INCORRECT
            call restarteunicegame from _call_restarteunicegame_49
            jump eunicepaintinggame_loop
    else:
        play sound SOUND_INCORRECT
        jump eunicepaintinggame_loop

label eunicepaintinggame_restart:
    call restarteunicegame from _call_restarteunicegame_50

label eunicepaintinggame_giveup:
    jump eunicepaintingfail
