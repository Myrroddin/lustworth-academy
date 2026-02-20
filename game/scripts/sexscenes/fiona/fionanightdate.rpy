label fiona_nightdate_scene:
    play music MUSIC_SEXY_THEME
    scene fionatitjobanimslow
    play sound "audio/sfx/mh1.ogg"
    Jimmy "Mmm, your those tits feel amazing around my dick, babe."
    "{i}Hearing that, Fiona redoubled her efforts to make [player_name] feel even better.{/i}"
    Fiona "Oh, yes. I can feel it getting harder."
    Jimmy "Keep at it, and it will be hard as a rock."
    Fiona "Ufff, yes, that's exactly what I want."
    Fiona "Please, don't cum yet. I want more of it."
    Jimmy "I can do this all night, baby."
    jump fionatitjobslow

label fionatitjobslow:
    play sound "audio/sfx/handjob01.ogg"
    menu:
        "Faster":
            scene fionatitjobanimfast
            $ renpy.pause()
            jump fionatitjobfast
        "Move on":
            jump fionamissionarysex

label fionatitjobfast:
    menu:
        "Slow":
            scene fionatitjobanimslow
            $ renpy.pause()
            jump fionatitjobslow
        "Move on":
            jump fionamissionarysex

label fionamissionarysex:
    play sound "audio/sfx/ah1.ogg"
    "{i}When she released him, [player_name] got up and helped Fiona take her swinsuit off.{/i}"
    "{i}Her panties were a little tight because of the wetness between her legs.{/i}"
    "{i}Fiona couldn't stop watching [player_name]'s cock with awe, is was as hard as she wanted it to be.{/i}"
    scene fionamissionarysideanim with fade
    play sound "audio/sfx/cowgirl01.ogg"
    "{i}With her eyes fixated on the manhood in front of her, she laid down in the sand and opened her legs for him.{/i}"
    Fiona "AH! FUCK!"
    Fiona "It's so hard!"
    "{i}The tip of his cock made his way inside, pushing aside the lips and going in smoothly.{/i}"
    "{i}The juiced dripping from her pussy made it all easier.{/i}"
    Fiona "Oh my god! I can feel it in my belly!"
    Fiona "Yes, baby! It feels so goood!"

label fionamissionary01:
    menu:
        "Change angle":
            scene fionamissionaryfrontanim with vpunch
            play sound "audio/sfx/cowgirl01.ogg"
            Fiona "Yes, [player_name]! Fuck me hard, please!"
            "{i}[player_name] started pushing and pulling in a perfect rythm.{/i}"
            "{i}He could feel Fiona's legs twitching every time he pushed his dick deep inside.{/i}"
            jump fionamissionary02
        "Cum":
            jump fionamissionarycum

label fionamissionary02:
    menu:
        "Change angle":
            scene fionamissionarysideanim with vpunch
            play sound "audio/sfx/cowgirl02.ogg"
            Fiona "AHHH! FUCK ME, FUCK ME, FUCK MEEEE!"
            "{i}Her moans drowned his thoughts along with the movement of her boobs shaking with every thrust.{/i}"
            jump fionamissionary01
        "Cum":
            jump fionamissionarycum
    
    
label fionamissionarycum:
    scene fionamissionary01cum with vpunch
    play sound "audio/sfx/cowgirlcum.ogg"
    "{i}Finally, she came putting her knuckles inside her mouth to silence the scream.{/i}"
    Fiona "Oh, [player_name]. That felt so good!"
    Jimmy "Your pussy is so warm, babe."
    play sound "audio/sfx/cumshotone.ogg"
    Fiona "Did you cum inside me?"
    Jimmy "Yeah, I'm sorry. It was too hot."
    Fiona "It feels like a river flowing inside me."
    Fiona "Good thing I got a contraceptive shot last week."
    Jimmy "That's great news..."
    if fionagallery == True:
        call screen fionagallery
    return

#ANIMATIONS

image fionatitjobanimslow:
    'fionatitjob01'
    pause 0.2
    'fionatitjob02'
    pause 0.2
    'fionatitjob03'
    pause 0.2
    'fionatitjob04'
    pause 0.2
    'fionatitjob05'
    pause 0.2
    'fionatitjob06'
    pause 0.2
    'fionatitjob07'
    pause 0.2
    'fionatitjob08'
    pause 0.2
    'fionatitjob09'
    pause 0.2
    'fionatitjob10'
    pause 0.2
    'fionatitjob11'
    pause 0.2
    'fionatitjob12'
    pause 0.2
    'fionatitjob13'
    pause 0.2
    'fionatitjob12'
    pause 0.2
    repeat

image fionatitjobanimfast:
    'fionatitjob01'
    pause 0.1
    'fionatitjob02'
    pause 0.1
    'fionatitjob03'
    pause 0.1
    'fionatitjob04'
    pause 0.1
    'fionatitjob05'
    pause 0.1
    'fionatitjob06'
    pause 0.1
    'fionatitjob07'
    pause 0.1
    'fionatitjob08'
    pause 0.1
    'fionatitjob09'
    pause 0.1
    'fionatitjob10'
    pause 0.1
    'fionatitjob11'
    pause 0.1
    'fionatitjob12'
    pause 0.1
    'fionatitjob13'
    pause 0.1
    'fionatitjob12'
    pause 0.1
    repeat

image fionamissionaryfrontanim:
    'fionamissionaryfront01'
    pause 0.1
    'fionamissionaryfront02'
    pause 0.1
    'fionamissionaryfront03'
    pause 0.1
    'fionamissionaryfront04'
    pause 0.1
    'fionamissionaryfront05'
    pause 0.1
    'fionamissionaryfront04'
    pause 0.1
    'fionamissionaryfront03'
    pause 0.1
    'fionamissionaryfront02'
    pause 0.1
    repeat

image fionamissionarysideanim:
    'fionamissionaryside01'
    pause 0.1
    'fionamissionaryside02'
    pause 0.1
    'fionamissionaryside03'
    pause 0.1
    'fionamissionaryside04'
    pause 0.1
    'fionamissionaryside05'
    pause 0.1
    'fionamissionaryside06'
    pause 0.1
    'fionamissionaryside07'
    pause 0.1
    'fionamissionaryside08'
    pause 0.1
    'fionamissionaryside09'
    pause 0.1
    repeat
