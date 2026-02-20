label prologue_day3morning:
    stop music
    play sound "audio/sfx/distantsiren.ogg"
    scene jimmytownhouseday with fade
    show policecarstationed with dissolve
    $ renpy.pause()
    $ showscene('townhouselivingroom', transition=fade)
    show kassandra casual serious with vpunch
    Kassandra "Oh my god, [player_name]! I was so worried about you!"
    Kassandra "Why were you dropped off in a police car? What's going on?"
    show jimmy neutral with dissolve
    Jimmy talk "It's a long story. I had some things to do."
    Jimmy "But it's alright. I'm here, now."
    show jimmy neutral with dissolve
    play sound "audio/sfx/frustratedhum.ogg"
    Kassandra "Come on, [player_name]. Why would you sneak out of the house like that in the middle of the night?"
    Kassandra "It could be dangerous out there."
    Kassandra "I mean, I know you're an adult and you need your independence."
    Kassandra "But there are rules for everyone in this house, and that includes you."
    play sound "audio/sfx/femaleclearthroat.ogg"
    Kassandra "Please, don't do that again. If you ever need something, you can talk to me."
    Kassandra "And besides, it would be better for you to use the main door, instead of climbing out the window."
    Jimmy talk "You're right, Kassandra. I'm sorry. I'll check with you next time."
    Kassandra "You're sure you aren't in trouble with the police?"
    Jimmy "Nah, it was just a misunderstanding."
    Kassandra neutral "Okay, [player_name]. Do you remember Dakota offered for you to work on her ranch today?"
    Jimmy "Oh, right. I forgot about that."
    Kassandra "I can call her and tell her you need to rest..."
    Jimmy "No! Don't worry Kassandra, I managed to sleep a couple of hours."
    Jimmy "I can do it. Besides, I need some fresh air."
    play sound "audio/sfx/alright05.ogg"
    Kassandra "Alright, I'll tell her to pick you up, then."
    Jimmy "Thank you, Kass. I'm gonna take a bath and get changed."
    jump prologue_dakotaranchintro

label prologue_blairusbcollision:
    "The USB stick must be in one of these boxes."
    call item_pickup(ItemBlairUsb) from _call_item_pickup_20
    "Now I can finish setting up my PC."
    hide screen freeroamhud
    stop music
    play sound SOUND_RECORD_SCRATCH
    show blair house neutral with vpunch
    "{i}As Blair was coming down the stairs, you bumped into her.{/i}"
    "{i}Your USB stick fell to the floor, along with hers.{/i}"
    play music MUSIC_FUNNY_MOMENT
    show jimmy talk with dissolve
    Jimmy "Oh, crap. Sorry, I didn't see you coming."
    Blair "Oh, [player_name]. I forgot you live here now."
    Kassandra "Blair, could you wear something more appropiate in the house?"
    Kassandra "Your [roommate_male] is living with us now, so..."
    Blair "Oh, come on, Mom!"
    Blair rebel "This guy? I bet he's already seen tits like this, ha!"
    Blair "[player_name], do you mind the way I dress?"
    Jimmy smug "Umm, no, I don't mind."
    Blair "Great, cause' you'll have to deal with it."
    Kassandra "My lord..."
    Blair neutral "Okey, back to business. The USB stick..."
    show usbstickdilemma with dissolve
    Blair "Shit, seems like we both have the same model."
    Jimmy "Yeah, I think mine is the one on the left."
    Blair "You sure? I mean... I have important stuff on mine and... Oh, nevermind."
    hide usbstickdilemma with dissolve
    hide blair with vpunch
    show jimmy neutral with dissolve
    "{i}Blair took the USB stick on the right and ran back to her room.{/i}"
    "Wow, she was in a hurry."
    "Alright, let's get back to my room."
    $ quests.blairUSB = SATISFIED
    $ gotoscene('townhouselivingroom')

label prologue_blairlesbianvideo:
    stop music
    hide screen freeroamhud
    scene pcscreenblairusbdesktop with dissolve
    "Hey, I forgot I still had this wallpaper."
    "I took that picture with Amanda across the lake in San Pestillo, my home town."
    "Those were good times."
    "I wonder how Amanda is doing. She was my first girlfriend back in 7th grade."
    "A lot of things have happened since then."
    "Anyways, let's see if this USB still works."
    scene pcscreenblairusbwindow
    "What the? This isn't mine."
    "What is this folder?"
    scene pcscreenblairusbwindow02
    "\"Ophelia.mp4\""
    "Let's take a look."
    call blair_opheliascissoring_scene from _call_blair_opheliascissoring_scene
    Cassidy "[player_name]! Hey, I need a favor."
    Cassidy "Oh, you dirty boy. You're already watching porn?"
    Cassidy "Wait, is that Blair?"
    $ showscene('townhousejimmysroom', transition=fade, playMusic=False)
    play music "audio/music/crazymoment01.ogg"
    show cassidy pajama shocked with vpunch
    Cassidy "OMG!"
    Cassidy "I can't believe this!"
    Cassidy "She's a lesbian?!"
    Jimmy "Shut up, Cassidy! Everyone's going to hear you!"
    show blair left house neutral hairup with vpunch
    Blair "[player_name]! I think we switched our USB sticks!"
    "{i}As Blair entered the room, sweating and nervous, she looked at Cassidy, then at [player_name], then finally at the screen.{/i}"
    "{i}When she saw the video playing, her whole body froze.{/i}"
    Blair blushed "Fuck, no..."
    Cassidy neutral "Wow... Just, wow..."
    Cassidy "That explains why I've never seen you with a guy before!"
    Blair "Shut up, Cassidy."
    "{i}[player_name] quickly stopped the video and pulled the USB out of his computer.{/i}"
    Jimmy "Sorry, Blair. I thought it was a virus or something."
    Jimmy "Here's your stick."
    Blair "[player_name], I..."
    Cassidy "Ha! Wait until I tell Alice about this, she's gonna be like \"What? With another woman, is that even possible?\""
    Blair "Cassidy, not a word of this will leave this room."
    Blair "Or everyone will know about your little secret."
    Cassidy blush "What are you talking about, bitch?"
    Blair "You know what I'm talking about."
    Blair "[player_name], I'm sure you'll keep this a secret, right?"
    Jimmy "What? I didn't see anything."
    Blair "You're cool, [player_name]. Thanks."
    "{i}An uncomfortable silence filled the room as Cassidy and Blair shot daggers at each other.{/i}"
    if breakfast_ready == True:
        Jimmy "Oh, by the way. Breakfast is ready."
    $ quests.blairUSB = COMPLETE
    $ Jimmy.inventory.remove(ItemBlairUsb)
    $ gotoscene('townhousejimmysroom')

label prologue_awkwardbreakfast:
    play music MUSIC_FUNNY_MOMENT
    scene breakfasttime01 with fade
    "{i}The first day in his new house, [player_name] realized how good his [landlady_name]'s food was.{/i}"
    "{i}Everything on the table looked, smelled, and tasted delicious.{/i}"
    scene awkwardbreakfast02 with dissolve
    "{i}However, Cassidy and Blair were really quiet.{/i}"
    Kassandra "Girls, you're all so quiet today..."
    scene awkwardbreakfast01 with dissolve
    Alice "The food is really good, Mom."
    Kassandra "Thank you, baby. You always say nice things about my food."
    Kassandra "What about you, [player_name]? Did you like the food?"
    Jimmy "Oh, yeah. I don't talk much when the food is really good."
    scene awkwardbreakfast02 with dissolve
    Cassidy "Wow, talk about kissing ass."
    Kassandra "What did you say, Cass?"
    Cassidy "Nothing, Mom."
    "{i}The tension between Blair, Cassidy, and [player_name] was growing as time passed.{/i}"
    "{i}[player_name] tried to finish his food as fast as he could.{/i}"
    scene breakfasttime01 with fade
    Jimmy "That was nice, Kassandra, thank you."
    Kassandra "Anytime, darling."
    Kassandra "You should get some rest."
    scene jimmyhousediningroom with fade
    "{i}As he got up from the table, the girls left the room in a rush.{/i}"
    Kassandra "Wait a minute, [player_name]."
    play music MUSIC_KASSANDRAS_THEME
    show jimmy neutral with dissolve
    show kassandra pajamas with dissolve
    Kassandra "I forgot to give this to you last night."
    Kassandra "I know you need all the support you can get in your last year of high school, so I thought this could be useful."
    Kassandra "It's a wallet for you to keep your money in."
    Kassandra "Things can be expensive around here, but I'm sure you'll figure out how to cover your needs."
    Jimmy unamused "Oh, Kassandra. You didn't have to do this."
    Kassandra happy "It's no problem, [player_name]."
    Kassandra "I just want you to feel welcomed in your new house."
    Kassandra "And I'm really glad you're here after all this time."
    Jimmy "Thank you, I appreciate it."
    $ glob.walletUnlocked = True
    $ prologue.awkwardBreakfast = True
    $ showscene('townhouselivingroom', transition=fade)
    show screen freeroamhud(False)
    Developer "{i}Cool, now you can keep track of how poor you are in the top right corner.{/i}"
    Developer "{i}Don't worry, getting money won't be a grindy headache in this game.{/i}"
    Developer "{i}Of course, like in real life, some things are more expensive than others.{/i}"
    Developer "{i}And some girls are more expensive than others too. Watch out for gold diggers ;){/i}"
    "Alright, now I have time to go to the beach and check on the mansion."
    call nexttime from _call_nexttime_32
    $ gotoscene('townhouselivingroom')

label prologue_alicewakeup:
    $ showscene('townhousejimmysroom', transition=fade)
    show alice casual blush with dissolve
    Alice "Hey, [player_name]. My Mom wanted me to tell you that you should join her in the kitchen."
    Jimmy "Okay, thanks Alice."
    hide alice with dissolve
    $ prologue.afternoonNap = True
    $ gotoscene('townhousejimmysroom')

label prologue_dakotaantonellaintro:
    hide screen freeroamhud with None
    $ showscene('townhousediningroom', transition=dissolve)
    show kassandra left casual neutral with dissolve
    Kassandra happy "[player_name]! I'm glad you're here."
    Kassandra "Here, I want you to meet my sister Antonella."
    $ Antonella.met = True
    show antonella wine with dissolve
    Antonella "Hey, handsome."
    Kassandra "And my friend, Dakota."
    $ Dakota.met = True
    hide kassandra with dissolve
    show dakota wine left with dissolve
    play music MUSIC_DAKOTAS_RANCH
    Dakota "Hello, cowboy. Wow, Kassandra, he's even better looking than I expected."
    Antonella "Yes, he is."
    Kassandra "Control yourselves, girls."
    Kassandra "He just became an adult."
    Antonella "Is that so?"
    Dakota "Well, I'm sure he's mature enough to go for a ride with a true mare."
    Antonella "Oh, I would pay to see that."
    hide dakota with dissolve
    show kassandra left casual neutral with vpunch
    Kassandra serious "Oh my god! Stop teasing the poor boy..."
    Antonella "HAHAHAHAHAHA!"
    play sound SOUND_RECORD_SCRATCH
    play music MUSIC_FUNNY_MOMENT
    Antonella wine spill "Oh, shit... I can't laugh while drinking this, obviously." with vpunch
    Kassandra "Oh, sis. And this wine is strong, it could leave a stain on that pretty shirt."
    Kassandra "I think I have some clothes in the basement that would fit you."
    Kassandra "And you can put that shirt in the washer while you're down there, before it's too late."
    Antonella "Yeah, I think I'll do that."
    Antonella "[player_name], would you mind accompanying me?"
    Antonella "I don't like entering basements alone."
    Jimmy "Um, sure, no problem."
    Antonella "Oh, you're such a gentlemen."
    Kassandra "..."
    jump prologue_antonellabasement

label prologue_antonellabasement:
    scene townhousebasement01 with fade
    Antonella "Here we are."
    show antonella striptease with dissolve
    Antonella "[player_name], turn around while I change."
    Antonella "And, please... no peeking ;)"
    #"I don't know about you, but that sounds like she's begging for me to peek on her."
    menu:
        "Peek":
            call antonella_titshow_scene from _call_antonella_titshow_scene
            scene townhousebasement01 with dissolve
            hide antonella with dissolve
            show antonella change with dissolve
            Antonella "I think I should visit here more often."
            Antonella "You seem to be the daring kind, and I like that."
            Jimmy "Well, if you want me to watch you change clothes, I'm always available."
            Antonella "You naughty boy."
            Antonella "You can go back, now."
            Antonella "I'm going to wait for my shirt to wash."
            $ Antonella.relPoints += 1
        "Don't peek":
            Jimmy "No problem. Let me know when you're finished."
            Antonella "Mmm, my boobs are all wet with wine..."
            "I'm a gentlemen, I won't turn around."
            Antonella "Kassandra's clothes are so... small."
            "I respect women and I'm not a toxic masculine man."
            Antonella "They barely fit on me."
            "I don't want to see her boobs. That would be rude."
            Antonella "Ah, come on, [player_name]."
            show antonella change with dissolve
            Antonella "I thought you were more daring."
            Antonella "But I see you're as boring as Kassandra."
            Antonella "Good for you, I guess."
            Jimmy "I... I'm not sure what you wanted me to do."
            Antonella "Yeah, whatever, you can go back now."
            Antonella "I'm going to wait for my shirt to wash."
    jump prologue_dakotajoboffer

label prologue_dakotajoboffer:
    $ showscene('townhousediningroom', transition=fade)
    show kassandra left casual neutral with dissolve
    Kassandra "[player_name]! You're back."
    Kassandra "I hope she didn't try anything inappropiate."
    Jimmy "I'm... not sure what you're talking about."
    play music MUSIC_DAKOTAS_RANCH
    show dakota wine with dissolve
    Dakota "Of course she did."
    Dakota "She's the family slut, isn't she?"
    Kassandra "Dakota!"
    Dakota "What? She's loves when I say it."
    Dakota "Anyway, I was talking with Kassandra, [player_name]."
    Dakota "And you look strong enough to work on a ranch."
    Dakota "I've been looking for an extra hand and you might be perfect for the job."
    Kassandra "Oh yeah, I forgot to mention."
    Kassandra "Dakota has a ranch near the mountain lake."
    Dakota "Yep. It's a small ranch, but it's a great place."
    Dakota "I'm sure you'd love it."
    Dakota "You can go there on Sundays and earn a bit of money by lending me a hand."
    Dakota "And I'm sure my daughters would love to meet you."
    Kassandra "What do you think, [player_name]?"
    Jimmy "Well, I do need the money..."
    Dakota "Alright, buckaroo. That's settled, then. I'll pick you up tomorrow morning."
    Dakota "Now, leave us alone, will ya? We're having some girl time here."
    Jimmy "Alright, it was nice meeting you."
    Jimmy "See you tomorrow."
    $ prologue.dakotaJobOffer = True
    $ gotoscene('townhousediningroom', transition=fade)
