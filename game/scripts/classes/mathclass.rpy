label mathclass:
    hide screen freeroamhud
    scene mathclassroom01 with fade
    call subject('math') from _call_subject_6
    # if calendar.when[0] == PROLOGUE:
    #     jump prologue_missdawsontitshow
    # elif quests.beatrixDiary == LOCKED:
    #     jump beatrixdiaryquest
    $ gotoscene('mainbuildingrighthallway', transition=fade)

label math_minigame:
    $ lesson = classes['math'].lesson
    # TODO: add more lessons
    if lesson > 1:
        return True
    call expression ('mathclass_lesson' + str(lesson)) from _call_expression_7
    return _return

## Lesson failed
label math_failintro:
    play music "audio/music/mathclasstheme.ogg"
    show camembert with dissolve
    Camembert "Alright class, get your books out and keep your mouths shut."
    Camembert "The last lesson didn't seem to make its way into your little brains as well as I expected."
    Camembert "So, let's try again, shall we?"
    return

label math_failoutro:
    Camembert "Come on, [player_surname]. You can do better than that."
    Camembert "You should learn from Beatrix; she's the best in my class."
    hide camembert with dissolve
    show beatrix uniform talk with dissolve
    Beatrix "What can I say. Being smart is not for everyone."
    show jimmy suspicious with dissolve
    Jimmy "Brace yourselves, the train tracks are shaking."
    Beatrix mad "What do you mean by that..." with vpunch
    Jimmy suspicious arm "Think about it, clever girl."
    play sound "audio/sfx/mad01.ogg"
    stop music
    hide beatrix
    hide jimmy
    with dissolve
    return

## Lesson 1
label math_lesson1intro:
    call prologue_mathclassintro from _call_prologue_mathclassintro
    return

label math_lesson1outro:
    stop music
    play sound "audio/sfx/missioncomplete.ogg"
    Camembert "Good job, [player_surname]."
    Camembert "I didn't think someone could beat Beatrix in my class."
    Camembert "If you keep this up, I might start to think you have some brains."
    hide camembert with dissolve
    show beatrix uniform mad with vpunch
    play sound "audio/sfx/mad01.ogg"
    Beatrix "How'd you do that?"
    Beatrix "You have to be cheating."
    show jimmy smug with dissolve
    Jimmy "Oh, come on. Just get over the fact that I can be smart too."
    Beatrix "I'm gonna expose you, new kid."
    Jimmy unamused arm "Whatever... Y'know, I could give you some lessons if you want."
    Beatrix "Ughh..."
    play sound "audio/sfx/mad02.ogg"
    hide beatrix with vpunch
    show jimmy neutral with dissolve
    "What's her problem?"
    hide jimmy with dissolve
    return

## Lesson 2
label math_lesson2intro:
    Developer "{i}More lessons coming soon.{/i}"
    return

label math_lesson2outro:
    return
