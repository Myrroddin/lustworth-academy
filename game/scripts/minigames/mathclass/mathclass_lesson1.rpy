#VARIABLES
define mathclass.lesson1Answers = ['answer2', 'answer1', 'answer3', 'answer2']

#SCREENS
screen mathclass_lesson1:
    $ path = 'images/misc/classes/mathclass/lesson1/'
    $ q = str(question + 1)
    imagemap:
        ground (path + 'mathquestion' + q + '.webp')
        hover  (path + 'mathquestion' + q + 'hover.webp')

        hotspot (445, 651, 165, 120)  clicked Return('answer1')
        hotspot (666, 651, 166, 122)  clicked Return('answer2')
        hotspot (900, 651, 166, 122)  clicked Return('answer3')
        hotspot (1125, 651, 169, 122) clicked Return('answer4')

#LABELS
label mathclass_lesson1:
    $ question = 0
    $ points = 0
    scene mathboardempty with fade
    jump mathclass_lesson1_loop

label mathclass_lesson1_loop:
    call screen mathclass_lesson1
    $ mapclick = _return
    $ answer = mathclass.lesson1Answers[question]
    if mapclick == answer:
        $ points += 1
        play sound SOUND_CORRECT
    else:
        play sound SOUND_INCORRECT
    $ question += 1
    if question == len(mathclass.lesson1Answers):
        jump mathclass_lesson1_end
    jump mathclass_lesson1_loop

label mathclass_lesson1_end:
    scene mathclassroom01 with fade
    show camembert with dissolve
    Camembert "Alright class, let's see how everyone did."
    return points == 4
