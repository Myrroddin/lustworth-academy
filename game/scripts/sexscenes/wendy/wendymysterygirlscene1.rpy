label wendy_mysterygirlnight1_scene:
    play music MUSIC_SEXY_THEME volume 0.2
    scene jimmyroomwendypeek with fade
    "{i}In the middle of the night, a figure hiding under a red cape slipped quietly into [player_name]'s room.{/i}"
    play sound "audio/sfx/dooropen01.ogg"
    show jimmyroomwendypeek02 with dissolve
    "{i}Her objective? Look for someone who didn't sleep in that room anymore.{/i}"
    "{i}The last owner of this room had left the town without notice the day before.{/i}"
    "{i}Luckily for [player_name], she didn't realize there was actually a stranger in the bed.{/i}"
    scene bedroomwall01 with fade
    show wendy cape hidden with dissolve
    play sound "audio/sfx/hey05.ogg"
    Wendy "T, are you awake?"
    "{i}\"Is she naked?\", thought [player_name]. \"Who's T?\".{/i}"
    "{i}He was curious about what she could possibly want by sneaking into his room in the middle of the night.{/i}"
    Wendy "I'm sorry for what I said, okay?"
    Wendy "I didn't really mean it."
    Wendy "It's getting harder to sneak into the boys' dorm. My Dad is starting to suspect something is wrong."
    "{i}[player_name] knew that answering would give away his real identity and scare off the lady.{/i}"
    "{i}At that moment, he wondered how far he could go on with it.{/i}"
    Wendy "Okay, I'm not gonna push you to talk to me."
    Wendy "But, at least..."
    Jimmy "..."
    Wendy "I'm gonna get closer now."
    show mysteryhandjobintro with dissolve
    play sound "audio/sfx/giggle01.ogg"
    Wendy "If you want me to leave just say it."
    Wendy "Some nights we don't talk at all and just do our thing, he, he."
    Wendy "So, it's fine by me if you just let me..."
    Wendy "Oh my god!"
    Wendy "Did you enlarge your penis overnight?"
    scene mysterygirlhandjobanim
    play sound "audio/sfx/mh1.ogg"
    Wendy "Mmm, it feels so good in my hand."
    Wendy "Like it's made perfectly for me."
    Jimmy "Uhmmm..."
    Wendy "I know you like this."
    jump wendy_mysterygirlnight1_handjob

## Handjob
label wendy_mysterygirlnight1_handjob:
label .slow:
    play sound "audio/sfx/mh1.ogg"
    scene mysterygirlhandjobslow
    $ renpy.pause()
    menu:
        "Faster":
            jump .fast

label .fast:
    play sound "audio/sfx/ah1.ogg"
    scene mysterygirlhandjobfast
    $ renpy.pause()
    menu:
        "Slower":
            jump .slow
        "Finish":
            jump .finish

label .finish:
    $ renpy.pause()
    scene mysteryhandjobend with dissolve
    play sound "audio/sfx/hmm03.ogg"
    Wendy "Wow, it's still hard!"
    Wendy "Usually my hands are enough for you to cum..."
    Wendy "I know you love when I use my mouth on this sweet cock of yours."
    scene mysteryblowjobintro with fade
    play sound "audio/sfx/bj1.ogg"
    Wendy "Here I come."
    Wendy "I hope I don't gag with this thing."
    "{i}'Oh, I hope you do', thought [player_name] while feeling her warm tongue wrapping around his manhood.{/i}"
    jump wendy_mysterygirlnight1_blowjob

## Fuck
label wendy_mysterygirlnight1_blowjob:
    label .slow:
        play sound "audio/sfx/bj1.ogg"
        scene mysteryblowjobslow
        $ renpy.pause()
        menu:
            "Faster":
                jump .fast

    label .fast:
        play sound "audio/sfx/bj4.ogg"
        scene mysteryblowjobfast
        $ renpy.pause()
        menu:
            "Slower":
                jump .slow
            "Finish":
                jump .finish

label .finish:
    scene mysteryblowjobgag with vpunch
    play sound "audio/sfx/dp1.ogg"
    Wendy "Hoggy giit! I'm gaggin!"
    Wendy "Agh! Agh! Gag! gaaahg!"
    play sound "audio/sfx/cumshotone.ogg"
    Wendy "GAAAGGGAAAAAHHHHH!" with vpunch
    scene mysteryblowjobend with vpunch
    play sound "audio/sfx/ah2.ogg"
    Wendy "Fuck! I thought I wasn't going to make it."
    "{i}Not being able to contain the excitement, [player_name] let out a moan.{/i}"
    show mysteryblowjobend02 with dissolve
    "{i}A small beam of light snuck through the door illuminating part of [player_name]'s face."
    "{i}[player_name] tried to hide under the sheets, but it was too late.{/i}"
    scene bedroomwall01 with fade
    stop music
    show wendy cape hidden cum with vpunch
    play sound "audio/sfx/gasp01.ogg"
    Wendy "T? You look different..."
    Wendy "What..."
    show wendy cape escape with vpunch
    play sound "audio/sfx/run01.ogg"
    "{i}The mysterious girl ran for the door.{/i}"
    "{i}She managed to make it out before [player_name] could see more under the cape.{/i}"
    play sound "audio/sfx/doorclose01.ogg"
    scene misterygirlshadow with vpunch
    play music "audio/music/suspensetheme01.ogg"
    "{i}However, [player_name] quickly realized there was a figure in the window.{/i}"
    "{i}Someone was watching.{/i}"
    Jimmy "Hey! Who's there!?"
    scene misterygirlshadow02 with dissolve
    "{i}The figure slowly disappeared into the blackness of the night.{/i}"
    Jimmy "What the fuck is wrong with this place?"
    if wendygallery == True:
        call screen wendygallery
    return

#ANIMATIONS
image mysterygirlhandjobanim:
    'mysteryhandjob01'
    pause 0.2
    'mysteryhandjob02'
    pause 0.2
    'mysteryhandjob03'
    pause 0.2
    'mysteryhandjob04'
    pause 0.2
    'mysteryhandjob05'
    pause 0.2
    'mysteryhandjob04'
    pause 0.2
    'mysteryhandjob03'
    pause 0.2
    'mysteryhandjob02'
    pause 0.2
    repeat

image mysterygirlhandjobslow:
    'mysteryhandjob01'
    pause 0.1
    'mysteryhandjob02'
    pause 0.1
    'mysteryhandjob03'
    pause 0.1
    'mysteryhandjob04'
    pause 0.1
    'mysteryhandjob05'
    pause 0.1
    'mysteryhandjob06'
    pause 0.1
    'mysteryhandjob07'
    pause 0.1
    'mysteryhandjob08'
    pause 0.1
    'mysteryhandjob09'
    pause 0.1
    'mysteryhandjob10'
    pause 0.1
    'mysteryhandjob09'
    pause 0.1
    'mysteryhandjob08'
    pause 0.1
    'mysteryhandjob07'
    pause 0.1
    'mysteryhandjob06'
    pause 0.1
    'mysteryhandjob05'
    pause 0.1
    'mysteryhandjob04'
    pause 0.1
    'mysteryhandjob03'
    pause 0.1
    'mysteryhandjob02'
    pause 0.1
    repeat

image mysterygirlhandjobfast:
    'mysteryhandjob01'
    pause 0.08
    'mysteryhandjob03'
    pause 0.08
    'mysteryhandjob05'
    pause 0.08
    'mysteryhandjob07'
    pause 0.08
    'mysteryhandjob09'
    pause 0.08
    'mysteryhandjob10'
    pause 0.08
    'mysteryhandjob08'
    pause 0.08
    'mysteryhandjob06'
    pause 0.08
    'mysteryhandjob04'
    pause 0.08
    'mysteryhandjob02'
    pause 0.08
    repeat

image mysteryblowjobanim:
    'mysteryblowjob01'
    pause 0.2
    'mysteryblowjob02'
    pause 0.2
    'mysteryblowjob03'
    pause 0.2
    'mysteryblowjob04'
    pause 0.2
    'mysteryblowjob05'
    pause 0.2
    'mysteryblowjob06'
    pause 0.2
    'mysteryblowjob07'
    pause 0.2
    'mysteryblowjob08'
    pause 0.2
    'mysteryblowjob09'
    pause 0.2
    repeat

image mysteryblowjobslow:
    'mysteryblowjob01'
    pause 0.1
    'mysteryblowjob02'
    pause 0.1
    'mysteryblowjob03'
    pause 0.1
    'mysteryblowjob04'
    pause 0.1
    'mysteryblowjob05'
    pause 0.1
    'mysteryblowjob06'
    pause 0.1
    'mysteryblowjob07'
    pause 0.1
    'mysteryblowjob09'
    pause 0.1
    repeat

image mysteryblowjobfast:
    'mysteryblowjob01'
    pause 0.08
    'mysteryblowjob02'
    pause 0.08
    'mysteryblowjob03'
    pause 0.08
    'mysteryblowjob04'
    pause 0.08
    'mysteryblowjob05'
    pause 0.08
    'mysteryblowjob06'
    pause 0.08
    'mysteryblowjob07'
    pause 0.08
    'mysteryblowjob09'
    pause 0.08
    repeat

image mysteryblowjobgag:
    'mysteryblowjobgag01'
    pause 0.3
    'mysteryblowjobgag02'
    pause 0.3
    repeat
