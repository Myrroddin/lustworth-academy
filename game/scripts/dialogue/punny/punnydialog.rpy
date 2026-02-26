default moneyhelp01 = False

label misspunnydialog:
    hide screen freeroamhud with None
    play music MUSIC_MISSPUNNY_THEME
    if PunnyDaylimit == True:
        hide misspunnysprite01 with dissolve
        show misspunny desk with dissolve
        Punny "Sr. [player_surname]. I have a lot of work to do right now."
        Punny "We can talk tomorrow, maybe."
        $ gotoscene('spanishclassroom')
    elif quests.punnyDatingTeacher == SATISFIED:
        jump punnyhusbandarrival
    $ objective = getSideObjective('misspunny', keyOnly=True)
    hide misspunnysprite01 with dissolve
    show misspunny desk with dissolve
    Punny "Sr. [player_surname], ¿qué puedo hacer por usted?"
    jump .dialogmenu

label .dialogmenu:
    if Jimmy.money < 100:
        __("Don't have enough money, yet.")
        $ gotoscene('spanishclassroom')
    else:
        menu:
            __("Private Lessons I (100$)") if quests.punnyPrivateLessons == ACTIVE:
                jump misspunnyprivatelesson01
            __("Private Lessons II (100$)") if quests.punnyPrivateLessons == COMPLETE and quests.punnyDatingTeacher == LOCKED and glob.halloweenEventComplete:
                jump misspunnyprivatelesson02
            __("Nevermind"):
                pass
        $ gotoscene('spanishclassroom')
