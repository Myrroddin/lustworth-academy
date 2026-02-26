#VARIABLES

#SCREENS
init 1 python:
    scene_defs['dakotasranch'] = {
        'music': MUSIC_DAKOTAS_RANCH,
        'altermusic': MUSIC_DAKOTAS_RANCH,
        'maps': {
            'morning': ('dakotafarmgeneralview01', 'dakotafarmgeneralview01hover'),
            'afternoon': ('dakotafarmgeneralview01after', 'dakotafarmgeneralview01afterhover'),
            'default': ('dakotafarmgeneralview01after', 'dakotafarmgeneralview01afterhover'),
        },
        'hotspots': [
            ('tree', (115, 671, 220, 301)),
            ('barn', (418, 625, 364, 295)),
            ('house', (811, 638, 409, 313)),
            ('shed', (1246, 760, 281, 203)),
            ('truck', (1528, 847, 338, 202)),
            ('lake', (1255, 530, 663, 235)),
        ],
        'sprites': [
            # Sprite(key, image, (x, y, w, h), showif)
        ]
    }

#LABELS
label dakotasranch:
    $ day4morning = (calendar.when == (PROLOGUE, SUNDAY, MORNING))
    jump dakotasranch_loop

label dakotasranch_loop:
    $ resetscene()
    call screen map('dakotasranch')
    jump dakotasranch_loop

label dakotasranch_tree:
    __("How do you like them apples?")
    jump dakotasranch_loop

label dakotasranch_barn:
    if prologue.complete:
        menu:
            __("Stack some hay(25$)"):
                if WorkDaylimit == False:
                    __("Nice work doing nothing (for now)")
                    play sound "audio/sfx/moneyget.ogg"
                    $ Jimmy.money += 25
                    call nexttime from _call_nexttime_37
                    $ WorkDaylimit = True
                    jump dakotasranch_loop
                else:
                    Jimmy "Already worked today."
                    jump dakotasranch_loop
            __("Nevermind"):
                jump dakotasranch_loop            
    elif day4morning:
        jump prologue_dakotaranchbarnintro
    else:
        __("Already did my job for the day.")
    jump dakotasranch_loop

label dakotasranch_house:
    if day4morning:
        __("I should go to the barn and do what I came to do.")
    else:
        Developer "Coming soon."
    jump dakotasranch_loop

label dakotasranch_shed:
    if prologue.complete:
        menu:
            __("Cucumber Fun (v0.40.8)"):
                $ showscene('dakotasranch', transition=fade)
                __("...I think I hear voices coming from inside the shed.")
                hide screen freeroamhud
                scene farmshedintro with fade
                play music MUSIC_SNEAK_THEME
                __("{i}The shed was packed with boxes, shelves, and tools.{/i}")
                __("{i}[player_name] followed the voices coming from the back, trying not to be heard.{/i}")
                Barbara "Come on, Sally!"
                Barbara "That cucumber looks so tasty."
                Sally "Don't rush me, Barbara. I'm really tight down there."
                __("What are they talking about?")
                __("{i}When [player_name] saw them, his eyes opened wide.{/i}")
                play sound SOUND_RECORD_SCRATCH
                call barbara_cucumberstrapon_scene from _call_barbara_cucumberstrapon_scene
                __("{i}After watching for a few more moments, [player_name] made his way out before they caught him.{/i}")
                jump dakotasranch_loop
            __("Nevermind"):
                jump dakotasranch_loop
    elif day4morning:
        __("I should go to the barn and do what I came to do.")
    else:
        __("The shed is locked.")
    jump dakotasranch_loop

label dakotasranch_truck:
    if day4morning:
        __("I didn't come all the way here to leave empty-handed.")
    else:
        menu:
            __("Leave"):
                if prologue.complete:
                    show dakota neutral with dissolve
                    Dakota "Howdy pardner. Thanks for your help today."
                    Dakota "It's gettin' late. Ready to head back?"
                    Jimmy "Yeah. I go back to class tomorrow, so I shouldn't stay out too late."
                    Dakota "Alright. Hop in my truck and I'll take ya home."
                    hide dakota with dissolve
                    hide jimmy with dissolve
                    stop music
                    hide screen freeroamhud
                    call nexttime from _call_nexttime_38
                    $ showscene('townhousefront', transition=fade)
                    pause 0.8
                    $ showscene('townhouselivingroom', transition=fade)
                    show screen freeroamhud(False)
                    $ gotoscene('townhouselivingroom')
                else:
                    jump prologue_leaveranch
            __("Stay"):
                jump dakotasranch_loop
    jump dakotasranch_loop

label dakotasranch_lake:
    __("That lake is huge.")
    __("Reminds me of San Pestillo.")
    jump dakotasranch_loop
