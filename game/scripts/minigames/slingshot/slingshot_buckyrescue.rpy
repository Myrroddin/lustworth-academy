label start_buckyrescue_slingshot:
    hide window
    $ showscene('schoolgroundsjunkyard', transition=fade)
    play music "audio/music/happyrock01.ogg"
    show slingshot_gun with dissolve
    $ quick_menu = False
    $ battle_config = get_battle_config("buckyrescue")

    call screen shooter(
        initial_enemies=battle_config["enemies"],
        timer_delay=battle_config["timer_delay"],
        kill_limit=battle_config["kill_limit"],
    )
    
    $ quick_menu = True
    $ renpy.pause()
    return
