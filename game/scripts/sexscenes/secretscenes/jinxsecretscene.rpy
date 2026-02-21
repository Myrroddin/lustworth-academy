label jinxsecretscene:
    hide screen freeroamhud
    play music MUSIC_SEXY_THEME
    jump jinxsecretscene_menu

label jinxsecretscene_menu:
    scene jinxbackground with fade
    Jinx "Hey, handsome, wanna have some fun?"
    menu:
        "Missionary":
            Jinx "Let's fuck on the table!"
            scene jinxmissionaryanim01 with fade
            $ renpy.pause()
            jump jinxsecretscene_menu
        "Leave":
            return

image jinxmissionaryanim01:
    "jinxmissionary01"
    pause 0.1
    "jinxmissionary02"
    pause 0.1
    "jinxmissionary03"
    pause 0.1
    "jinxmissionary04"
    pause 0.1
    "jinxmissionary05"
    pause 0.1
    "jinxmissionary06"
    pause 0.1
    "jinxmissionary07"
    pause 0.1
    "jinxmissionary08"
    pause 0.1
    repeat
