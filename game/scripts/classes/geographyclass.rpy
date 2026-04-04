label geographyclass:
    hide screen freeroamhud
    scene geographyclassroomday with fade
    call subject('geography') from _call_subject_4
    $ gotoscene('mainbuildingrighthallway', transition=fade)

label geography_minigame:
    $ lesson = classes['geography'].lesson
    # TODO: add more lessons
    if lesson > 1:
        return True
    call expression ('geographyclass_lesson' + str(lesson)) from _call_expression_6
    return _return

## Lesson failed
label geography_failintro:
    show missjones sit with dissolve
    Jones "My little puppies, we are finally together again!"
    Jones "The last lesson didn't go too well for us. So today we are going to try again, okay?"
    return

label geography_failoutro:
    scene geographyclassroomday with fade
    show missjones sit with dissolve
    Jones "Oh, no, darling... That's not correct."
    Jones "Don't worry, I'm sure you'll get it next time."
    return

## Lesson 1
label geography_lesson1intro:
    "{i}[player_name] knew he was in the right classroom as soon as he entered.{/i}"
    "{i}The room was filled with flags and maps and different clocks in different times from different countries.{/i}"
    "{i}[player_name] made his way to the back of the room.{/i}"
    show missjones sit with dissolve
    Jones "My little darlings, we are finally together again!"
    Jones "I'm so happy to have you here with me once more."
    Jones "I see we have some new faces with us today, so allow me to introduce myself again."
    Jones "My name is Miss Jones."
    $ Jones.met = True
    Jones "My great-grandfather was a famous explorer, and I inherited his passion for adventure!"
    Jones "My goal is to transfer that excitement to you, my little pumpkins."
    "Well isn't she a cheery one."
    Jones "Today, we are going to start light, and we are going to identify the continents of our world, okay?"
    Jones "I know you're excited to discover the world with me!"
    Jones "Let's begin."
    return

label geography_lesson1outro:
    scene geographyclassroomday with fade
    show missjones sit with dissolve
    Jones "Oh, yes! Yes! YES! That's correct!"
    Jones "Wow, Mr. [player_surname], it's seems that you're a total adventurer."
    show geographyreward01 with dissolve
    "{i}Nice one!{/i}"
    "{i}Keep it up and you might have a different kind of adventure with her...{/i}"
    hide geographyreward01 with dissolve
    play sound SOUND_SCHOOL_BELL
    Jones "'Til next time, class!"
    return

## Lesson 2
label geography_lesson2intro:
    Developer "{i}More lessons coming soon.{/i}"
    return

label geography_lesson2outro:
    return
