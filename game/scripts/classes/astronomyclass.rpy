label astronomyclass:
    hide screen freeroamhud
    scene black with fade
    call subject('astronomy') from _call_subject_1
    $ gotoscene('boysdormplaza', transition=fade)

label astronomy_minigame:
    return False

## Lesson failed
label astronomy_failintro:
    return

label astronomy_failoutro:
    return

## Lesson 1
label astronomy_lesson1intro:
    Developer "{i}Astronomy class will arrive in a future update.{/i}"
    return

label astronomy_lesson1outro:
    return
