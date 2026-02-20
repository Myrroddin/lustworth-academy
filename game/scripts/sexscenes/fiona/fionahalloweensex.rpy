label fiona_halloweensex_scene:
    play music MUSIC_SEXY_THEME
    scene fionahalloweensex01 with fade
    play sound "audio/sfx/giggle01.ogg"
    Fiona "What do you think, [player_name]?"
    Fiona "My pussy is craving for your cock."
    Fiona "Last time, I sucked that dick so good..."
    Fiona "But, tonight you're going to get inside me."
    play sound "audio/sfx/mh1.ogg"
    Fiona "You gonna lay down right here and I'm gonna sit hard on your dick."
    Jimmy "Oh, yes, babe. Let's do it."
    jump .slow

label .slow:
    play sound "audio/sfx/cowgirl01.ogg"
    scene fionahalloweensexanimslow with fade
    Fiona "I love how the tip of your cock stretch my lips wide!"
    Fiona "I feel like I could get and orgasm just with the tip inside."
    Fiona "But, I want it all."
    Fiona "I want this pussy to have your full cock inside."
    Fiona "So, I'm just gonna... SIT ON IT!"
    menu:
        "Harder":
            jump .fast
        "Cum":
            play sound "audio/sfx/cowgirlcum.ogg"
            Jimmy "I'm gonna cum!"
            Fiona "Me too! CUM INSIDE ME!"
            scene fionahalloweensexcum with vpunch
            Fiona "AAAGGGHHHH FUCK YES!"
            Fiona "My legs can't stop shaking."
            Fiona "That was so good."
            Fiona "I love your warm cum inside me."
            Fiona "Don't worry, I'm still on the pill."
            if fionagallery == True:
                call screen fionagallery
            return

label .fast:
    scene fionahalloweensexanimfast with vpunch
    play sound "audio/sfx/cowgirl02.ogg"
    Fiona "AAAHHH! OH MY LORD!"
    Fiona "Fuck, [player_name], you're tearing me apart!"
    Fiona "It's so up inside me."
    Fiona "I feel in heaven riding on the clouds."
    Fiona "Do you like how I sit deep on your big dick, baby?"
    Jimmy "Oh, yes, baby. Ride me!"
    Fiona "YES YES YES!"
    menu:
        "Slow down":
            jump .slow
        "Cum":
            play sound "audio/sfx/cowgirlcum.ogg"
            Jimmy "I'm gonna cum!"
            Fiona "Me too! CUM INSIDE ME!"
            scene fionahalloweensexcum with vpunch
            Fiona "AAAGGGHHHH FUCK YES!"
            Fiona "My legs can't stop shaking."
            Fiona "That was so good."
            Fiona "I love your warm cum inside me."
            Fiona "Don't worry, I'm still on the pill."
            if fionagallery == True:
                call screen fionagallery
            return
    

image fionahalloweensexanimslow:
    "fionahalloweensexanim01"
    pause 0.1
    "fionahalloweensexanim02"
    pause 0.1
    "fionahalloweensexanim03"
    pause 0.1
    "fionahalloweensexanim04"
    pause 0.1
    "fionahalloweensexanim05"
    pause 0.1
    "fionahalloweensexanim06"
    pause 0.1
    "fionahalloweensexanim07"
    pause 0.1
    "fionahalloweensexanim08"
    pause 0.1
    "fionahalloweensexanim09"
    pause 0.1
    "fionahalloweensexanim10"
    pause 0.1
    repeat

image fionahalloweensexanimfast:
    "fionahalloweensexanim01"
    pause 0.08
    "fionahalloweensexanim02"
    pause 0.08
    "fionahalloweensexanim03"
    pause 0.08
    "fionahalloweensexanim04"
    pause 0.07
    "fionahalloweensexanim05"
    pause 0.07
    "fionahalloweensexanim06"
    pause 0.06
    "fionahalloweensexanim07"
    pause 0.07
    "fionahalloweensexanim08"
    pause 0.07
    "fionahalloweensexanim09"
    pause 0.08
    "fionahalloweensexanim10"
    pause 0.08
    repeat