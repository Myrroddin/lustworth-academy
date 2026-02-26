#VARIABLES
default art1line1_2 = False
default art1line2_3 = False
default art1line3_4 = False
default art1line4_5 = False
default art1line5_6 = False
default art1line6_7 = False
default art1line7_8 = False
default art1line8_9 = False
default art1line9_10 = False
default art1line10_11 = False
default art1line11_12 = False
default art1line12_13 = False
default art1line13_14 = False
default art1line14_15 = False
default art1line15_9 = False
default art1line9_5 = False
default art1line5_16 = False
default art1line16_1 = False
default art1line1_17 = False
default art1line17_18 = False
default art1line18_14 = False

#VARIABLESDOT
default art1dot.active = 0
default art1points = 0

#VARIABLESPLUS


label artclass_lesson1:
    scene artclassroomfallday with fade
    $ gotoscene('artclasslesson01')

init 1 python:
    def showif_art1line1_2():
        if art1line1_2 == True:
            return True
        else:
            return False
    
    def showif_art1line2_3():
        if art1line2_3 == True:
            return True
        else:
            return False

    def showif_art1line3_4():
        if art1line3_4 == True:
            return True
        else:
            return False
    
    def showif_art1line4_5():
        if art1line4_5 == True:
            return True
        else:
            return False

    def showif_art1line5_6():
        if art1line5_6 == True:
            return True
        else:
            return False
    
    def showif_art1line6_7():
        if art1line6_7 == True:
            return True
        else:
            return False
    
    def showif_art1line7_8():
        if art1line7_8 == True:
            return True
        else:
            return False
    
    def showif_art1line8_9():
        if art1line8_9 == True:
            return True
        else:
            return False
    
    def showif_art1line9_10():
        if art1line9_10 == True:
            return True
        else:
            return False

    def showif_art1line10_11():
        if art1line10_11 == True:
            return True
        else:
            return False

    def showif_art1line11_12():
        if art1line11_12 == True:
            return True
        else:
            return False
    
    def showif_art1line12_13():
        if art1line12_13 == True:
            return True
        else:
            return False
    
    def showif_art1line13_14():
        if art1line13_14 == True:
            return True
        else:
            return False
    
    def showif_art1line14_15():
        if art1line14_15 == True:
            return True
        else:
            return False
    
    def showif_art1line15_9():
        if art1line15_9 == True:
            return True
        else:
            return False

    def showif_art1line9_5():
        if art1line9_5 == True:
            return True
        else:
            return False
    
    def showif_art1line5_16():
        if art1line5_16 == True:
            return True
        else:
            return False
    
    def showif_art1line16_1():
        if art1line16_1 == True:
            return True
        else:
            return False
    
    def showif_art1line1_17():
        if art1line1_17 == True:
            return True
        else:
            return False
    
    def showif_art1line17_18():
        if art1line17_18 == True:
            return True
        else:
            return False

    def showif_art1line18_14():
        if art1line18_14 == True:
            return True
        else:
            return False

    def showif_art1button1():
        if art1line1_2 == True:
            return True
        elif art1line1_17 == True:
            return True
        elif art1line16_1 == True:
            return True
        else:
            return False

    def showif_art1button5():
        if art1line4_5 == True:
            return True
        elif art1line5_6 == True:
            return True
        elif art1line9_5 == True:
            return True
        elif art1line5_16 == True:
            return True
        else:
            return False

    def showif_art1button9():
        if art1line8_9 == True:
            return True
        elif art1line9_5 == True:
            return True
        elif art1line9_10 == True:
            return True
        elif art1line15_9 == True:
            return True
        else:
            return False

    def showif_art1button14():
        if art1line13_14 == True:
            return True
        elif art1line14_15 == True:
            return True
        elif art1line18_14 == True:
            return True
        else:
            return False
    
    scene_defs['artclasslesson01'] = {
        'music': MUSIC_ART_CLASS,
        'altermusic': MUSIC_ART_CLASS,
        'maps': {
            'default':   ("artclasspaint01", "artclasspaint01hover"),
        },
        'hotspots': [
            ('dot01', (955, 233, 36, 38)),
            ('dot02', (1118, 190, 35, 36)),
            ('dot03', (1237, 288, 36, 36)),
            ('dot04', (1251, 454, 31, 39)),
            ('dot05', (1142, 599, 34, 37)),
            ('dot06', (1171, 738, 34, 35)),
            ('dot07', (1128, 892, 37, 34)),
            ('dot08', (1032, 757, 38, 32)),
            ('dot09', (942, 601, 37, 35)),
            ('dot10', (846, 713, 37, 34)),
            ('dot11', (613, 695, 33, 36)),
            ('dot12', (519, 512, 33, 34)),
            ('dot13', (583, 355, 34, 33)),
            ('dot14', (751, 332, 35, 31)),
            ('dot15', (849, 456, 42, 34)),
            ('dot16', (1054, 390, 40, 34)),
            ('dot17', (838, 172, 33, 30)),
            ('dot18', (717, 187, 34, 32)),
            ('restart', (983, 946, 196, 129)),
            ('giveup', (770, 945, 187, 128)),
        ],
        'sprites': [
            Sprite('artline1', 'art1line01', (0, 0, 0, 0), showif_art1line1_2),# Sprite(key, image, (x, y, w, h), showif)
            Sprite('artline2', 'art1line02', (0, 0, 0, 0), showif_art1line2_3),
            Sprite('artline3', 'art1line03', (0, 0, 0, 0), showif_art1line3_4),
            Sprite('artline4', 'art1line04', (0, 0, 0, 0), showif_art1line4_5),
            Sprite('artline5', 'art1line05', (0, 0, 0, 0), showif_art1line5_6),
            Sprite('artline6', 'art1line06', (0, 0, 0, 0), showif_art1line6_7),
            Sprite('artline7', 'art1line07', (0, 0, 0, 0), showif_art1line7_8),
            Sprite('artline8', 'art1line08', (0, 0, 0, 0), showif_art1line8_9),
            Sprite('artline9', 'art1line09', (0, 0, 0, 0), showif_art1line9_10),
            Sprite('artline10', 'art1line10', (0, 0, 0, 0), showif_art1line10_11),
            Sprite('artline11', 'art1line11', (0, 0, 0, 0), showif_art1line11_12),
            Sprite('artline12', 'art1line12', (0, 0, 0, 0), showif_art1line12_13),
            Sprite('artline13', 'art1line13', (0, 0, 0, 0), showif_art1line13_14),
            Sprite('artline14', 'art1line14', (0, 0, 0, 0), showif_art1line14_15),
            Sprite('artline15', 'art1line15', (0, 0, 0, 0), showif_art1line15_9),
            Sprite('artline16', 'art1line16', (0, 0, 0, 0), showif_art1line9_5),
            Sprite('artline17', 'art1line17', (0, 0, 0, 0), showif_art1line5_16),
            Sprite('artline18', 'art1line18', (0, 0, 0, 0), showif_art1line16_1),
            Sprite('artline19', 'art1line19', (0, 0, 0, 0), showif_art1line1_17),
            Sprite('artline20', 'art1line20', (0, 0, 0, 0), showif_art1line17_18),
            Sprite('artline21', 'art1line21', (0, 0, 0, 0), showif_art1line18_14),
            Sprite('artbutton1', 'art1button', (961, 241, 24, 24), showif_art1button1),
            Sprite('artbutton5', 'art1button', (1146, 606, 24, 24), showif_art1button5),
            Sprite('artbutton9', 'art1button', (948, 606, 24, 24), showif_art1button9),
            Sprite('artbutton14', 'art1button', (756, 337, 24, 24), showif_art1button14),
            

        ]
    }

    
#LABELS

label restart1game:
    $ art1points = 0
    $ art1dot.active = 0
    $ art1line1_2 = False
    $ art1line2_3 = False
    $ art1line3_4 = False
    $ art1line4_5 = False
    $ art1line5_6 = False
    $ art1line6_7 = False
    $ art1line7_8 = False
    $ art1line8_9 = False
    $ art1line9_10 = False
    $ art1line10_11 = False
    $ art1line11_12 = False
    $ art1line12_13 = False
    $ art1line13_14 = False
    $ art1line14_15 = False
    $ art1line15_9 = False
    $ art1line9_5 = False
    $ art1line5_16 = False
    $ art1line16_1 = False
    $ art1line1_17 = False
    $ art1line17_18 = False
    $ art1line18_14 = False
    $ gotoscene('artclasslesson01')

label artclasslesson01:
    hide screen freeroamhud
    jump artclasslesson01_loop

label artclasslesson01_loop:
    hide screen freeroamhud
    if art1points == 21:
        play sound "audio/sfx/missioncomplete.ogg"
        show artclass01success with dissolve
        $ renpy.pause()
        return True
    $ resetscene()
    call screen map('artclasslesson01')
    jump artclasslesson01_loop

label artclasslesson01_dot01:
    if art1dot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ art1dot.active = 1
        jump artclasslesson01_loop
    elif art1dot.active == 1:
        play sound SOUND_PAINTSTROKE
        jump artclasslesson01_loop
    elif art1dot.active == 2:
        if art1line1_2 == False:
            show art1line01
            $ art1dot.active = 1
            $ art1line1_2 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game
            jump artclasslesson01_loop
    elif art1dot.active == 3:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 4:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 5:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 6:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 7:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 8:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 9:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 10:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 11:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 12:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 13:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 14:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 15:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 16:
        if art1line16_1 == False:
            show art1line18
            $ art1dot.active = 1
            $ art1line16_1 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_1
            jump artclasslesson01_loop
    elif art1dot.active == 17:
        if art1line1_17 == False:
            show art1line19
            $ art1dot.active = 1
            $ art1line1_17 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_2
            jump artclasslesson01_loop
    elif art1dot.active == 18:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop

label artclasslesson01_dot02: 
    if art1dot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ art1dot.active = 2
        jump artclasslesson01_loop
    elif art1dot.active == 1:
        if art1line1_2 == False:
            $ art1dot.active = 2
            $ art1line1_2 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_3
            jump artclasslesson01_loop
    elif art1dot.active == 2:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 3:
        if art1line2_3 == False:
            show art1line02
            $ art1dot.active = 2
            $ art1line2_3 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_4
            jump artclasslesson01_loop
    elif art1dot.active == 4:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 5:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 6:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 7:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 8:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 9:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 10:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 11:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 12:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 13:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 14:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 15:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 16:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 17:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 18:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop

label artclasslesson01_dot03:
    if art1dot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ art1dot.active = 3
        jump artclasslesson01_loop
    elif art1dot.active == 1:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 2:
        if art1line2_3 == False:
            show art1line02
            $ art1dot.active = 3
            $ art1line2_3 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_5
            jump artclasslesson01_loop
    elif art1dot.active == 3:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 4:
        if art1line3_4 == False:
            show art1line03
            $ art1dot.active = 3
            $ art1line3_4 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_6
            jump artclasslesson01_loop
    elif art1dot.active == 5:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 6:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 7:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 8:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 9:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 10:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 11:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 12:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 13:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 14:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 15:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 16:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 17:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 18:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop

label artclasslesson01_dot04:
    if art1dot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ art1dot.active = 4
        jump artclasslesson01_loop
    elif art1dot.active == 1:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 2:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 3:
        if art1line3_4 == False:
            show art1line03
            $ art1dot.active = 4
            $ art1line3_4 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_7
            jump artclasslesson01_loop
    elif art1dot.active == 4:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 5:
        if art1line4_5 == False:
            show art1line04
            $ art1dot.active = 4
            $ art1line4_5 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_8
            jump artclasslesson01_loop
    elif art1dot.active == 6:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 7:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 8:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 9:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 10:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 11:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 12:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 13:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 14:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 15:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 16:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 17:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 18:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop

label artclasslesson01_dot05:
    if art1dot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ art1dot.active = 5
        jump artclasslesson01_loop
    elif art1dot.active == 1:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 2:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 3:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 4:
        if art1line4_5 == False:
            show art1line04
            $ art1dot.active = 5
            $ art1line4_5 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_9
            jump artclasslesson01_loop
    elif art1dot.active == 5:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 6:
        if art1line5_6 == False:
            show art1line05
            $ art1dot.active = 5
            $ art1line5_6 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_10
            jump artclasslesson01_loop
    elif art1dot.active == 7:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 8:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 9:
        if art1line9_5 == False:
            show art1line16
            $ art1dot.active = 5
            $ art1line9_5 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_11
            jump artclasslesson01_loop
    elif art1dot.active == 10:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 11:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 12:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 13:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 14:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 15:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 16:
        if art1line5_16 == False:
            show art1line17
            $ art1dot.active = 5
            $ art1line5_16 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_12
            jump artclasslesson01_loop
    elif art1dot.active == 17:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 18:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop

label artclasslesson01_dot06:
    if art1dot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ art1dot.active = 6
        jump artclasslesson01_loop
    elif art1dot.active == 1:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 2:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 3:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 4:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 5:
        if art1line5_6 == False:
            show art1line05
            $ art1dot.active = 6
            $ art1line5_6 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_13
            jump artclasslesson01_loop
    elif art1dot.active == 6:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 7:
        if art1line6_7 == False:
            show art1line06
            $ art1dot.active = 6
            $ art1line6_7 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_14
            jump artclasslesson01_loop
    elif art1dot.active == 8:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 9:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 10:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 11:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 12:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 13:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 14:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 15:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 16:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 17:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 18:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop

label artclasslesson01_dot07:
    if art1dot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ art1dot.active = 7
        jump artclasslesson01_loop
    elif art1dot.active == 1:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 2:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 3:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 4:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 5:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 6:
        if art1line6_7 == False:
            show art1line06
            $ art1dot.active = 7
            $ art1line6_7 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_15
            jump artclasslesson01_loop
    elif art1dot.active == 7:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 8:
        if art1line7_8 == False:
            show art1line07
            $ art1dot.active = 7
            $ art1line7_8 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_16
            jump artclasslesson01_loop
    elif art1dot.active == 9:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 10:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 11:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 12:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 13:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 14:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 15:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 16:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 17:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 18:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop

label artclasslesson01_dot08:
    if art1dot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ art1dot.active = 8
        jump artclasslesson01_loop
    elif art1dot.active == 1:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 2:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 3:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 4:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 5:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 6:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 7:
        if art1line7_8 == False:
            show art1line07
            $ art1dot.active = 8
            $ art1line7_8 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_17
            jump artclasslesson01_loop
    elif art1dot.active == 8:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 9:
        if art1line8_9 == False:
            show art1line08
            $ art1dot.active = 8
            $ art1line8_9 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_18
            jump artclasslesson01_loop
    elif art1dot.active == 10:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 11:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 12:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 13:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 14:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 15:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 16:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 17:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 18:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop

label artclasslesson01_dot09:
    if art1dot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ art1dot.active = 9
        jump artclasslesson01_loop
    elif art1dot.active == 1:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 2:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 3:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 4:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 5:
        if art1line9_5 == False:
            show art1line16
            $ art1dot.active = 9
            $ art1line9_5 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_19
            jump artclasslesson01_loop
    elif art1dot.active == 6:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 7:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 8:
        if art1line8_9 == False:
            show art1line08
            $ art1dot.active = 9
            $ art1line8_9 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_20
            jump artclasslesson01_loop
    elif art1dot.active == 9:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 10:
        if art1line9_10 == False:
            show art1line09
            $ art1dot.active = 9
            $ art1line9_10 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_21
            jump artclasslesson01_loop
    elif art1dot.active == 11:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 12:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 13:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 14:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 15:
        if art1line15_9 == False:
            show art1line15
            $ art1dot.active = 9
            $ art1line15_9 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_22
            jump artclasslesson01_loop
    elif art1dot.active == 16:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 17:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 18:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop

label artclasslesson01_dot10:
    if art1dot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ art1dot.active = 10
        jump artclasslesson01_loop
    elif art1dot.active == 1:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 2:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 3:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 4:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 5:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 6:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 7:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 8:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 9:
        if art1line9_10 == False:
            show art1line09
            $ art1dot.active = 10
            $ art1line9_10 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_23
            jump artclasslesson01_loop
    elif art1dot.active == 10:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 11:
        if art1line10_11 == False:
            show art1line10
            $ art1dot.active = 10
            $ art1line10_11 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_24
            jump artclasslesson01_loop
    elif art1dot.active == 12:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 13:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 14:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 15:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 16:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 17:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 18:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop

label artclasslesson01_dot11:
    if art1dot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ art1dot.active = 11
        jump artclasslesson01_loop
    elif art1dot.active == 1:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 2:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 3:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 4:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 5:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 6:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 7:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 8:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 9:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 10:
        if art1line10_11 == False:
            show art1line10
            $ art1dot.active = 11
            $ art1line10_11 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_25
            jump artclasslesson01_loop
    elif art1dot.active == 11:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 12:
        if art1line11_12 == False:
            show art1line11
            $ art1dot.active = 11
            $ art1line11_12 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_26
            jump artclasslesson01_loop
    elif art1dot.active == 13:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 14:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 15:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 16:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 17:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 18:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop

label artclasslesson01_dot12:
    if art1dot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ art1dot.active = 12
        jump artclasslesson01_loop
    elif art1dot.active == 1:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 2:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 3:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 4:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 5:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 6:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 7:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 8:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 9:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 10:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 11:
        if art1line11_12 == False:
            show art1line11
            $ art1dot.active = 12
            $ art1line11_12 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_27
            jump artclasslesson01_loop
    elif art1dot.active == 12:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 13:
        if art1line12_13 == False:
            show art1line12
            $ art1dot.active = 12
            $ art1line12_13 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_28
            jump artclasslesson01_loop
    elif art1dot.active == 14:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 15:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 16:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 17:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 18:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop

label artclasslesson01_dot13:
    if art1dot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ art1dot.active = 13
        jump artclasslesson01_loop
    elif art1dot.active == 1:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 2:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 3:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 4:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 5:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 6:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 7:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 8:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 9:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 10:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 11:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 12:
        if art1line12_13 == False:
            show art1line12
            $ art1dot.active = 13
            $ art1line12_13 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_29
            jump artclasslesson01_loop
    elif art1dot.active == 13:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 14:
        if art1line13_14 == False:
            show art1line13
            $ art1dot.active = 13
            $ art1line13_14 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_30
            jump artclasslesson01_loop
    elif art1dot.active == 15:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 16:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 17:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 18:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop

label artclasslesson01_dot14:
    if art1dot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ art1dot.active = 14
        jump artclasslesson01_loop
    elif art1dot.active == 1:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 2:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 3:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 4:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 5:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 6:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 7:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 8:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 9:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 10:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 11:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 12:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 13:
        if art1line13_14 == False:
            show art1line13
            $ art1dot.active = 14
            $ art1line13_14 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_31
            jump artclasslesson01_loop
    elif art1dot.active == 14:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 15:
        if art1line14_15 == False:
            show art1line14
            $ art1dot.active = 14
            $ art1line14_15 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_32
            jump artclasslesson01_loop
    elif art1dot.active == 16:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 17:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 18:
        if art1line18_14 == False:
            show art1line21
            $ art1dot.active = 14
            $ art1line18_14 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_33
            jump artclasslesson01_loop

label artclasslesson01_dot15:
    if art1dot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ art1dot.active = 15
        jump artclasslesson01_loop
    elif art1dot.active == 1:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 2:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 3:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 4:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 5:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 6:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 7:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 8:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 9:
        if art1line15_9 == False:
            show art1line15
            $ art1dot.active = 15
            $ art1line15_9 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_34
            jump artclasslesson01_loop
    elif art1dot.active == 10:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 11:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 12:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 13:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 14:
        if art1line14_15 == False:
            show art1line14
            $ art1dot.active = 15
            $ art1line14_15 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_35
            jump artclasslesson01_loop
    elif art1dot.active == 15:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 16:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 17:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 18:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop

label artclasslesson01_dot16:
    if art1dot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ art1dot.active = 16
        jump artclasslesson01_loop
    elif art1dot.active == 1:
        if art1line16_1 == False:
            show art1line18
            $ art1dot.active = 16
            $ art1line16_1 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_36
            jump artclasslesson01_loop
    elif art1dot.active == 2:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 3:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 4:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 5:
        if art1line5_16 == False:
            show art1line17
            $ art1dot.active = 16
            $ art1line5_16 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_37
            jump artclasslesson01_loop
    elif art1dot.active == 6:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 7:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 8:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 9:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 10:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 11:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 12:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 13:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 14:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 15:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 16:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 17:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 18:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop

label artclasslesson01_dot17:
    if art1dot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ art1dot.active = 17
        jump artclasslesson01_loop
    elif art1dot.active == 1:
        if art1line1_17 == False:
            show art1line19
            $ art1dot.active = 17
            $ art1line1_17 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_38
            jump artclasslesson01_loop
    elif art1dot.active == 2:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 3:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 4:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 5:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 6:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 7:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 8:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 9:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 10:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 11:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 12:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 13:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 14:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 15:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 16:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 17:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 18:
        if art1line17_18 == False:
            show art1line20
            $ art1dot.active = 17
            $ art1line17_18 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_39
            jump artclasslesson01_loop

label artclasslesson01_dot18:
    if art1dot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ art1dot.active = 18
        jump artclasslesson01_loop
    elif art1dot.active == 1:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 2:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 3:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 4:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 5:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 6:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 7:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 8:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 9:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 10:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 11:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 12:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 13:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 14:
        if art1line18_14 == False:
            show art1line21
            $ art1dot.active = 18
            $ art1line18_14 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_40
            jump artclasslesson01_loop
    elif art1dot.active == 15:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 16:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 17:
        if art1line17_18 == False:
            show art1line20
            $ art1dot.active = 18
            $ art1line17_18 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_41
            jump artclasslesson01_loop
    elif art1dot.active == 18:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop

label artclasslesson01_artline1:
    jump artclasslesson01_loop

label artclasslesson01_artline2:
    jump artclasslesson01_loop

label artclasslesson01_artline3:
    jump artclasslesson01_loop

label artclasslesson01_artline4:
    jump artclasslesson01_loop

label artclasslesson01_artline5:
    jump artclasslesson01_loop

label artclasslesson01_artline6:
    jump artclasslesson01_loop

label artclasslesson01_artline7:
    jump artclasslesson01_loop

label artclasslesson01_artline8:
    jump artclasslesson01_loop

label artclasslesson01_artline9:
    jump artclasslesson01_loop

label artclasslesson01_artline10:
    jump artclasslesson01_loop

label artclasslesson01_artline11:
    jump artclasslesson01_loop

label artclasslesson01_artline12:
    jump artclasslesson01_loop

label artclasslesson01_artline13:
    jump artclasslesson01_loop

label artclasslesson01_artline14:
    jump artclasslesson01_loop

label artclasslesson01_artline15:
    jump artclasslesson01_loop

label artclasslesson01_artline16:
    jump artclasslesson01_loop

label artclasslesson01_artline17:
    jump artclasslesson01_loop

label artclasslesson01_artline18:
    jump artclasslesson01_loop

label artclasslesson01_artline19:
    jump artclasslesson01_loop

label artclasslesson01_artline20:
    jump artclasslesson01_loop

label artclasslesson01_artline21:
    jump artclasslesson01_loop

label artclasslesson01_artbutton1:
    if art1dot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ art1dot.active = 1
        jump artclasslesson01_loop
    elif art1dot.active == 1:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 2:
        if art1line1_2 == False:
            show art1line01
            $ art1dot.active = 1
            $ art1line1_2 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_42
            jump artclasslesson01_loop
    elif art1dot.active == 3:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 4:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 5:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 6:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 7:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 8:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 9:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 10:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 11:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 12:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 13:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 14:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 15:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 16:
        if art1line16_1 == False:
            show art1line18
            $ art1dot.active = 1
            $ art1line16_1 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_43
            jump artclasslesson01_loop
    elif art1dot.active == 17:
        if art1line1_17 == False:
            show art1line19
            $ art1dot.active = 1
            $ art1line1_17 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_44
            jump artclasslesson01_loop
    elif art1dot.active == 18:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop

label artclasslesson01_artbutton5:
    if art1dot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ art1dot.active = 5
        jump artclasslesson01_loop
    elif art1dot.active == 1:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 2:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 3:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 4:
        if art1line4_5 == False:
            show art1line04
            $ art1dot.active = 5
            $ art1line4_5 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_45
            jump artclasslesson01_loop
    elif art1dot.active == 5:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 6:
        if art1line5_6 == False:
            show art1line05
            $ art1dot.active = 5
            $ art1line5_6 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_46
            jump artclasslesson01_loop
    elif art1dot.active == 7:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 8:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 9:
        if art1line9_5 == False:
            show art1line16
            $ art1dot.active = 5
            $ art1line9_5 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_47
            jump artclasslesson01_loop
    elif art1dot.active == 10:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 11:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 12:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 13:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 14:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 15:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 16:
        if art1line5_16 == False:
            show art1line17
            $ art1dot.active = 5
            $ art1line5_16 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_48
            jump artclasslesson01_loop
    elif art1dot.active == 17:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 18:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop

label artclasslesson01_artbutton9:
    if art1dot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ art1dot.active = 9
        jump artclasslesson01_loop
    elif art1dot.active == 1:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 2:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 3:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 4:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 5:
        if art1line9_5 == False:
            show art1line16
            $ art1dot.active = 9
            $ art1line9_5 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_49
            jump artclasslesson01_loop
    elif art1dot.active == 6:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 7:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 8:
        if art1line8_9 == False:
            show art1line08
            $ art1dot.active = 9
            $ art1line8_9 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_50
            jump artclasslesson01_loop
    elif art1dot.active == 9:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 10:
        if art1line9_10 == False:
            show art1line09
            $ art1dot.active = 9
            $ art1line9_10 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_51
            jump artclasslesson01_loop
    elif art1dot.active == 11:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 12:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 13:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 14:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 15:
        if art1line15_9 == False:
            show art1line15
            $ art1dot.active = 9
            $ art1line15_9 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_52
            jump artclasslesson01_loop
    elif art1dot.active == 16:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 17:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 18:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop

label artclasslesson01_artbutton14:
    if art1dot.active == 0:
        play sound SOUND_PAINTSTROKE
        $ art1dot.active = 14
        jump artclasslesson01_loop
    elif art1dot.active == 1:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 2:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 3:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 4:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 5:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 6:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 7:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 8:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 9:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 10:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 11:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 12:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 13:
        if art1line13_14 == False:
            show art1line13
            $ art1dot.active = 14
            $ art1line13_14 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_53
            jump artclasslesson01_loop
    elif art1dot.active == 14:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 15:
        if art1line14_15 == False:
            show art1line14
            $ art1dot.active = 14
            $ art1line14_15 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_54
            jump artclasslesson01_loop
    elif art1dot.active == 16:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 17:
        play sound SOUND_INCORRECT
        jump artclasslesson01_loop
    elif art1dot.active == 18:
        if art1line18_14 == False:
            show art1line21
            $ art1dot.active = 14
            $ art1line18_14 = True
            play sound SOUND_PAINTSTROKE
            $ art1points += 1
            jump artclasslesson01_loop
        else:
            play sound SOUND_INCORRECT
            call restart1game from _call_restart1game_55
            jump artclasslesson01_loop

label artclasslesson01_restart:
    call restart1game from _call_restart1game_56

label artclasslesson01_giveup:
    return
