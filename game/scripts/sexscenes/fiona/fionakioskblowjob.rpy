label fiona_kioskblowjob_scene:
    play music MUSIC_SEXY_THEME
    scene fionablowjobintro with fade
    play sound "audio/sfx/gasp01.ogg"
    Fiona "Oh my god! I love your cock."
    Fiona "I feel like it's going to choke me..."
    scene fionablowanimation01 with fade
    play sound "audio/sfx/mh1.ogg"
    __("{i}Suddenly, [player_name]'s cock got so hard that the tip almost inserted itself in Fiona's mouth.{/i}")
    __("{i}She stopped moving, but didn't dare to move away, and allowed his hands to take control.{/i}")
    __("{i}[player_name] felt her tongue measuring his shaft while trapped between her lips.{/i}")
    Fiona "Ough..."
    Fiona "Ishh so bighh..."
    Fiona "Umm, thass nice..."
    __("{i}Fiona was struggling with his manhood.{/i}")
    __("{i}However, with every push, she was getting the hang of it.{/i}")
    Fiona "I'mm gonnaah swaalow!"
    scene fionablowanimation02slow
    play sound "audio/sfx/bj1.ogg"
    __("{i}She finally made it all the way down his shaft.{/i}")
    __("{i}Her mouth just clenched around [player_name]'s dick and sucked exquisitely with every thrust.{/i}")
    menu:
        __("Faster"):
            jump .fast

label .slow:
    play sound "audio/sfx/gag02.ogg"
    scene fionablowanimation02slow
    $ renpy.pause()
    menu:
        __("Faster"):
            jump .fast

label .fast:
    play sound "audio/sfx/dp1.ogg"
    scene fionablowanimation02fast
    $ renpy.pause()
    menu:
        __("Slower"):
            jump .slow
        __("Finish"):
            play sound "audio/sfx/gasp01.ogg"
            jump .finish

label .finish:
    pause 0.5
    play sound "audio/sfx/cumshotone.ogg"
    scene fionablowcum with vpunch
    $ renpy.pause()
    if fionagallery == True:
        call screen fionagallery
    return

#ANIMATIONS
image fionalickanim:
    'fionalickanim01'
    pause 0.2
    'fionalickanim02'
    pause 0.2
    'fionalickanim03'
    pause 0.2
    'fionalickanim04'
    pause 0.2
    'fionalickanim05'
    pause 0.2
    'fionalickanim06'
    pause 0.2
    repeat

image fionablowanimation01:
    'fionablowanim01'
    pause 0.3
    'fionablowanim02'
    pause 0.3
    'fionablowanim03'
    pause 0.3
    'fionablowanim02'
    pause 0.3
    repeat

image fionablowanimation02slow:
    'fionablowanim01'
    pause 0.1
    'fionablowanim02'
    pause 0.1
    'fionablowanim03'
    pause 0.1
    'fionablowanim04'
    pause 0.1
    'fionablowanim05'
    pause 0.1
    'fionablowanim06'
    pause 0.1
    'fionablowanim07'
    pause 0.1
    'fionablowanim08'
    pause 0.1
    'fionablowanim09'
    pause 0.1
    'fionablowanim02'
    pause 0.1
    repeat

image fionablowanimation02fast:
    'fionablowanim01'
    pause 0.07
    'fionablowanim02'
    pause 0.07
    'fionablowanim03'
    pause 0.07
    'fionablowanim04'
    pause 0.07
    'fionablowanim05'
    pause 0.07
    'fionablowanim06'
    pause 0.07
    'fionablowanim07'
    pause 0.07
    'fionablowanim08'
    pause 0.07
    'fionablowanim09'
    pause 0.07
    'fionablowanim02'
    pause 0.07
    repeat
