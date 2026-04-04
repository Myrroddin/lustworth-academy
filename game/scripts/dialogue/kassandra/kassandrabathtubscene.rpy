label kassandrabathtubscene:
    hide screen freeroamhud
    stop music
    play sound "audio/sfx/doorsqueak01.ogg"
    "{i}The squeaking sound of a door opening took [player_name] by surprise.{/i}"
    "{i}It came from the living room, was it possible that someone entered the house?{/i}"
    call kassandra_bathgasm_scene from _call_kassandra_bathgasm_scene_1
    $ quests.kassandraBathtubClimax = COMPLETE
    if quests.aliceScienceProject == COMPLETE and quests.antonellaBeachFun == COMPLETE and quests.blairDrunk == COMPLETE:
        hide screen freeroamhud with None
        play music MUSIC_BLAIR_THEME
        scene v0_5_5extendedpreview with fade
        $ renpy.pause()
        "{i}You have reached the end of v0.5.5 Extended Edition. Beyond this point, the game hasn't been updated.{/i}"
        "{i}Work on v0.5.6 is currently ongoing with new content for the Ranch and more content for the weekends.{/i}"
        "{i}Cheers, everyone!{/i}"
    $ gotoscene('townhousejimmysroom')
