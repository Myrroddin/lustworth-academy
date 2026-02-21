label tatsumakisecretscene:
    hide screen freeroamhud
    play music MUSIC_SEXY_THEME
    $ entry = True
    jump tatsumakisecretscene_menu

label tatsumakisecretscene_menu:
    scene tatsumakiintro with fade
    if entry:
        Tatsumaki "You took your time to get here."
        Tatsumaki "I hate when someone makes me wait."
        Jimmy "Don't talk to me like that, you spoiled brat."
        $ entry = False
    menu:
        "Grinding":
            jump tatsumakisecretscene_grinding
        "Carry and fuck":
            jump tatsumakisecretscene_carryfuck
        "Leave":
            Jimmy "You'll just have to wait a little longer."
            Tatsumaki "Hmph."
            return

label tatsumakisecretscene_grinding:
    Jimmy "Come here and rub your pussy against my dick."
    Tatsumaki "How dare you?"
    Tatsumaki "I will only do it because I really enjoy it."
    scene tatsumakigrind with fade
    Tatsumaki "Hm... What do I need to do to get some cock around here?"
    Tatsumaki "Everyone is so incompetent. I have to do everything myself."
    Tatsumaki "But, I like your big cock grinding against my little pussy."
    Tatsumaki "It feels so good between my lips."
    scene tatsumakigrindcum with vpunch
    Tatsumaki "Wow, there's so much cum..."
    jump tatsumakisecretscene_menu

label tatsumakisecretscene_carryfuck:
    Jimmy "Come here."
    scene tatsumakicarryfuck1 with fade
    Tatsumaki "WHAT ARE YOU DOING?"
    Tatsumaki "You're lucky I like a big cock inside me."
    Tatsumaki "Otherwise, I would turn you into dust."
    Tatsumaki "OH MY! I hate not being in control but... FUCK, this feels so good."
    scene tatsumakicarryfuck2
    Tatsumaki "YES YES YES! PUMP ME UP!"
    scene tatsumakicarryfuckcum with vpunch
    Tatsumaki "Wow, that was really good... I still feel warm down there."
    jump tatsumakisecretscene_menu

#ANIMATIONS
image tatsumakigrind:
    'tatsumakigrind01'
    pause 0.2
    'tatsumakigrind02'
    pause 0.2
    'tatsumakigrind03'
    pause 0.2
    'tatsumakigrind04'
    pause 0.2
    'tatsumakigrind05'
    pause 0.2
    'tatsumakigrind06'
    pause 0.2
    repeat

image tatsumakicarryfuck1:
    'tatsumakicarryfuck01'
    pause 0.3
    'tatsumakicarryfuck02'
    pause 0.3
    'tatsumakicarryfuck03'
    pause 0.3
    'tatsumakicarryfuck04'
    pause 0.3
    'tatsumakicarryfuck05'
    pause 0.3
    'tatsumakicarryfuck06'
    pause 0.3
    'tatsumakicarryfuck07'
    pause 0.3
    'tatsumakicarryfuck08'
    pause 0.3
    repeat

image tatsumakicarryfuck2:
    'tatsumakicarryfuck01'
    pause 0.1
    'tatsumakicarryfuck02'
    pause 0.1
    'tatsumakicarryfuck03'
    pause 0.1
    'tatsumakicarryfuck04'
    pause 0.1
    'tatsumakicarryfuck05'
    pause 0.1
    'tatsumakicarryfuck06'
    pause 0.1
    'tatsumakicarryfuck07'
    pause 0.1
    'tatsumakicarryfuck08'
    pause 0.1
    repeat
