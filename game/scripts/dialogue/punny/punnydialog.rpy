default moneyhelp01 = False

label misspunnydialog:
    hide screen freeroamhud with None
    play music MUSIC_MISSPUNNY_THEME
    if PunnyDaylimit == True:
        hide misspunnysprite01 with dissolve
        show misspunny desk with dissolve
        Punny "Mr. [player_surname]. I have a lot of work to do right now."
        Punny "We can talk tomorrow, maybe."
        $ gotoscene('spanishclassroom')
    elif quests.punnyDatingTeacher == SATISFIED:
        jump punnyhusbandarrival
    $ objective = getSideObjective('misspunny', keyOnly=True)
    hide misspunnysprite01 with dissolve
    show misspunny desk with dissolve
    Punny "Mr. [player_surname], ¿qué puedo hacer por usted?"
    jump .dialogmenu

label .dialogmenu:
    menu:
        "Private Lessons I (100$)" if quests.punnyPrivateLessons == ACTIVE:
            if Jimmy.money >= 100:
                jump misspunnyprivatelesson01
            else:
                "Don't have enough money, yet."
                $ gotoscene('spanishclassroom')
        "Private Lessons II (100$)" if quests.punnyPrivateLessons == COMPLETE and quests.punnyDatingTeacher == LOCKED and glob.halloweenEventComplete:
            if Jimmy.money >= 100:
                jump misspunnyprivatelesson02
            else:
                "Don't have enough money, yet."
                $ gotoscene('spanishclassroom')
        "Nevermind":
            pass
    $ gotoscene('spanishclassroom')