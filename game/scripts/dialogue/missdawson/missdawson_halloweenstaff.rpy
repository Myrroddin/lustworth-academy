#VARIABLES
default quests.missdawsonHalloweenStaff = LOCKED
default quests.missdawsonHalloweenAurora = LOCKED
default quests.missdawsonHalloweenAudrey = LOCKED
default quests.missdawsonHalloweenCamembert = LOCKED

#LABELS

label halloweenreunionstart:
    show missdawson neutral
    show jimmy neutral
    with dissolve
    Dawson amazed "[player_surname]! I'm glad you came!"
    Dawson talk "I believe everything is ready for the reunion."
    Dawson "You have done very good work, but I need your help one more time."
    Dawson "Please, would you come with me to the reunion?"
    Dawson "I will feel much better knowing that I have someone I can rely on by my side."
    Jimmy "Well, I don't have much else to do."
    Jimmy "If you need me, I'll be there."
    play sound "audio/sfx/giggle02.ogg"
    Dawson "Oh, that's wonderful!"
    Dawson "You don't need to wear a costume. If they see you in your school uniform they'll know you are there as an assistant."
    Jimmy "Alright, so... When is it?"
    Dawson "Saturday evening! I'll be waiting for you!"
    Jimmy "Alright, Miss."
    $ quests.missdawsonHalloweenStaff = ACTIVE
    __("Do you want to skip time to the reunion?")
    menu:
        __("Yes"):
            jump halloweenstaffreunionintro
        __("Yes, of course"):
            jump halloweenstaffreunionintro
        __("By all means"):
            jump halloweenstaffreunionintro
            

label halloweenstaffreunionintro:
    scene nightsky with fade
    __("Sometime later...")
    $ calendar.when = (1, 6, EVENING)
    play music MUSIC_SNEAK_THEME
    scene secretaryoffice01 with fade
    Jimmy "Good evening!"
    Jimmy "Miss Dawson? Is there anyone here?"
    Dawson "[player_name]! I'm here!"
    Jimmy "The voice is coming from the headmaster's office."
    scene headmasterstudyfallevening with fade
    play sound "audio/sfx/dooropen01.ogg"
    Jimmy "..."
    play music MUSIC_DAWSONS_THEME
    show missdawson halloween happy with vpunch
    play sound "audio/sfx/sexyintro.ogg"
    Dawson "Tah-daaaa!"
    Jimmy "Wow!"
    Dawson "What do you think?"
    Jimmy "You look great!"
    Dawson "You think so?"
    Jimmy "Yabba dabba do!"
    play sound "audio/sfx/giggle02.ogg"
    Dawson "Aha! Ha, ha, ha, ha, you got it!"
    Dawson "You look nice too. Thank you for coming."
    Jimmy "No problem. I don't like missing a good party."
    Dawson halloween neutral "Well, I hope this is a decent party for once."
    Dawson "We should get going, the teachers must be waiting for us in the cafeteria."
    Jimmy "Alright, let's go."
    play sound "audio/sfx/highheels.ogg"
    scene laterthatday with fade
    pause 1.0
    $ showscene ('cafeteriahalloween')
    Jimmy "Everyone is here..."
    Jimmy "That's a nice decoration. Miss Dawson really put a lot of effort into this."
    show missdawson halloween happy with dissolve
    play sound "audio/sfx/hmm01.ogg"
    Dawson "Aha! Mr. [player_surname], here we are."
    Dawson halloween neutral "*whispers* Hey... You must understand I can't call you by your name while we are in public... *whispers*"
    Jimmy "Got it."
    Dawson halloween happy "Great! Make yourself comfortable, Mr. [player_surname]. Oh, can you check on the kitchen and see if everything is in order?"
    Dawson halloween neutral "*whispers* You never know with that foul woman... *whispers*"
    Jimmy "Sure thing."
    Dawson halloween happy "Miss Punny! I'm so glad you came, my dear!"
    hide missdawson with vpunch
    play sound "audio/sfx/highheels.ogg"
    __("Miss Dawson looks very nervous. I should help her in any way I can. Hopefully, there will a good reward for this.")
    scene schoolkitchendayfall with fade
    Jimmy "Well, it still smells like crap in here..."
    play music MUSIC_EDNA_THEME
    show edna cook neutral left with dissolve
    Edna "Hey, kid!"
    Edna "Welcome to the most boring party in town!"
    play sound "audio/sfx/ednalaugh.ogg"
    show audrey halloween neutral with dissolve
    Audrey "You're so mean! But, you're right, though."
    Edna booze "Hey, hey, kiddo... Want some booze?"
    Audrey "Oh, Edna, you really shouldn't be asking that of a student."
    play sound "audio/sfx/ednalaugh.ogg"
    Edna "Oh, come on. He's an adult and this stuff is good for the balls, if you know what I mean! Ha, ha, ha, ha, ha!"
    Jimmy "No, thanks. I'm alright."
    Audrey "Good choice, pal."
    hide edna with dissolve
    Audrey drinking "Give that to me, Edna."
    play sound "audio/sfx/ednaahgorgeous.ogg"
    show edna cook neutral with dissolve
    Edna neutral "Ahhhh, gorgeous. It's a good thing you're just a substitute teacher, ha, ha, ha, ha!"
    Jimmy "Well, I see you are having a good time here, so..."
    Edna "Yeah, yeah, go tell that bitch that everything is in order."
    Edna "By the way! Where did I leave that fucking gift?"
    stop music
    $ showscene ('cafeteriahalloween')
    show missdawson halloween angry with dissolve
    Jimmy "It's all good in there, Miss."
    Dawson "Good to hear that."
    Jimmy "You look mad, what's going on?"
    play sound "audio/sfx/femaleclearthroat.ogg"
    Dawson "Oh, [player_name]. Sorry, Mr. [player_surname]!"
    Dawson "*whispers* I forgot who my secret ghost is. *whispers*"
    Dawson "I don't know why this is happening to me..."
    play sound "audio/sfx/frustratedhum.ogg"
    Dawson "I'm so stressed out that I cannot think clearly."
    Jimmy "You should just calm down for a bit."
    Jimmy "Maybe I can get some clues from the others."
    Dawson halloween neutral "Oh, that's a good idea..."
    Dawson "Would you help me figure it out?"
    Jimmy "Yeah, sure. I'll ask around."
    hide missdawson with dissolve
    Jimmy "Alright, here we go again..."
    play sound "audio/sfx/signature01.ogg"
    show dawsonsecretghostlayout with dissolve
    Jimmy "I gotta figure out who is Miss Dawson's secret ghost."
    play sound "audio/sfx/signature02.ogg"
    show dawsonsecretghostlayout02 with dissolve
    Jimmy "There are six possible suspects... Sorry, candidates."
    Jimmy "I should ask around to get some clues and start ruling out some of them."
    $ gotoscene ('cafeteriahalloween')
