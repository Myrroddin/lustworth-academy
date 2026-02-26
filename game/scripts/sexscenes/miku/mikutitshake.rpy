default mikutitshake01 = False
default mikutitshakenet = False

label miku_titshake_scene:
    if mikutitshakenet == True:
        jump miku_titshakenet_scene
    play music MUSIC_SEXY_THEME
    scene mikutitshakestatic with fade
    __("{i}Suddenly, Miku started to shake her body in excitement.{/i}")
    __("{i}That shirt barely left any room for imagination.{/i}")
    scene mikutitshakeanimation with dissolve
    __("{i}Just by fixing his eyes on her boobs, he could imagine those breasts dancing in the air naked.{/i}")
    __("{i}Suddenly, Miku started to shake her body in excitement.{/i}")
    __("{i}No words were necessary for the moment.{/i}")
    __("{i}[player_name] was hynotized with the movement of her boobs, just bouncing in the air like two soft ballons dancing for him.{/i}")
    __("{i}Something twitched between his legs, and at that moment, he knew he wanted to see those tits naked.{/i}")
    stop music
    $ mikutitshake01 = True
    if mikugallery == True:
        call screen mikugallery
    return

label miku_titshakenet_scene:
    play music MUSIC_SEXY_THEME
    scene mikutitshakenetanimation with fade
    __("{i}As Miku started shaking her tits in excitement,{/i}")
    __("{i}[player_name] couldn't help but think about her inclination to wear clothes that usually a stripper would.{/i}")
    __("{i}It seemed strange that she didn't mind to be that exposed.{/i}")
    __("{i}Was it natural for her to do that?{/i}")
    __("{i}What would her parents say if they saw her like this?{/i}")
    Miku "What do you think about it?"
    Jimmy "I totally love it."
    Miku "Ha, ha, thanks. I'm not sure yet about it. But, I'll keep trying new stuff until I'm sure."
    $ mikutitshakenet = False
    if mikugallery == True:
        call screen mikugallery
    return

image mikutitshakeanimation:
    'mikutitshake01'
    pause 0.1
    'mikutitshake02'
    pause 0.1
    'mikutitshake03'
    pause 0.1
    'mikutitshake04'
    pause 0.1
    'mikutitshake05'
    pause 0.1
    'mikutitshake06'
    pause 0.1
    'mikutitshake07'
    pause 0.1
    'mikutitshake08'
    pause 0.1
    'mikutitshake09'
    pause 0.1
    'mikutitshake10'
    pause 0.1
    'mikutitshake11'
    pause 0.1
    'mikutitshake12'
    pause 0.1
    'mikutitshake13'
    pause 0.1
    'mikutitshake14'
    pause 0.1
    'mikutitshake15'
    pause 0.1
    'mikutitshake16'
    pause 0.1
    'mikutitshake15'
    pause 0.1
    'mikutitshake14'
    pause 0.1
    'mikutitshake13'
    pause 0.1
    'mikutitshake12'
    pause 0.1
    'mikutitshake11'
    pause 0.1
    'mikutitshake10'
    pause 0.1
    'mikutitshake09'
    pause 0.1
    'mikutitshake08'
    pause 0.1
    'mikutitshake07'
    pause 0.1
    'mikutitshake06'
    pause 0.1
    'mikutitshake05'
    pause 0.1
    'mikutitshake04'
    pause 0.1
    'mikutitshake03'
    pause 0.1
    'mikutitshake02'
    pause 0.1
    repeat

image mikutitshakenetanimation:
    'mikutitshakenet01'
    pause 0.1
    'mikutitshakenet02'
    pause 0.1
    'mikutitshakenet03'
    pause 0.1
    'mikutitshakenet04'
    pause 0.1
    'mikutitshakenet05'
    pause 0.1
    'mikutitshakenet06'
    pause 0.1
    'mikutitshakenet07'
    pause 0.1
    'mikutitshakenet08'
    pause 0.1
    'mikutitshakenet09'
    pause 0.1
    'mikutitshakenet10'
    pause 0.1
    'mikutitshakenet11'
    pause 0.1
    'mikutitshakenet12'
    pause 0.1
    'mikutitshakenet13'
    pause 0.1
    'mikutitshakenet14'
    pause 0.1
    'mikutitshakenet15'
    pause 0.1
    'mikutitshakenet16'
    pause 0.1
    'mikutitshakenet15'
    pause 0.1
    'mikutitshakenet14'
    pause 0.1
    'mikutitshakenet13'
    pause 0.1
    'mikutitshakenet12'
    pause 0.1
    'mikutitshakenet11'
    pause 0.1
    'mikutitshakenet10'
    pause 0.1
    'mikutitshakenet09'
    pause 0.1
    'mikutitshakenet08'
    pause 0.1
    'mikutitshakenet07'
    pause 0.1
    'mikutitshakenet06'
    pause 0.1
    'mikutitshakenet05'
    pause 0.1
    'mikutitshakenet04'
    pause 0.1
    'mikutitshakenet03'
    pause 0.1
    'mikutitshakenet02'
    pause 0.1
    repeat
