default cassidyshowerrewatch = False

label cassidy_townhouseshower_scene:
    hide screen freeroamhud
    play music "audio/music/sexytheme02.ogg"
    scene cassidyshoweranim with dissolve
    "Oh, boy. It's Cassidy."
    "Seems like she really can't get enough of those toys."
    "I wonder if she's even tried a real cock..."
    $ renpy.pause()
    "Alright, that's enough. I don't want to give her a reason to yell at me."
    stop music
    stop sound
    if prologue.complete:
        $ cassidyshowerrewatch = True
    elif cassidygallery == True:
        call screen cassidygallery
    return


#ANIMATIONS
image cassidyshoweranim:
    'cassidyshoweranim01'
    pause 0.1
    'cassidyshoweranim02'
    pause 0.1
    'cassidyshoweranim03'
    pause 0.1
    'cassidyshoweranim04'
    pause 0.1
    'cassidyshoweranim05'
    pause 0.1
    'cassidyshoweranim06'
    pause 0.1
    'cassidyshoweranim07'
    pause 0.1
    'cassidyshoweranim08'
    pause 0.1
    'cassidyshoweranim09'
    pause 0.1
    'cassidyshoweranim10'
    pause 0.1
    'cassidyshoweranim11'
    pause 0.1
    repeat