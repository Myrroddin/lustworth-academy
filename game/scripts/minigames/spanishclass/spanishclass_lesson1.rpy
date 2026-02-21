#SCREENS
screen spanishclasslesson1:
    $ path = 'images/misc/classes/spanishclass/lesson1/'
    imagemap:
        ground (path + day + 'card.webp')
        hover (path + 'mondaycardhover.webp')

        hotspot (286, 617, 303, 106)  clicked Return('saturday')
        hotspot (213, 828, 306, 105)  clicked Return('thursday')
        hotspot (610, 740, 305, 109)  clicked Return('tuesday')
        hotspot (834, 614, 405, 90)   clicked Return('wednesday')
        hotspot (1275, 726, 324, 102) clicked Return('friday')
        hotspot (1429, 603, 321, 93)  clicked Return('sunday')
        hotspot (1012, 839, 255, 91)  clicked Return('monday')

    $ prompt = "What is " + day.upper() + " in Spanish?"
    text prompt:
        xanchor 0.5
        pos 0.50, 0.94

#LABELS
label spanishclass_lesson1:
    $ points = 0
    $ fridayMeme = 0
    $ days = list(range(7))
    # randomize order
    $ renpy.random.shuffle(days)
    # show first day with fade
    $ day = DAY_STRINGS[days[-1]]
    scene expression (day + 'card') with fade
    jump spanishclass_lesson1_loop

label spanishclass_lesson1_loop:
    $ day = DAY_STRINGS[days.pop()]
    scene expression (day + 'card')
    call screen spanishclasslesson1
    $ mapclick = _return
    if mapclick == day:
        $ points += 1
        play sound SOUND_CORRECT
    else:
        play sound SOUND_INCORRECT
    if mapclick == 'friday':
        $ fridayMeme += 1
    if len(days) == 0:
        jump spanishclass_lesson1_end
    jump spanishclass_lesson1_loop

label spanishclass_lesson1_end:
    if fridayMeme == 7:
        show fridaymeme with dissolve
        $ renpy.pause()
    return points == 7
