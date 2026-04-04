label beatrixhalloweengrindingquest:
    if quests.beatrixHalloweenGrinding == LOCKED:
        jump .intro
    elif quests.beatrixHalloweenGrinding == ACTIVE:
        jump .active

label .intro:
    show beatrix mavis drunk with dissolve
    Beatrix "Heeey, [player_name]. The paarteeh is gettin gud riight?"
    Jimmy "Are you okay?"
    Beatrix "Yess, neveeh better."
    Jimmy "Riiight."
    "That apple juice must have something in it. Maybe I should go taste it."
    $ quests.beatrixHalloweenGrinding = ACTIVE
    $ gotoscene('harrisonhousebar')

label .active:
    show beatrix mavis drunk with dissolve
    Jimmy "Are you sure you're okay?"
    Beatrix "Whaddyou mean? I feel {i}*hic*{/i} greaaat."
    Jimmy "Whatever you say, Beatrix."
    "There is definitely something up. I should double-check that juice."
    $ gotoscene('harrisonhousebar')
