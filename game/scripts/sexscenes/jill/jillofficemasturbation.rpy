label jill_officemasturbation_scene:
    scene jillmasturbationspritedoor with fade
    "[player_name] slowly opened the door."
    play music "audio/music/sexytheme02.ogg"
    scene jillmasturbationanim01 with dissolve
    Jill "Uff, yes..."
    Jill "It's been too long since I saw a cock that big."
    Jill "That fucking perv..."
    Jill "Oh, shit! I can just imagine his balls pounding against my ass."
    Jill "FUCK! I need a man so bad!"
    scene jillmasturbationdream01 with dissolve
    Jill "YES! Just shut up and fuck me, Mr. [player_surname]!"
    Jill "Your cock feels so good inside me."
    $ renpy.pause()
    Jill "I'm cumming, I'm cumming!! OHHH!"
    scene jillmasturbationcum with vpunch
    "{i}Her body shook with pleasure until she passed out.{/i}"
    if jilliangallery == True:
        call screen jilliangallery
    return

#ANIMATIONS
image jillmasturbationanim01:
    'jillmastanim01'
    pause 0.3
    'jillmastanim02'
    pause 0.3
    'jillmastanim03'
    pause 0.3
    'jillmastanim04'
    pause 0.3
    'jillmastanim05'
    pause 0.3
    'jillmastanim06'
    pause 0.3
    'jillmastanim07'
    pause 0.3
    repeat

image jillmasturbationdream01:
    'jilldreamanim01'
    pause 0.2
    'jilldreamanim02'
    pause 0.2
    'jilldreamanim03'
    pause 0.2
    'jilldreamanim04'
    pause 0.2
    'jilldreamanim05'
    pause 0.2
    'jilldreamanim06'
    pause 0.2
    'jilldreamanim07'
    pause 0.2
    repeat
