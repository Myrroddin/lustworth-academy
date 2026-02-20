define thadsquire_actions = ["Attack", "Defend"]

image battletutorialbganim:
    "wrestling bg 01"
    pause 0.1
    "wrestling bg 02"
    pause 0.1
    "wrestling bg 03"
    pause 0.1
    "wrestling bg 04"
    pause 0.1
    "wrestling bg 05"
    pause 0.1
    "wrestling bg 06"
    pause 0.1
    "wrestling bg 07"
    pause 0.1
    "wrestling bg 08"
    pause 0.1
    repeat

label start_battletutorial:
    # 1. Create the fighter instances for this specific battle.
    $ mcfighter01 = Fighter(
        name=Jimmy.name,
        clique="None",
        guts=Jimmy.stats['guts'],
        wits=Jimmy.stats['wits'],
        charisma=Jimmy.stats['charisma'],
        endurance_current = Jimmy.stats['endurance'] * 100,
        endurance_max = Jimmy.stats['endurance'] * 100,
        special_current = 0,
        special_max = 10,
    )
    
    $ thadsquire = Fighter(
        name= "Thad The Squire",
        clique= "Nerd",
        guts=1, wits=3, charisma=1,
        endurance_current = 1 * 100,
        endurance_max = 1 * 100,
        special_current = 0,
        special_max = 10,
    )

    # 2. Tutorial Dialogue
    scene battletutorialbganim with fade
    show mcfighter01_idle_anim at Transform(pos=(450, 550)) with dissolve 
    show thadsquire_idle_anim  at Transform(pos=(1150, 550)) with dissolve
    "A nervous-looking kid in steps up."
    Toord "Alright, Thad, today you're going to be someone else's punching bag, as usual."
    Toord "Here's the deal, new kid."  
    Toord "Use your imagination to see how much damage you can take until you pass out."
    show battletutorialhud01 with dissolve
    Toord "Don't worry, I will use a taser to revive you."
    Thad "Uhh, do you mean our Endurance, sir?"
    Toord "Yeah, yeah, shut up, smarty pants."
    hide battletutorialhud01
    show battletutorialhud02 with dissolve
    Toord "Your Endurance is your health. If it hits zero, you're toast."
    hide battletutorialhud02
    show battletutorialhud03 with dissolve
    Toord "You also need to have a mental capacity to harvest your desire for violence."
    hide battletutorialhud03
    show battletutorialhud04 with dissolve
    Toord "This desire is basically how much you want to kick your opponents ass, and it goes up every time you make a move, either attacking or defending."
    Toord "Your opponent also charges this desire each turn, so be careful."
    Thad "That's right, my special meter bar allows me to device the best attacks I have available in my arsenal."
    Toord "This is not one of your videogames, you wimp, so shut the hell up."
    hide battletutorialhud04
    show battletutorialhud05 with dissolve
    Toord "Now, in this type of wrestling you can choose to Attack, Defend or if your desire for violence is enough, you can use an Special attack."
    Toord "Alright wimps, I'm getting tired of talking, so show those fists and start smacking each other!"
    Toord "Let's see what you got, new kid!"
    # Pass the created fighters to the battle label as arguments.
    call battletutorial(mcfighter01, thadsquire) from _call_battletutorial
    if _return == False:
        return False
    if _return == True:
        return True

#VARIABLES

#SCREENS
init 1 python:

    scene_defs['battletutorial'] = {
        'music': MUSIC_GYM_CLASS,
        'altermusic': MUSIC_GYM_CLASS,
        'maps': {
            'default':   ("battletutorialbganim", "battletutorialbganim"),
        },
        'hotspots': [
            ('', ),
        ],
        'sprites': [
            # Sprite(key, image, (x, y, w, h), showif)
        ]
    }

# The label now accepts 'p_fighter' and 'e_fighter' parameters to avoid scope conflicts.
label battletutorial(p_fighter, e_fighter):
    jump .battlestart

    label .loop:
        if e_fighter.special_current >= 10:
            $ e_fighter.special_current = 10
        if p_fighter.special_current >= 10:
            $ p_fighter.special_current = 10
        if e_fighter.endurance_current <= 0:
            jump battletutorial_victory
        elif p_fighter.endurance_current <= 0:
            jump battletutorial_defeat
        
        if player_battleturn:
            $ player_defending = False
            hide mcfighter01_defend_anim
            if player_stunned:
                "[player_name] is stunned and cannot take this turn."
                $ player_battleturn = False
                $ enemy_battleturn = True
                $ player_stunned = False
                hide mcfighter01_stunned_anim
                show mcfighter01_idle_anim at Transform(pos=(400, 550))
                jump .loop
            show mcfighter01_idle_anim at Transform(pos=(400, 550))
            call screen battle_actions_screen
            $ battlechoice = _return
            if battlechoice == "Attack":
                jump .playerattack
            elif battlechoice == "Defend":
                jump .playerdefend
            elif battlechoice == "Special":
                jump .playerspecial
        
        elif enemy_battleturn:
            hide thadsquire_defend_anim
            show thadsquire_idle_anim at Transform(pos=(1150, 550))
            $ enemy_defending = False
            $ thadsquire_action = renpy.random.choice(thadsquire_actions)
            if e_fighter.special_current >= 6:
                jump .enemyspecial
            elif thadsquire_action == "Attack":
                jump .enemyattack
            elif thadsquire_action == "Defend":
                jump .enemydefend
        
        jump .loop

    label .battlestart:
        scene battletutorialbganim with fade
        stop music
        play sound "audio/sfx/warhorn01.ogg"
        show thadsquire_victory_anim at Transform(pos=(0, 550)) with vpunch
        pause 1.0
        play sound "audio/sfx/metalclang.ogg"
        Thad "This is my chance to finally win a battle, so I'm not going to waste this opportunity."
        play sound "audio/sfx/shockeffect01.ogg"
        show thadthesquirename with vpunch
        Thad "My superior intellect shall be your doom!"
        $ renpy.pause()
        hide thadsquire_victory_anim
        hide thadthesquirename
        play music "audio/music/battlebackground01.ogg"
        $ player_battleturn = True
        show screen battle_screen(p_fighter, e_fighter)
        show mcfighter01_idle_anim at Transform(pos=(400, 550)) with dissolve 
        show thadsquire_idle_anim  at Transform(pos=(1150, 550)) with dissolve
        jump .loop

    label .playerattack:
        "[player_name] attacks Thad 'The Squire'!"
        hide mcfighter01_idle_anim
        if enemy_defending:
            hide thadsquire_idle_anim
            play sound "audio/sfx/punch01.ogg"
            show mcfighter01_attack_anim at Transform(pos=(0, 550)) with vpunch
            pause 0.1
            hide thadsquire_idle_anim
            show thadsquire_defend_anim at Transform(pos=(0, 550)) with vpunch
            play sound "audio/sfx/metalclang.ogg"
            "Thad 'The Squire' is defending!"
            $ e_fighter.endurance_current -= ((p_fighter.guts * 2) + 30 - (e_fighter.wits * 2)) / 2
            $ p_fighter.special_current += 1
            $ e_fighter.special_current += 3
            $ renpy.pause()
            hide mcfighter01_attack_anim
            hide thadsquire_defend_anim
        else:
            play sound "audio/sfx/punch01.ogg"
            show mcfighter01_attack_anim at Transform(pos=(0, 550)) with vpunch
            pause 0.1
            hide thadsquire_idle_anim
            show thadsquire_hurt_anim at Transform(pos=(0, 550)) with vpunch
            "Thad 'The Squire' is not defending!"
            $ e_fighter.endurance_current -= (p_fighter.guts * 2) + 30
            $ p_fighter.special_current += 1
            $ e_fighter.special_current += 1
            $ renpy.pause()
            hide mcfighter01_attack_anim
            hide thadsquire_hurt_anim
        show thadsquire_idle_anim at Transform(pos=(1150, 550))
        show mcfighter01_idle_anim at Transform(pos=(400, 550))
        $ player_battleturn = False
        $ enemy_battleturn = True
        jump .loop

    label .playerdefend:
        hide mcfighter01_idle_anim
        play sound "audio/sfx/metalclang.ogg"
        show mcfighter01_defend_anim at Transform(pos=(0, 550)) with vpunch
        "[player_name] is defending!"
        $ player_defending = True
        $ player_battleturn = False
        $ enemy_battleturn = True
        jump .loop

    label .playerspecial:
        if p_fighter.special_current >= 4:
            Jimmy "Let's get this over with..."
            if enemy_defending:
                hide mcfighter01_idle_anim
                play sound "audio/sfx/bullcharge01.ogg"
                show mcfighter01_bullcharge_anim at Transform(pos=(0, 550)) with vpunch
                pause 0.5
                play sound "audio/sfx/metalclang.ogg"
                show thadsquire_defend_anim at Transform(pos=(0, 550)) with vpunch
                "Thad 'The Squire' is defending!"
                $ e_fighter.endurance_current -= ((p_fighter.guts * 2) + 50 - (e_fighter.wits * 2)) / 2
                $ e_fighter.special_current += 1
                $ p_fighter.special_current -= 4
                hide thadsquire_defend_anim
                show thadsquire_idle_anim at Transform(pos=(1150, 550))
                $ renpy.pause()
            else:
                hide mcfighter01_idle_anim
                play sound "audio/sfx/bullcharge01.ogg"
                show mcfighter01_bullcharge_anim at Transform(pos=(0, 550)) with vpunch
                pause 0.5
                hide thadsquire_idle_anim
                show thadsquire_hurt_anim at Transform(pos=(0, 550)) with vpunch
                "Thad 'The Squire' is not defending!"
                $ e_fighter.endurance_current -= (p_fighter.guts * 2) + 50 - (e_fighter.wits * 2)
                $ e_fighter.special_current += 1
                $ p_fighter.special_current -= 4
                hide thadsquire_hurt_anim
                show thadsquire_idle_anim at Transform(pos=(1150, 550))
                $ renpy.pause()
        else:
            "You don't have enough 'violence desire' to make this move."
            jump .loop # Go back to the main loop to re-select an action
        
        hide mcfighter01_bullcharge_anim
        show mcfighter01_idle_anim at Transform(pos=(400, 550))
        $ player_battleturn = False
        $ enemy_battleturn = True
        jump .loop

    label .enemyattack:
        "Thad 'The Squire' attacks [player_name]!"
        if player_defending:
            hide thadsquire_idle_anim
            play sound "audio/sfx/swordslash01.ogg"
            show thadsquire_attack_anim at Transform(pos=(0, 550)) with vpunch
            pause 0.5
            play sound "audio/sfx/metalclang.ogg"
            show mcfighter01_defend_anim at Transform(pos=(0, 550)) with vpunch
            "[player_name] is defending!"
            $ p_fighter.endurance_current -= ((e_fighter.guts * 2) + 10 - (p_fighter.wits * 2)) / 2
            $ e_fighter.special_current += 1
            $ p_fighter.special_current += 3
            hide mcfighter01_defend_anim
            show mcfighter01_idle_anim at Transform(pos=(400, 550))
            $ renpy.pause()
        else:
            hide thadsquire_idle_anim
            play sound "audio/sfx/swordslash01.ogg"
            show thadsquire_attack_anim at Transform(pos=(0, 550)) with vpunch
            pause 0.5
            hide mcfighter01_idle_anim
            show mcfighter01_hurt_anim at Transform(pos=(0, 550)) with vpunch
            "[player_name] is not defending!"
            $ p_fighter.endurance_current -= (e_fighter.guts * 2) + 10 - (p_fighter.wits * 2)
            $ e_fighter.special_current += 1
            $ p_fighter.special_current += 1
            hide mcfighter01_hurt_anim
            show mcfighter01_idle_anim at Transform(pos=(400, 550))
            $ renpy.pause()
        hide thadsquire_attack_anim
        show thadsquire_idle_anim at Transform(pos=(1150, 550))
        $ enemy_battleturn = False
        $ player_battleturn = True
        $ player_defending = False # Reset defending status after enemy turn
        jump .loop

    label .enemydefend:
        hide thadsquire_idle_anim
        play sound "audio/sfx/metalclang.ogg"
        show thadsquire_defend_anim at Transform(pos=(0, 550)) with vpunch
        "Thad 'The Squire' is defending!"
        $ enemy_defending = True
        $ enemy_battleturn = False
        $ player_battleturn = True
        jump .loop

    label .enemyspecial:
        Thad "Meet your doom!"
        if player_defending:
            hide thadsquire_idle_anim
            play sound "audio/sfx/stinkybomb.ogg"
            show thadsquire_stinkybomb_anim at Transform(pos=(0, 550)) with vpunch
            pause 0.5
            play sound "audio/sfx/metalclang.ogg"
            show mcfighter01_defend_anim at Transform(pos=(0, 550)) with vpunch
            "[player_name] is defending!"
            $ p_fighter.endurance_current -= ((e_fighter.wits * 2) - (p_fighter.wits * 2)) / 2
            $ p_fighter.special_current += 1
            $ e_fighter.special_current -= 6
            $ player_stunned = True
            hide mcfighter01_defend_anim
            show mcfighter01_stunned_anim at Transform(pos=(0, 550))
            $ renpy.pause()
        else:
            hide thadsquire_idle_anim
            play sound "audio/sfx/stinkybomb.ogg"
            show thadsquire_stinkybomb_anim at Transform(pos=(0, 550)) with vpunch
            pause 0.5
            hide mcfighter01_idle_anim
            show mcfighter01_hurt_anim at Transform(pos=(0, 550)) with vpunch
            "[player_name] is not defending!"
            $ p_fighter.endurance_current -= (e_fighter.wits * 2) - (p_fighter.wits * 2)
            $ p_fighter.special_current += 1
            $ e_fighter.special_current -= 6
            $ player_stunned = True
            hide mcfighter01_hurt_anim
            show mcfighter01_stunned_anim at Transform(pos=(0, 550))
            $ renpy.pause()
        hide thadsquire_stinkybomb_anim
        show thadsquire_idle_anim at Transform(pos=(1150, 550))
        $ enemy_battleturn = False
        $ player_battleturn = True
        $ player_defending = False # Reset defending status after enemy turn
        jump .loop

# These labels are now global and can be jumped to from the battle loop.
label battletutorial_defeat:
    stop music
    hide screen battle_screen
    scene battletutorialbganim
    play sound "audio/sfx/fightlose.ogg"
    show mcfighter01_defeat_anim at Transform(pos=(0, 550)) with dissolve 
    Jimmy "Oh, crap..."
    show thadsquire_victory_anim  at Transform(pos=(0, 550)) with dissolve
    play sound "audio/sfx/metalclang.ogg"
    Thad "Try not. Do, or do not. There is no try."
    return False

label battletutorial_victory:
    stop music
    hide screen battle_screen
    scene battletutorialbganim
    play sound "audio/sfx/thadimpossible.ogg"
    show thadsquire_defeat_anim  at Transform(pos=(0, 550)) with dissolve
    Thad "NOOOOO! That's impossible!"
    play sound "audio/sfx/fightvictory.ogg"
    show mcfighter01_victory_anim at Transform(pos=(0, 550)) with dissolve 
    Jimmy "A man's got to know his limitations."
    return True