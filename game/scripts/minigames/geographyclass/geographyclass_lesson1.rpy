#SCREENS
screen geographyclasslesson1:
    $ path = 'images/misc/classes/geographyclass/lesson1/'
    imagemap:
        ground (path + 'continents_' + continent + '.webp')
        hover  (path + 'continents_hover.webp')

        hotspot (1, 173, 670, 372)    clicked Return('northamerica')
        hotspot (197, 550, 516, 419)  clicked Return('southamerica')
        hotspot (876, 356, 395, 196)  clicked Return('europe')
        hotspot (780, 552, 481, 334)  clicked Return('africa')
        hotspot (1284, 291, 632, 478) clicked Return('asia')
        hotspot (1515, 813, 403, 256) clicked Return('oceania')
        hotspot (506, 977, 842, 103)  clicked Return('antarctica')

#LABELS
label geographyclass_lesson1:
    $ points = 0
    $ continents = ['asia', 'europe', 'northamerica', 'southamerica', 'africa', 'oceania', 'antarctica']
    # randomize order
    $ renpy.random.shuffle(continents)
    # show first continent with fade
    $ continent = continents[-1]
    scene expression ('continents_' + continent) with fade
    jump geographyclass_lesson1_loop

label geographyclass_lesson1_loop:
    $ continent = continents.pop()
    scene expression ('continents_' + continent)
    call screen geographyclasslesson1
    $ mapclick = _return
    if mapclick == continent:
        $ points += 1
        play sound SOUND_CORRECT
    else:
        play sound SOUND_INCORRECT
    if len(continents) == 0:
        jump geographyclass_lesson1_end
    jump geographyclass_lesson1_loop

label geographyclass_lesson1_end:
    return points == 7
