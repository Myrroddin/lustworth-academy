label gymclass:
    hide screen freeroamhud
    scene gymring01 with fade
    call subject('gym') from _call_subject_5
    if calendar.when == (PROLOGUE, THURSDAY, EVENING):
        jump prologue_cassidyintro
    $ gotoscene('schoolgym', transition=fade)

label gym_minigame:
    $ lesson = classes['gym'].lesson
    # TODO: add more lessons
    if lesson > 1:
        return True
    menu:
        __("Play minigame"):
            call start_battletutorial from _call_start_battletutorial
    return _return

## Lesson failed
label gym_failintro:
    show toord with dissolve
    play sound "audio/sfx/mrtoordalrightwimps.ogg"
    Toord "Alright, wimps! Get back up here [player_surname]."
    Toord "Show me you're not hopeless after all."
    return

label gym_failoutro:
    show toord with vpunch
    Toord "No, no, no! That's not how a man fights!"
    Toord "I hope to see some improvement next time, [player_surname]."
    return

## Lesson 1
label gym_lesson1intro:
    play music "audio/music/gymclasstheme.ogg" volume 0.5
    show toord with vpunch
    play sound "audio/sfx/mrtoordalrightwimps.ogg"
    Toord "Alright, wimps!"
    Toord "Time for some wrestling instruction."
    Toord "This will require physical contact between you and your opponent."
    Toord "Some of you might even enjoy that."
    Toord "Hey, new guy! Come here."
    Toord "Mr. Carlson, get your ass in the ring right now!"
    Toord "Now, let's smash some faces!"
    hide toord
    return

label gym_lesson1outro:
    play sound "audio/sfx/missioncomplete.ogg"
    show toord with vpunch
    Toord "Good job, [player_surname]!"
    play music MUSIC_MRTOORD_THEME
    Toord "You fight like myself at a young age."
    Toord "Maybe you have the balls of a champion after all."
    Toord "My best students always get a piece of one of my personal collections."
    Toord "Here you go, fella. Don't ask how I got that. I mean it."
    play sound SOUND_SEXY_INTRO
    show gymclassonereward with dissolve
    __("{i}Congratulations, you beat Thad Carlson.{/i}")
    __("{i}Don't get too cocky though. He was the weakest fighter in the lineup.{/i}")
    __("{i}If you want to become Truthworth's wrestling champion, you'll have to beat tougher opponents.{/i}")
    __("{i}But if you somehow manage to do it, then maybe you'll have a chance with that sexy redhead, Christy.{/i}")
    pause 0.6
    hide gymclassonereward with dissolve
    play sound SOUND_SCHOOL_BELL
    Toord "Alright, class dismissed."
    if newcontentskipactive == True:
        scene laterthatdaysomewhere with fade
        $ renpy.pause()
        jump eunicetheater_practiceintro
    return

## Lesson 2
label gym_lesson2intro:
    Developer "{i}More lessons coming soon.{/i}"
    return

label gym_lesson2outro:
    return
