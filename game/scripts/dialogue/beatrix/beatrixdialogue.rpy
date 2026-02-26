#VARIABLES
default quests.beatrixDiary = LOCKED
default quests.beatrixAppleCider = LOCKED
default quests.beatrixHalloweenGrinding = LOCKED
default quests.beatrixHomework = LOCKED
default quests.beatrixHerpes = LOCKED

#LABELS
label beatrixdialogue:
    hide screen freeroamhud with None
    stop music
    $ objective = getSideObjective('beatrix', keyOnly=True)
    if objective == 'herpes_active':
        jump beatrixherpestreatment
    elif objective == 'homework_satisfied':
        jump beatrixbiologyessay
    elif objective == 'diary_locked':
        jump beatrixdiaryquest
    show jimmy neutral

    with dissolve
    if quests.beatrixHerpes <= COMPLETE:
        if quests.beatrixHerpes == ACTIVE:
            show beatrix herpes talk
        elif quests.beatrixHerpes == SATISFIED:
            show beatrix herpes talk
        else:
            show beatrix uniform talk
            Beatrix "I'm kind of busy studying quantum physics..."
            Beatrix "Oh, don't worry, I know you don't have any idea what that is."
            Beatrix "Well, do you need something?"
            jump .dialogmenu
    Beatrix "I'm kind of busy studying quantum physics..."
    Beatrix "Oh, don't worry, I know you don't have any idea what that is."
    Beatrix "Well, do you need something?"
    jump .dialogmenu

label .dialogmenu:
    menu:
        __("Reset Beatrix Get Laid Quest (v0.5.4)") if quests.beatrixGetlaid == SATISFIED or quests.beatrixHerpes == COMPLETE:
            $ Beatrix.relPoints -= 1
            $ quests.beatrixGetlaid = ACTIVE
            if Jimmy.hasItem(ItemCrownofGods):
                $ Jimmy.inventory.remove(ItemCrownofGods)
            $ showscene('schoollibrarynerdcliquehq', transition=fade)
            jump rpgcampaignintro
        __("Herpes Cream") if quests.beatrixHerpes == SATISFIED:
            jump beatrixherpestreatment
        __("\"Math notes\"") if quests.beatrixDiary in [ACTIVE, SATISFIED]:
            jump beatrixdiaryquest
        __("Lap dance") if quests.beatrixDiary == COMPLETE:
            Jimmy smug "I just wanted to... you know, relax a bit."
            Jimmy "Maybe we could just sit together, if you know what I mean."
            Beatrix "Oh, my god... You guys all think like prehistoric men, just thinking about coitus all the time."
            Beatrix "Well, I guess I owe you one. Let's get this over with."
            Jimmy "Nice."
            call beatrix_lapdance_scene from _call_beatrix_lapdance_scene
            call nexttime from _call_nexttime_5
            $ gotoscene('mainbuildingrighthallway', transition=fade)
        __("Nevermind"):
            pass
    $ gotoscene('mainbuildingrighthallway')

label beatrixhalloweendialogue:
    hide screen freeroamhud with None
    if quests.beatrixAppleCider != COMPLETE:
        jump beatrixappleciderquest
    else:
        jump beatrixhalloweengrindingquest

label beatrixmathquestreset:
    $ quests.beatrixDiary = LOCKED
    jump chapterone_beatrixdiaryintro
