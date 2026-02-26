default secretghostclue = 0
default jonesandtoordclue = False
default ednaandaudreyclue = False
default camembertclue = False
default misspunnyclue = False

#SCREENS
init 1 python:

    scene_defs['cafeteriahalloween'] = {
        'music': MUSIC_HALLOWEEN_THEME,
        'altermusic': MUSIC_HALLOWEEN_THEME,
        'maps': {
            'default': ("cafeteriahalloweennight", "cafeteriahalloweennighthover"),
        },
        'hotspots': [
            ('kitchen', (1744, 308, 176, 354)),
            ('dawson', (1208, 391, 411, 686)),
            ('jonesandtoord', (634, 362, 311, 425)),
            ('camembert', (217, 354, 191, 394)),
            ('misspunny', (8, 410, 209, 617)),
        ],
        'sprites': [
        ]
    }

#LABELS

label edna_drunk_intervention:
    Edna "Pssssst... Hey, kid."
    Jimmy "Uh?"
    show edna cook neutral with dissolve
    Edna "I'm having a good time, but look at her..."
    show audrey halloween drunk with dissolve
    Edna "She's barely keeping herself up."
    Edna "That redhead bitch shouldn't see her like this."
    Edna "Do me a favor and take her out of here..."
    Edna "I will distract the bitch so you can slip out."
    Edna "The janitor's out for the weekend, maybe you can hide her in his place."
    Edna "She just needs some rest..."
    Jimmy "Wow, Edna. I didn't know you had a heart..."
    Edna "Ahhh, what can I say, kid... Now go, before I regret it."
    Jimmy "Alright..."
    jump audreyhalloweendrunk

label edna_party_outro:
    Audrey "Mine is Edna!"
    play sound "audio/sfx/ednalaugh.ogg"
    Edna "Ha, ha, ha, ha! Yeah, and we are drinking my gift already!"
    Edna "Tell you what, kid! I know that redhead bitch will be giving her gift to one of those pricks outside."
    play sound "audio/sfx/ednalaugh.ogg"
    Edna "And by the way, I'm glad they are all outside, because the real party is in here, ha, ha, ha, ha!"
    play sound "audio/sfx/ednaahgorgeous.ogg"
    Edna "Ahhh, this bottle is gorgeous!"
    hide edna with dissolve
    hide audrey with dissolve
    play sound "audio/sfx/signature01.ogg"
    return

label jones_toord_ghost_shutdown:
    play sound "audio/sfx/femaleclearthroat.ogg"
    Jones "Mr. Toord! You cannot give away who's your secret ghost!"
    Toord "Ah, who cares... This is stupid."
    Jimmy "Alright, thanks."
    $ showscene('cafeteriahalloween')
    play sound "audio/sfx/signature01.ogg"
    return

label cafeteriahalloween:
    $ checkcurfew()
    jump cafeteriahalloween_loop

label cafeteriahalloween_loop:
    $ resetscene()
    hide screen freeroamhud
    call screen map('cafeteriahalloween')
    jump cafeteriahalloween_loop

label cafeteriahalloween_dawson:
    hide screen freeroamhud
    if secretghostclue == 3:
        jump missdawsonhalloweendialog
    else:
        Jimmy "I need to find out who is her secret ghost."
    jump cafeteriahalloween_loop

label cafeteriahalloween_jonesandtoord:
    hide screen freeroamhud
    if jonesandtoordclue == False:
        jump jonesandtoorddialog
    else:
        Jimmy "I don't want to talk with Mr. Toord again. It's just unbearable."
    jump cafeteriahalloween_loop

label cafeteriahalloween_kitchen:
    hide screen freeroamhud
    if ednaandaudreyclue == False:
        jump ednaandaudreydialog
    else:
        Jimmy "Edna is drunk. That's enough information to stay away from her."
    jump cafeteriahalloween_loop

label cafeteriahalloween_camembert:
    hide screen freeroamhud
    if camembertclue == False:
        jump camemberthalloweendialog
    else:
        Jimmy "I got what I needed from him."
    jump cafeteriahalloween_loop

label cafeteriahalloween_misspunny:
    hide screen freeroamhud
    if misspunnyclue == False:
        jump misspunnyhalloweendialog
    else:
        Jimmy "She looks so hot in that costume. But, I gotta focus on Miss Dawson now."
    jump cafeteriahalloween_loop

label jonesandtoorddialog:
    hide screen freeroamhud
    show toord halloween with dissolve
    Toord "Then, I said 'You know what being lazy gets you, it gets you another lap you lazy guts!'"
    show missjones halloween with dissolve
    Jones "Oh, wow. Isn't that a little bit to much for students?"
    Toord "That's nonsense, cherry pie. How will the children grow into upstanding members of society if we let them run rampant?"
    Jones "Well, I don't know about that. But, that dictator costume really suits ya."
    Toord "Oh, yeah? Do you like it?"
    Toord "Maybe you can help take this hat off later tonight, sugar."
    play sound "audio/sfx/femaleclearthroat.ogg"
    Jones "Oh, no, thank you, dear. I prefer to go raid a tomb before doing that."
    Toord "[player_surname]! What are you looking at?"
    Toord "What a stupid costume you're wearing..."
    Toord "See what I meant, darling? This guy had another boy dress him, I'm sure."
    Jones "Hey, I'm glad you came to our reunion."
    Jimmy "Thank you, Miss. I like your costume."
    Jones "Oh, yes... Who doesn't like a little bit of adventure with Clara Loft."
    Toord "Oh, I can give you adventure, sugar."
    play sound "audio/sfx/frustratedhum.ogg"
    Jimmy "Sorry, Miss. I just wanted to ask you about the secret ghost."
    Jimmy "Are you sure about who your secret ghost is?"
    Jones "Oh, yes, my dear. I am."
    $ jonesandtoordclue = True
    if secretghostclue == 0:
        Toord "I heard that foul woman in the kitchen already got her gift, slacker!"
        play sound "audio/sfx/femaleclearthroat.ogg"
        Jones "Mr. Toord! You cannot give away information about the secret ghost!"
        Toord "Ah, who cares... This is stupid."
        Jimmy "Alright, thanks."
        $ showscene('cafeteriahalloween')
        play sound "audio/sfx/signature01.ogg"
        show dawsonsecretghost01 with dissolve
        Jimmy "Okay, I got the first clue."
        play sound "audio/sfx/signature02.ogg"
        show dawsonsecretghost02 with dissolve
        Jimmy "It's obvious he's talking about Edna. If she got her gift already, she's out."
        $ secretghostclue += 1
        $ gotoscene('cafeteriahalloween')
    elif secretghostclue == 1:
        Toord "Mine is a substitute, so it's lazy like you, slacker!"
        call jones_toord_ghost_shutdown
        show dawsonsecretghost03 with dissolve
        Jimmy "Okay, I got the second clue."
        play sound "audio/sfx/signature02.ogg"
        show dawsonsecretghost04 with dissolve
        Jimmy "It's obvious the substitute is Audrey, she's covering for her cousin in Shop class."
        $ secretghostclue += 1
        $ gotoscene('cafeteriahalloween')
    elif secretghostclue == 2:
        Toord "Mine is a woman, so it might have the same taste for dressing like you, slacker!"
        Toord "Oh, and I heard old Camembert also got a woman, it's the only way he can get some! Ha, ha, ha, ha!"
        call jones_toord_ghost_shutdown
        show dawsonsecretghost05 with dissolve
        Jimmy "If Toord and Camembert secret ghost's are women, only Miss Punny and Miss Jones are remaining."
        Jimmy "So, the secret ghost must be a man."
        play sound "audio/sfx/signature02.ogg"
        show dawsonsecretghost06 with dissolve
        Jimmy "Alright, need one more clue to figure out between this two."
        Jimmy "Maybe Miss Dawson herself can give me a clue..."
        $ secretghostclue += 1
        $ gotoscene('cafeteriahalloween')

    
label ednaandaudreydialog:
    hide screen freeroamhud
    scene schoolkitchendayfall with fade
    play music MUSIC_EDNA_THEME
    play sound "audio/sfx/ednalaugh.ogg"
    Edna "HAHAHAHAHAHAHAHAHAHA!"
    show edna cook daring with vpunch
    Edna "You and I will get along just fine, girl!"
    show audrey halloween drinking with vpunch
    Audrey "Aaah dring for dat! Ha, ha, ha, ha!"
    Audrey "Oh, hey priddy boy... Wanna dring some?"
    Jimmy "No, thanks... I wanted to ask you two something."
    Audrey "Suuuuuure..."
    play sound "audio/sfx/ednalaugh.ogg"
    Edna "Ask quickly kid, because we are drunk already, ha, ha, ha, ha!"
    Jimmy "Who's you secret ghost?"
    Edna "Ahhh, I'm drunk but not stupid!"
    $ ednaandaudreyclue = True
    if secretghostclue == 0:
        call edna_party_outro
        show dawsonsecretghost01 with dissolve
        Jimmy "Okay, I got the first clue."
        play sound "audio/sfx/signature02.ogg"
        show dawsonsecretghost02 with dissolve
        hide dawsonsecretghost01
        Jimmy "Edna it's Audrey's secret ghost."
        $ secretghostclue += 1
        hide dawsonsecretghost02 with dissolve
        call edna_drunk_intervention
    elif secretghostclue == 1:
        call edna_party_outro
        show dawsonsecretghost03 with dissolve
        Jimmy "Okay, I got the second clue."
        play sound "audio/sfx/signature02.ogg"
        show dawsonsecretghost04 with dissolve
        hide dawsonsecretghost03
        Jimmy "Edna says Miss Dawson's secret ghost is one of the teachers in the dining room."
        Jimmy "So, Audrey is out."
        $ secretghostclue += 1
        hide dawsonsecretghost04 with dissolve
        call edna_drunk_intervention
    elif secretghostclue == 2:
        call edna_party_outro
        show dawsonsecretghost05 with dissolve
        Jimmy "Okay, I got the third clue."
        play sound "audio/sfx/signature02.ogg"
        show dawsonsecretghost06 with dissolve
        hide dawsonsecretghost05
        Jimmy "Edna says Miss Dawson's secret ghost is one of the men."
        $ secretghostclue += 1
        Jimmy "Alright, need one more clue to figure out between this two."
        Jimmy "Maybe Miss Dawson herself can give me a clue..."
        hide dawsonsecretghost06 with dissolve
        call edna_drunk_intervention

label camemberthalloweendialog:
    hide screen freeroamhud
    show camembert halloween with dissolve
    Camembert "Aha! I know you, young man."
    Camembert "That is not a proper way to wear the uniform, but we are in a our spare time."
    Camembert "Remember I told you I had trouble finding a costume for my size?"
    Camembert "Well, I had to make it myself!"
    Jimmy "Wow, that's... impressive."
    Camembert "So, what brings you here?"
    Camembert "Are you trying to saciate your knowledge about the precise mathematic explanation of the universe existance?"
    Jimmy "Well, sir..."
    __("{i}'This guy is insufferable, thought [player_name].{/i}")
    Jimmy "I'm not that smart, but I'm actually trying to solve a riddle of my own."
    Camembert "Ah, interesting. Tell me more."
    Jimmy "You know about the secret ghost, right?"
    Jimmy "I'm trying to guess who's everyone's secret ghost by gathering clues and making my own investigation."
    Camembert "What a great idea to keep the brain working, young man!"
    Camembert "I already know the answers myself."
    Camembert "I have a riddle for you if you want to have a real challenge..."
    Jimmy "I'm ready, sir."
    $ camembertclue = True
    if secretghostclue == 0:
        Camembert "Alright, it goes like this."
        Camembert "There is only one force capable of standing up to the man that thinks himself to be El Presidente."
        Camembert "Armed with the scent of a thousand meals served per day, you can rule her out so she has already won her prize and is not a Bentley."
        $ showscene('cafeteriahalloween')
        play sound "audio/sfx/signature01.ogg"
        show dawsonsecretghost01 with dissolve
        Jimmy "Okay, I got the first clue."
        Jimmy "El Presidente... That must be Toord wearing that dictator costume."
        Jimmy "The scent of a thousand meals... Rule her out..."
        Jimmy "It's Edna. She already won her prize?"
        Jimmy "She got her gift already, maybe?"
        play sound "audio/sfx/signature02.ogg"
        show dawsonsecretghost02 with dissolve
        Jimmy "If that's the case, it's obvious she is not Miss Dawson secret ghost."
        $ secretghostclue += 1
        $ gotoscene('cafeteriahalloween')
    elif secretghostclue == 1:
        Camembert "Alright, it goes like this."
        Camembert "El Presidente has spoken to the people, he cannot rule a whole nation in solitude."
        Camembert "He might like his old colleagues, but he needs a passport, and to fix his transport, here comes a new substitute."
        $ showscene('cafeteriahalloween')
        play sound "audio/sfx/signature01.ogg"
        show dawsonsecretghost03 with dissolve
        Jimmy "Okay, I got the second clue."
        Jimmy "El Presidente... That must be Toord wearing that dictator costume."
        Jimmy "Old colleagues... Fix his transport... Get a substitute..."
        Jimmy "Crap, this is hard..."
        Jimmy "Wait, Audrey is a substitute teacher, she's new here, covering class for her cousin."
        Jimmy "Maybe she's Mr. Toord's secret ghost?"
        play sound "audio/sfx/signature02.ogg"
        show dawsonsecretghost04 with dissolve
        Jimmy "If that's the case, it's obvious she is not Miss Dawson's secret ghost."
        $ secretghostclue += 1
        $ gotoscene('cafeteriahalloween')
    elif secretghostclue == 2:
        Camembert "Alright, it goes like this."
        Camembert "I'm tired of this reunion and I want to go home..."
        Camembert "So, get rid of the women and for god's sake get it done."
        $ showscene('cafeteriahalloween')
        play sound "audio/sfx/signature01.ogg"
        show dawsonsecretghost03 with dissolve
        Jimmy "Okay, I got the third clue."
        Jimmy "Get rid of the women?"
        Jimmy "Well..."
        play sound "audio/sfx/signature02.ogg"
        show dawsonsecretghost04 with dissolve
        Jimmy "If that's the case, Miss Dawson's secret ghost is a man."
        $ secretghostclue += 1
        Jimmy "Alright, need one more clue to figure out between this two."
        Jimmy "Maybe Miss Dawson herself can give me a clue..."
        $ gotoscene('cafeteriahalloween')

label misspunnyhalloweendialog:
    hide screen freeroamhud
    show misspunny halloween with dissolve
    play sound "audio/sfx/hey01.ogg"
    Punny "Buenas noches, darling."
    Jimmy "Ummm... Hello, Miss."
    if quests.punnyPrivateLessons == ACTIVE:
        Punny "I'm still waiting for those private lessons."
        Jimmy "Oh, yeah, I'll reach you soon, Miss."
        Punny "Good to hear that."
    elif quests.punnyPrivateLessons == SATISFIED:
        Punny "I hope you liked your first lesson!"
        Jimmy "Oh, yes, Miss. I loved the food."
        Punny "Good to hear that."
    elif quests.punnyPrivateLessons == COMPLETE:
        Punny "I hope you don't mind me not calling you by your name, Mr. [player_surname]."
        Punny "I mean, all the teachers are here, so..."
        Jimmy "Don't worry, Miss. I get it."
        Punny "Good to hear that. *whisper* I loved our dance the other day *whisper*..."
    else:
        Punny "Ah, I remember you now, you're in my class!"
        Punny "The new student, verdad?"
        Jimmy "The one and only." 
    Jimmy "I wanted to ask you something, Miss. Si no le impeerta."
    Punny "Oh, ha, ha, of course, dear. It's 'importa'. What do you need?"
    Jimmy "Do you know the fantasma secriito tradition?"
    Punny "Fantasma secreto? Si, por supuesto. I got my gift right here."
    __("Goddamn she is hot! I would love to have some private classes with her.")
    Jimmy "Could you give me a clue of who is your fantasmo secreto?"
    Punny "Ha, ha, ha, I love your effort, my dear."
    Punny "But, lo siento. I can't tell you who is it. It's part of the tradition."
    Jimmy "Oh, lo siento, mi seniora."
    Punny "Don't worry, guapo. I love students who are curious."
    Punny "But, what I can actually do for you is give you some private lessons to reinforce your Spanish."
    Jimmy "Oh, that would be great, miss."
    Punny "I'm mainly interested on helping my students, so the classes are cheap."
    Punny "Contact me after Halloween and I'll see what I can do for you, okay?"
    Jimmy "Sure, Miss. Mochas gracias!"
    Punny "De nada, guapo!"
    hide misspunny with dissolve
    Jimmy "Well, I didn't got a clue, but I'm totally interested in those private classes..."
    $ misspunnyclue = True
    $ gotoscene('cafeteriahalloween')

label missdawsonhalloweendialog:
    hide screen freeroamhud
    show missdawson halloween neutral with dissolve
    Jimmy "Hey, Miss. I've some clues that might help you remember who's your secret ghost."
    play sound "audio/sfx/gasp01.ogg"
    Dawson halloween happy "Oh, that's great news!"
    Dawson halloween neutral "Let's see..."
    show dawsonsecretghost06 with fade
    Jimmy "Alright, Edna is definitely not your secret ghost, because Audrey gave her the gift already."
    play sound "audio/sfx/frustratedhum.ogg"
    Dawson "Ugh, I don't even know why I try with this people..."
    Jimmy "Audrey is not your secret ghost either, because Mr. Toord's secret ghost is a substitute teacher, and she's the only substitute here."
    play sound "audio/sfx/hmm02.ogg"
    Dawson "Ummm, interesting. I wonder how you came up with that..."
    Jimmy "And, finally, neither Miss Punny or Miss Jones are your secret ghosts, because I've concluded that your secret ghost must be a man."
    Dawson "Wait... Oh, yes, you're right, Mr. [player_surname]."
    Dawson "I remember each one of us put a piece of paper with our names inside a bowl and I got one that had some kind of pet name."
    Dawson "The Black Bigelow, I think that was it."
    Jimmy "The Black Bigelow, hum..."
    Jimmy "Well, I don't want to rush conclusions, but it's clear that..."
    Jimmy "Camembert is the Black Bigelow?"
    play sound "audio/sfx/giggle02.ogg"
    Dawson "Well, that's kind of racist, but why don't you ask him?"
    Jimmy "Good idea."
    $ showscene('cafeteriahalloween')
    show camembert halloween with dissolve
    Jimmy "Hello, again, sir."
    Camembert "Oh, you came back for more, young man?"
    Jimmy "Actually I wanted to ask you something kind of weird."
    Camembert "Shoot, my boy."
    Jimmy "Are you the Black Bigelow?"
    play sound SOUND_RECORD_SCRATCH
    play music "audio/music/crazymoment01.ogg"
    Camembert "The Black what!!??" with vpunch
    Camembert "Is that some kind of racist slur!?"
    Jimmy "Oh, not at all, sir!"
    Jimmy "I just heard about it and someone told me it was one of the teachers!"
    Jimmy "I... I thought, well... you know..."
    Camembert "Because is 'Black' it must be me, right?"
    Camembert "Ha, ha, ha, ha, ha! You should have seen your face, boy."
    Camembert "First, I gotta tell you that there is no way in hell I would have such a stupid pet name."
    Camembert "Second, there is someone stupid enough for that."
    Camembert "It's a wrestling name, so..."
    Jimmy "Mr Toord?"
    Camembert "Indeed, he wore that name during his high school days. He has been a racist asshole all his life."
    Jimmy "Wow, thank you for the information, sir!"
    Jimmy "I'm sorry if I offended you."
    Camembert "Offend me? Ha, ha, ha, you have to do more than that, young man."
    play sound "audio/sfx/signature01.ogg"
    show dawsonsecretghost08 with dissolve
    Jimmy "Alright, so The Black Bigelow is..."
    play sound "audio/sfx/signature02.ogg"
    show dawsonsecretghost09 with dissolve
    Jimmy "Mr. Toord, the biggest asshole in school."
    hide camembert halloween with dissolve
    $ showscene('cafeteriahalloween')
    show missdawson halloween neutral with dissolve
    Jimmy "I got it! It's Mr. Toord!"
    Dawson halloween happy "Oh, yes! Of course! It's a stupid wrestling name!"
    Dawson "I remember now!"
    Dawson "Thank you so much, [player_name]!"
    Dawson "You have earned yourself a very good reward, dear."
    Dawson "Let's get this over with!"
    scene laterthatday with fade
    hide missdawson with dissolve
    $ renpy.pause()
    $ showscene('cafeteriahalloween')
    play music MUSIC_FUNNY_MOMENT
    show missdawson halloween happy with vpunch
    Dawson "Alright, everyone! It's time for our secret ghost exchange!"
    Edna "Hell, yeah! I go first! I wanna go home already!"
    scene halloweensecretghost01 with fade
    Edna "Camembert! Get your ass over here!"
    Edna "Aha! Look what I found in my basement."
    scene halloweensecretghost02 with vpunch
    play sound "audio/sfx/ednalaugh.ogg"
    Edna "I sent my dogs to bring me whatever they found down there, and I found this! Ha, ha, ha, ha!"
    Camembert "Well, thank you, I guess..."
    Edna "By the way, I already drank my gift so, I'm off!"
    scene halloweensecretghost03 with fade
    Camembert "Ah, Miss Jones. I spent several nights thinking about something to give you."
    $ Jones.met = True
    scene halloweensecretghost04 with dissolve
    Camembert "What do you think? Ha, ha!"
    Jones "Oh, ha, ha, ha, that's very nice, Camembert."
    Toord "We all know that the Earth is flat, so what the hell is this, Camembert?" with vpunch
    Jones "Ugh, shut up, Toord. Thank you so much, Camembert. I love it."
    scene halloweensecretghost05 with fade
    Jones "Miss Punny! I remember you told me about that red dress you have and that you needed something to pair with it."
    scene halloweensecretghost06 with dissolve
    Jones "So, I got the perfect gift for you, queeeeeen!"
    Punny "Oh, my god! Montana, thank you so much!"
    Toord "BOOOOORING! I would love to see Punny in that dress, though." with vpunch
    Punny "In your dreams, Toord."
    scene halloweensecretghost07 with fade
    Punny "My beautiful friend, Miss Dawson. I know you enough to know that you will love what I brought you."
    scene halloweensecretghost08 with dissolve
    Punny "Feliz Halloween, querida!"
    Dawson "YEEES! I love it, Vicky!"
    Dawson "I've been wanting this perfume forever!"
    Toord "How does it smell? I've seen those in the brothels in town." with vpunch
    Dawson "Oh, my god. I hate this guy."
    scene halloweensecretghost09 with fade
    Dawson "Come here, Toord."
    scene halloweensecretghost10 with dissolve
    Dawson "Here, that's your gift."
    Toord "Well, that's the shittiest gift I've ever had, ha, ha, ha, ha!" with vpunch
    Dawson "Ugh, whatever..."
    Dawson "Thank you for coming, everyone! See you next week!"
    Toord "Alright, my turn now!" with vpunch
    scene halloweensecretghost11 with fade
    Toord "Hey, where is everyone going?"
    scene halloweensecretghost12 with vpunch
    play sound SOUND_RECORD_SCRATCH
    stop music
    Toord "Got this for the new girl! The one that fixes cars!"
    Toord "Come here, sugar! I want you to wear this and send me photos..."
    Toord "What the hell? Everyone left?"
    Jimmy "Yep."
    Toord "Fucking bastards..."
    scene laterthatday with fade
    $ renpy.pause()
    scene cafeteriahalloweennightempty with fade
    play music MUSIC_DAWSONS_THEME
    show missdawson halloween neutral
    Dawson "Well, that didn't turn out that bad."
    Jimmy "That's right."
    Dawson "Thank you so much for helping me, [player_name]"
    Jimmy "No problem, Miss."
    Dawson "You know what? When we are alone, you can call me Margaret."
    Jimmy "Oh, I finally know your name, Maggie."
    Dawson "Ha, ha, ha, I guess you're on my soft side, now."
    Dawson "I got you a gift, too."
    Jimmy "Really?"
    call item_pickup(ItemPartyInvitation) from _call_item_pickup_25
    Dawson "Yes, it's an invitation to the Harrison house Halloween party."
    Dawson "They are very selective with who they invite, but you earned it."
    Jimmy "Wow, that's very cool. Thank you!"
    Dawson "And one more thing..."
    call missdawson_deepthroat_scene from _call_missdawson_deepthroat_scene
    call missdawson_fucking_scene from _call_missdawson_fucking_scene
    scene cafeteriahalloweennightempty with fade
    show missdawson naked neutral cum with dissolve
    stop music
    Dawson "[player_name], that was amazing. But, we cannot do this anymore."
    Dawson "At least for a time..."
    Dawson "I'm getting to attached to you and everyone will notice."
    Dawson "Here, take this money, that's for your help with the reunion."
    $ Jimmy.money += 200
    call yougotmoney from _call_yougotmoney_5
    Dawson "Please, just stick to your duties and I will do the same."
    Dawson "I'll contact you one day, I promise."
    play sound "audio/sfx/highheels.ogg"
    hide missdawson with dissolve
    __("Right before leaving, [player_name] noticed there was something shiny in the floor.")
    Jimmy "There is something in the floor."
    __("Yes, I just said that.")
    call item_pickup(ItemHeadmasterKey) from _call_item_pickup_3
    Jimmy "Oh, it's a key..."
    Jimmy "Might this be the key to the Headmaster's office?"
    if quests.fionaDadTrouble == ACTIVE and quest.fionaheadmastertalk == True:
        Jimmy "Fiona will be happy."
        $ quests.fionaDadTrouble = SATISFIED
    else:
        Jimmy "I'm sure it will come in handy in the future."
    $ quest.missdawsondeepdone = True
    $ Dawson.relPoints += 1
    scene laterthatday with fade
    call nexttime from _call_nexttime_23
    $ showscene('boysdormjimmysroom')
    Jimmy "Wow, that was an intense night."
    Jimmy "She's so fucking hot, but she's right."
    Jimmy "We should take it easy for now."
    if quests.garyHalloweenHeist >= ACTIVE:
        show halloweenheistplans05 with dissolve
        Jimmy "Well, I got lucky."
        show halloweenheistplans06 with dissolve
        Jimmy "I finally got an invitation for the Halloween party."
        Jimmy "All that's left to do is getting myself a costume."
        Jimmy "Maybe Fiona can help me with that."
    else:
        Jimmy "Not sure what to do with this Halloween party invitation."
        Jimmy "Maybe and I can get a costume or something."
    $ quests.missdawsonHalloweenStaff = COMPLETE
    $ DawsonDaylimit = True
    call sleep from _call_sleep_12
    call nextday from _call_nextday_14
    $ gotoscene ('boysdormjimmysroom')