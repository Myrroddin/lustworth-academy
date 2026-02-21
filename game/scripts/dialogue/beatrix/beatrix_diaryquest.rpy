label beatrixdiaryquest:
    if quests.beatrixDiary == LOCKED:
        jump .intro
    elif quests.beatrixDiary == ACTIVE:
        jump .active
    elif quests.beatrixDiary == SATISFIED:
        jump .satisfied

label .intro:
    jump chapterone_beatrixdiaryintro

label .active:
    Jimmy talk "I'm still not sure how the fuck I'm supposed to get inside the girl's dorm to get your math notebook."
    Beatrix mad arm "Are you serious? You are hopeless."
    Beatrix "Maybe try talking to the girl sitting IN FRONT OF THE GATE."
    Jimmy "Right."
    jump beatrixdialogue.dialogmenu

label .satisfied:
    jump chapterone_beatrixlapdance
