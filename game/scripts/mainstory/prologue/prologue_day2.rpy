label prologue_day2morning:
    $ showscene('boysdormjimmysroom', transition=fade)
    show jimmy smug with dissolve
    show pete uniform neutral with dissolve
    play sound "audio/sfx/heypete01.ogg"
    Pete "Hey! Good morning, [player_name]."
    Jimmy "Pete! Just the man I needed to see."
    Pete "Uhh, [player_name]... There's someone that wants to meet you."
    __("{i}[player_name] could instantly tell that Pete was afraid of the person who came through the door.{/i}")
    hide jimmy with dissolve
    play music MUSIC_GARYS_THEME
    show gary uniform cocky left with dissolve
    play sound "audio/sfx/heygary01.ogg"
    Gary "Hey, you're the new guy."
    Jimmy "Yeah, what's it to you?"
    Gary "Friendly, aren't you?"
    Jimmy "Give me a break, loser."
    Gary pointing left "Hey, relax friend, you're all pent up."
    Gary "Go easy, or they'll put you on medication."
    Gary "They did that to me, and I almost went insane."
    Jimmy "That's fascinating... Now get out of my room."
    Gary thinking left "Listen to me, tough guy. You just arrived at the toughest school in the country."
    Gary "And in a place like this, you're gonna need friends."
    Gary "So, ya gonna play nice or what?"
    Jimmy "What's your problem, man?"
    Gary "Let's see. ADHD mostly, but also my parents, hipsters, inclusive language, K-Pop..."
    Gary "But enough about me."
    Gary "I see you've already met femboy here."
    Pete "Leave me alone, Gary."
    $ Gary.met = True
    Gary "Y'know, I'm just being nice to the new guy, before he inevitably gets an STD or goes to prison."
    Jimmy "Alright, that's enough."
    Jimmy "Could you both get out of here?"
    Gary "Oh, Petey, look what you've done. He can't stand you already."
    Gary "Look, all I'm saying, [player_name], is that you should be careful who you make your friend. And who you make your enemy..."
    hide gary with dissolve
    Jimmy "We'll talk later, Pete."
    Pete "Bye, [player_name]."
    stop music
    hide pete with dissolve
    __("Jesus, what an asshole.")
    __("I gotta be careful around that guy.")
    $ prologue.secondNight = True
    $ gotoscene('boysdormjimmysroom')

label prologue_mathclassintro:
    play sound "audio/sfx/doorclose01.ogg"
    __("Man, these desks are really cramped, I can hardly get my legs under.")
    __("Oh god, here comes brace face.")
    play music "audio/music/beatrixtheme.ogg" volume 0.5
    show beatrix uniform mad with vpunch
    play sound "audio/sfx/mad01.ogg"
    Beatrix "That's my seat, new guy."
    show jimmy talk with dissolve
    Jimmy "I didn't know it had your name on it."
    Beatrix "Just because you're the new guy, doesn't mean you can do whatever you want. Now move!"
    Jimmy "Make me."
    Camembert "Get to your seats, everyone!"
    play sound "audio/sfx/hey02.ogg"
    Beatrix smile "Oh, hi Mr. Camembert, you look wonderful today!"
    __("Talk about boot licking...")
    Beatrix mad "This isn't over, dork."
    play sound "audio/sfx/mad02.ogg"
    hide beatrix with vpunch
    stop music
    show jimmy neutral with dissolve
    hide jimmy with dissolve
    $ Camembert.met = True
    show camembert with dissolve
    play sound "audio/sfx/mrcamembertclassintro.ogg"
    Camembert "I hope you're ready to learn something, this is not Spanish class..."
    Camembert "Now listen up everyone. Today, we have a pop quiz!"
    Camembert "It should be a piece of cake."
    Camembert "Even my son could ace it - and he's seven!"
    play music "audio/music/mathclasstheme.ogg"
    $ prologue.mathIntro = True
    return

label prologue_shopclassintro:
    show screen freeroamhud(False)
    __("Looks like I got to class a bit early.")
    __("Wow, look at that beauty. I would love to have a car like that.")
    __("I can hear a sound coming from inside the car...")
    hide screen freeroamhud
    call lola_carmasturbation_scene from _call_lola_carmasturbation_scene
    $ showscene('schoolgarage', transition=fade, playMusic=False)
    show blair mechanic neutral with dissolve
    Blair "I don't blame you. She does that very often, too much, actually."
    Blair "It's a miracle she hasn't been caught by a teacher or a monitor."
    Blair "I think is a matter of time."
    Jimmy "Well, it's not going to come out of my mouth."
    Blair "Good to hear that. It's better that way, to keep the distance."
    Jimmy "The name is [player_name], by the way."
    Blair "Blair, nice to meet you."
    $ Blair.met = True
    Blair "And speak of the devil..."
    show lola neutral with dissolve
    Lola "Well, well, well... I didn't know you had a boyfriend, Blair."
    Blair "Not your problem, Lola. But, no, he's not."
    Blair "By the way, now I'm not the only one that knows how dirty the backseat of that car is thanks to you."
    $ Lola.met = True
    Lola "Come on, Blair. Can't a girl have some private time?"
    Blair "Well, this is the garage, and shop class is about to begin, so... No, not here, and certainly not right now."
    Lola "Oh my god! Time really does fly when you're having fun."
    Lola "Well, keep that image in your memory, new guy, cause' you'll never get anything more."
    Lola "I'm gonna tell Vincent you were spying on me."
    Jimmy "Who the fuck is Vincent?"
    Lola "You'll learn soon enough."
    Blair "Give him a break, Lola."
    Blair "It's not {i}his{/i} fault you fuck random guys just to make your boyfriend jealous."
    Lola "What the fuck? Why are you defending him?"
    Lola "You are fucking this guy, right?"
    Blair "No, I'm not a whore like you, Lola."
    Lola "Whatever. You could never land a guy that doesn't look like a nerd, anyway."
    Lola "I'm outta here."
    hide lola with dissolve
    show jimmy neutral with dissolve
    Blair "You should be more careful."
    Blair "Most of the girls in this place are... weird."
    Jimmy unamused "Yeah, I've noticed."
    Jimmy "..."
    Jimmy "...Do I know you from somewhere?"
    Blair "I don't think so."
    Jimmy "Huh. I feel like I've seen you before."
    Blair "No clue. Well, Neil should be arriving soon, so you should get changed in the locker room."
    Jimmy "Sure. Oh, and uh, I'm sorry for causing you this trouble."
    Blair "Haha, trust me, it's not the first time something like that has happened."
    Blair "Lola has a bit of a... reputation."
    stop music
    hide blair
    hide jimmy
    with dissolve
    show audrey neutral with dissolve
    play music MUSIC_AUDREY_THEME
    Audrey "Hey guys!"
    Audrey "Is this Neil's turf?"
    Blair "Yeah, this is where he teaches his class."
    Audrey "Great! Well, he won't be coming in today."
    Audrey "He says he's sick, but I know he's just hung over."
    Audrey "My name is Audrey, I'm Neil's cousin."
    $ Audrey.met = True
    Audrey "Neil doesn't believe women can be real mechanics, yet when he needs a substitute, he always comes to me. Isn't that a laugh?"
    Audrey "Anyway, let's begin our lesson today!"
    hide audrey with dissolve
    $ prologue.shopIntro = True
    return

label prologue_aftershop:
    show audrey neutral with dissolve
    Audrey "Good job, everyone!"
    hide audrey neutral with dissolve
    show missdawson neutral with dissolve
    play sound "audio/sfx/femaleclearthroat.ogg"
    Dawson "Good evening. Sorry to interrupt."
    show audrey neutral left with dissolve
    play music MUSIC_DAWSONS_THEME
    Dawson "Where is Mr. Neil?"
    Audrey "Sorry, Miss. Neil asked me to cover his class for him today."
    Audrey "I'm his cousin, nice to meet ya!"
    Dawson "Oh, yes, right..."
    Dawson happy "I guess they let everyone teach these days..."
    Audrey "Wow, you're the rude type, huh."
    Audrey "Don't worry, girl, I'm used to entitled gals like you."
    Dawson unamused "I'm not sure what you mean with that strange slang, but anyways..."
    Dawson unamused talk "All students must go to the Auditorium as soon as possible."
    Dawson "The mayor will honor us with his presence today."
    Dawson unamused point "It is a direct order from the Headmaster!"
    hide missdawson with dissolve
    hide audrey neutral left with dissolve
    stop music
    play sound SOUND_SCHOOL_BELL
    pause 1.0
    show audrey neutral with dissolve
    Audrey "There's the bell. You guys can go now! Neil should be back next week."
    hide audrey with dissolve
    __("The mayor? Interesting...")
    __("Let's see who runs this town.")
    jump prologue_mayorassembly

label prologue_mayorassembly:
    stop music
    play music MUSIC_HEADMASTERS_THEME
    hide screen freeroamhud
    scene auditoriumhallfallevening with fade
    show jimmy neutral with dissolve
    __("This place is huge...")
    show pete uniform neutral with dissolve
    play sound "audio/sfx/heypete01.ogg"
    Pete "Hey, [player_name]!"
    Jimmy unamused "'Sup, Pete."
    Pete "We're about to meet the mayor."
    Jimmy "That's... exciting?"
    Pete "Not exactly, he's kind of scary."
    Pete "The Headmaster is a bitch compared to him."
    Jimmy smug "Hmm."
    Pete "Let's take a seat. It's about to start."
    hide pete
    hide jimmy
    with dissolve
    scene auditoriumclose01 with fade

    show stapleneck neutral with dissolve
    Stapleneck talk "Good evening, students."
    Stapleneck "Thank you for coming today."
    Stapleneck "This is a special event for our renowned institution."
    Stapleneck "Our esteemed mayor, Jack Donaguy, has decided to grace us with his presence today."
    $ Donaguy.met = True
    Stapleneck "He's a brilliant man, so please give him your undivided attention."
    hide stapleneck with dissolve
    jump prologue_mayorspeech

label prologue_mayorspeech:
    scene mayorspeech02 with fade
    # TODO: add a unique theme for the mayor
    play music MUSIC_MAYORSLOW_THEME
    __("An imposing man walked up to the podium with an expression of absolute seriousness.")
    __("Everyone in the room went silent, waiting for him to start his speech.")
    __("Instead, he just stood there, looking at every single person in the crowd with an intimidating stare.")
    __("When he reached [player_name], he paused.")
    __(" [player_name] didn't flinch for a moment.")
    Donaguy "Ladies and gentlemen, esteemed faculty, and students."
    Donaguy "Let me put this hat down before I start..."
    scene mayorspeech03 with fade
    Donaguy "As I stand before you in this grand auditorium, a testament to our collective will,"
    Donaguy "I am reminded of the days when our beloved town was but a shadow of its current glory."
    Donaguy "A time when apathy and sin were not just words, but a living, breathing presence in our streets."
    Donaguy "But look around you now! See the fruits of our labor, the result of our unyielding resolve."
    Donaguy "It was I who steered our ship away from the tempest, who brought discipline to these halls."
    Donaguy "The uniforms you now wear with pride are an example of this; they are the banners of our victory over chaos."
    Donaguy "You have learned to present yourselves with dignity, to dress not just your bodies, but your minds in the armor of propriety."
    Donaguy "And yet, our journey is far from over. We stand on the cusp of a new dawn, the next phase of our school's illustrious program."
    Donaguy "What awaits is the culmination of our efforts, which will soon be unveiled."
    Donaguy "A hard step forward that will ensure our legacy for generations to come."
    __("Murmurs of expectation and uncertainty filled the room.")
    Jimmy "This guy is intense."
    Pete "Oh, yeah. Donaguy is famous for making radical changes."
    Pete "The thing is this town was so fucked up that his programs have actually worked."
    Pete "But, I don't know, it all seems too good to be true."
    Pete "I mean, last year he imposed a rule for students to wear uniforms and not normal clothes."
    Pete "But, there are people who still wear whatever they want, even in classes."
    Pete "So, we are still resistant to these changes..."
    Jimmy "Maybe the next phase of the program will tighten things up."
    Pete "Maybe, yeah... For better of for worse."
    scene mayorspeech02 with fade
    Donaguy "I extend my gratitude to the Headmaster for this gracious invitation, and I nod to the future that sits among you: our students."
    Donaguy "A also want to make a special mention to my precious little dove, who, although she no longer walks these halls, carries the spirit of our institution in her heart."
    Donaguy "She reminds me there is still good here in Peacock Valley. You should all strive to be more like her."
    Donaguy "Come on up, Wendy!"
    scene mayorspeech01 with dissolve
    stop music
    play music "audio/music/funrocktheme01.ogg"
    __("Wait a minute...")
    __("She's...")
    show wendyrecuerdo01 with dissolve
    Wendy "{i}Oh, God!{/i}"
    Wendy "{i}I have to resist the urge of putting it inside my pussy.{/i}"
    hide wendyrecuerdo01 with dissolve
    show wendyrecuerdo02 with dissolve
    Wendy "{i}You can do it! You can do it!{/i}"
    hide wendyrecuerdo02 with dissolve
    __("It's her...")
    __("She's the one!")
    __("When the applause and cheers ended, everyone started to slowly leave the auditorium.")
    __("The mayor went to talk to the Headmaster while his daughter went backstage.")
    scene auditoriumhallfallevening with fade
    show jimmy neutral
    show pete uniform neutral
    with dissolve
    Jimmy unamused "Do you know that girl?"
    Jimmy "She was a student here?"
    Pete "Yeah, but sometimes she visits the prep mansion, 'cause well... she's the mayor's daughter and she represents his interest here."
    Jimmy "So, I'm sure she can get around the school at night without a problem."
    Pete "Well, I guess she must have a prefect pass, yeah."
    Jimmy "I need to talk to her."
    Pete "What? Are you nuts?"
    Pete "You can't just walk up to the mayor's daughter like that, man."
    Jimmy "Watch me."
    jump prologue_wendybackstage

label prologue_wendybackstage:
    scene auditoriumbackstage01 with fade
    __("Being careful not to be seen by the monitors, [player_name] snuck backstage looking for Wendy.")
    show wendy doubt with dissolve
    __("He finally saw her behind some curtains. Being up close, he saw her green eyes and the orange hair, she was the one for sure.")
    Wendy "I don't know why he always does that."
    Wendy "Every time he makes a speech, he calls me and puts me in front of everyone like a trophy. I hate that."
    show jimmy talk with dissolve
    Jimmy "Maybe you should tell him that you don't like it."
    Wendy talk "What are you doing here?!"
    Wendy "Umm... ah... Who the hell are you?"
    Jimmy "I know this is your kingdom, princess. But, you shouldn't be getting into the beds of the common folk."
    Jimmy "I mean, I enjoyed our time together, but I don't think your dad would be pleased to know about your nightly excursions."
    Jimmy "You know, you could invite me to your house to have a proper dinner or something."
    Jimmy "Or should I speak with a high wizard for an audience with your grace..."
    __("Wendy's face blushed for a moment, and her voice started to tremble.")
    Wendy blush "I... I don't know who you are, or what you're talking about."
    Jimmy "So you don't remember slipping inside my room the last couple of nights?"
    Jimmy "Look, I know it was you. I remember your voice, your eyes and your hair, and you even left your panties in my room."
    Wendy "I... I didn't..."
    Wendy angry "Look, I'm gonna tell you something, new guy."
    Wendy "Guys like you always come to me begging for attention and the answer is always the same."
    Jimmy "Oh, so you do this with other guys, too?"
    Wendy blush "What?! Of course not."
    Wendy "Y'know what? I don't have to talk to you..."
    Wendy angry "So go back to your dirty room and fantasize about me getting in your bed. 'Cause it's never going to happen."
    Jimmy "Listen to me, princess."
    Jimmy "One of this days, I'm gonna show up in your room, just like you did with me."
    Jimmy "And you're the one who's going to beg me to fuck."
    Wendy blush "Ha! You wouldn't even dare to do that... Would you?"
    Wendy angry "I don't know if you're aware, but I'm the mayor's daughter, and if I scream right now, I could get you arrested."
    Jimmy "Yeah? I'm waiting..."
    Wendy "I... just... Fuck this."
    play sound "audio/sfx/stopmusiceffect.ogg"
    hide jimmy
    play music MUSIC_HEADMASTERS_THEME
    show stapleneck stern with vpunch
    Stapleneck "What is the meaning of this?"
    Stapleneck "Miss Donaguy, is this boy bothering you?"
    Wendy "Headmaster... I think..."
    __("Wendy looked at [player_name] in the eyes and raised an eyebrow. [player_name] felt that this time he was in real trouble.")
    Wendy talk "No, no problem, Headmaster."
    Wendy "He was just introducing himself because he's new in town."
    Stapleneck neutral "Alright..."
    Stapleneck "Well, Miss, your father is looking for you."
    Wendy "In that case, I better get going."
    Wendy "Nice meeting you, friend."
    Jimmy "The pleasure was mine... Umm"
    Wendy "Wendy... Wendy Donaguy."
    $ Wendy.met = True
    hide wendy with dissolve
    __("A mischevious smile showed on Wendy's face as she went out.")
    Stapleneck arm "I don't know what you're planning, boy."
    Stapleneck "But you should be careful who you approach."
    stop music
    $ showscene('mainbuildingentrance', transition=fade)
    show screen freeroamhud(False)
    __("She didn't give me away... That's a message.")
    __("She's into the game.")
    __("I don't know how, but I'm gonna get into her room this weekend.")
    __("Speaking of the weekend, Kassandra should be coming to pick me up any minute.")
    __("I should get changed and meet her in front of the school.")
    $ prologue.mayorsSpeech = True
    $ gotoscene('mainbuildingentrance')

label prologue_kassandraintro:
    show screen freeroamhud(False)
    __("Alright, I'm ready to go.")
    hide screen freeroamhud
    stop music
    scene academygatefallevening with fade
    __("I haven't seen Kassandra since I was four years old. I don't even remember her face.")
    __("She and my dad have a weird relationship.")
    __("They still get along, but just enough to keep each other informed about their lives.")
    __("I think she has three daughters, but I don't know them at all.")
    __("My dad told me they were students here at Trustworth, which means I may have even met them without knowing.")
    scene academygatefallevening with dissolve
    play music MUSIC_KASSANDRAS_THEME
    play sound "audio/sfx/carpullover.ogg"
    show kassandraminicaringate with dissolve
    __("A tall, voluptuous woman with braided hair got out of a blue mini convertible.")
    show kassandra neutral with dissolve
    __("This woman was beautiful, and when [player_name] saw her, he felt as if he had known her his whole life.")
    $ landlady_name = renpy.input("Kassandra is your... (default: landlady)")
    $ landlady_name = landlady_name.strip()
    if landlady_name == "":
        $ landlady_name = "landlady"
    $ Kassandra.met = True
    Kassandra casual happy "Hi, [player_name]."
    Jimmy "Hey... um..."
    Kassandra "Kassandra. Don't worry, I understand you may not remember me."
    Jimmy "It's been a long time, that's all."
    Kassandra "Yes, but you still have the cutest cheeks, just like when you were a baby!"
    Kassandra "Cassidy has the same cheeks. She was born just a minute after you, you know!"
    Kassandra "Blair was so excited to have a younger sister then. You wouldn't believe it if you saw them together now though!"
    stop music
    play sound SOUND_RECORD_SCRATCH
    __("Cassidy? Blair? I know those names...")
    Cassidy "Hey, Mom!"
    Kassandra "Oh, here they come now!"
    hide kassandra with dissolve
    play music MUSIC_FUNNY_MOMENT
    show cassidy pajama neutral with dissolve
    Kassandra "Cass, baby. How are you?"
    Cassidy "Beautiful as ever, Mom."
    show blair roommate intro with dissolve
    Blair "What's up, Mom?"
    Blair "Before you ask, I'm okay."
    show alice roommate intro with dissolve
    Alice "Hey, Mom."
    Kassandra "Alice! Honey, how was your week?"
    $ Alice.met = True
    Alice "As always, not much to say."
    $ roommate_female = renpy.input("Cassidy/Blair/Alice is your... (default: roommate)")
    $ roommate_female = roommate_female.strip()
    if roommate_female == "":
        $ roommate_female = "roommate"
    $ roommate_male = renpy.input("And you are their... (default: roommate)")
    $ roommate_male = roommate_male.strip()
    if roommate_male == "":
        $ roommate_male = "roommate"
    #"{i}There they are, your three [roommate_female]s.{/i}"
    Kassandra "Girls! It's time you finally met your [roommate_male]. His name is [player_name]."
    __("An uncomfortable silence along with dismayed stares was the first formal interaction they had.")
    hide blair
    hide cassidy
    with dissolve
    Alice "Hi, I'm Alice."
    __("Alice - she was the shy girl I saw in Spanish class.")
    __("Now I know why she was looking at me as if she'd seen a ghost.")
    Jimmy "Nice to meet you, Alice."
    Jimmy "I think I saw you in Spanish class."
    Jimmy "I didn't know you were my [roommate_female] then."
    Alice "Yeah, I kind of did, but I wasn't sure."
    hide alice with dissolve
    show blair roommate intro with dissolve
    __("Blair, the girl who saw me spying on Lola inside the car, before Shop class.")
    __("Now that's a weird secret to share with your [roommate_female].")
    Blair "We know each other already, right, [player_name]?"
    Jimmy "Umm... Yeah, we have Shop class together."
    Blair "Yes, we do."
    hide blair with dissolve
    show cassidy pajama neutral with dissolve
    __("Cassidy... The only thing I know about her is that she loves to play with dildos in weird places.")
    Cassidy "He's my [roommate_male]? Are you sure, Mom?"
    Cassidy "I mean... This guy? Really?"
    Jimmy "Did you expect something else?"
    Cassidy "Well, kinda. I expected someone taller and more masculine."
    Jimmy "Yeah, well, I'm sorry I don't have the same appeal as a rubber toy."
    __("Cassidy blushed almost immediately.")
    Cassidy blush "I... I don't know what you're talking about... Um, anyway... Nice meeting you."
    Jimmy "The pleasure is mine."
    hide cassidy with dissolve
    show kassandra neutral with dissolve
    # show alice neutral with dissolve
    # show blair neutral center with dissolve
    # show cassidy neutral with dissolve
    Kassandra casual happy "It's nice to see you all getting along already."
    Kassandra "It's getting late. Let's go home, then."
    __("Oh, boy. This is going to be fun.")
    play music "audio/music/happyrock01.ogg"
    scene seasideneighborhoodfallevening with fade
    __("The buildings and houses around town were pretty colorful.")
    __("A lot of vegetation covered the valley to the coastline.")
    __("Far away, you could see the mountains to the northeast...")
    __("Followed by lush hills where fancier houses and mansions stood.")
    __("For a moment, [player_name] thought that his new house was among the richest part in town.")
    __("The sight of a huge mansion near a cliff called his attention.")
    Jimmy "That's a big house."
    Kassandra "That's the Mayor's house, actually."
    Jimmy "Huh, good to know that."
    Cassidy "I would kill to live in a mansion like that."
    Blair "You wouldn't kill a fly, Cassidy."
    Alice "Stop talking about killing, guys."
    scene townpierareafallnight with fade
    __("The house seemed to be in a residential area not far away from the coastline.")
    __("As the car rounded a corner, [player_name] caught a glimpse of a large carnival on a pier.")
    __("Even further away, he had a sight of what seemed to be a small industrial area.")
    scene housefrontfallnight with fade
    __("Minutes later, they finally arrived home.")
    __("It was a modest house, but a lot bigger than [player_name] expected.")
    scene jimmytownroomempty with fade
    play music MUSIC_TOWNHOUSE
    show kassandra neutral with dissolve
    Kassandra "Your father left your things in some boxes in the living room."
    Kassandra "I haven't touched anything. I wanted to respect your privacy."
    Kassandra "I know you must be tired from your first two days at school, so you don't have to worry about unpacking them until tomorrow."
    Kassandra "So, what do you think about your room?"
    Jimmy "It's bigger than my old room."
    Kassandra "Well, that's a start."
    Jimmy "I always wanted to live in an attic."
    Kassandra "I remember you always said that when you were little."
    Kassandra "But you were too small to get up the ladder safely."
    Kassandra "Anyways, I'll let you rest for the night."
    Kassandra "Make yourself comfortable."
    Jimmy "Thanks."
    hide kassandra with dissolve
    __("Well, I guess this is my home now. I like it, it's cozy.")
    play music "audio/music/heistplan.ogg"
    show planner_template with dissolve
    show wendyplan01 with dissolve
    __("So, I have a goal this weekend.")
    show wendyplan02 with dissolve
    __("Sneak into the Mayor's mansion...")
    show wendyplan03 with dissolve
    __("And get to Wendy....")
    __("I'm not sure how to do that, but I know where it is, so that's a start.")
    scene jimmytownroomempty with fade
    __("I think I'll organize my stuff tomorrow, set up my PC, and then I will go and take a peek at the beach near the mansion.")
    __("Maybe taking a bath will open my mind to new ideas.")
    __("There has to be a way to enter the mansion. It's on top of a cliff, so there are many ways to get close to it.")
    __("Anyways, I'm tired as fuck. Gonna sleep the night away.")
    stop music
    $ prologue.kassandraIntro = True
    call nextday from _call_nextday_12
    jump prologue_day3start

label prologue_day3start:
    scene seasideneighborhoodfallday with fade
    __("When the sun came out that morning, [player_name] woke up early to start the development of his plan.")
    scene jimmytownroomday01 with fade
    __("Alright, the PC is set up, but I can't find my USB drive.")
    __("I need it to install a couple of things.")
    __("It must still be in the boxes down in the living room.")
    $ quests.blairUSB = ACTIVE
    $ gotoscene('townhousejimmysroom')


label prologue_cassidycaught:
    hide screen freeroamhud
    show jimmy neutral with dissolve
    __("Seems like a good spot to sneak out.")
    __("The fall's not that high.")
    show cassidy pajama talk with vpunch
    play music "audio/music/crazymoment01.ogg"
    Cassidy "Aha! Gotcha."
    Cassidy "Trying to escape?"
    Jimmy "Not your problem."
    Cassidy "It is actually, because I can just scream and Mom will be here in two seconds."
    Jimmy "So, why haven't you?"
    Cassidy "'Cause I need a favor."
    Jimmy "{i}Sigh.{/i} Of course you do."
    Cassidy "You see, before you moved here... I used to hang out in the attic."
    Cassidy "But now that you're there, I can't anymore."
    Jimmy "What do you want, exactly?"
    Cassidy horny "I left something of mine in your room, somewhere."
    Cassidy "I don't remember where, but it's... a toy."
    Jimmy "Right, like your kind of toy?"
    Cassidy "Shut up, asshole. That thing in the locker room was just a mistake."
    Cassidy "Get over it, 'cause you'll never see me like that again."
    Jimmy "Alright, if I get you your toy, you don't say a word about this."
    Cassidy "That's exactly what I was thinking."
    Cassidy "I'll be in my room waiting."
    Jimmy "Right."
    hide jimmy
    hide cassidy
    with dissolve
    $ quests.cassidyDildo = ACTIVE
    $ gotoscene('townhousehallwayfirstnight')

label prologue_cassidydildo:
    __("{i}*Knock* *knock*{/i}")
    hide screen freeroamhud
    show jimmy neutral with dissolve
    show cassidy pajama talk with dissolve
    Cassidy "Yes?"
    Jimmy "Here's your toy."
    Cassidy dildo "Oh, hell yes!"
    Cassidy "Well, you can go now and do your freak stuff."
    Jimmy "Do you ever say thank you?"
    Cassidy "Never."
    Cassidy "Now, get lost."
    hide cassidy with vpunch
    hide jimmy with dissolve
    pause 0.5
    __("I already hear noises inside.")
    __("I wonder if there's a way to take a peek...")
    $ quests.cassidyDildo = COMPLETE
    $ Jimmy.inventory.remove(ItemCassidyDildo)
    $ gotoscene('townhousejimmysroomnightinfiltration')

label prologue_cassidypeephole:
    __("I can hear coming moans from the hole.")
    hide screen freeroamhud
    scene cassidybedroomdildopeek with fade
    stop music
    __("Oh, I was hoping to see Cassidy on the other side.")
    __("Wait... There she is.")
    __("Holy shit, she's going for it!")
    call cassidy_townhousepeephole_scene from _call_cassidy_townhousepeephole_scene
    $ showscene('townhousejimmysroomnightinfiltration', transition=fade)
    __("She's really hot.")
    __("It's kind of weird that she's my [roommate_female], but I can't stop watching that sweet pussy.")
    __("Now at least I should be able to get out.")
    $ prologue.cassidyPeephole = True
    $ gotoscene('townhousejimmysroomnightinfiltration')

label prologue_mayorsmansion:
    hide screen freeroamhud
    scene seasideneighborhoodfallnight with fade
    __("With one goal in mind, [player_name] crept out of the window and started walking towards the beach.")
    __("It was exciting. He was going to fulfill his promise to Wendy and let her know that he meant serious business.")
    __("Of course, he was thinking with his penis, not even considering the real consequences his actions might bring.")
    __("Everything worked just like he planned, and soon he found himself in the backyard of the huge mansion.")
    $ showscene('mayorsmansionbackyard', transition=fade)
    show jimmy neutral with dissolve
    show screen freeroamhud(False)
    __("Damn, it looks bigger from here.")
    __("There doesn't seem to be much surveillance for a place so important.")
    __("Alright, there's a shed, a pool, and a lot of terrain to cover.")
    __("How the fuck am I going to get in?")
    __("And where exactly is Wendy's room?")
    $ prologue.sneakOutTownhouse = True
    $ gotoscene('mayorsmansionbackyard')

label prologue_wendykitchen:
    __("Looks like the kitchen is behind the glass.")
    __("Wait, I think I can see someone inside.")
    hide screen freeroamhud
    show wendyfridgepose with fade
    __("That's Wendy!")
    __("Fuck, look at that hot ass.")
    __("Now I just need to wait for her to go back to bed.")
    hide wendyfridgepose with fade
    show screen freeroamhud(False)
    __("Show me where your room is, princess...")
    $ mayorsmansionbackyard.wendysLightOn = True
    pause 1.0
    $ showscene('mayorsmansionbackyard')
    pause 0.5
    __("There you are.")
    __("Coming for you, princess.")
    $ gotoscene('mayorsmansionbackyard')

label prologue_wendyinfiltration:
    hide screen freeroamhud
    __("After climbing the trellis with cat-like grace, [player_name]'s fingers grazed the cold ledge as he pulled himself up.")
    scene wendyroomnightintro with fade
    __("Wendy's room was on the top floor. A symphony of opulence with velvet drapes, gilded mirrors, and a bed that could fit a dozen people.")
    stop music
    scene wendywalkmandancing with dissolve
    play music "audio/sfx/wendyheadphones.ogg"
    __("There she was in the middle of the room, holding a walkman with headphones covering her ears.")
    __("Her eyes were closed, and her lips moved silently, mouthing the lyrics.")
    __("[player_name] watched as she danced, her movements fluid and not selfconscious.")
    __("He admired her butt moving slowly with grace, remembering the last night the danced together in his bed.")
    __("Then, as if sensing his presence, she opened her eyes.")
    stop music
    play sound "audio/sfx/scream01.ogg"
    scene wendywalkmansurprise with vpunch
    Wendy "AAAHHHH!"
    __("The walkman slipped from her fingers as she put the headphones away. She hurried to the window, her eyes wide.")
    scene wendyroomnightintro with fade
    show jimmy smug with dissolve
    play music "audio/music/funnymoment.ogg"
    Jimmy "Hello, princess."
    show wendy panties with vpunch
    play sound "audio/sfx/mad01.ogg"
    play music MUSIC_WENDY_THEME
    Wendy "What the fuck?!"
    Wendy "You scared the shit out of me!"
    Jimmy "I could say the same about the first time you snuck in my room."
    Wendy "Oh my fucking god. I can't believe you did this."
    Wendy "You are nuts!"
    Wendy "If my dad notices you're here, you're totally going to jail."
    Jimmy "That depends whether you tell him."
    Wendy "Well, I could..."
    Jimmy "It doesn't matter if I get punished for this. You're worth every second of it."
    __("Wendy couldn't hold a laugh as she made sure her door was closed.")
    Wendy "You know, seeing you sneaking in my room {i}is{/i} kind of sexy."
    Jimmy "Tell me more..."
    Wendy "You kept your promise."
    Wendy "No one has done that for me before."
    Jimmy "I always keep my promises."
    play sound "audio/sfx/hum01.ogg"
    Wendy panties doubt "But, this is so dangerous."
    Wendy "You do realize that this thing between us is impossible, right?"
    Wendy "You don't know my dad, he's..."
    Jimmy "Hey, I know what I'm getting into."
    Jimmy "I wanted to prove that I can get to you, no matter if you're in the highest tower of a castle."
    Jimmy "I'm here now, there is no coming back from this."
    Wendy "Oh, my god... I'm sorry, but you saying that is making so wet, ha, ha, ha, ha!"
    Wendy "I can't stand it, anymore."
    Wendy "I want you."
    Wendy "Get your cock out!"
    scene wendyfootjobintro with fade
    play sound "audio/sfx/giggle01.ogg"
    Wendy "I'm want to try something."
    call wendy_roominfiltration_scene from _call_wendy_roominfiltration_scene
    jump prologue_jimmycaught

label prologue_jimmycaught:
    play sound SOUND_RECORD_SCRATCH
    play music "audio/music/crazymoment01.ogg"
    scene wendyroomnightintro
    show jill police gunpoint with vpunch
    Jill "P.V.P.D! Get on your knees and put your hands on your head! You are under arrest!"
    Jimmy "Oh, fuck."
    show jimmy cockout with dissolve
    Jimmy "Hey, don't shoot!"
    Jill "Get your hands in the air, now! I don't want any-"
    Jill police gundown blush "Oh, my..."
    pause 0.5
    Jill "Ummm, can you put your pants on, please?"
    Jimmy "Oh, sure. No problem."
    hide jimmy with dissolve
    play music MUSIC_MAYORSLOW_THEME
    scene mayormansiongatepolice with fade
    show donaguy neutral with dissolve
    play sound "audio/sfx/clearthroat01.ogg"
    Donaguy "Are you proud of yourself, boy?"
    Donaguy "This must be a huge accomplishment for you."
    Donaguy "Officer Jillian will give you a ride to the police station."
    $ Jill.met = True
    play sound "audio/sfx/malehum01.ogg"
    Donaguy "I will meet you there to have a talk about this."
    Donaguy "But first, I must talk to my daughter."
    Donaguy "Get in the car, now."
    __("Without saying a word, [player_name] did as the Mayor asked.")
    jump prologue_policestation

label prologue_policestation:
    play sound "audio/sfx/distantsiren.ogg"
    stop music
    scene policestationfrontnight with fade
    $ renpy.pause()
    stop sound
    scene policestationcellblock
    play music MUSIC_SUSPENSE
    show jimmy neutral
    show jill police neutral
    with fade
    play sound "audio/sfx/alright02.ogg"
    Jill "Alright, Mr. [player_surname]."
    Jill "You'll stay here until the Mayor arrives."
    Jimmy "Whatever..."
    Jill "I'll be in my office."
    Jill "Oh, and be careful with Grant. He's... special."
    Jimmy "Who's Grant?"
    play sound "audio/sfx/highheels.ogg"
    hide jill with dissolve
    __("The sexy officer left without answering [player_name]'s question.")
    Jimmy "Well, shit."
    Jimmy "This is exactly what I needed to avoid."
    Jimmy "I guess this is the end of the road for me."
    Jimmy "Fuck, I wanted to try to do better... for my dad."
    play sound SOUND_RECORD_SCRATCH
    stop music
    play sound "audio/sfx/boohoo.ogg"
    Grant "Oh, boohoo, cryin' for daddy?"
    Jimmy "What?"
    Jimmy "Who the fuck is that?"
    Grant "Your consciousness, idiot."
    Grant "You should be ashamed of yourself."
    play music MUSIC_GRANTS_THEME
    show grant neutral with dissolve
    $ Grant.met = True
    Jimmy "Who are you?"
    Grant "Oh, I'm the physical manifestation of your consciousness."
    Grant "Admit it, kiddo. You're finally going nuts."
    Jimmy "Come on, man. My consciousness definitely doesn't look like you."
    Grant "But I have beautiful blue eyes! Don't you see?"
    Jimmy "Yeah... That doesn't make you attractive at all."
    Grant concerned "Whatever, pal. The important thing is that I'm your ticket outta here."
    Jimmy "What are you talking about?"
    Grant "You see that door over there?"
    Grant "I know the code to open it."
    Grant "But, I'm not leaving here without my bag."
    Grant neutral "So here's the deal. You recover my bag, and I'll help you escape with me."
    Jimmy "And where is your bag?"
    Grant "That sexy candy that brought you in has it in her office, on the second floor."
    Jimmy "Let's pretend I believe you."
    Jimmy "Even if I could somehow snatch it from her, how the fuck am I gonna open the cell?"
    Grant "Let me handle that."
    hide grant with dissolve
    hide jimmy with dissolve
    show policestationcellblockgrant with dissolve
    play sound "audio/sfx/spit.ogg"
    __("The hobo approached the lock and, making a weird sound with his throat, spat over it.")
    __("More disgusted than he'd ever been, [player_name] watched the green slime slide into the lock... and suddenly heard a click.")
    Grant "Here we go."
    scene policestationcellblockgrantopen with vpunch
    play sound "audio/sfx/metalgateopen.ogg"
    __("The gate opened, also leaving [player_name] more confused than he'd ever been.")
    Jimmy "How the fuck did you do that?"
    show grant neutral with dissolve
    Grant "I never brush my teeth, kiddo."
    Grant crazy "Fluoride is for pussies!" with vpunch
    Grant "The government wants to control all of us with fluoride!"
    Grant "They will kill us all!" with vpunch
    Grant neutral "Anyway, my natural spit is acidic enough to melt most locks."
    Jimmy "Oh, gross."
    Grant "Just go get my bag, kiddo. I'll wait for you here."
    stop music
    __("This guy is totally nuts. But he might be telling the truth.")
    __("Besides, I have no other options.")
    $ quests.grantHoboBag = ACTIVE
    $ gotoscene('policestationcellswest')

label prologue_grantsbagfetch:
    Jimmy "I guess this is Grant's bag."
    hide hobobag
    call item_pickup(ItemGrantsBag) from _call_item_pickup_19
    Jimmy "Ugh, it's slimy..."
    Jimmy "I don't even wanna know what's inside."
    Jimmy "Uhhh, there is some cash stuck under the bag..."
    $ Jimmy.money += 25
    call yougotmoney from _call_yougotmoney_8
    $ quests.grantHoboBag = SATISFIED
    $ gotoscene('policestationjillsoffice')

label prologue_grantescape:
    hide screen freeroamhud
    show jimmy neutral with dissolve
    show grant neutral with dissolve
    play music MUSIC_GRANTS_THEME
    $ quests.grantHoboBag = COMPLETE
    $ Jimmy.inventory.remove(ItemGrantsBag)
    Jimmy talk "Here's your bag. Now, can you open the door or not?"
    Grant bag "Thanks, kiddo!"
    scene policestationcellblockpadlock with dissolve
    Grant "Sure I can open the door."
    Grant "You just watch the stairs, in case someone comes."
    Jimmy "Alright, I'll keep an eye out."
    scene prisonmorgueintro with dissolve
    show jimmy talk with dissolve
    Jimmy "The coast is clear!"
    Grant "Oh, yeah! Clear it is!"
    play sound "audio/sfx/firealarmsprinkler.ogg"
    scene prisonmorguefirealarm with vpunch
    Grant "Ha! See ya, kiddo!"
    Jimmy "What?"
    play music "audio/music/crazymoment01.ogg"
    scene policestationcellblockfirealarm with vpunch
    Grant "You shouldn't trust a man with beautiful blue eyes!"
    scene policestationcellblockescape with vpunch
    play sound "audio/sfx/run01.ogg"
    Jimmy "HEY, WAIT!"
    play sound "audio/sfx/doorclose01.ogg"
    scene policestationcellblockfirealarmopen with vpunch
    Jimmy "That motherfucker!"
    Jill "What's going on down here!"
    show jill police gunpoint with vpunch
    Jill "What are you doing out of your cell?!"
    Jimmy "That hobo piece of shit set me up!"
    play sound "audio/sfx/laugh01.ogg"
    Jill police relaxed "I should've known. I told you to be careful with him."
    Jill "Don't worry, we'll catch him tomorrow."
    Jill "Come with me, the Mayor wants to speak with you."
    jump prologue_mayorwarning

label prologue_mayorwarning:
    play music MUSIC_MAYORSLOW_THEME
    scene interrogationroomintro with fade
    show donaguy neutral with dissolve
    play sound "audio/sfx/malehum01.ogg"
    Donaguy crossed "Mr. [player_name] [player_surname]."
    Donaguy "I can't say it's a pleasure to meet you after what you did."
    Donaguy "Why are your clothes wet?"
    Jimmy "It's a long story..."
    Donaguy "Hm..."
    play sound "audio/sfx/malehum02.ogg"
    Donaguy imponent "Well, kid. I've been dealing with people like you all my life, you know?"
    Donaguy "Young folks who believe they can get away with anything."
    Donaguy "Guys with a broken moral compass, just wandering in life with no real goal in sight."
    Donaguy "But I understand, because I was one of you when I was younger."
    Donaguy "However, I chose a different path, and now I'm gonna help you find that path too."
    play sound "audio/sfx/malehum01.ogg"
    __("Blah, blah, blah...")
    Donaguy "In fact, I think I owe you my thanks."
    Donaguy think "You see, until now I had thought my methods were getting a little too... extreme."
    Donaguy "But you have helped me to see the truth."
    Donaguy "And the truth is that this town needs a reformation from the roots if we want a better future."
    Donaguy "Guys like you need rules enforced on them, so you can actually learn what should be done."
    Donaguy "I was hesitating to implement my new reformation program."
    Donaguy "But now I see this is the only way."
    play sound "audio/sfx/beastgrunt01.ogg"
    __("What is this guy talking about?")
    __("This is getting weird.")
    play sound "audio/sfx/clearthroat01.ogg"
    Donaguy neutral "My daughter decided not to press charges against you."
    Donaguy "I couldn't disagree more, but she's an adult and she's capable of making her own decisions, for now."
    Donaguy "So, you should go home and think about what you did today, because there will be consequences..."
    Donaguy "And when you least expect it, when you think you've gotten out Scot-free..."
    Donaguy "It will be too late, kid."
    __("...Did he just threaten me?")
    Donaguy "Now, get out of my sight."
    play sound "audio/sfx/malehum01.ogg"
    if prologue.complete:
        $ gotoscene('seasidecliff')
    call nextday from _call_nextday_13
    $ Wendy.relPoints += 1
    jump prologue_day3morning

#ANIMATIONS
image dawsontitshowanim101:
    'dawsontitshowanim01'
    pause 0.2
    'dawsontitshowanim02'
    pause 0.2
    'dawsontitshowanim03'
    pause 0.2
    'dawsontitshowanim04'
    pause 0.2
    'dawsontitshowanim05'
    pause 0.2
    'dawsontitshowanim06'
    pause 0.2
    'dawsontitshowanim07'
    pause 0.2
    'dawsontitshowanim08'
    pause 0.2
