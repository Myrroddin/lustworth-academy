define derekbrute_actions = ["Attack", "Attack", "Defend", "Attack", "Attack", "Attack",]

label start_battlederekfinal:
    # 1. Create the fighter instances for this specific battle.
    $ mcfighter02 = Fighter(
        name=[bard_name],
        clique="None",
        guts=Jimmy.stats['guts'],
        wits=Jimmy.stats['wits'],
        charisma=Jimmy.stats['charisma'],
        endurance_current = Jimmy.stats['endurance'] * 100,
        endurance_max = Jimmy.stats['endurance'] * 100,
        special_current = 0,
        special_max = 10,
    )
    
    $ derekbrute = Fighter(
        name= "Derek 'The Piece of Shit'",
        clique= "Bully",
        guts=4, wits=1, charisma=1,
        endurance_current = 4 * 100,
        endurance_max = 4 * 100,
        special_current = 0,
        special_max = 10,
    )

    # 2. Tutorial Dialogue
    stop music
    scene rpgthroneroomempty with fade
    show mcfighter02_idle_anim at Transform(pos=(450, 625)) with dissolve
    call battlederekfinal(mcfighter02, derekbrute) from _call_battlederekfinal
    if _return == False:
        menu:
            __("Try again?"):
                jump start_battlederekfinal
            __("Skip"):
                jump derekdefeatedrpgending
    if _return == True:
        jump derekdefeatedrpgending

#VARIABLES

# The label now accepts 'p_fighter' and 'e_fighter' parameters to avoid scope conflicts.
label battlederekfinal(p_fighter, e_fighter):
    jump .battlestart

    label .loop:
        if e_fighter.special_current >= 10:
            $ e_fighter.special_current = 10
        if p_fighter.special_current >= 10:
            $ p_fighter.special_current = 10
        if e_fighter.endurance_current <= 0:
            jump battlederekfinal_victory
        elif p_fighter.endurance_current <= 0:
            jump battlederekfinal_defeat
        
        if player_battleturn:
            $ player_defending = False
            hide mcfighter02_defend_anim
            if player_stunned:
                "[player_name] is stunned and cannot take this turn."
                $ player_battleturn = False
                $ enemy_battleturn = True
                $ player_stunned = False
                hide mcfighter02_stunned_anim
                show mcfighter02_idle_anim at Transform(pos=(450, 625))
                jump .loop
            show mcfighter02_idle_anim at Transform(pos=(450, 625))
            call screen battle_actions_screen
            $ battlechoice = _return
            if battlechoice == "Attack":
                jump .playerattack
            elif battlechoice == "Defend":
                jump .playerdefend
            elif battlechoice == "Special":
                jump .playerspecial
        
        elif enemy_battleturn:
            $ enemy_defending = False
            hide derekbrute_defend_anim
            hide derekbrute
            show derekbrute_idle_anim at Transform(pos=(1150, 600))
            $ derekbrute_action = renpy.random.choice(derekbrute_actions)
            if e_fighter.special_current >= 6:
                jump .enemyspecial
            elif derekbrute_action == "Attack":
                jump .enemyattack
            elif derekbrute_action == "Defend":
                jump .enemydefend
        
        jump .loop

    label .battlestart:
        stop music
        play sound "audio/sfx/warhorn01.ogg"
        show derekbrute_victory_anim at Transform(pos=(-50, 550)) with vpunch
        pause 1.0
        play sound "audio/sfx/metalclang.ogg"
        Derek "You won't get in my way anymore, new kid."
        play sound "audio/sfx/shockeffect01.ogg"
        show derekbrutename with vpunch
        Derek "After I kick you ass, I'll fuck your girl too."
        $ renpy.pause()
        hide derekbrute_victory_anim
        hide derekbrutename
        play music "audio/music/epictheme04.ogg"
        $ player_battleturn = True
        show screen battle_screen(p_fighter, e_fighter)
        show mcfighter02_idle_anim at Transform(pos=(450, 625)) with dissolve 
        show derekbrute_idle_anim  at Transform(pos=(1150, 600)) with dissolve
        jump .loop

    label .playerattack:
        __("{} attacks Derek 'The Piece of Shit'!".format(player_name))
        hide mcfighter02_idle_anim
        if enemy_defending:
            hide derekbrute_idle_anim
            play sound "audio/sfx/punch01.ogg"
            show mcfighter02_attack_anim at Transform(pos=(0, 625)) with vpunch
            pause 0.1
            hide derekbrute_idle_anim
            show derekbrute_defend_anim at Transform(pos=(0, 550)) with vpunch
            play sound "audio/sfx/metalclang.ogg"
            __("Derek 'The Piece of Shit' is defending!")
            $ e_fighter.endurance_current -= ((p_fighter.guts * 2) + 30 - (e_fighter.wits * 2)) / 2
            $ p_fighter.special_current += 1
            $ e_fighter.special_current += 3
            $ renpy.pause()
            hide mcfighter02_attack_anim
            hide derekbrute_defend_anim
        else:
            play sound "audio/sfx/punch01.ogg"
            show mcfighter02_attack_anim at Transform(pos=(0, 625)) with vpunch
            pause 0.1
            hide derekbrute_idle_anim
            show derekbrute_hurt_anim at Transform(pos=(0, 600)) with vpunch
            __("Derek 'The Piece of Shit' is not defending!")
            $ e_fighter.endurance_current -= (p_fighter.guts * 2) + 30
            $ p_fighter.special_current += 1
            $ e_fighter.special_current += 1
            $ renpy.pause()
            hide mcfighter02_attack_anim
            hide derekbrute_hurt_anim
        show derekbrute_idle_anim at Transform(pos=(1150, 600))
        show mcfighter02_idle_anim at Transform(pos=(450, 625))
        $ player_battleturn = False
        $ enemy_battleturn = True
        jump .loop

    label .playerdefend:
        hide mcfighter02_idle_anim
        play sound "audio/sfx/metalclang.ogg"
        show mcfighter02_defend_anim at Transform(pos=(0, 615)) with vpunch
        __("{} is defending!".format(player_name))
        $ player_defending = True
        $ player_battleturn = False
        $ enemy_battleturn = True
        jump .loop

    label .playerspecial:
        if p_fighter.special_current >= 4:
            Jimmy "Let's get this over with..."
            if enemy_defending:
                hide mcfighter02_idle_anim
                play sound "audio/sfx/bullcharge01.ogg"
                show mcfighter02_bullcharge_anim at Transform(pos=(0, 625)) with vpunch
                pause 0.5
                play sound "audio/sfx/metalclang.ogg"
                show derekbrute_defend_anim at Transform(pos=(0, 550)) with vpunch
                __("Derek 'The Piece of Shit' is defending!")
                $ e_fighter.endurance_current -= ((p_fighter.guts * 2) + 50 - (e_fighter.wits * 2)) / 2
                $ e_fighter.special_current += 1
                $ p_fighter.special_current -= 4
                hide derekbrute_defend_anim
                show derekbrute_idle_anim at Transform(pos=(1150, 600))
                $ renpy.pause()
            else:
                hide mcfighter02_idle_anim
                play sound "audio/sfx/bullcharge01.ogg"
                show mcfighter02_bullcharge_anim at Transform(pos=(0, 625)) with vpunch
                pause 0.5
                hide derekbrute_idle_anim
                show derekbrute_hurt_anim at Transform(pos=(0, 600)) with vpunch
                __("Derek 'The Piece of Shit' is not defending!")
                $ e_fighter.endurance_current -= (p_fighter.guts * 2) + 50 - (e_fighter.wits * 2)
                $ e_fighter.special_current += 1
                $ p_fighter.special_current -= 4
                hide derekbrute_hurt_anim
                show derekbrute_idle_anim at Transform(pos=(1150, 600))
                $ renpy.pause()
        else:
            __("You don't have enough 'violence desire' to make this move.")
            jump .loop # Go back to the main loop to re-select an action
        
        hide mcfighter02_bullcharge_anim
        show mcfighter02_idle_anim at Transform(pos=(450, 625))
        $ player_battleturn = False
        $ enemy_battleturn = True
        jump .loop

    label .enemyattack:
        __("Derek 'The Piece of Shit' attacks {}!".format(player_name))
        if player_defending:
            hide derekbrute_idle_anim
            play sound "audio/sfx/rockthrow.ogg"
            show derekbrute_attack_anim at Transform(pos=(0, 600)) with vpunch
            pause 0.5
            play sound "audio/sfx/metalclang.ogg"
            show mcfighter02_defend_anim at Transform(pos=(0, 615)) with vpunch
            __("{} is defending!".format(player_name))
            $ p_fighter.endurance_current -= ((e_fighter.guts * 2) + 10 - (p_fighter.wits * 2)) / 2
            $ e_fighter.special_current += 1
            $ p_fighter.special_current += 3
            hide mcfighter02_defend_anim
            show mcfighter02_idle_anim at Transform(pos=(400, 625))
            $ renpy.pause()
        else:
            hide derekbrute_idle_anim
            play sound "audio/sfx/rockthrow.ogg"
            show derekbrute_attack_anim at Transform(pos=(0, 600)) with vpunch
            pause 0.5
            hide mcfighter02_idle_anim
            show mcfighter02_hurt_anim at Transform(pos=(0, 625)) with vpunch
            __("{} is not defending!".format(player_name))
            $ p_fighter.endurance_current -= (e_fighter.guts * 2) + 10 - (p_fighter.wits * 2)
            $ e_fighter.special_current += 1
            $ p_fighter.special_current += 1
            hide mcfighter02_hurt_anim
            show mcfighter02_idle_anim at Transform(pos=(400, 625))
            $ renpy.pause()
        hide derekbrute_attack_anim
        show derekbrute_idle_anim at Transform(pos=(1150, 600))
        $ enemy_battleturn = False
        $ player_battleturn = True
        $ player_defending = False # Reset defending status after enemy turn
        jump .loop

    label .enemydefend:
        hide derekbrute_idle_anim
        play sound "audio/sfx/metalclang.ogg"
        show derekbrute_defend_anim at Transform(pos=(0, 550)) with vpunch
        __("Derek 'The Piece of Shit' is defending!")
        $ enemy_defending = True
        $ enemy_battleturn = False
        $ player_battleturn = True
        jump .loop

    label .enemyspecial:
        Derek "Take this, bitch!"
        if player_defending:
            hide derekbrute_idle_anim
            play sound "audio/sfx/watergun.ogg"
            show derekbrute_stinkybomb_anim at Transform(pos=(0, 600)) with vpunch
            pause 0.5
            play sound "audio/sfx/metalclang.ogg"
            show mcfighter02_defend_anim at Transform(pos=(0, 615)) with vpunch
            __("{} is defending!".format(player_name))
            $ p_fighter.special_current += 1
            $ e_fighter.special_current -= 6
            $ player_stunned = True
            hide mcfighter02_defend_anim
            show mcfighter02_stunned_anim at Transform(pos=(0, 625))
            $ renpy.pause()
        else:
            hide derekbrute_idle_anim
            play sound "audio/sfx/watergun.ogg"
            show derekbrute_stinkybomb_anim at Transform(pos=(0, 600)) with vpunch
            pause 0.5
            hide mcfighter02_idle_anim
            show mcfighter02_hurt_anim at Transform(pos=(0, 625)) with vpunch
            __("{} is not defending!".format(player_name))
            $ p_fighter.endurance_current -= 10
            $ p_fighter.special_current += 1
            $ e_fighter.special_current -= 6
            $ player_stunned = True
            hide mcfighter02_hurt_anim
            show mcfighter02_stunned_anim at Transform(pos=(0, 625))
            $ renpy.pause()
        hide derekbrute_stinkybomb_anim
        show derekbrute_idle_anim at Transform(pos=(1150, 600))
        $ enemy_battleturn = False
        $ player_battleturn = True
        $ player_defending = False # Reset defending status after enemy turn
        jump .loop


# These labels are now global and can be jumped to from the battle loop.
label battlederekfinal_defeat:
    stop music
    hide screen battle_screen
    scene rpgthroneroomempty
    play sound "audio/sfx/fightlose.ogg"
    show mcfighter02_defeat_anim at Transform(pos=(0, 625)) with dissolve 
    Jimmy "Oh, crap..."
    show derekbrute_victory_anim  at Transform(pos=(0, 600)) with dissolve
    play sound "audio/sfx/slap.ogg"
    Derek "What's wrong, new kid? Too much for you?"
    return False

label battlederekfinal_victory:
    stop music
    hide screen battle_screen
    scene rpgthroneroomempty
    play sound "audio/sfx/ohnoderek.ogg"
    show derekbrute_defeat_anim at Transform(pos=(0, 600)) with dissolve
    Derek "Ahhh, fuck man... Russell will now about this."
    play sound "audio/sfx/fightvictory.ogg"
    show mcfighter02_victory_anim at Transform(pos=(0, 625)) with dissolve 
    Jimmy "Go tell your boyfriend I kicked your ass."
    return True
