define chemistry.recipes = [
    # Lesson 1
    {
        'name': 'Cannabiotics',
        'red'    : (40.0, 60.0),
        'yellow' : (40.0, 60.0),
        'green'  : (40.0, 60.0),
        'blue'   : (40.0, 60.0),
        'purple' : (40.0, 60.0),
    },
]

label chemistryclass:
    hide screen freeroamhud
    scene black with fade
    call subject('chemistry') from _call_subject_3
    $ gotoscene('mainbuildinglefthallway', transition=fade)

label chemistry_minigame:
    $ lesson = classes['chemistry'].lesson
    # TODO: add more lessons
    if lesson > 1:
        return True
    menu:
        "Play minigame":
            show chemclasswarning with dissolve
            $ renpy.pause()
            hide chemclasswarning with dissolve
            $ _return = True
        "Skip":
            $ _return = True
    return _return

## Lesson failed
label chemistry_failintro:
    return

label chemistry_failoutro:
    'You lost...'
    return

## Lesson 1
label chemistry_lesson1intro:
    scene chemistrylab01 with fade
    show mrwhite01 with dissolve
    $ White.met = True
    White "Chemistry."
    White "It is the study of what? Anyone?"
    Unk "Uhhh, chemicals?"
    White "Not exactly, Jones."
    White "Technically, chemistry is the study of matter, or as I prefer to see it, a study of change."
    White "A fascinating subject if you actually understand what you can create by manipulating matter, molecules and... chemicals, of course."
    White "Today, we are going to work on one of my specialties."
    White "A dru... *Ahem*... A substance that will allow us to understand how various types of chemicals respond to one another."
    White "Please try not to inhale or eat anything you see on the tables."
    White "Let's start processing some cannabi... Umm, cannabiotics, yes, a medicinal compound."
    Unk "Mr. White..."
    White "Questions are over, folks. Let's get to business. I want a good shipment of these before the class is over."
    return

label chemistry_lesson1outro:
    scene chemistrylab01 with fade
    show mrwhite01 with dissolve
    White "Good job, everyone! This is enough for at least one shipment."
    White "Let's see if next week, we can try some opio... Umm, some options, some other options."
    White "[player_name], outstanding job! Keep going like that and you might win me over."
    play sound SOUND_SCHOOL_BELL
    return

label chemistry_lesson2intro:
    "This content is not available yet."
    return

label chemistry_lesson2outro:
    return
