label missdawson_fucking_scene:
    play music MUSIC_SEXY02_THEME
    scene dawsonfuckhalloween01 with fade
    play sound "audio/sfx/undress01.ogg"
    Dawson "Please, tell me you still have some of that cum in you..."
    Dawson "Now that I felt that cock in my mouth, I want to feel it in my pussy..."
    play sound "audio/sfx/mh1.ogg"
    Dawson "Please, I need you to fuck me, [player_name]"
    Jimmy "As you wish..."
    scene dawsonfuckhalloweenanimslow with fade
    play sound "audio/sfx/cowgirl01.ogg"
    Dawson "Yes, pull it inside just like that!"
    Dawson "Oh, my god! That cock feels amazing in me..."
    Dawson "This is the man I deserve. A man that can actually fuck me hard like this."
    Dawson "FUCK, [player_name]!! Please, fuck me harder!"
    menu:
        "Harder":
            jump .fast
        "Cum":
            jump .cum

label .slow:
    play sound "audio/sfx/cowgirl01.ogg"
    scene dawsonfuckhalloweenanimslow with dissolve
    Dawson "Yes, put it inside just like that!"
    Dawson "Oh, my god! That cock feels amazing in me..."
    Dawson "This is the man I deserve. A man that can actually fuck me hard like this."
    Dawson "FUCK, [player_name]!! Please, fuck me harder!"
    menu:
        "Harder":
            jump .fast
        "Cum":
            jump .cum

label .fast:
    play sound "audio/sfx/cowgirl02.ogg"
    scene dawsonfuckhalloweenanimfast with vpunch
    Dawson "YES! FUCK ME! FUCK ME! FUCK ME!"
    Dawson "That's right! Take this pussy!"
    Dawson "Pound my ass, come on!"
    Dawson "I love sitting on this hard cock, [player_name]."
    Dawson "You have been such a nice boy!"
    Dawson "Fuck, I'm almost cumming!!"
    menu:
        "Slow":
            jump .slow
        "Cum":
            jump .cum


label .cum:
    play sound "audio/sfx/cowgirlcum.ogg"
    scene dawsonfuckhalloweencum with vpunch
    Dawson "Dear lord..."
    Dawson "That was the most incredible sex I've ever had..."
    Dawson "I cannot believe I fucked a student."
    stop music
    stop sound
    if dawsongallery == True:
        call screen dawsongallery
    return

image dawsonfuckhalloweenanimslow:
    "dawsonfuckhalloweenanim01"
    pause 0.1
    "dawsonfuckhalloweenanim02"
    pause 0.1
    "dawsonfuckhalloweenanim03"
    pause 0.1
    "dawsonfuckhalloweenanim04"
    pause 0.2
    "dawsonfuckhalloweenanim05"
    pause 0.2
    "dawsonfuckhalloweenanim06"
    pause 0.1
    "dawsonfuckhalloweenanim07"
    pause 0.1
    "dawsonfuckhalloweenanim08"
    pause 0.1
    "dawsonfuckhalloweenanim09"
    pause 0.1
    repeat

image dawsonfuckhalloweenanimfast:
    "dawsonfuckhalloweenanim01"
    pause 0.08
    "dawsonfuckhalloweenanim02"
    pause 0.08
    "dawsonfuckhalloweenanim03"
    pause 0.08
    "dawsonfuckhalloweenanim04"
    pause 0.08
    "dawsonfuckhalloweenanim05"
    pause 0.08
    "dawsonfuckhalloweenanim06"
    pause 0.08
    "dawsonfuckhalloweenanim07"
    pause 0.08
    "dawsonfuckhalloweenanim08"
    pause 0.08
    "dawsonfuckhalloweenanim09"
    pause 0.08
    repeat
