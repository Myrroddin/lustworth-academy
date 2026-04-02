default quests.antonellaBeachFun = LOCKED

label familybeachtripintro:
    hide screen freeroamhud
    $ showscene('townhousebackyard', transition=fade) 
    __("{i}That day the air smelled like lemon-scented detergent mixed with cigarette smoke.{/i}")
    play sound "audio/sfx/hum01.ogg"
    show kassandrahangingclothes01 with dissolve
    Kassandra "Nella, please. Don't smoke near the clothes, they will stink like nicotine."
    Antonella "I'm telling you, Kass, this house is a beautiful tomb."
    play sound "audio/sfx/frustratedhum.ogg"
    Antonella "You're basically a slave to this kids at this point."
    Kassandra "It's called 'parenting,' Nella."
    Kassandra "You should try it."
    play sound "audio/sfx/whisperfemale.ogg"
    Antonella "Hard pass. I prefer my freedom without the constant requests for 'crustless sandwiches.'"
    Antonella "Remember when we used to hike up to the cliffs?"
    Antonella "You wanted to study the valley's ecosystem..."
    Antonella "Build a botanic garden to show everyone why we should care about green stuff."
    Kassandra "I still have my notebooks, you know."
    Kassandra "I guess it's just a... dormant project."
    play sound "audio/sfx/mad01.ogg"
    Antonella "Honey, just like your libido."
    Kassandra "Ugh, I can't deal with you."
    $ showscene('townhousebackyard', transition=fade)
    show antonella casual neutral with dissolve
    play sound "audio/sfx/hey01.ogg"
    Antonella "Look at that! The prodigal son returns."
    Antonella proud "He looks so much like his dad... Ain't that true, Kassandra?"
    Kassandra "[player_name]! Don't listen to her. She has a grudge on all males at this point, but can't stop flirting with them."
    play sound "audio/sfx/femaleclearthroat.ogg"
    Antonella "I have my needs, Kass."
    Antonella "You know what? We are all going to the beach, Kass, as a family."
    Antonella "This Saturday. No excuses. I need to see salt water, and you need to remember you have a pulse."
    Kassandra "I'd love to, but Blair is working double shifts at the pharmacy."
    Kassandra "And Cassidy... well, she's not available."
    Kassandra "So, it's just me, you, and Alice."
    play sound "audio/sfx/giggle02.ogg"
    Antonella glad "Perfect. The sitcom family is going to the beach!"
    Kassandra "I guess it'll be good for us to get out a bit."
    Antonella "Saturday morning. It's a deal."
    play sound "audio/sfx/highheels.ogg"
    $ quests.antonellaBeachFun = ACTIVE
    $ gotoscene('townhousebackyard')

label familybeachtrip02:
    hide screen freeroamhud
    play music "audio/music/funrocktheme02.ogg"
    scene familybeachtrip02 with fade
    __("{i}Antonella was laying down in the front of the Mini Cooper looking like a diva, while Kassandra begged her to help with the baggage.{/i}")
    Antonella "Take a picture, Kass!"
    Antonella "I bet I could have been a super model in another life..."
    Antonella "[player_name]! Finally!"
    Kassandra "Good thing you came, darling."
    Alice "Hey, [player_name]. Good to see you."
    Antonella "How do I look, [player_name]? You think aunt Nella' is sexy?"
    Kassandra "Oh, god..."
    Alice "..."
    Jimmy "Let me help you with the bags, [landlady_name]."
    Kassandra "Finally, thank you so much, dear."
    scene beachground01 with fade
    show antonella bikini glad left with dissolve
    Antonella "God, I love the smell of salt water and 'family bonding' in the morning."
    Antonella "What I would give to be in a nudist beach. I mean, I could start a new trend, what do you think, sis?"
    Antonella "Free the boobs! Free the boobs! And the balls!"
    show kassandra bikini neutral with dissolve
    Kassandra "Alice, honey, ignore your aunt. You know she's a bit... off."
    Antonella "Oh, yeah! I'm off to get a margarita!"
    Kassandra "Nella, it's not even noon. Could you at least slow down the drinking?"
    stop music
    scene laterthatday with fade
    scene familybeachtrip03 with fade
    play music MUSIC_SEASIDEAMBIENCEDAY_THEME
    __("{i}A couple of hours later, the sun was a hammer.{/i}")
    play sound "audio/sfx/weirdlaugh.ogg"
    __("{i}Antonella was three margaritas deep into a very vocal lecture on why the Mayor should be a woman.{/i}")
    Jimmy "..."
    Antonella "Oh, [player_name], sexy boy. Be a dear and do some manual labor."
    Antonella "My back is starting to feel like a well-done steak, and only you can get to the 'danger zones'."
    __("{i}Antonella tossed a bottle of SPF 50 to [player_name]. It was warm from the sun, or the margaritas. Hard to tell.{/i}")
    play sound "audio/sfx/frustratedhum.ogg"
    Kassandra "I think I'm going to take a bath. Talking about politics is a bit off for the beach."
    Alice "I'm going with you, mom!"
    play sound "audio/sfx/sexyintro.ogg"
    scene familybeachtrip04 with fade
    __("{i}[player_name] knelt down. Her skin was hot, smelling like coconut.{/i}")
    "{i}As he spread the lotion, she let out a long, exaggerated sigh that made a nearby family look at them in a weird manner.{/i}"
    play sound "audio/sfx/mh1.ogg"
    Antonella "You've got strong hands, kid."
    Antonella "Do you like the view? Look at your [landlady_name] over there."
    scene kassandrabeachbath with fade
    Antonella "Kassandra's still got the best curves, even if she hides them."
    Antonella "She's in such a need of a real man."
    Antonella "Oh, and little Alice..."
    scene alicebeachbath with fade
    Antonella "She's going to be a heartbreaker once she comes back from the Moon."
    Antonella "I'm not making you uncomfortable. Right, boy? You know what I'm talking about."
    play sound "audio/sfx/girlsigh01.ogg"
    Antonella "I bet your hormones are acting right now..."
    Antonella "Come on, slap that ass! I know you want it!"
    scene familybeachtripslap with vpunch
    play sound "audio/sfx/spank01.ogg"
    Antonella "Oh, yes!"
    play sound "audio/sfx/oh1.ogg"
    Antonella "That felt so good..."
    Antonella "You know what? I need another drink."
    Antonella "Give me ten minutes to grab a fresh one at the Tiki bar."
    Antonella "Then, meet me over by the cliff side."
    Jimmy "I'll be there."
    Antonella "I know..."
    call nexttime from _call_nexttime_57
    $ quests.antonellaBeachFun = SATISFIED
    $ gotoscene('seasideareamap')

label familybeachantonellascene:
    hide screen freeroamhud
    $ showscene('seasidecliff', transition=fade)
    show antonella bikini neutral with dissolve
    play music MUSIC_ANTONELLA_THEME
    play sound "audio/sfx/femaleclearthroat.ogg"
    Antonella "Look at you. Actually showed up."
    Antonella "You are looking for trouble, don't you?"
    Jimmy "I think trouble manages to find me, instead. Depends on your point of view."
    play sound "audio/sfx/gasp01.ogg"
    Antonella proud "Well, young man. I wanted to talk to you about a serious matter."
    Antonella "You're living in a house full of women who are either too busy folding laundry or studying or looking to get attention from a college fuckboys."
    play sound "audio/sfx/frustratedhum.ogg"
    Antonella "It must be sooo boring having to deal with Saint Kassandra and her rightful ways..."
    Antonella "You need a hobby. And I need... an assistant."
    play sound "audio/sfx/hmm02.ogg"
    Antonella "A 'Sugar Boy,' if we're being poetic."
    Antonella "I've got the cash, and a very expensive taste in men." 
    play sound "audio/sfx/hum01.ogg"
    Antonella "You've got the youth and the lack of a moral compass. Oh, yes, I've heard about your little encounter with the police."
    Jimmy "A Sugar Boy? Usually, that involves a lot more grey hair and a lot less... well, you."
    Jimmy "Why should I be against that? Is like a dream for any guy."
    play sound "audio/sfx/femaleclearthroat.ogg"
    Antonella glad "Spoken like a true mercenary."
    Antonella "It'll be fun, [player_name]. I'll teach you things your father didn't even mentioned."
    Antonella "However, you need to keep your mouth shut about this, specially with my sister."
    Jimmy "Don't worry, Kassandra won't know a thing."
    Antonella neutral "Come on. Let's take a walk."
    Antonella "This beach has 'hidden spots' where people go to forget their marriage vows."
    __("{i}[player_name] opened his eyes wide in curiosity as they took a stroll along the shore.{/i}")
    call antonella_hiddenbeachhandjob_scene from _call_antonella_hiddenbeachhandjob_scene
    call nexttime from _call_nexttime_58
    stop music
    scene fewmomentslater with fade
    play sound "audio/sfx/fewmomentslater.ogg"
    $ renpy.pause()
    $ showscene('seasideareamap', transition=fade)
    play music MUSIC_ANTONELLA_THEME
    show kassandra bikini neutral with dissolve
    __("{i}They walked back to the main area. Kassandra was packing some stuff and Alice was staring at the horizon.{/i}")
    Kassandra "There you two where gone for a while. Where have you been?"
    play sound "audio/sfx/femaleclearthroat.ogg"
    show antonella bikini cum with dissolve
    Antonella "Just giving some life advice for [player_name]. He's a natural."
    Antonella "I'm sure he's going to become quite a man."
    Alice "The tide is coming in. Also, Aunt Nella, you have some weird stuff in your hair."
    Antonella "Oh, silly me. That must be some Piña Colada. It's the milk, darling, is very thick."
    Antonella "Let's move. I need to get the sand of my butt as soon as possible."
    hide kassandra
    __("{i}The beach trip was over, but things were getting interesting. The 'deal' between Antonella and [player_name] was sealed, for better or worse.{/i}")
    $ quests.antonellaBeachFun = COMPLETE
    $ gotoscene('seasideareamap')