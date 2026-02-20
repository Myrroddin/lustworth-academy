label spanishclass:
    hide screen freeroamhud
    scene spanishclassroomfallday
    if classes['spanish'].lesson > 2 and quests.punnyPrivateLessons == LOCKED:
        $ classes['spanish'].lesson = 2
    call subject('spanish') from _call_subject_9
    $ gotoscene('spanishclassroom', transition=fade)

label spanish_minigame:
    $ lesson = classes['spanish'].lesson
    call expression ('spanishclass_lesson' + str(lesson)) from _call_expression_8
    return _return

## Lesson failed
label spanish_failintro:
    show misspunny desk with dissolve
    Punny "Okay, clase!"
    Punny "The last lesson didn't have good results for us, so we are going to try again, okay?"
    Punny "Ven aquí, [player_name]."
    return

label spanish_failoutro:
    stop music
    play sound "audio/sfx/wrongfx.ogg"
    scene spanishclasspunny
    show misspunny desk
    with dissolve
    Punny "That isn't exactly what I was looking for..."
    Punny "That was it for today, clase."
    Punny "I hope you practice for next time, Señor [player_surname]."
    Punny "I know you can do better!"
    return

## Lesson 1
label spanish_lesson1intro:
    call prologue_spanishclassintro from _call_prologue_spanishclassintro
    return

label spanish_lesson1outro:
    scene spanishclasspunny
    show misspunny desk
    with dissolve
    stop music
    play sound "audio/sfx/missioncomplete.ogg"
    Punny standbook "¡Oh por Dios, [player_name]!"
    Punny "That was a great result."
    Punny polaroid "I knew you were as smart as you are guapo."
    "{i}Looks like something fell from the teacher's desk.{/i}"
    play sound SOUND_SEXY_INTRO
    show misspunnyunlockable01 with dissolve
    "{i}That was great, [player_name]!{/i}"
    "{i}You've unlocked an exclusive piece of art and added 1 point to your charisma stat. The benefits of being bilingual!{/i}"
    "{i}You also added 1 point to your relationship with Miss Punny.{i}"
    "{i}If you keep succeeding at her class, you'll be able to advance her story (and maybe even have a shot at that ass).{/i}"
    hide misspunnyunlockable01 with dissolve
    play sound SOUND_SCHOOL_BELL
    Punny arm "Okay class, you are dismissed!"
    return

## Lesson 2
label spanish_lesson2intro:
    scene spanishclasspunny
    show misspunny teacher neutral
    with dissolve
    play sound "audio/sfx/femaleclearthroat.ogg"
    Punny lean "Good morning, mis pequeñas calabazas."
    Punny "I hope you have practiced your Spanish."
    Punny "Today! We are going to check some VERBOS."
    Punny talk "Just like in English they are used to describe an action."
    Punny "Por ejemplo..."
    play music "audio/music/funnymoment03.ogg"
    play sound "audio/sfx/slap.ogg"
    Punny jumping "¡SALTAR!" with vpunch
    Punny lean "Oh, I almost fell on top of you, Señor [player_surname]!"
    play sound "audio/sfx/giggle01.ogg"
    Jimmy "{i}*You can fall on top of me whenever you want, Miss...*{i}"
    play sound "audio/sfx/scream01.ogg"
    Punny surprised "¡GRITAR!"
    Punny talk "Is another example of a verb in Spanish."
    with vpunch
    Punny "Alright, so, I have a better way of explaining this without causing a mess."
    Punny "Necesito ayuda from one of you..."
    Punny "Señor [player_surname]! I believe you can help us this time."
    Jimmy "I'm not that sure..."
    Punny "Yo creo en ti, venga..."
    #START OF LESSON 2 MINIGAME
    return

label spanish_lesson2outro:
    scene lesson2boardcomplete
    with fade
    stop music
    play sound "audio/sfx/missioncomplete.ogg"
    play music "audio/music/funnymoment.ogg"
    Punny "¡Oh por Dios, [player_name]!"
    Punny "The last one is a bit strange..."
    Punny "Coger means PICK UP, so..."
    Jimmy "Oh, umm, well... The guy is picking up someone else?"
    Punny "OH! Of course. For a moment I thought about something else."
    Punny "Silly of me... Right, he's helping someone to get up, right?"
    Jimmy "Yeah, exactly! He likes COGER a lot."
    Punny "Ah, that doesn't sound good, but, you did a great job!"
    scene spanishclasspunny
    show misspunny teacher neutral
    with dissolve
    play sound "audio/sfx/femaleclearthroat.ogg"
    Punny "Well, that's it for today, clase."
    Punny "Tengan una linda semana!"
    Punny "Señor [player_surname], could you come talk to me, please?"
    Jimmy "Sure..."
    Pete "Oh, man. Looks like you're in trouble."
    Pete "See you later."
    scene spanishclassmandy with fade
    show misspunny teacher neutral
    with dissolve
    play music MUSIC_MISSPUNNY_THEME
    Jimmy "Need something, Miss?"
    Punny "Oh, yes, [player_name]."
    Punny "You've been doing really well so far, cariño."
    Punny "I just wanted to tell you that I'm available if you need some private lessons to catch up."
    Jimmy "Oh, that's very nice of you, Miss."
    Punny talk "Yeah, I'm gonna be honest with you..."
    Punny "I'm offering this private classes to earn some extra money, ¿me entiendes?"
    Jimmy "Entiendo, Señorita."
    Punny "Ah! Muy bien, guapo. I think these private lessons could really help you improve your performance."
    Jimmy "Yeah, sure. Umm, how much are we talking about?"
    Punny suggestive "Umm, ¿cien la hora? A hundred dollars an hour?"
    Jimmy "Wow, I..."
    Punny talk "I understand if it's too much..."
    Jimmy "No, it's okay, Miss. Maybe I'll have to do some extra gigs, but I'm sure I can pay."
    Punny lean "Oh, [player_name]. Muchas gracias, I'll make sure to give you the best treatment, alright?"
    Jimmy "Yes, Miss. I'll let you know when I have the money."
    Punny "Esperaré con ansias, guapo."
    $ quests.punnyPrivateLessons = ACTIVE
    play sound SOUND_SCHOOL_BELL
    return
