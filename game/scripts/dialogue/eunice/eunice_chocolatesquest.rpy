default quests.euniceChocolates = LOCKED

label eunicechocolatesquest:
    if quests.euniceChocolates == LOCKED:
        jump .intro

label .intro:
    play music "audio/music/funnymoment04.ogg"
    __("{i}As [player_name] entered the cafeteria, a chubby girl stood near one of the tables, visibly flustered.{/i}")
    show eunice uniform mad left with vpunch
    Eunice "Derek! Just give them back, seriously -- those were a gift from my cousin!"
    Derek "Finders keepers, chubby cheeks!"
    play sound "audio/sfx/frustratedhum.ogg"
    Eunice "You're unbelievable! You're a thief!"
    show derek chocolate with vpunch
    Derek "Shut up, Eunice!"
    $ Eunice.met = True
    if Derek.met:
        Jimmy "*This guy again.*"
    else:
        $ Derek.met = True
    Jimmy "Come on, pal. Give her stuff back."
    Derek "Huh? Who're you, mall security?"
    Jimmy "She's scared, man. Don't you see? Why don't you go bother someone else?"
    Jimmy "Oh, shit. Camembert is coming..."
    hide derek with dissolve
    Derek "What?..."
    play sound "audio/sfx/slap.ogg"
    __("{i}As Derek turned his head to see, [player_name] plucked the box from Derek's hand while he was distracted.{/i}")
    play sound "audio/sfx/wow01.ogg"
    Eunice acting left "Wait, how did you?"
    show derek confront with vpunch
    Derek "Hey! That's not fair!"
    Jimmy "Are you going to lecture me now?"
    Jimmy "Get out of here. You're not getting this back from me."
    play sound "audio/sfx/clearthroat01.ogg"
    Derek "You stupid..."
    Derek "You know what? Let this bitch have her candy. She'll explode one of this days."
    play sound "audio/sfx/run01.ogg"
    hide derek with vpunch
    __("{i}Derek ran away before [player_name] could do anything else.{/i}")
    hide eunice
    show eunice uniform chocolate with dissolve
    __("{i}Eunice took the box, stunned. Her cheeks flushed with warmth.{/i}")
    play music MUSIC_EUNICES_THEME
    Eunice "Um… wow. Thanks."
    Jimmy "Glad to help. I'm [player_name], by the way."
    Eunice "Eunice. Thanks again, but my humor just went downhill."
    __("{i}She hesitated, clutching the box tightly.{/i}")
    play sound "audio/sfx/girlsigh01.ogg"
    Eunice "Derek is right. I shouldn't eat this. I'm too fat."
    Jimmy "Are you really going to let that guy dictate your life?"
    Jimmy "You realize he doesn't have too much brain, right?"
    Jimmy "It's not his problem what you eat or not."
    Eunice "Maybe you're right, but... Do you think I'm fat?"
    Jimmy "Well, I'm not going to say that you're skinny."
    Jimmy "But you look good and... huggable."
    play sound "audio/sfx/laugh02.ogg"
    Eunice happy "Ha, ha, ha, ha, ha! Oh my god, that's so funny." with vpunch
    Eunice "Thank you so much for making me laugh."
    Jimmy "The thing is that you shouldn't let other people make you feel bad for your body."
    Jimmy "Only you can decide what you want."
    Jimmy "Some people make fun of my height, but I don't give a fuck."
    Jimmy "I can still throw punches from down here."
    Eunice chocolate "Ha, ha, ha, you're right, [player_name]. Thank you."
    Eunice "Do you want a chocolate?"
    Jimmy "Sure, if it's one of the good ones."
    play sound "audio/sfx/giggle01.ogg"
    __("{i}Eunice giggled and offered him one from the box, then paused.{/i}")
    show eunice uniform blushed with dissolve
    Eunice "Or... I could offer you something sweeter, that can produce the same effect and serotonin as a chocolate."
    Jimmy "What could that be?"
    Eunice seductive "A kiss?"
    play sound "audio/sfx/giggle02.ogg"
    __("{i}Jimmy raised an eyebrow, half-smiling.{/i}")
    Jimmy "That's quite the upgrade from chocolate."
    stop music
    play sound "audio/sfx/weirdkiss.ogg"
    show jimmyeunicefirstkiss with vpunch
    $ renpy.pause()
    __("{i}The kiss was wet, that's for sure.{/i}")
    __("{i}She wasn't very skilled in the art of kissing, but [player_name] wasn't going to let her know upfront.{/i}")
    play sound "audio/sfx/weirdkiss.ogg"
    __("{i}He could totally feel her huge tits pressing onto him, though, so it wasn't that bad in the end.{/i}")
    __("{i}It was a kiss he was never going to forget, for sure.{/i}")
    hide jimmyeunicefirstkiss with dissolve
    play music MUSIC_EUNICES_THEME
    Jimmy "Wow, that was... different." with dissolve
    Eunice blushed "See you around, [player_name]."
    Jimmy "Yeah... sure."
    $ Eunice.relPoints += 1
    $ quests.euniceChocolates = COMPLETE
    $ EuniceDaylimit = True
    hide jimmy
    hide eunice
    with dissolve
    stop music
    call nexttime from _call_nexttime_11
    $ gotoscene('mainbuildingcafeteria')
