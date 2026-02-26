label wendy_roominfiltration_scene:
    play music MUSIC_SEXY_THEME
    scene wendyfootjobanim01slow with fade
    play sound "audio/sfx/mh1.ogg"
    Wendy "Fuck, I love the size of your cock."
    Wendy "Look, it's larger than my foot!"
    jump .slow

label .slow:
    scene wendyfootjobanim01slow
    $ renpy.pause()
    menu:
        __("Faster"):
            play sound "audio/sfx/mh1.ogg"
            jump .fast

label .fast:
    scene wendyfootjobanim01fast
    $ renpy.pause()
    menu:
        __("Slower"):
            play sound "audio/sfx/mh1.ogg"
            jump .slow
        __("Finish"):
            jump .finish

label .finish:
    scene wendycowgirlintro
    play sound "audio/sfx/gasp01.ogg"
    Wendy "Uff, it's so hard right now!"
    Wendy "Are you ready?"
    Jimmy "Come on, sit on my cock."
    jump wendy_roominfiltration_cowgirl

label wendy_roominfiltration_cowgirl:
    scene wendycowgirlanim01slow with fade
    play sound "audio/sfx/cowgirl01.ogg"
    Wendy "I already know how it feels, but every time I think about this, it turns me on so much."
    Wendy "Oh, [player_name], thanks for coming here."
    Wendy "You sure know how to keep your word."
    jump .slow

label .slow:
    scene wendycowgirlanim01slow
    $ renpy.pause()
    menu:
        __("Faster"):
            jump .fast

label .fast:
    scene wendycowgirlanim01fast
    play sound "audio/sfx/cowgirl02.ogg"
    Jimmy "Ride me, princess."
    Wendy "OH FUCK YES!"
    Wendy "It's filling me up so much!"
    Wendy "I can feel it in my belly!"
    $ renpy.pause()
    menu:
        __("Slower"):
            jump .slow
        __("Cum inside"):
            jump .finish

label .finish:
    play sound "audio/sfx/cowgirlcum.ogg"
    Wendy "Fuck, that's so good! I'm cumming!"
    Jimmy "I'm gonna cum too!"
    Wendy "Cum inside me, [player_name]!"
    if wendygallery == True:
        call screen wendygallery
    return

#ANIMATIONS
image wendyfootjobanim01slow:
    'wendyfootjobanim01'
    pause 0.3
    'wendyfootjobanim02'
    pause 0.3
    'wendyfootjobanim03'
    pause 0.3
    'wendyfootjobanim04'
    pause 0.3
    'wendyfootjobanim05'
    pause 0.3
    'wendyfootjobanim06'
    pause 0.3
    'wendyfootjobanim07'
    pause 0.3
    'wendyfootjobanim08'
    pause 0.3
    'wendyfootjobanim09'
    pause 0.3
    'wendyfootjobanim10'
    pause 0.3
    'wendyfootjobanim11'
    pause 0.3
    'wendyfootjobanim10'
    pause 0.3
    'wendyfootjobanim09'
    pause 0.3
    'wendyfootjobanim08'
    pause 0.3
    'wendyfootjobanim07'
    pause 0.3
    'wendyfootjobanim06'
    pause 0.3
    'wendyfootjobanim05'
    pause 0.3
    'wendyfootjobanim04'
    pause 0.3
    'wendyfootjobanim03'
    pause 0.3
    'wendyfootjobanim02'
    pause 0.3
    repeat

image wendyfootjobanim01fast:
    'wendyfootjobanim01'
    pause 0.1
    'wendyfootjobanim02'
    pause 0.1
    'wendyfootjobanim03'
    pause 0.1
    'wendyfootjobanim04'
    pause 0.1
    'wendyfootjobanim05'
    pause 0.1
    'wendyfootjobanim06'
    pause 0.1
    'wendyfootjobanim07'
    pause 0.1
    'wendyfootjobanim08'
    pause 0.1
    'wendyfootjobanim09'
    pause 0.1
    'wendyfootjobanim10'
    pause 0.1
    'wendyfootjobanim11'
    pause 0.1
    'wendyfootjobanim10'
    pause 0.1
    'wendyfootjobanim09'
    pause 0.1
    'wendyfootjobanim08'
    pause 0.1
    'wendyfootjobanim07'
    pause 0.1
    'wendyfootjobanim06'
    pause 0.1
    'wendyfootjobanim05'
    pause 0.1
    'wendyfootjobanim04'
    pause 0.1
    'wendyfootjobanim03'
    pause 0.1
    'wendyfootjobanim02'
    pause 0.1
    repeat

image wendyfootjobanimcum:
    'wendyfootjobanimcum01'
    pause 0.3
    'wendyfootjobanimcum02'
    pause 0.3
    'wendyfootjobanimcum03'
    pause 0.3
    'wendyfootjobanimcum04'
    pause 0.3

image wendycowgirlanim01slow:
    'wendycowgirlanim01'
    pause 0.3
    'wendycowgirlanim02'
    pause 0.3
    'wendycowgirlanim03'
    pause 0.3
    'wendycowgirlanim04'
    pause 0.3
    'wendycowgirlanim05'
    pause 0.3
    'wendycowgirlanim06'
    pause 0.3
    'wendycowgirlanim07'
    pause 0.3
    'wendycowgirlanim08'
    pause 0.3
    repeat

image wendycowgirlanim01fast:
    'wendycowgirlanim01'
    pause 0.1
    'wendycowgirlanim02'
    pause 0.1
    'wendycowgirlanim03'
    pause 0.1
    'wendycowgirlanim04'
    pause 0.1
    'wendycowgirlanim05'
    pause 0.1
    'wendycowgirlanim06'
    pause 0.1
    'wendycowgirlanim07'
    pause 0.1
    'wendycowgirlanim08'
    pause 0.1
    repeat
