default quests.fionaHideAndSeek = LOCKED
default FionaWineFound = False
default FionaDonutFound = False

label fionaconfrontderekquest:
    if quests.fionaConfrontDerek == LOCKED:
        jump .intro
    elif quests.fionaConfrontDerek == ACTIVE:
        jump .active
    elif quests.fionaConfrontDerek == SATISFIED:
        jump .satisfied

label .intro:
    jump chapterone_fionaderekintro

label .active:
    if quests.fionaHideAndSeek == SATISFIED:
        jump chapterone_dereknote02
    elif quests.fionaHideAndSeek == COMPLETE:
        Jimmy "I have to find Fiona!"
        $ gotoscene('girlsdormfrontgate')
    Fiona "Hey [player_name], did you talk to Derek?"
    Jimmy "Not yet, I'm looking for him."
    Fiona "He should be somewhere around the boys' dorm."
    Fiona "Please, get him away from me."
    jump fionadialogue.dialogmenu

label .derekfight:
    if quests.fionaHideAndSeek == LOCKED:
        jump chapterone_derekhideandseekintro

label .satisfied:
    jump chapterone_dereknote02

## Derek Quest #####################################################################################

label chapterone_fionaderekintro:
    hide screen freeroamhud with None
    play music MUSIC_FIONAS_THEME
    scene fionastoreshelf with fade
    show fiona clerk altshirt with vpunch
    play sound "audio/sfx/hum01.ogg"
    Fiona "Derek has crossed the line!"
    Fiona "He creeped behind me and got his cock out asking me to suck it!"
    Jimmy "And what did you do?"
    play sound "audio/sfx/mad01.ogg"
    Fiona "Do you think I'm a whore or something?"
    Fiona "I kicked that idiot in the balls and he ripped my top off!"
    Fiona "He even took a bottle of wine I had in the fridge and a box of donuts, shit..."
    Fiona "[player_name], I'm so scared of him right now."
    Fiona "Please, [player_name]. You have to talk to him and tell him to leave me alone."
    Fiona "I'm sure you can scare him enough."
    Jimmy "Where is he?"
    play sound "audio/sfx/frustratedhum.ogg"
    Fiona "I don't know! He ran away to the boys' dorm."
    Fiona "Please, [player_name], get him off my back."
    Fiona "And if you can get my things back, well, nevermind... I just need him to leave me alone."
    Jimmy "Don't worry. I'll take care of him."
    if Derek.met:
        Jimmy "I've dealt with that bastard before."
    Fiona "Thank you, [player_name]."
    $ quests.fionaConfrontDerek = ACTIVE
    $ gotoscene('girlsdormfrontgate')

label chapterone_derekhideandseekintro:
    hide screen freeroamhud
    $ showscene('boysdormbackalley', transition=fade)
    show derek neutral with dissolve
    $ Derek.met = True
    play music "audio/music/derektheme.ogg"
    Jimmy "Hey, are you Derek?"
    Derek "What if I am, new guy?"
    Jimmy "We need to talk about Fiona."
    Derek "Oh, yeah, that hot piece."
    Derek "Have you seen her tits?"
    Derek "They're the shit, dude."
    Jimmy "Stay away from her."
    Derek confront "And what if I don't?" with vpunch
    Derek "That whore friend of yours just wants me to put my dick inside her, that's it."
    Derek "No big deal, I'm sure you understand."
    Jimmy "I'm about to knock your teeth out, pal."
    Derek "Ah, come on... This discussion is kind of boring, dude."
    Derek "Tell you what, new guy..."
    Derek "I don't want this to end up in a stupid fight."
    Derek neutral "So, I wanna play some good old hide and seek."
    Derek "Wait! Hear me out, before you say something else..." with vpunch
    Derek "I will help you find the stuff I took from her kiosk, alright?"
    Derek "And if you find them, I will call it a day and I will leave her alone."
    Derek "Besides, I already got someone else to bother, so..."
    Derek "What do you say?"
    Jimmy "It's simple, if you stay away from her, we won't have any problem."
    Jimmy "Where is her stuff?"
    Derek confront "I'll be going with you, just walk along and I will be telling you how cold or hot you're from the spot."
    Derek "Two objects, two places. Come on, let's take a walk together, like pals!"
    "Trying so hard to keep his hands from punching Derek's face, [player_name] decided to play along."
    "{i}I'll play along until I find the stolen things, [player_name] thought.{/i}"
    $ quests.fionaConfrontDerek = SATISFIED
    $ quests.fionaHideAndSeek = ACTIVE
    $ gotoscene('boysdormbackalley', transition=fade)

label chapterone_dereknote02:
    hide screen freeroamhud
    play sound "audio/sfx/run01.ogg"
    $ showscene('girlsdormfrontgate', transition=fade)
    $ renpy.pause()
    scene fionastoreshelf with fade
    Jimmy "Fuck, Fiona's not here." with vpunch
    Jimmy "Another note..."
    show dereknote02 with dissolve
    Jimmy "..."
    Jimmy "Shit, gotta get there fast!"
    $ quests.fionaHideAndSeek = COMPLETE
    jump chapterone_fionaderekconfrontation

label chapterone_fionaderekconfrontation:
    hide screen freeroamhud
    play sound "audio/sfx/run01.ogg"
    $ showscene('boysdormplaza', transition=fade)
    $ renpy.pause()
    $ showscene('boysdormbackalley', transition=fade)
    show derekfionahostage with vpunch
    play music "audio/music/derektheme.ogg"
    play sound "audio/sfx/gasp01.ogg"
    Fiona "[player_name]! Help me!"
    Derek "[player_name]! You're finally here!"
    Derek "Oh, yeah. I know your name now."
    Derek "This sexy chocolate told me everything about you..."
    Jimmy "Let her go, you piece of shit!"
    Jimmy "You really think a water gun will stop me from kicking your ass?"
    Derek "Oh, yeah, specially if it has my own piss..."
    Derek "What do you say, baby?"
    Derek "Wanna taste of Derek's golden shower?"
    play sound "audio/sfx/hum01.ogg"
    Fiona "Oh, my god, please no! That's disgusting!" with vpunch
    Jimmy "Alright, alright... Let's just talk about this."
    Fiona "What do you want from me, Derek?"
    play sound "audio/sfx/frustratedhum.ogg"
    Fiona "Just leave me alone!"
    Derek "Oh, sexy chocolate, I want a lot of things from you."
    Derek "Those tits of yours, God damn!"
    Derek "But, I also want your idiot boyfriend to see how I play with you."
    Derek "What do you say, [player_name] boy!"
    Jimmy "Let me tell you something, pal."
    Jimmy "What are you going to do after you shoot your piss at her or me?"
    Jimmy "You really think that is going to stop me from putting you down?"
    Jimmy "At this point, I'll make sure you won't be able to piss again for weeks!"
    Jimmy "And then I'll just take my girl to have a shower together and get rid of the stench."
    Jimmy "So, why don't you just think this shit through and be smart about what are you going to do next..."
    Derek "Wow, you're a real asshole, you know?"
    Derek "I'll tell you what... I'll trade the donuts and the bottle for your girlfriend."
    Derek "I mean, at least I can get something out of this."
    play sound "audio/sfx/girlsigh01.ogg"
    Fiona "Yes, you can keep that, just get your hands off me!" with vpunch
    Jimmy "Alright, you heard the lady."
    Derek "Okay, let's do this slowly..."
    "Still doubtful, Derek started to release his grip on Fiona's neck while pointing the piss gun at her."
    play music "audio/music/crazymoment01.ogg"
    show derekfionahostagedonut with vpunch
    play sound "audio/sfx/slap.ogg"
    "Suddenly, a flying donut appeared out of nowhere..."
    Derek "What the..."
    play sound "audio/sfx/big_punch.ogg"
    scene fionaderekballkick with vpunch
    Fiona "Take that, asshole!"
    Derek "Ahhhhh, fuck!"
    play sound "audio/sfx/mad02.ogg"
    Fiona "And drink your own piss!"
    Jimmy "There you go, ha, ha, ha!"
    Derek "You fucking whore!"
    scene derekfuckedup with vpunch
    play sound "audio/sfx/trashcanfall.ogg"
    Jimmy "What's the matter, pal?"
    Jimmy "Are you comfortable?"
    play sound "audio/sfx/malepain01.ogg"
    Derek "Fuck, my balls hurt..."
    Jimmy "Want some more? Or will you leave Fiona alone?"
    Derek "I will! I will... God dammit!"
    Derek "Russell will know about this, new guy!"
    Derek "Oh, yeah, you'll enter a world of pain..."
    Jimmy "Whatever, piss boy..."
    Jimmy "Let's get out of here, Fiona."
    play sound "audio/sfx/hum01.ogg"
    Fiona "Yes, [player_name]."
    stop music
    scene fionastoreshelf with fade
    show fiona clerk neutral with dissolve
    play music MUSIC_FIONAS_THEME
    play sound "audio/sfx/undress01.ogg"
    Fiona "Alright, I got my uniform back..."
    Jimmy "Well, I think he's learned his lesson."
    play sound "audio/sfx/giggle01.ogg"
    Fiona "Oh my god, [player_name]! I owe you so much..."
    Fiona "I was so scared of what he could do to me!"
    Fiona "And you also got my stuff back."
    Jimmy "Nah, it's nothing. The idiot led me right to them."
    Fiona happy "Are we going to take a shower together now?"
    Jimmy "Ha, ha, ha, sorry about that."
    Jimmy "I just tried to persuade him to let you go, you know."
    Fiona neutral "Don't worry, that was kind of smart."
    Fiona "I love how you stood up for me back there..."
    Fiona "I feel I can really count on you, you know?"
    Fiona "Here, I managed to get a couple of bucks from that asshole."
    $ Jimmy.money += 25
    call yougotmoney from _call_yougotmoney
    Fiona "I... Can you do one more thing for me?"
    Jimmy "Sure."
    Fiona "That asshole really scared me today and..."
    Fiona "I want you to..."
    stop music
    play sound "audio/sfx/sexyintro.ogg"
    Fiona aroused "Would you like to see my boobs?"
    Jimmy "Wow, that's umm..."
    Fiona "I know it's weird, but you have been good to me."
    Fiona "You actually deserve something, not like that idiot."
    Fiona "I don't know if it will make me feel better, but I want it to be my choice, not anyone else's."
    Jimmy "Girl, I would totally love to see those mermaid boobs..."
    play sound "audio/sfx/laugh01.ogg"
    Fiona happy "Ha, ha, ha, ha! You, silly..."
    Fiona "Okay, but this will only happen under one condition."
    Fiona "You won't tell anyone about it, okay?"
    play sound "audio/sfx/hum01.ogg"
    Fiona mad "If word gets to my dad, I don't know what he would do."
    Jimmy "You have my word, Fiona."
    Fiona "Thank you, [player_name]."
    Fiona "Alright, help me take this off, then."
    call fiona_kiosktitflash_scene from _call_fiona_kiosktitflash_scene_1
    scene fionastoreshelf with fade
    show fiona clerk aroused tits with dissolve
    play sound "audio/sfx/mh1.ogg"
    Fiona "This feels weird but, in some way... It's liberating."
    Fiona "I think we should get to know each other a little more."
    Jimmy "Well, I'm your unpaid intern now, remember?"
    Jimmy "So, we'll have time for that."
    play sound "audio/sfx/laugh01.ogg"
    Fiona "Ha, ha, ha, ha! Thank you, [player_name]."
    Fiona "We should go and hang out at the beach sometime!"
    play sound "audio/sfx/giggle01.ogg"
    Jimmy "I won't say no to that."
    Fiona "What about this weekend?"
    Fiona "Remember where we met?"
    Jimmy "Yeah! Near the cliffs."
    Fiona "During the evening, the sun looks beautiful on the horizon from there..."
    Jimmy "That's a date, then."
    Fiona "Great! You don't need to bring anything, alright? I'll take care of it."
    Jimmy "Alright, then." 
    Fiona "See you at the beach!"
    $ Jimmy.inventory.remove(ItemGrapeWine)
    $ Jimmy.inventory.remove(ItemDonutBox)
    $ quests.fionaConfrontDerek = COMPLETE
    $ FionaDaylimit = True
    call nexttime from _call_nexttime_29
    $ gotoscene('girlsdormfrontgate')
