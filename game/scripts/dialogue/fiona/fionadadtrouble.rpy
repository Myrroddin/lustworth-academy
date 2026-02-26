default quest.fionaheadmastertalk = False
default prefectpass = False
default fionaLoveYou = False

label fionadadtroublequest:
    if quests.fionaDadTrouble == SATISFIED:
        if calendar.when[2] in [EVENING]:
            jump .sexscene
        else:
            __("I should wait until the evening to hide in the kiosk.")
            $ gotoscene('girlsdormfrontgate')
    elif quests.fionaDadTrouble == ACTIVE:
        if quest.fionaheadmastertalk == False:
            jump .active
        else:
            __("I need to get the headmaster office key, maybe the secretary can help me with that.")
            $ gotoscene('girlsdormfrontgate')

label .active:
    hide fionakioskdialogbutton
    show fiona clerk neutral with dissolve
    Jimmy "Hello, beautiful."
    play sound "audio/sfx/hey02.ogg"
    Fiona "[player_name]! How's it going?"
    Fiona happy "Wow, that was the best Halloween night I've ever had!"
    Fiona "I still feel my legs are a bit numb..."
    Jimmy "I had a great time, too."
    play sound "audio/sfx/giggle01.ogg"
    Fiona neutral "And I heard about your adventures around the house."
    Jimmy "Oh, what did you hear, exactly?"
    Fiona "Huh, it was really you."
    Fiona "Well, I heard you played some pranks on the preps."
    play sound "audio/sfx/hum01.ogg"
    Fiona "And Derby has an eye on you, I'm not sure why, but it seems you need to watch yourself."
    Jimmy "Well, the ideas weren't mine."
    Jimmy "Gary was the mastermind, he blackmailed me after knowing I got inside the girls dorm without permission."
    Fiona "Gary? Gary... Doesn't ring a bell... OH! GARY!"
    play sound "audio/sfx/frustratedhum.ogg"
    Fiona mad "Oh, [player_name], you shouldn't hang out with that psycho."
    Fiona "He's a really weird guy. I don't like him."
    Jimmy "Don't worry. I got it under control."
    Fiona "News fly very fast in this place, [player_name]."
    play sound "audio/sfx/girlsigh01.ogg"
    Fiona "You need to watch your back. I don't want anything bad happening to you."
    Fiona "I care about you."
    Jimmy "Thank you, I appreciate it, a lot."
    Jimmy "And don't worry, I can take care of myself."
    Fiona "I know, babe."
    play music MUSIC_DAWSONS_THEME
    show missdawson neutral with vpunch
    play sound "audio/sfx/femaleclearthroat.ogg"
    Dawson "Good day, Miss Stapleneck."
    Dawson "Oh, you're here too, Mr. [player_surname]."
    Dawson "Good thing I don't have to look for you."
    Dawson talk "Miss Stapleneck, your father, the headmaster, wants to talk to you in his office."
    Dawson talk arm "He also wants to see you, Mr. [player_surname]."
    play sound "audio/sfx/hmm01.ogg"
    Fiona "Why doesn't my dad comes to find me himself? He sends his assistant to talk with his daughter?"
    Dawson unamused point "Mr. Stapleneck is a very busy man, darling. He is wainting for you, both, in his office. Now come, please."
    play sound "audio/sfx/mad01.ogg"
    Fiona "Fine, but, we'll go... ON OUR OWN."
    Dawson "As you wish, I have other things to do."
    play sound "audio/sfx/highheels.ogg"
    __("{i}Fiona grabbed [player_name]'s hand and they both made their way to the headmaster's office.{/i}")
    $ showscene('mainbuildingsecretarysoffice', transition=fade)
    play music MUSIC_HEADMASTERS_THEME
    show fiona clerk mad with dissolve
    play sound "audio/sfx/frustratedhum.ogg"
    Fiona "Ugh... I avoid talking to him most of the time."
    Jimmy "I've had problems with my dad, too."
    Jimmy "It's normal to have different views on stuff."
    play sound "audio/sfx/hum01.ogg"
    Fiona "You don't undertand. This is different."
    Fiona "Our conflict is... unsolvable."
    Jimmy "I can go first, if you need more time."
    play sound "audio/sfx/girlsigh01.ogg"
    Fiona "Yes, please do. Thank you."
    Fiona "By the way, don't mention anything about us."
    Fiona "It could be a problem."
    Jimmy "Why would I do that? Don't worry."
    play sound "audio/sfx/dooropen01.ogg"
    $ showscene('mainbuildingheadmaster', transition=fade)
    show stapleneck arm with dissolve
    pause 1.0
    play sound "audio/sfx/clearthroat01.ogg"
    Stapleneck talk "Ah! Yes, you're here now."
    Stapleneck "Take a seat."
    __("{i}The headmaster sat down in his chair with his face reddening with anger.{/i}")
    scene stapleneckdiscussion with fade
    Stapleneck "I wanted to talk to you about recent activities. I've heard some reports that you were involved in some inappropriate behavior during Halloween festivities."
    Stapleneck "Do you have something to say about that?"
    Jimmy "I'm not sure of what you are accusing me of."
    Stapleneck "Were you involved in the incident with the flag?"
    Jimmy "..."
    Stapleneck "What about the graffiti drawn next to the Jacuzzi..."
    __("{i}[player_name] already knew that the headmaster wasn't going to believe anything he said.{/i}")
    play sound "audio/sfx/clearthroat01.ogg"
    Stapleneck "I must remind you that you are a representative, whether you want it or not, of this school."
    Stapleneck "Your behavior reflects on the reputation of this academy, and I expect you to act accordingly."
    Stapleneck "There is not concrete evidence, so I cannot press clear charges against you."
    Stapleneck "Miss Gauthier, who is still in shock for what happened in her bedroom, didn't confess anything, either."
    Stapleneck "She decided not to press any charges against you, even after Mister Derby Harrison pleaded her to do it."
    Stapleneck "However, I want you to stop this nonsense and I want you to behave yourself."
    Stapleneck "This is your FIRST warning and I will write to your parents about this."
    Jimmy "Fine, can I go now?... Sir?"
    play sound "audio/sfx/clearthroat01.ogg"
    Stapleneck "Go on, now. I need to talk to my daughter."
    scene laterthatday with fade
    pause 1.0
    call nexttime from _call_nexttime_14
    $ showscene('mainbuildingentrance', transition=fade)
    show fiona clerk mad with vpunch
    play sound "audio/sfx/mad01.ogg"
    Fiona "That was so unfair! He is so patronizing!"
    Fiona "I can't believe he took my permit away! He's such a control freak!"
    Fiona "I'm not gonna stand here and let him walk over me."
    Jimmy "Fiona, take it easy. You might pass out of anger."
    play sound "audio/sfx/mad02.ogg"
    Fiona "I need that permit. If I can't work here in the school, I will go somewhere else."
    Fiona "Please, [player_name]. You have to help me."
    Jimmy "Listen, let's go to a less crowded place and we can talk about it, alright?"
    play sound "audio/sfx/girlsigh01.ogg"
    Fiona "Good idea."
    $ showscene('girlsdormfrontgate', transition=fade)
    hide fionakioskdialogbutton
    show fiona clerk mad with vpunch
    play music MUSIC_FIONAS_THEME
    Fiona "..."
    Jimmy "You need to think about what you want to do."
    Jimmy "If you go and take the permit, he will find out anyways."
    play sound "audio/sfx/femaleclearthroat.ogg"
    Fiona neutral "You're right, but without that permit, I can't sell anything here or in town."
    Fiona "My dad helped me get that permit from the Mayor."
    Fiona "If I recover it, he will make me close the kiosk, but I can use it to sell stuff somewhere else where he doesn't have a jurisdiction."
    Fiona "If I don't recover it, I will close the kiosk anyways and I won't be able to win enough money with an underpaid job somewhere else."
    Jimmy "Mhmm, I shouldn't look for more trouble, but I hate seeing you like this."
    Jimmy "What's your plan?"
    play sound "audio/sfx/girlsigh01.ogg"
    Fiona "During the night, the only one left inside the main building is the concierge."
    Fiona "It is a good chance to get inside my dad's office."
    Fiona "But, we need the key to the office and that key is in Dawson's hands."
    Jimmy "The assistant?"
    Fiona "Exactly."
    if quest.missdawsondeepdone == True:
        play sound "audio/sfx/clearthroat01.ogg"
        Jimmy "Well, what if I tell you I already have the key."
        play sound "audio/sfx/gasp01.ogg"
        Fiona "No way..."
        Jimmy "I got it by... accident. I believe she's still not aware that I have it."
        Jimmy "So, if we are going to use it, we need to do it quickly."
        Jimmy "Before she remembers I have the key."
        play sound "audio/sfx/gasp02.ogg"
        Fiona "Oh my god, [player_name]."
        $ quests.fionaDadTrouble = SATISFIED
    else:
        play sound "audio/sfx/frustratedhum.ogg"
        Fiona "There is no way I can get the key from her."
        Fiona "She doesn't trust me."   
        Fiona "However, you could find a way to get close to her."
        play sound "audio/sfx/femaleclearthroat.ogg"
        Fiona "I mean, not that close, but, you know what I mean."
        Jimmy "Right."
    Fiona "Bring me the key during the evening and we can hide in the kiosk to avoid the monitors."
    Fiona "You can hide until it's safe to get in there at night."
    Jimmy "Alright, I'll come back with the key."
    play sound "audio/sfx/girlsigh01.ogg"
    Fiona "I know, babe."
    $ quest.fionaheadmastertalk = True
    $ FionaDaylimit = True
    $ gotoscene('girlsdormfrontgate')

label .satisfied:
    Fiona "[player_name]! How's it going?"
    play sound "audio/sfx/surprisedhum.ogg"
    Fiona "Any progress on our mission?"
    Jimmy "I'm working on it. But it will be done, don't worry."
    play sound "audio/sfx/girlsigh01.ogg"
    Fiona "I know, [player_name]. I trust you."
    $ gotoscene('girlsdormfrontgate')

label .sexscene:
    play sound "audio/sfx/clearthroat01.ogg"
    Jimmy "Fiona! I'm ready. Here's the key."
    play sound "audio/sfx/gasp01.ogg"
    Fiona "YES! Thank you so much, [player_name]."
    Fiona "We need to wait until late at night, it's the best time to sneak in."
    play sound "audio/sfx/hmm01.ogg"
    Fiona "I have a prefect pass, but you don't, so you need to hide inside the kiosk until then."
    Jimmy "Well, I will spending time with you, so I don't mind."
    scene laterthatday with fade
    pause 1.0
    $ renpy.pause()
    stop music
    scene fionateasingkiosk with fade
    play sound "audio/sfx/sexyintro.ogg"
    Jimmy "Uff, I could really get used to this..."
    play sound "audio/sfx/laugh01.ogg"
    Fiona "Ha, ha, ha, you, silly."
    play sound "audio/sfx/mh1.ogg"
    scene fionateasingkiosk02 with dissolve
    Fiona "This is all yours, babe."
    Jimmy "I know."
    scene laterthatday with fade
    pause 1.0
    $ renpy.pause()
    call nexttime from _call_nexttime_53
    $ showscene('girlsdormfrontgate', transition=fade)
    hide fionakioskdialogbutton
    play music MUSIC_SNEAK_THEME
    show fiona clerk happy with dissolve
    play sound "audio/sfx/hum01.ogg"
    Fiona "Okay, I think it's time."
    Fiona "The way to the main building should be clear."
    play sound "audio/sfx/gasp02.ogg"
    Fiona "I'm so excited!"
    scene mainplazafallnight with fade
    __("{i}Fiona and [player_name] crept down the schoolgrounds, the light from the full moon spilling through the trees' branches.{/i}")
    Jimmy "Wow, the school looks very different at night."
    play sound "audio/sfx/hmm02.ogg"
    Fiona "Personally, I love it."
    Fiona "Less annoying people to deal with..."
    scene schoolhallfallnight with fade
    play music "audio/music/mysterytheme.ogg"
    play sound "audio/sfx/whispermale.ogg"
    Jimmy "{i}*whispers*{/i} Hold on, Fiona. I can see the concierge talking with someone."
    play sound "audio/sfx/whisperfemale.ogg"
    Fiona "{i}*whispers*{/i} Okay..."
    scene conciergetalkingpascal with fade
    play sound "audio/sfx/clearthroat01.ogg"
    Marlon "The wheater is getting colder."
    Pascal "Yeah, I feel it too."
    Pascal "We are working on it, my brother."
    Pascal "I promise, this mess will be fixed."
    Marlon "I trust you, Cal, you know I do. But, I don't trust your friend."
    Pascal "He knows a lot of things, Mar. He'll help us, I'm sure."
    Marlon "I pray to the heavens that you're right..."
    Marlon "Anyways, do you want some tea? I got some at the cafeteria."
    Pascal "Sure, lead the way."
    __("{i}For a moment, [player_name] saw the face of the old man with the coat and thought he knew him from somewhere.{/i}")
    Jimmy "{i}*whispers*{/i} Shit, I think he saw me..."
    __("{i}Indeed, it looked like the man in the coat crossed his eyes with [player_name].{/i}")
    __("{i}However, the old man didn't say anything and followed the concierge to the cafeteria.{/i}")
    __("{i}Was he blind?, thought [player_name]. Lucky for them, the way was cleared now.{/i}")
    scene secretaryoffice01night with fade
    play music "audio/music/sneaking01.ogg"
    play sound "audio/sfx/dooropen01.ogg"
    __("{i}They went upstairs, crossing the assistant's office and stopped in front of the headmaster's.{/i}")
    Fiona "This is it."
    __("{i}[player_name] got the key out and opened it.{/i}")
    scene headmasterstudyfallnight with fade
    play music "audio/music/sneaking01.ogg"
    play sound "audio/sfx/doorclose02.ogg"
    __("{i}Fiona stepped inside her father's office, her eyes wide with excitement.{/i}")
    Fiona "We did it!"
    __("{i}She went directly for the desk, and after checking all the drawers, she finally found her permit.{/i}")
    show fiona clerk happy with dissolve
    Jimmy "Alright, you got it. Let's get out of here."
    play sound "audio/sfx/girlsigh01.ogg"
    Fiona mad "Wait..."
    Jimmy "What? I thought you just needed the permit."
    Fiona "This is the last time I'll be able to get in here..."
    play sound "audio/sfx/hum01.ogg"
    Fiona "I will leave the academy..."
    Fiona "[player_name]..."
    call fiona_dadrevenge_scene from _call_fiona_dadrevenge_scene
    play music "audio/music/sadmoment01.ogg"
    Jimmy "I came inside you, Fiona."
    Fiona "I... know, [player_name]. I was so into it..."
    play sound "audio/sfx/frustratedhum.ogg"
    Fiona "Don't worry, I will take a pill."
    Fiona "That was amazing, but..."
    Fiona  "God, I feel so shitty now."
    Jimmy "..."
    Fiona "Thank you so much for helping me, [player_name]."
    play sound "audio/sfx/womansobbing01.ogg"
    scene fionarevengesadcum with fade
    Fiona "I'm sorry I got you into this."
    Fiona "I'm sorry you have to see me like this..."
    Jimmy "Fiona, you don't have to feel sorry with me."
    Jimmy "I can do anything for you."
    Jimmy "We are in this together."
    play sound "audio/sfx/clearthroat01.ogg"
    Jimmy "I undertand your rage towards your father."
    Jimmy "I mean, he's a jerk, but after all this, he's still your father, you know?"
    Jimmy "You have a right to build your life."
    Jimmy "But, you shouldn't build on top of the bad blood you feel for your father right now."
    play sound "audio/sfx/girlsigh01.ogg"
    Fiona "Oh, [player_name]. I love you so much."
    Fiona "You got in my life, right when I needed you."
    menu:
        __("I love you too"):
            play sound "audio/sfx/clearthroat01.ogg"
            Jimmy "I love you too, Fiona."
            $ fionaLoveYou = True
            __("{i}[player_name] knew that a girl with daddy issues was an easy one to get, but he actually felt bad for her.{/i}")
            __("{i}Having developed actual feelings for her, he felt the need to help her for real as someone he deeply cared about.{/i}")
        __("I know"):
            play sound "audio/sfx/clearthroat01.ogg"
            Jimmy "I know, babe."
            Jimmy "You can count on me."
            __("{i}[player_name] knew that a girl with daddy issues was an easy one to get, but he actually felt bad for her.{/i}")
            __("{i}He didn't know exactly where this was going to lead, but he was having a lot of fun with it.{/i}")
    play sound "audio/sfx/hum01.ogg"
    call sleep from _call_sleep_2
    scene revengeheadmasterarrival with fade
    play music MUSIC_FUNNY_MOMENT
    play sound "audio/sfx/clearthroat01.ogg"
    __("{i}The next morning, the headmaster came into his office like every morning for work.{/i}")
    __("{i}However, this time it smelled a bit odd. Did the concierge not clean his office last night?, he thought.{/i}")
    Stapleneck "Miss Dawson, there is a weird smell in the air."
    play sound "audio/sfx/femaleclearthroat.ogg"
    Dawson "Oh, headmaster. I will call Mr. Marlon at once!"
    Stapleneck "I can sense a bit of my daughter's perfume, but... that's nonsense."
    $ Fiona.relPoints += 2
    $ quests.fionaDadTrouble = COMPLETE
    $ Jimmy.inventory.remove(ItemHeadmasterKey)
    $ gotoscene('boysdormjimmysroom')
