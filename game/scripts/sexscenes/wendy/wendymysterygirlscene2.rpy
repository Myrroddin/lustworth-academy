label wendy_mysterygirlnight2_scene:
    play music MUSIC_SEXY_THEME volume 0.2
    scene jimmyroomwendypeek with fade
    "{i}That night, [player_name] received another visit from the mysterious horny girl.{/i}"
    play sound "audio/sfx/doorknock01.ogg"
    "{i}This time, however, she knocked at the door.{/i}"
    Jimmy "Come in!"
    show jimmyroomwendypeek02 with dissolve
    play sound "audio/sfx/dooropen01.ogg"
    "{i}It seemed like she wanted to have a serious talk.{/i}"
    scene bedroomwall01 with fade
    show wendy cape hidden with dissolve
    play sound "audio/sfx/hey05.ogg"
    Wendy "Hey... Umm, I... I wanted to come here to apologize for what happened yesterday."
    Wendy "I got confused, I thought you were someone else and I just... I did stuff that I shouldn't have."
    Jimmy "Well, first of all. Nice to meet you."
    Jimmy "And, don't worry about it. I had a good time, actually."
    Wendy "You did? Oh... well, I... Can you keep this between us?"
    Jimmy "Oh, yeah. No problem."
    Wendy "It's good to hear that."
    Wendy "Well, I just wanted to say that."
    Wendy "I think... I think I'm gonna go."
    Jimmy "Wait!"
    Wendy "Yeah?"
    Jimmy "Don't tell me you came all the way here again, wearing only panties, because you wanted to just talk."
    Wendy "I... Well, I like to wear little clothing..."
    Jimmy "Little clothing? Well, that's very little, alright."
    Jimmy "Let me ask you something."
    Jimmy "Did you like what you saw last night?"
    Wendy "..."
    Wendy "I... Yes, I did."
    Jimmy "Let's be honest. You came for more."
    Jimmy "Otherwise, you wouldn't have come here, again, naked."
    Wendy "Oh my god..."
    Wendy "You're right, okay? I was curious, that's all."
    Wendy "I just really liked your cock. That's it."
    Jimmy "Now we are being honest."
    Jimmy "Well, I'm naked, you're naked. There is only one way out of this."
    "{i}She didn't hesitate anymore and took a couple of steps closer to him.{/i}"
    "{i}[player_name] sat down and showed his meat tower pointing at her.{/i}"
    "{i}She just fell for it, again.{/i}"
    scene mysteryhandjobintro with fade
    play sound "audio/sfx/giggle01.ogg"
    Wendy "Here it is."
    Wendy "It's truly the best cock I've seen."
    Jimmy "Thanks, but, can I get your name before we do this?"
    Wendy "No names. No need to know our identities."
    Wendy "I don't want to know who you are, either."
    Jimmy "Fair enough."
    Wendy "Let's try something different today, okay?"
    Jimmy "Be my guest."
    play sound "audio/sfx/mh1.ogg"
    scene mysteryrubintrosprite with fade
    Wendy "I can't risk losing my nerves like last night."
    Wendy "So, today I'm just gonna rub against it."
    Wendy "No insertion of any kind."
    Jimmy "Oh, that's a way to start, I guess."
    play sound "audio/sfx/ah1.ogg"
    scene mysteryrubnightanim1 with fade
    Wendy "Mmm... It barely fits between my lips."
    Wendy "His sausage is too big for my little bun!"
    "{i}[player_name] was trying his best to make out the girl's face in the dark.{/i}"
    "{i}The main thing he could identify, however, was her short orange hair.{/i}"
    $ renpy.pause()
    Wendy "Fuck, yes! Oh, it feels so good against my clit."
    Wendy "Let me try another position."
    play sound "audio/sfx/ah2.ogg"
    scene mysteryrubnightanim2 with fade
    Wendy "Oh fuck, yes! Mmmm..."
    "{i}[player_name] was enjoying every single movement of her incredible hips.{/i}"
    "\"She must be a cheerleader\" {i}he thought...{/i}"
    jump wendy_mysterygirlnight2_grind

label wendy_mysterygirlnight2_grind:
label .slow:
    scene mysteryrubnightanim2
    play sound "audio/sfx/ah1.ogg"
    $ renpy.pause()
    menu:
        "Faster":
            jump .fast

label .fast:
    scene mysteryrubnightanim3
    play sound "audio/sfx/ah2.ogg"
    $ renpy.pause()
    menu:
        "Slower":
            jump .slow
        "Finish":
            jump .finish

label .finish:
    play sound "audio/sfx/orgasm1.ogg"
    Wendy "YES! YES! YES! I love this big hard cock rubbing against my pussy!"
    Wendy "Oh god!"
    Wendy "I have to resist the urge to put it inside."
    Wendy "I can do it, I can do it!"
    Wendy "No, I can't. No, I can't."
    Wendy "Fuck, I want to ride this cock so badly..."
    Wendy "Fuck it, I'm gonna do it."
    jump wendy_mysterycowgirl

label wendy_mysterycowgirl:
label .slow:
    scene mysterycowgirlanimslow
    play sound "audio/sfx/cowgirl01.ogg"
    Jimmy "Holy shit..."
    Wendy "Ohhh, holy shit, indeed!"
    Wendy "This is better than I expected!"
    Wendy "YES YES YES!"
    Wendy "Let me ride it, let me ride it!"
    $ renpy.pause()
    menu:
        "Faster":
            jump .fast

label .fast:
    scene mysterycowgirlanimfast
    play sound "audio/sfx/cowgirl02.ogg"
    Wendy "Fuck, this is so good."
    Wendy "I'm cumming!"
    Jimmy "Me too!"
    Wendy "Oh, fuck. Not inside, pull it out!"
    $ renpy.pause()
    menu:
        "Slower":
            jump .slow
        "Finish":
            jump .finish

label .finish:
    stop music
    scene mysteryrubnightcumanim
    play sound "audio/sfx/cowgirlcum.ogg"
    Wendy "AAAHHH FUUUUUCK!"
    "{i}Having reached her climax, the girl remained quiet for a minute.{/i}"
    play sound "audio/sfx/gasp01.ogg"
    stop music
    Wendy "Oh my god... What did I do?"
    Wendy "I shouldn't have come here."
    scene bedroomwall01 with fade
    show wendy cape hidden pussycum with dissolve
    Wendy "I'm so sorry, this is so wrong."
    Wendy "I trust you will keep your word! Bye!"
    show wendy cape escape with vpunch
    play sound "audio/sfx/run01.ogg"
    "{i}She quickly ran for the door, again.{/i}"
    "{i}[player_name] noticed her legs were trembling on the way out.{/i}"
    play sound "audio/sfx/doorclose01.ogg"
    if wendygallery == True:
        call screen wendygallery
    return

#ANIMATIONS
image mysteryrubnightanim1:
    'mysteryrubanim01'
    pause 0.3
    'mysteryrubanim02'
    pause 0.3
    'mysteryrubanim03'
    pause 0.3
    'mysteryrubanim04'
    pause 0.3
    'mysteryrubanim03'
    pause 0.3
    'mysteryrubanim02'
    pause 0.3
    repeat

image mysteryrubnightanim2:
    'mysteryrubbinganim01'
    pause 0.2
    'mysteryrubbinganim02'
    pause 0.2
    'mysteryrubbinganim03'
    pause 0.2
    'mysteryrubbinganim04'
    pause 0.2
    'mysteryrubbinganim05'
    pause 0.2
    'mysteryrubbinganim06'
    pause 0.2
    'mysteryrubbinganim07'
    pause 0.2
    'mysteryrubbinganim08'
    pause 0.2
    repeat

image mysteryrubnightanim3:
    'mysteryrubbinganim01'
    pause 0.1
    'mysteryrubbinganim02'
    pause 0.1
    'mysteryrubbinganim03'
    pause 0.1
    'mysteryrubbinganim04'
    pause 0.1
    'mysteryrubbinganim05'
    pause 0.1
    'mysteryrubbinganim06'
    pause 0.1
    'mysteryrubbinganim07'
    pause 0.1
    'mysteryrubbinganim08'
    pause 0.1
    repeat

image mysteryrubnightcumanim:
    'mysteryrubbinganim01'
    pause 0.2
    'mysteryrubbinganim02'
    pause 0.2
    'mysteryrubbinganim03'
    pause 0.2
    'mysteryrubbinganim04'
    pause 0.2
    'mysteryrubbinganim05'
    pause 0.2
    'mysteryrubbingcum01'
    pause 0.2
    'mysteryrubbingcum02'
    pause 0.2
    'mysteryrubbingcum03'
    pause 0.2
    'mysteryrubbingcum04'
    pause 0.2

image mysterycowgirlanimslow:
    'mysterycowgirl01'
    pause 0.1
    'mysterycowgirl02'
    pause 0.1
    'mysterycowgirl03'
    pause 0.1
    'mysterycowgirl04'
    pause 0.1
    'mysterycowgirl05'
    pause 0.1
    'mysterycowgirl06'
    pause 0.1
    'mysterycowgirl07'
    pause 0.1
    'mysterycowgirl08'
    pause 0.1
    'mysterycowgirl09'
    pause 0.1
    'mysterycowgirl10'
    pause 0.1
    'mysterycowgirl11'
    pause 0.1
    repeat

image mysterycowgirlanimfast:
    'mysterycowgirl01'
    pause 0.06
    'mysterycowgirl02'
    pause 0.06
    'mysterycowgirl03'
    pause 0.06
    'mysterycowgirl04'
    pause 0.06
    'mysterycowgirl05'
    pause 0.06
    'mysterycowgirl06'
    pause 0.06
    'mysterycowgirl07'
    pause 0.06
    'mysterycowgirl08'
    pause 0.06
    'mysterycowgirl09'
    pause 0.06
    'mysterycowgirl10'
    pause 0.06
    'mysterycowgirl11'
    pause 0.06
    repeat
