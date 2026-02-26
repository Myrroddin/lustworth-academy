label ivanasecretscene:
    hide screen freeroamhud
    play music MUSIC_SEXY_THEME
    $ entry = True
    jump ivanasecretscene_menu

label ivanasecretscene_menu:
    scene ivanaintro with fade
    if entry:
        Ivana "Hey, [player_name]. You finally came."
        Ivana "I've been so lonely waiting for you."
        Ivana "Let's do naughty things!"
        $ entry = False
    menu:
        Ivana "I'm all yours baby..."
        __("Deep Throat"):
            jump ivanasecretscene_deepthroat
        __("Doggy style"):
            jump ivanasecretscene_doggystyle
        __("Leave"):
            Jimmy "I'll come back again later."
            Ivana "I'll be waiting, darling."
            return

label ivanasecretscene_deepthroat:
    scene ivanadeepthroatanimslow with fade
    Ivana "Oh, yes. Put it inside my mouth."
    Ivana "I'm gonna suck it so hard."
    menu:
        __("Faster"):
            jump ivanasecretscene_deepthroat_fast

label ivanasecretscene_deepthroat_slow:
    scene ivanadeepthroatanimslow
    Ivana "Oh, yes. Put it inside my mouth."
    Ivana "I'm gonna suck it so hard."
    Ivana "Ohgg my gsdhod!"
    Ivana "*Gasp* Fuck my mouth, [player_name]! Nnggguckkk"
    menu:
        __("Faster"):
            jump ivanasecretscene_deepthroat_fast
        __("Cum"):
            jump ivanasecretscene_deepthroat_cum

label ivanasecretscene_deepthroat_fast:
    scene ivanadeepthroatanimfast
    Ivana "*Gasp* Wow, [player_name]."
    Ivana "It barely fits inghgside my moughgth."
    Ivana "I caghgn't breathgghghe!"
    Ivana "*Gasp* Fuck my mouth, [player_name]! Nnggguckkk"
    menu:
        __("Slower"):
            jump ivanasecretscene_deepthroat_slow
        __("Cum"):
            jump ivanasecretscene_deepthroat_cum

label ivanasecretscene_deepthroat_cum:
    scene ivanadeepthroatcum with vpunch
    Ivana "UGhghgggg!"
    Ivana "*Coughs*"
    Ivana "I swallowed all your cum, baby!"
    Ivana "Let's do something else."
    jump ivanasecretscene_menu

label ivanasecretscene_doggystyle:
    scene ivanadoggystyleanimslow with fade
    Ivana "Yes! Fuck me from behind!."
    Ivana "It's been a long time since I had a good cock pounding my pussy."
    menu:
        __("Faster"):
            jump ivanasecretscene_doggystyle_fast

label ivanasecretscene_doggystyle_slow:
    scene ivanadoggystyleanimslow
    Ivana "YES! YES! Fuck me harder!"
    menu:
        __("Faster"):
            jump ivanasecretscene_doggystyle_fast
        __("Cum"):
            jump ivanasecretscene_doggystyle_cum

label ivanasecretscene_doggystyle_fast:
    scene ivanadoggystyleanimfast
    Ivana "OH YES! Keep going, keep going."
    Ivana "I can feel you going in and out so fast!"
    Ivana "You're pounding my butt so hard!"
    menu:
        __("Slower"):
            jump ivanasecretscene_doggystyle_slow
        __("Cum"):
            jump ivanasecretscene_doggystyle_cum

label ivanasecretscene_doggystyle_cum:
    Ivana "I'm gonna cum!"
    scene ivanadoggystylecum with vpunch
    Ivana "Holy shit! That was so good!"
    Ivana "I can't feel my buttcheeks anymore."
    Ivana "Wanna do something else?"
    jump ivanasecretscene_menu

#ANIMATIONS
image ivanadeepthroatanimslow:
    'ivanadeepthroatanim01'
    pause 0.3
    'ivanadeepthroatanim02'
    pause 0.3
    'ivanadeepthroatanim03'
    pause 0.3
    'ivanadeepthroatanim04'
    pause 0.3
    'ivanadeepthroatanim05'
    pause 0.3
    'ivanadeepthroatanim06'
    pause 0.3
    'ivanadeepthroatanim05'
    pause 0.3
    'ivanadeepthroatanim06'
    pause 0.3
    'ivanadeepthroatanim05'
    pause 0.3
    'ivanadeepthroatanim04'
    pause 0.3
    'ivanadeepthroatanim03'
    pause 0.3
    'ivanadeepthroatanim02'
    pause 0.3
    repeat

image ivanadeepthroatanimfast:
    'ivanadeepthroatanim01'
    pause 0.1
    'ivanadeepthroatanim02'
    pause 0.1
    'ivanadeepthroatanim03'
    pause 0.1
    'ivanadeepthroatanim04'
    pause 0.1
    'ivanadeepthroatanim05'
    pause 0.1
    'ivanadeepthroatanim06'
    pause 0.1
    'ivanadeepthroatanim05'
    pause 0.1
    'ivanadeepthroatanim04'
    pause 0.1
    'ivanadeepthroatanim03'
    pause 0.1
    'ivanadeepthroatanim02'
    pause 0.1
    repeat

image ivanadoggystyleanimslow:
    'ivanadoggystyleanim01'
    pause 0.2
    'ivanadoggystyleanim02'
    pause 0.2
    'ivanadoggystyleanim03'
    pause 0.2
    'ivanadoggystyleanim04'
    pause 0.2
    'ivanadoggystyleanim05'
    pause 0.2
    'ivanadoggystyleanim06'
    pause 0.2
    'ivanadoggystyleanim07'
    pause 0.2
    'ivanadoggystyleanim08'
    pause 0.2
    repeat

image ivanadoggystyleanimfast:
    'ivanadoggystyleanim01'
    pause 0.1
    'ivanadoggystyleanim02'
    pause 0.1
    'ivanadoggystyleanim03'
    pause 0.1
    'ivanadoggystyleanim04'
    pause 0.1
    'ivanadoggystyleanim05'
    pause 0.1
    'ivanadoggystyleanim06'
    pause 0.1
    'ivanadoggystyleanim07'
    pause 0.1
    'ivanadoggystyleanim08'
    pause 0.1
    repeat
