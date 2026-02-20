label fiona_kiosktitflash_scene:
    play music MUSIC_SEXY_THEME
    scene fionatitflash00 with dissolve
    menu:
        "Off with it!":
            pass
    scene fionatitsflashanimation with dissolve
    play sound "audio/sfx/gasp01.ogg"
    $ renpy.pause()
    jump .loop

label .loop:
    menu:
        "Again?":
            scene fionatitsflashanimation with dissolve
            play sound "audio/sfx/gasp01.ogg"
            $ renpy.pause()
            jump .loop
        "Continue":
            jump .end

label .end:
    Fiona "Well? What do you think?"
    Jimmy "Fuck, they're so hot."
    Jimmy "They look even bigger on the loose."
    if fionagallery == True:
        call screen fionagallery
    return

#ANIMATIONS
image fionatitsflashanimation:
    'fionatitflash00'
    pause 0.1
    'fionatitflash01'
    pause 0.1
    'fionatitflash02'
    pause 0.1
    'fionatitflash03'
    pause 0.1
    'fionatitflash04'
    pause 0.1
    'fionatitflash05'
    pause 0.1
    'fionatitflash06'
    pause 0.1
    'fionatitflash07'
    pause 0.1
    'fionatitflash08'
    pause 0.1
    'fionatitflash09'
    pause 0.1
    'fionatitflash10'
    pause 0.1
    'fionatitflash11'
    pause 0.1
    'fionatitflash12'
    pause 0.1
    'fionatitflash13'
    pause 0.1
    'fionatitflash14'
    pause 0.1
    'fionatitflash15'
