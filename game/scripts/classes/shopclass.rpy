label shopclass:
    hide screen freeroamhud
    play music MUSIC_SHOP_CLASS
    call subject('shop') from _call_subject_8
    if calendar.when[0] == PROLOGUE:
        jump prologue_aftershop
    $ gotoscene('schoolgarage')

label shop_minigame:
    $ lesson = classes['shop'].lesson
    show shopclasswarning with dissolve
    Developer "{i}Shop class minigame coming soon!{/i}"
    hide shopclasswarning with dissolve
    return True

## Lesson failed
label shop_failintro:
    Audrey "I know you guys struggled with the last class, so we're gonna do it again."
    Audrey "You know what they say - if ya don't succeed, try, try again!"
    return

label shop_failoutro:
    Audrey "C'mon [player_surname], I know you can do better than that!"
    Audrey "That's alright, we'll just give it another go next time."
    return

## Lesson 1
label shop_lesson1intro:
    call prologue_shopclassintro from _call_prologue_shopclassintro
    return

label shop_lesson1outro:
    return

## Lesson 2
label shop_lesson2intro:
    return

label shop_lesson2outro:
    return
