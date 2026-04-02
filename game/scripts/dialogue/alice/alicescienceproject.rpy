default quests.aliceScienceProject = LOCKED

label alicescienceprojectintro:
    hide screen freeroamhud
    play sound "audio/sfx/doorknock01.ogg"
    $ renpy.pause()
    Alice "Come in!"
    play music MUSIC_ALICES_THEME
    scene alicereadingfront with fade
    "{i}After knocking at the door, [player_name] opened and found Alice reading again in a weird pose.{/i}"
    Jimmy "You busy?"
    Alice "[player_name]! I..."
    scene alicebedroom with fade
    show alice casual blush left with dissolve
    play sound "audio/sfx/hey02.ogg"
    "{i}She jumped on the bed, untangling her legs from a position that looked like a human pretzel."
    Jimmy "I just wanted to talk to you about what happened in the attic."
    Jimmy "Basically, thank you for not calling the cops."
    play sound "audio/sfx/giggle01.ogg"
    Alice laugh "Ha, ha, ha, ha, I wouldn't do that... Unless you kill someone."
    Jimmy "Got it, I'll make sure that doesn't happen."
    Alice "You can get spelled if you do that. Just, be careful."
    Jimmy "I owe you one. If you need help with anything, I'm here."
    play sound "audio/sfx/hum01.ogg"
    Alice thinking "Well, I believe your timing is perfect... I am working on something."
    Alice "A science project, a personal science project. But it's... it's a bit ambitious."
    Jimmy "I think I can handle a science fair, little [roommate_female], so try me."
    Alice "Come with me, to the backyard."
    $ showscene('townhousebackyard', transition=fade)
    Alice "Wait here..."
    "{i}Alice went to the back of the tree and retrieved a strange artifact. As she got closer, [player_name] realized what it was.{/i}"
    play sound "audio/sfx/guitarriff01.ogg"
    scene alicescienceprojectintro with fade
    Jimmy "Whoa! Okay. For a science project I was thinking baking soda volcanoes, not a weapon of massive destruction."
    Alice "Ha, ha, ha. It's a small rocket, [player_name]. Or it will be..."
    Alice "I want to see how high I can get it."
    Alice "Maybe reach the upper atmosphere..."
    $ showscene('townhousebackyard', transition=fade)
    stop music
    show alice casual neutral with dissolve
    play music MUSIC_ALICES_THEME
    Jimmy "So, you're some kind of secret genius, like Melon Husk, I love it."
    play sound "audio/sfx/giggle02.ogg"
    Alice laugh "Yeah, but poor and small chested."
    Jimmy "Ha, touche! So, you want me to be the pilot?"
    Alice "Sure, you can be the pilot, ha, ha. But, right now, the problem is the propulsion."
    Alice "Solid fuel is too volatile, and liquid oxygen is... well, hard to buy at a convenience store."
    play sound "audio/sfx/hmm02.ogg"
    Alice thinking "So, I'm thinking about Biofuel."
    Alice "It's clean, sustainable, and surprisingly potent if you get the right... consistency."
    Alice "Can you go to the Ranch? I need organic base material."
    Alice "Specifically... horse manure. Fresh stuff."
    Jimmy "Horse shit? That's all we need to go to the moon?"
    Jimmy "Well, I owe you, so horse shit I'll will bring."
    play sound "audio/sfx/girlsigh01.ogg"
    Alice neutral "Maybe some high-sugar compost or spoiled fruit could help too, if you find any."
    Alice "I will calibrate the fuel tank while you get the fuel."
    Jimmy "Alright, I'll be back full of shit."
    Alice "Good one, [roommate_male], ha, ha."
    $ quests.aliceScienceProject = ACTIVE
    $ gotoscene('townhousediningroom')

label alicescienceprojectoutro:
    hide screen freeroamhud
    play sound "audio/sfx/doorknock01.ogg"
    $ renpy.pause()
    Alice "Come in!"
    play music MUSIC_ALICES_THEME
    scene alicereadingfront with fade
    "{i}Alice was back in that same position, head hanging toward the floor, reading a book about propulsion.{/i}"
    scene alicereadingback with fade
    "{i}[player_name] tried to focus, but the image of Sally emerging from the lake was burned into his retinas.{/i}"
    "{i}His brain was doing laps around her curves, flashing images of Sally while Alice moved her spreaded legs on the bed.{/i}"
    play sound "audio/sfx/oh1.ogg"
    scene aliceintrusivethought01 with vpunch
    "{i}The intrusive thought of getting his cock out and fucking Alice right there on top of the bed in that same position, took over everything else.{/i}"
    Jimmy "{i}*Focus, [player_name]. Think about... I don't know, baseball.*{/i}"
    Jimmy "{i}*Or taxes... She's your little [roommate_female].*{/i}"
    scene alicereadingfront with fade
    Jimmy "Hey, Melon! I've got the... uh... additives you wanted."
    scene alicebedroom with fade
    show alice casual blush left with dissolve
    play sound "audio/sfx/hey02.ogg"
    "{i}Alice flips upright, her eyes wide with excitement.{/i}"
    "{i}She doesn't even notice [player_name] was standing there in a strange pose, trying to hide a certain 'situation.'{/i}"
    Alice "You got it? Oh, [roommate_male]! You're a lifesaver!"
    Jimmy "Yeah, let's get this to the backyard."
    scene laterthatday with fade
    $ renpy.pause()
    $ showscene('townhousebackyard', transition=fade)
    play music "audio/music/rocketlaunch.ogg"
    "{i}The two space engineers spent the next hour mixing the 'biofuel.'{/i}"
    "{i}It was a disgusting slurry of brown and grey, but Alice handled it like she was working with liquid gold.{/i}"
    scene alicescienceprojectintro with fade
    Alice "Okay. Tank is pressurized. Bio-mix is stable...ish."
    Alice "[player_name], would you do the honors?"
    Jimmy "If this thing blows up and takes the fence with it, I'm gonna run like my life depends on it."
    play sound "audio/sfx/rocketignite.ogg"
    "{i}For three seconds, nothing happened.{/i}"
    scene rocketlaunch01 with vpunch
    play sound "audio/sfx/rocketboost.ogg"
    "{i}Then, the rocket started vibrating like an angry hornet.{/i}"
    "{i}A cloud of thick, brown smoke—smelling really bad engulfed the yard.{/i}"
    scene rocketlaunch02 with vpunch
    "{i}With a sound like a wet firecracker, the 'Sterculius-1' screeched into the sky.{/i}"
    "{i}It was a chaotic, spiraling mess of smoke and shit-fumes.{/i}"
    Alice "It's doing it! It's!"
    play sound "audio/sfx/rocketfall01.ogg"
    scene rocketlaunch03 with vpunch
    "{i}The rocket reached about fifty feet, sputtered a jet of brown flame, and then did a sharp, 180-degree turn.{/i}"
    "{i}It wasn't going to the stars; it was coming for Alice.{/i}"
    Jimmy "Look out!"
    play sound "audio/sfx/big_punch.ogg"
    "{i}[player_name] tackled her into the grass just as the rocket hissed over their heads, embedding itself three inches deep into the wooden porch.{/i}"
    scene alicerocketlaunchending with vpunch
    play sound "audio/sfx/slap.ogg"
    "{i}Alice was pinned under [player_name], in a very uncomfortable position.{/i}"
    "{i}He could smell her hair and it smelled good, and she could definitely smell the... well, everything he smelled like at that point.{/i}"
    Alice "..."
    Jimmy "Houston, we have a problem?"
    "{i}Her eyes were wide, blinking fast, and her face was turning a shade of red that rivaled the not-rotten apples.{/i}"
    Alice "Are you taking me into custody, officer?"
    Jimmy "Sorry, I should get up..."
    play sound "audio/sfx/undress01.ogg"
    $ showscene('townhousebackyard', transition=fade)
    stop music
    show alice casual blush with dissolve
    "{i}[player_name] scrambled up, dusting off his knees and tried to regain some of his 'tough-guy' composure.{/i}"
    Jimmy "I'm sorry it didn't work."
    play sound "audio/sfx/hmm01.ogg"
    Alice "I... I need to recalibrate the fins."
    Alice "And maybe the fuel-to-oxygen ratio."
    Alice "It was too... explosive."
    Jimmy "And smelly. Take your time."
    Jimmy "I think I've had enough horse shit for a while."
    Jimmy "I'm going to take a shower. A long one. Possibly with bleach."
    play sound "audio/sfx/girlsigh01.ogg"
    Alice "Thanks, [player_name]. Really. For everything."
    Jimmy "Don't mention it."
    $ quests.aliceScienceProject = COMPLETE
    if quests.antonellaBeachFun == COMPLETE and quests.blairDrunk == COMPLETE and quests.kassandraBathtubClimax == COMPLETE:
        hide screen freeroamhud with None
        play music MUSIC_BLAIR_THEME
        scene v0_5_5extendedpreview with fade
        $ renpy.pause()
        "{i}You have reached the end of v0.5.5 Extended Edition. Beyond this point, the game hasn't been updated.{/i}"
        "{i}Work on v0.5.6 is currently ongoing with new content for the Ranch and more content for the weekends.{/i}"
        "{i}Cheers, everyone!{/i}"
    call nexttime from _call_nexttime_56
    $ gotoscene('townhousebackyard')