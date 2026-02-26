label cassidynightdate01:
    hide screen freeroamhud with None
    stop music
    scene cassidycrossedlegs with fade
    play sound "audio/sfx/doorclose01.ogg"
    play music MUSIC_CASSIDY_THEME
    Cassidy "Hey, [roommate_male]. I was wondering when you would come."
    Jimmy "Well, here I am."
    Jimmy "I just wanted to check on you."
    play sound "audio/sfx/hum01.ogg"
    Cassidy "I'm okay. I feel better, you know?"
    Cassidy "Know I can see clearly what I need to do."
    Jimmy "Nice, good for you."
    Jimmy "Are you dropping that cheerleader thing?"
    play sound "audio/sfx/girlsigh01.ogg"
    Cassidy "Well, I deserve much more than that."
    Cassidy "I have to be honest with you."
    Cassidy "I've been thinking about what we did at the Harrison House."
    Jimmy "Oh, right... Well, it's pretty hard to forget."
    play sound "audio/sfx/frustratedhum.ogg"
    Cassidy "When I go to bed, when I go to class, even when I'm showering, it's just..."
    Jimmy "Hey, calm down, you seem to be really nervous."
    Cassidy "I'm just gonna say it, okay?"
    Jimmy "Go ahead."
    Cassidy "I can't stop thinking about your cock." with vpunch
    Jimmy "Oh..."
    play sound "audio/sfx/giggle01.ogg"
    Cassidy "It is stuck in my mind all the time."
    Cassidy "And every time I think about it, I get so wet down there..."
    Jimmy "Do you?"
    Cassidy "Yes! It is so frustrating."
    Cassidy "I try to please myself with my toys, but it doesn't work..."
    Cassidy "I... Have you ever thought of fucking me?"
    Jimmy "..."
    Jimmy "Honestly, I have... I know it's weird, but I have..."
    Cassidy "[player_name], I trust you so much."
    Cassidy "You know, I appreciate all your help with my problem with Christy."
    Cassidy "But I need one more thing from you."
    Jimmy "What do you mean?"
    Cassidy "I want you to be my first."
    Jimmy "I want you to take my virginity."
    __("{i}[player_name] looked at Cassidy, unsure of what to say.{/i}")
    Jimmy "I...I don't know, Cassidy."
    call cassidy_cassidycowgirl_scene from _call_cassidy_cassidycowgirl_scene
    scene cassidybedroomnight with fade
    show cassidy naked cum with dissolve
    Cassidy "Thank you, [player_name]."
    Cassidy "Thank you for opening my eyes to the truth."
    play sound "audio/sfx/stopmusiceffect.ogg"
    stop music
    play music "audio/music/tendertheme02.ogg"
    Cassidy "I know you lied to me about liking me more than Christy."
    play sound "audio/sfx/femaleclearthroat.ogg"
    Cassidy "She told me about your little adventure in the locker room." 
    Cassidy "All guys are the same. They all want to fuck the cheerleader."
    Jimmy "What the fuck? What are you talking about?"
    play sound "audio/sfx/frustratedhum.ogg"
    Cassidy "Don't worry. I'll become a cheerleader because I passed the final test..."
    Cassidy "Fucking my own [roommate_male]."
    Cassidy "Now, get out of my room. I'm way out of your league, now."
    $ quests.cassidyFirstFuck = COMPLETE
    $ quests.christyPlan = COMPLETE
    call nexttime from _call_nexttime_36
    call sleep from _call_sleep_10
    play music MUSIC_CHRISTY_THEME
    $ gotoscene('townhousejimmysroom')

label cassidy_cassidycowgirl_scene:
    play music MUSIC_SEXY_THEME
    play sound "audio/sfx/undress01.ogg"
    scene cassidytopoff with vpunch
    Cassidy "Please, [player_name], you're my [roommate_male]. No one else will be gentle with me."
    Jimmy "Cassidy, there is no going back after this."
    Cassidy "Don't worry, everything will be our secret."
    play sound "audio/sfx/mh1.ogg"
    scene cassidycowgirlintro with fade
    __("{i}Once [player_name] got his clothes off, she got on top of him on the bed.{/i}")
    __("{i}She guided his cock inside her pussy, moaning as it struggled to enter such a tight space.{/i}")
    play sound "audio/sfx/ah3.ogg"
    Cassidy "Oh my god, [roommate_male]. It feels so warm and hard..."
    Cassidy "I'm scared that is going to tear me apart."
    Cassidy "It's like I'm going to sit on a spear, but I can't help wanting it so much."
    play sound "audio/sfx/ah2.ogg"
    Cassidy "Fuck! It feels so big and it's just the tip."
    Cassidy "I'm going to go for it, [roommate_male], okay?"
    jump .slow

label .slow:
    scene cassidycowgirlanimslow with dissolve
    play sound "audio/sfx/cowgirl01.ogg"
    Cassidy "FUCK! It feels so good!"
    Cassidy "My [roommate_male]'s cock inside me feels so good."
    Cassidy "I've been wanting to do this since I met you."
    menu:
        __("Faster"):
            jump .fast
        ("Cum"):
            play sound "audio/sfx/cowgirlcum.ogg"
            Cassidy "Fuck, fuck fuuuuuck!"
            Cassidy "I'm gonna cum! I'm gonna cum!"
            Jimmy "Me too!"
            show cassidycowgirlcum with vpunch
            Cassidy "OH MY GOOOOOOOD!!!"
            Cassidy "Fuck, that was the best feeling of my life!"
            Cassidy "Sex is so fucking good! I love it!"
            if cassidygallery == True:
                call screen cassidygallery
            return

label .fast:
    scene cassidycowgirlanimfast with vpunch
    play sound "audio/sfx/cowgirl02.ogg"
    Cassidy "OHH MY GOD!"
    Cassidy "I didn't think I could take it so hard and so fast inside me."
    Cassidy "My pussy is so tight, but it's loving every inch of your cock."
    menu:
        __("Slow"):
            jump .slow
        __("Cum"):
            play sound "audio/sfx/cowgirlcum.ogg"
            Cassidy "Fuck, fuck fuuuuuck!"
            Cassidy "I'm gonna cum! I'm gonna cum!"
            Jimmy "Me too!"
            show cassidycowgirlcum with vpunch
            Cassidy "OH MY GOOOOOOOD!!!"
            Cassidy "Fuck, that was the best feeling of my life!"
            Cassidy "Sex is so fucking good! I love it!"
            if cassidygallery == True:
                call screen cassidygallery
            return

#ANIMATIONS
image cassidycowgirlanimslow:
    'cassidycowgirl01'
    pause 0.2
    'cassidycowgirl02'
    pause 0.15
    'cassidycowgirl03'
    pause 0.15
    'cassidycowgirl04'
    pause 0.1
    'cassidycowgirl05'
    pause 0.1
    'cassidycowgirl06'
    pause 0.1
    'cassidycowgirl07'
    pause 0.1
    'cassidycowgirl08'
    pause 0.1
    'cassidycowgirl09'
    pause 0.1
    'cassidycowgirl10'
    pause 0.15
    'cassidycowgirl11'
    pause 0.15
    repeat

image cassidycowgirlanimfast:
    'cassidycowgirl01'
    pause 0.08
    'cassidycowgirl02'
    pause 0.08
    'cassidycowgirl03'
    pause 0.06
    'cassidycowgirl04'
    pause 0.06
    'cassidycowgirl05'
    pause 0.06
    'cassidycowgirl06'
    pause 0.06
    'cassidycowgirl07'
    pause 0.06
    'cassidycowgirl08'
    pause 0.06
    'cassidycowgirl09'
    pause 0.06
    'cassidycowgirl10'
    pause 0.08
    'cassidycowgirl11'
    pause 0.08
    repeat
