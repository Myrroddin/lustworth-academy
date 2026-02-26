label quietsecretscene:
    hide screen freeroamhud
    play music MUSIC_SEXY_THEME
    $ entry = True
    jump quietsecretscene_menu

label quietsecretscene_menu:
    scene quietbackground with fade
    if entry:
        Developer "{i}The quality of the animations in this room will be improved in a future update.{/i}"
        $ entry = False
    menu:
        __("Anal"):
            scene quietanalanim01 with fade
            $ renpy.pause()
            jump quietsecretscene_menu
        __("Cowgirl"):
            scene quietplungeanim01 with fade
            $ renpy.pause()
            jump quietsecretscene_menu
        __("Leave"):
            return

#ANIMATIONS
image quietanalanim01:
    'quietanal01'
    pause 0.1
    'quietanal02'
    pause 0.1
    'quietanal03'
    pause 0.1
    'quietanal04'
    pause 0.1
    'quietanal05'
    pause 0.1
    repeat

image quietplungeanim01:
    'quietplunge01'
    pause 0.1
    'quietplunge02'
    pause 0.1
    'quietplunge03'
    pause 0.1
    'quietplunge04'
    pause 0.1
    'quietplunge05'
    pause 0.1
    'quietplunge06'
    pause 0.1
    repeat
