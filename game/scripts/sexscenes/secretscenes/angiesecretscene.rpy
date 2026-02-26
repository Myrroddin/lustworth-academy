label angiesecretscene:
    hide screen freeroamhud
    play music MUSIC_SEXY_THEME
    $ entry = True
    jump angiesecretscene_menu

label angiesecretscene_menu:
    scene angiepromo with fade
    if entry:
        Angie "Oh, [player_name]. You came."
        Angie "I'm so horny."
        $ entry = False
    menu:
        Angie "What do you want to do with my butt?"
        __("Doggy style"):
            jump angiesecretscene_doggy
        __("Anal"):
            jump angiesecretscene_anal
        __("Leave"):
            Jimmy "I'll come back sometime."
            Angie "Yes, please. I'll be here for you."
            return

label angiesecretscene_doggy:
    Jimmy "Get on all fours, baby."
    Jimmy "I want to watch that butt bounce against me."
    Angie "Ohh, yes, [player_name]."
    scene angiedoggyanimation01 with fade
    Angie "Oh, [player_name]... I know this is only the tip, but I feel my lips so stretched out."
    Angie "Let me get used to the feeling first..."
    Angie "I'm already wet down there, but I need to get used to the feel of this huge cock before going deep."
    Jimmy "Take your time, baby."
    Angie "Oh, shit..."
    Angie "I think I'm getting there..."
    Angie "Want me to start slow or fast?"
    menu:
        __("Slow"):
            jump angiesecretscene_doggy_slow
        __("Fast"):
            jump angiesecretscene_doggy_fast

label angiesecretscene_doggy_slow:
    scene angiedoggyanimation02 with dissolve
    Angie "Oh, yes..."
    Angie "I can feel every layer of my insides opening for you at this pace."
    Angie "I can feel the tip of your cock making its way to the top."
    Angie "I'm... I'm just gonna..."
    Angie "AAHHH!"
    Angie "Fuck! You fill me so good."
    menu:
        __("Faster"):
            jump angiesecretscene_doggy_fast
        __("Cum"):
            jump angiesecretscene_doggy_cum

label angiesecretscene_doggy_fast:
    scene angiedoggyanimation03 with vpunch
    Angie "OH FUCK!"
    Angie "YES! KEEP GOING!"
    Angie "Fuck, it feels so good!"
    Angie "You're gonna MAKE ME CUM!"
    Angie "AAAHHHH! FUCK YES!"
    Angie "I love how you fuck me so hard!"
    menu:
        __("Slower"):
            jump angiesecretscene_doggy_slow
        __("Cum"):
            jump angiesecretscene_doggy_cum

label angiesecretscene_doggy_cum:
    scene angiedoggycum with vpunch
    Angie "Oh my, [player_name]... That was intense."
    Angie "There's so much cum flowing inside me."
    Jimmy "That was good, baby."
    jump angiesecretscene_menu

label angiesecretscene_anal:
    Jimmy "I wannna fill your butt, baby."
    Jimmy "I want to stretch you so hard, you won't be able to sit for hours."
    Angie "Oh, yes, [player_name]."
    scene angieanalanimation01 with dissolve
    Angie "Oh, [player_name]... Be careful, please. It always hurts at first..."
    Angie "Oh, shit. Slowly, [player_name]."
    Angie "I am lubricated, but I need my little hole to get used to the feel of that big dick that is about to enter."
    Jimmy "I'll be careful, baby."
    Angie "Oh, fuck..."
    Angie "I think my ass is opening for you..."
    Jimmy "Want me to start slow or fast?"
    menu:
        __("Slow"):
            jump angiesecretscene_anal_slow
        __("Fast"):
            jump angiesecretscene_anal_fast

label angiesecretscene_anal_slow:
    scene angieanalanimation02
    Angie "Uh, take it easy, please..."
    Angie "If you go slow, my butt can open for you as much as you like."
    Angie "Your big cock can slide in and make me feel so full."
    Angie "Fuck... I can't believe I can have an orgasm through the butt..."
    Angie "OOHHH GOD!"
    Angie "My little butt is so stretched."
    menu:
        __("Faster"):
            jump angiesecretscene_anal_fast
        __("Cum"):
            jump angiesecretscene_anal_cum

label angiesecretscene_anal_fast:
    scene angieanalanimation03 with vpunch
    Angie "[player_name], just go for it!"
    Angie "OH GOD!"
    Angie "IT HURTS SO BAD!"
    Angie "BUT IT FEELS SO GOOD!"
    Angie "YES! I feel that big cock pushing my insides!"
    Angie "AAAHHHH! I LOVE IT!"
    Angie "Your cock feels so smooth in my butt!"
    menu:
        __("Slower"):
            jump angiesecretscene_anal_slow
        __("Cum"):
            jump angiesecretscene_anal_cum

label angiesecretscene_anal_cum:
    scene angieanalcum with vpunch
    Angie "Oh my, [player_name]... That was intense."
    Angie "There is so much cum in my butt."
    Jimmy "That was good, baby."
    jump angiesecretscene_menu

#ANIMATIONS
image angiedoggyanimation01:
    'angiedoggy06'
    pause 0.3
    'angiedoggy07'
    pause 0.3
    'angiedoggy08'
    pause 0.4
    'angiedoggy07'
    pause 0.4
    repeat

image angiedoggyanimation02:
    'angiedoggy06'
    pause 0.2
    'angiedoggy07'
    pause 0.2
    'angiedoggy08'
    pause 0.2
    'angiedoggy09'
    pause 0.2
    'angiedoggy01'
    pause 0.2
    'angiedoggy02'
    pause 0.2
    'angiedoggy03'
    pause 0.2
    'angiedoggy04'
    pause 0.2
    'angiedoggy05'
    pause 0.2
    repeat

image angiedoggyanimation03:
    'angiedoggy06'
    pause 0.08
    'angiedoggy07'
    pause 0.08
    'angiedoggy08'
    pause 0.08
    'angiedoggy09'
    pause 0.08
    'angiedoggy01'
    pause 0.08
    'angiedoggy02'
    pause 0.08
    'angiedoggy03'
    pause 0.08
    'angiedoggy04'
    pause 0.08
    'angiedoggy05'
    pause 0.08
    repeat

image angieanalanimation01:
    'angieanal01'
    pause 0.3
    'angieanal02'
    pause 0.3
    'angieanal03'
    pause 0.3
    'angieanal04'
    pause 0.4
    'angieanal03'
    pause 0.4
    'angieanal02'
    pause 0.4
    repeat

image angieanalanimation02:
    'angieanal01'
    pause 0.2
    'angieanal02'
    pause 0.2
    'angieanal03'
    pause 0.2
    'angieanal04'
    pause 0.2
    'angieanal05'
    pause 0.2
    'angieanal06'
    pause 0.2
    'angieanal07'
    pause 0.2
    'angieanal08'
    pause 0.2
    'angieanal09'
    pause 0.2
    'angieanal10'
    pause 0.2
    'angieanal11'
    pause 0.2
    repeat

image angieanalanimation03:
    'angieanal01'
    pause 0.08
    'angieanal02'
    pause 0.08
    'angieanal03'
    pause 0.08
    'angieanal04'
    pause 0.08
    'angieanal05'
    pause 0.08
    'angieanal06'
    pause 0.08
    'angieanal07'
    pause 0.08
    'angieanal08'
    pause 0.08
    'angieanal09'
    pause 0.08
    'angieanal10'
    pause 0.08
    'angieanal11'
    pause 0.08
    repeat
