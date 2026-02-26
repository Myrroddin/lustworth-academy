label prologue_start:
    stop music
    play sound "audio/sfx/guitarriff01.ogg"
    scene prologuelabel with fade
    pause 1.5
    scene academygatefallevening with fade
    play music MUSIC_MAIN_THEME
    show jimmy neutral with dissolve
    __("Well, I'm finally here.")
    __("I guess this shithole is gonna be my home now.")
    __("Just gotta get through one more year, [player_name]. Just one.")
    __("Then you're free from all this stupid crap.")
    Dawson "You must be the [player_surname] boy."
    play music MUSIC_DAWSONS_THEME
    show missdawson neutral with dissolve
    Jimmy suspicious "Did you just fade in?"
    Dawson happy "Welcome to Trustworth Academy."
    Dawson talk "We've been expecting you."
    Dawson "I'm sure you're very excited to be here."
    Dawson blush "Very excited, indeed..."
    show jimmy smug with dissolve
    __("Is she looking at my crotch?")
    Dawson talk arm "{i}Ahem.{/i} I have a man to make happy."
    Dawson "The Headmaster is expecting you in his study."
    Dawson "Don't keep Dr. Stapleneck waiting."
    $ Stapleneck.met = True
    play sound "audio/sfx/girlsigh01.ogg"
    Dawson happy "He's a brilliant man... Brilliant."
    Jimmy unamused "I'm on my way then."
    play sound "audio/sfx/stopmusiceffect.ogg"
    stop music
    show jimmy leave with dissolve
    play sound "audio/sfx/hum01.ogg"
    Dawson unamused point "His study is behind the gate, boy!"
    show jimmy neutral with dissolve
    Dawson unamused talk "In the main building."
    jump prologue_stapleneckintro

label prologue_stapleneckintro:
    stop music
    scene headmasterstudyfallafternoon with fade
    play music MUSIC_HEADMASTERS_THEME
    show stapleneck neutral with dissolve
    Stapleneck talk "Ah! Yes, you must be the [player_surname] boy."
    Jimmy "Uh, yeah."
    play sound "audio/sfx/clearthroat01.ogg"
    Stapleneck stern "Excuse me? Yeah, what?"
    Jimmy "I meant, yes, Sir."
    Stapleneck stern talk "Very good."
    Stapleneck "You know, I've seen your record."
    Stapleneck "Vandalism, graffiti, abusive language, violent conduct, disrespecting teachers..."
    Stapleneck sarcasm "OH! I'm so scared of you, [player_name]!" with vpunch
    Stapleneck "I've never seen a boy like you in my life!"
    Stapleneck "You're the nastiest without a doubt."
    Stapleneck stern talk "Tell me, [player_name]. Why should I waste my time with you?"
    Jimmy "..."
    Stapleneck smug talk "Because it is my calling!"
    Stapleneck arm "That is, after all, the mission of this revered institution."
    Stapleneck "To reform young delinquents like you into respectable members of society."
    stop music fadeout 1.0
    play sound "audio/sfx/teabell.ogg"
    show missdawson tea with dissolve
    Dawson "Headmaster, I've got your tea!"
    Stapleneck talk "You're too good to me, Miss Dawson."
    $ Dawson.met = True
    Dawson "No more than you deserve, Headmaster."
    play music MUSIC_SEXY_THEME
    scene missdawsonbodypeek01 onlayer cutscene with dissolve
    __("Wow...")
    play sound "audio/sfx/teapour.ogg"
    __("This woman is really hot.")
    __("I bet she's been \"reformed\" by this Stapleneck guy a few times.")
    scene missdawsonbodypeek02 onlayer cutscene with dissolve
    __("Damn, what I wouldn't give to clap those cheeks.")
    Stapleneck "Miss Dawson, please tell Miss Trudeau to come here."
    __("I bet Miss Trudeau is even hotter!")
    show missdawson amazed
    show stapleneck neutral
    hide missdawsonbodypeek02 onlayer cutscene with fade
    stop music fadeout 1.0
    Dawson "Of course, Headmaster."
    play sound "audio/sfx/highheels.ogg"
    hide missdawson with dissolve
    Stapleneck talk "So, boy."
    Stapleneck "This is your last year of school before you start college."
    Stapleneck stern talk "It will be your choice whether you become a college prospect or a county jail inmate."
    Stapleneck "With Trustworth's acclaimed program for young adults, you will have all the tools needed to succeed."
    Stapleneck "If you keep yourself out of trouble and remain diligent with your classwork, I'm sure you'll find we can get along just fine."
    play music MUSIC_BEATRIX_THEME
    show beatrix uniform smile with dissolve
    Beatrix talk "Headmaster! I'm here."
    Stapleneck "Very well, Miss Trudeau."
    __("That's Miss Trudeau?")
    Stapleneck "[player_name], this is Beatrix. She is a student here as well."
    $ Beatrix.met = True
    Stapleneck "She will show you to your room."
    show stapleneck neutral with dissolve
    Beatrix "Yes, Headmaster."
    Beatrix arm "Come along, then."
    stop music fadeout 1.0
    hide beatrix with dissolve
    play sound "audio/sfx/clearthroat01.ogg"
    Stapleneck talk "Oh, and remember, boy."
    Stapleneck "You will keep your nose clean..."
    Stapleneck arm "Or I will clean it for you."
    jump prologue_boysdormintro

label prologue_boysdormintro:
    $ calendar.when = (PROLOGUE, WEDNESDAY, NIGHT)
    scene boysdormhallwayafternoon with fade
    play music MUSIC_BEATRIX_THEME
    show beatrix uniform smile with dissolve
    show jimmy neutral with dissolve
    Beatrix talk "Here we are!"
    Beatrix "Um, I'm not sure which room is yours..."
    play sound SOUND_RECORD_SCRATCH
    play music "audio/music/funnymoment.ogg"
    Beatrix arm "But I'm sure even a brainworm like you will be able to figure it out."
    Jimmy suspicious "Wow... Easy, smartass."
    play sound "audio/sfx/hum01.ogg"
    Beatrix mad "What? You can't talk to me like that!" with vpunch
    Jimmy suspicious arm "You're the one calling me a brainworm."
    Beatrix mad arm "Well, I don't have time to argue with idiots, so I'm leaving." with vpunch
    Jimmy unamused arm "Whatever, mophead..."
    play sound "audio/sfx/mad02.ogg"
    hide beatrix with dissolve
    stop music
    show jimmy neutral with dissolve
    __("Jesus... People here are even crazier than I expected.")
    __("Well, here I am.")
    __("Let's see how bad this school turns out to be.")
    __("That old creep thinks he can tame me, but I only give people what they already have coming to them.")
    __("Anyway, I'm exhausted from the trip.")
    __("I should go to sleep, but I need to find my room first.")
    $ prologue.finishIntro = True
    $ gotoscene('boysdormhallway')

label prologue_jimmysroomintro:
    hide screen freeroamhud
    $ showscene('boysdormjimmysroom', transition=fade)
    __("Seems nice enough. Lots of space to store stuff.")
    __("First thing I'm gonna need is a punching bag.")
    __("I have a feeling I'm gonna have to punch a lot of people around here.")
    $ prologue.findJimmysRoom = True
    $ gotoscene('boysdormjimmysroom')

label prologue_mysterygirlnight1:
    scene jimmyroomshut with fade
    __("At least the bed looks cozy.")
    __("I'm gonna sleep like a log.")
    hide screen freeroamhud
    stop music
    scene black with fade
    pause 1.0
    call wendy_mysterygirlnight1_scene from _call_wendy_mysterygirlnight1_scene
    scene nightsky with fade
    __("It was uncertain if the girl left because she discovered his true identity...")
    __("or because someone else was watching through the window.{/i}")
    __("Still, she left a very good impression on [player_name], and now he wanted to know who she was.{/i}")
    __("{i}But, right there in the middle of the night, there is not much you can do besides sleeping...")
    __("{i}And that encounter made [player_name] even sleepier, as he fell back into a heavy slumber...{/i}")
    __("{i}...now with a smile on his face.{/i}")
    stop music
    call nextday from _call_nextday_10
    jump prologue_day1morning

label prologue_day1morning:
    $ showscene('boysdormjimmysroom', transition=fade)
    show jimmy smug with dissolve
    __("Damn, my first night here has been absolutely unforgettable.")
    __("It was too dark though. It's a shame I couldn't see her face.")
    __("By the things she said, I think she mistook me for someone else...")
    __("The guy that stayed here before me, I guess.")
    hide jimmy smug with dissolve
    __("Maybe I can find some clue that will lead me to her.")
    show pete uniform salute with dissolve
    play sound "audio/sfx/heypete01.ogg"
    Pete "Hey, how's it going? You must be the new kid."
    Pete "I'm Pete Kowalski."
    $ Pete.met = True
    Jimmy "[player_name] [player_surname]."
    Pete neutral "Welcome to Peacock Valley. A dump disguised as a brilliant coastal city."
    Pete "But there are a lot of hot girls on campus, and in the city too."
    Jimmy "Good to hear that."
    Pete "Do you know what classes you have today?"
    Jimmy "No idea."
    Pete givebook "Well, here's a planner for you. Consider it a gift."
    Pete neutral "I was as lost as you when I got here."
    Pete "I'm sure it'll help you."
    Jimmy "Alright, thanks."
    Pete "Okay... I guess I'll see you later."
    Pete "Oh, and make sure to wear your uniform!"
    hide pete with dissolve
    show jimmy neutral with dissolve
    __("Well, at least somebody is nice here.")
    __("I guess I should get changed and head to class. My uniform should be in the closet.")
    hide jimmy with dissolve
    $ glob.plannerUnlocked = True
    $ prologue.firstNight = True
    $ gotoscene('boysdormjimmysroom')

label prologue_spanishclassintro:
    play music MUSIC_CLASSROOMAMBIENCEDAY_THEME
    __("Looks like the teacher is not here yet.")
    __("I think I'll take a seat in the back. I don't wanna get too much attention.")
    scene spanishclassback with fade
    show jimmy smug with dissolve
    __("Alright... This seems like a good spot.")
    show pete uniform salute with dissolve
    play sound "audio/sfx/heypete01.ogg"
    Pete "Oh, hey, [player_name]."
    Pete "You have Spanish class with me."
    Jimmy unamused "What's up?"
    Pete neutral "Oh, nothing new. You know, just chilling."
    Pete "Have you met anyone else?"
    Jimmy "Just a fat man that doesn't let anyone get out of the boys' dorm at night."
    Pete "Oh, yeah. That's Mister Camembert. You need a prefect pass to walk around the campus at night."
    Pete "Thank god, he is just the math teacher. I could not stand having another class with him."
    Jimmy "I need to catch up with some of our 'classmates', if you know what I mean."
    Pete "Well, I think I can help you with that."
    Jimmy "Let's start with that girl over there, shall we?"
    play music "audio/music/funrocktheme01.ogg" volume 0.4
    scene spanishclassmandy with fade
    show mandyindeskintro01 with dissolve
    Pete "That's Mandy. She's your typical, self-absorbed cheerleader. She's dating the captain of the football team, naturally."
    $ Mandy.met = True
    Jimmy "She doesn't seem to care that the whole world can see her panties sitting like that."
    __("{i}[player_name] noticed that her panties were pink, just like the girl that went into his room last night.{/i}")
    __("{i}Of course, he knew there was a pretty big number of girls that liked to use pink stuff, even if feminists didn't agree.{/i}")
    __("{i}So, he just thought about how much he would love to see what was under that particular piece of pink panties.{/i}")
    pause 0.8
    Jimmy "Interesting..."
    Jimmy "And what about her, the one with the dark hair?"
    scene spanishclassroomfallday with fade
    show violetindeskintro with dissolve
    Pete "Oh, that's Violet. She's one of the preppies."
    Pete "Her father is a real estate mogul. He owns like half of the houses in Peacock Valley."
    $ Violet.met = True
    __("She seems like a bit of a brat, but with an ass like that, I don't think I mind.")
    pause 0.6
    scene spanishclassback with fade
    show jimmy smug with dissolve
    show pete uniform neutral with dissolve
    Jimmy smug "Man, you were right. There {i}are{/i} a lot of hot girls here."
    Pete "Oh yeah, and this is just the tip of the iceberg."
    Pete "Not that I stalk them or anything, but..."
    Pete "Well, it's pretty hard not to look."
    Jimmy "I get it, pal."
    Pete "Y'know what? After class, meet me in the gym and I'll show you a cool secret."
    Jimmy "Okay, sure."
    Pete "Um, someone's looking at you."
    hide pete
    hide jimmy
    with dissolve
    scene spanishclassmandy with fade
    show alice desk with dissolve
    Pete "I think she's been looking since you got here."
    __("{i}[player_name] had a feeling that he knew that girl from somewhere. She had a very familiar look.{/i}")
    Punny "¡Hola, clase!"
    stop music fadeout 0.5
    scene spanishclasspunny with fade
    show misspunny desk with dissolve
    play music MUSIC_MISSPUNNY_THEME volume 0.3
    __("\"Holy shit\" thought [player_name], realizing how hot the teacher was.")
    Punny "How are you doing, guys?"
    Violet "¡Muy bien, profesora!"
    Punny "Oh, Violet!"
    Punny "I see you've been practicing."
    Punny "Okay, guys!"
    Punny "I've been told we have a new student in class."
    stop sound fadeout 0.5
    __("Oh no...")
    Punny "Sr. [player_name]... [player_surname]."
    Punny "Sr. [player_surname]? Can you come up here?"
    show jimmy neutral with dissolve
    Punny "Un gusto en conocerte, [player_name]. ¡Eres muy guapo!"
    Jimmy suspicious "Yeah..."
    Punny "Don't worry, I will teach you how to say that, darling."
    Punny "My name is Miss Punny."
    $ Punny.met = True
    Punny arm "Can you tell us a bit about yourself?"
    Jimmy talk "There's not much to tell, really."
    Jimmy "I just moved here, so..."
    play sound "audio/sfx/hmm02.ogg"
    Punny "Oh! A new guy in town, how exciting it must be for you!"
    show jimmy smug with dissolve
    Jimmy "Exciting is one way to put it."
    Punny "Alright, you can go back to your seat, darling."
    hide jimmy with dissolve
    stop music
    play sound "audio/sfx/alright03.ogg"
    Punny standbook "¡Vamos a empezar la lección, clase!"
    play music "audio/music/spanishclasslessontheme.ogg"
    Punny "Alright, keep in mind the following tips for the test..."
    Punny "Saturday starts with the same letter in Spanish."
    Punny "Wednesday is the largest one in both languages."
    Punny "Tuesday might remind you of the red planet!"
    Punny "Sunday is when you GO to the church."
    Punny "The UV lights might hold the secret for Thursday."
    Punny "Monday is the shortest one in Spanish."
    Punny "And Friday is kind of a VR experience."
    Punny arm "That's it, guys! Let's start the test."
    $ prologue.spanishIntro = True
    return

label prologue_girlsshowersintro:
    hide screen freeroamhud
    with None
    show pete uniform neutral
    show jimmy neutral
    with dissolve
    play sound "audio/sfx/heypete01.ogg"
    Pete "Did you like Spanish class?"
    Jimmy smug "Let's just say I was more interested in the teacher."
    Pete "Oh, yeah, she's pretty."
    Pete "But as I promised, I'll show you a secret."
    Jimmy unamused "Alright, I'm all ears."
    Pete "There's a storage room near the back."
    Pete "Just before afternoon's gym class, the cheerleaders finish their training in the gym."
    Pete "And after that, y'know, they have to take a shower."
    Pete "Follow me."
    $ showscene('schoolgymstorageroom', transition=fade)
    play sound "audio/sfx/dooropen01.ogg"
    stop music
    show pete uniform neutral
    show jimmy unamused
    with dissolve
    play music "audio/music/sneaking01.ogg"
    Jimmy "Are you sure we should be in here?"
    Pete "Don't worry, no one comes in here at this time of the day."
    Pete "Now, remember what I told you about the cheerleaders?"
    Jimmy "Yeah."
    Pete "Well, their showers are right next to this room."
    Jimmy "Okay..."
    Pete "And there's a secret peephole right behind that poster."
    Jimmy smug "{i}Now{/i} we're talking."
    Pete "Yeah, not many people know about the hole, and no one knows who made it, but it's there."
    Pete "Here, take a look."
    scene gymlockergirlsbathpeek with fade
    Jimmy "Oh shit! You're right!"
    scene gymlockergirlsbath with fade
    Jimmy "I can see the showers from here!"
    Pete "Is there anyone there?"
    Jimmy "No, I don't..."
    scene christyshowerpeek with dissolve
    Jimmy "Wait, yes! A hot redhead just stepped into one of them!"
    call christy_gymshower_scene from _call_christy_gymshower_scene
    play sound SOUND_SCHOOL_BELL
    pause 0.5
    $ showscene('schoolgymstorageroom')
    show pete uniform neutral
    show jimmy smug
    with fade
    Pete "That's the bell."
    Pete "Gym class is about to start."
    Jimmy unamused "Oh, right."
    Pete "See you later, [player_name]."
    Jimmy "Wait, where are you going?"
    Pete "I... I don't like gym class."
    Jimmy "But you can't skip just it."
    Pete "Yeah, well. I have to, man."
    Pete "I can't stand Mr. Toord."
    Jimmy "But-"
    Toord "{i}Get over here, you damn wimps!{/i}"
    Pete "Shit, he's coming!"
    $ Toord.met = True
    hide pete with vpunch
    play music MUSIC_MRTOORD_THEME
    Toord "What are you doing in here, kid?"
    show jimmy neutral with dissolve
    show toord with dissolve
    Toord "Go get changed, immediately!"
    $ prologue.gymIntro = True
    jump gymclass

label prologue_cassidyintro:
    $ showscene('schoolgym', transition=fade)
    show screen freeroamhud(False)
    stop music
    __("Well, that was an interesting class.")
    __("I never thought beating up nerds would be a sanctioned school activity. Not that I'm complaining.")
    play sound "audio/sfx/ah1.ogg" volume 0.3
    __("...That's strange, I think I hear noises coming from the boys' locker room.")
    __("I thought everyone left already.")
    stop music
    hide screen freeroamhud with None
    $ showscene('schoolgymboyslockers', transition=fade, playMusic=False)
    show cassidy riding with vpunch
    play sound "audio/sfx/ah2.ogg"
    Cassidy "OH, GOD!"
    call cassidy_lockerroomdildo_scene from _call_cassidy_lockerroomdildo_scene
    $ showscene('schoolgymboyslockers', transition=dissolve)
    stop music
    play sound SOUND_RECORD_SCRATCH
    __("As I turned to leave, I heard her moan again.")
    play sound "audio/sfx/gasp02.ogg"
    __("This time though, it wasn't out of pleasure.")
    play music MUSIC_FUNNY_MOMENT
    show cassidy caught with vpunch
    Cassidy "AHH!"
    Cassidy "What are you doing here, pervert?"
    show jimmy talk with dissolve
    Jimmy "Well, I... I was coming to shower after gym class."
    Cassidy "In the girls' locker room?"
    Jimmy "Da fuck? This is the {i}boys'{/i} locker room."
    Cassidy "What?... Oh no... Oh my god..."
    Cassidy "Oh, not again..."
    Cassidy "Fuck, I just lose my mind when I'm horny."
    Jimmy unamused "You mean this has happened before?"
    Cassidy "Look, I'm sorry, okay?"
    Cassidy "Could you please not tell anyone about this?"
    Jimmy "Uh..."
    Cassidy "Okay, thank you! BYE!"
    play sound "audio/sfx/run01.ogg"
    hide cassidy with vpunch
    stop music
    show jimmy neutral with dissolve
    __("She just ran off.")
    __("Wow, that girl is crazy.")
    __("I feel like I've seen her before somewhere...")
    call nexttime from _call_nexttime_31
    jump prologue_day1night

label prologue_day1night:
    $ showscene('boysdormtvroom', transition=fade)
    show pete uniform neutral with dissolve
    show jimmy neutral with dissolve
    play sound "audio/sfx/heypete01.ogg"
    Pete "What's up!"
    Pete "How was gym class?"
    Jimmy unamused "Eh, I'm getting the hang of it."
    Jimmy smug "You wouldn't believe what happened after class though."
    Pete "Oh?"
    Jimmy "I heard screams coming from the locker room, and when I went to check..."
    Jimmy "...There was some girl in there riding a dildo."
    Pete "Dude, nice!"
    $ Cassidy.met = True
    Pete "I heard of some girl that got caught in there once by Mr. Toord. She didn't get detention, though, who knows how she got out of that situation."
    Pete "I'm sure Mr. Toord wasn't too upset about it, word is that he likes to perv on the girls."
    Jimmy "She was definitely putting on a show."
    Pete "I wish I could've been there."
    Pete "Oh, by the way, you can't leave the dorm at night."
    Pete "Unless you have a prefect pass that is."
    Jimmy unamused "Then I guess I should go to bed."
    Jimmy "Catcha later, Pete."
    Pete "Good night, [player_name]."
    hide pete
    hide jimmy
    with dissolve
    $ gotoscene('boysdormtvroom')

label prologue_mysterygirlnight2:
    hide screen freeroamhud
    stop music
    scene black with fade
    pause 1.0
    call wendy_mysterygirlnight2_scene from _call_wendy_mysterygirlnight2_scene
    stop music
    scene misterygirlshadow with vpunch
    play music "audio/music/suspensetheme01.ogg"
    __("Once more, [player_name] realized that there was figure in the window.")
    __("Someone was watching.")
    Jimmy "Hey! Who's there!?"
    Jimmy "Stay right there!"
    scene misterygirlshadow02 with dissolve
    __("The figure once more dissapeared in the blackness of the night.")
    Jimmy "What the fuck?"
    scene nightsky with fade
    __("He took a long breath one more time before falling sleep.")
    __("Not before he cleaned himself, of course. He's a very hygienic guy.")
    scene laterthatday with fade
    $ renpy.pause()
    show laterthatdaysomewhere with dissolve
    $ renpy.pause()
    scene lighthouseobservatorynight01 with fade
    play music "audio/music/mysterytheme.ogg"
    __("Peacock town seemed like a quiet and idillic place at night.")
    __("A place where the sky merged with the sea in the distance...")
    show oldsage neutral shadow with dissolve
    __("However, there were secrets lurking in the shadows, mysterious figures with unknown intentions.")
    __("And while the stars painted the dreams in which [player_name] was profoundly immersed...")
    __("He didn't even know he was part of a greater plan.")
    show pascal neutral light with dissolve
    Pascal "Goodnight, sir."
    Sage "Goodnight, my good friend."
    Sage "A little bird told me you had news for me."
    Pascal "Indeed, sir."
    Pascal "I've been watching over the lad since he arrived."
    Pascal "He's a vivid fella, this one."
    Sage "Interesting way of describing him. Proceed."
    Pascal "Well, I left a letter for the girl as you told me, sir."
    Pascal "The first day she went into his room at night, but she ran off too quickly."
    Pascal "I thought it wasn't going to work and I almost got caught by the lad."
    Pascal "He's a quick one, you see."
    Pascal "But, the second night, I saw the girl coming back."
    Pascal "Everything happened as you told me, sir."
    Sage "Well done, my friend. I knew I could count on you."
    Pascal "Of course, sir. So, what's next?"
    Sage "We wait, my friend. Patience is key for the development of this plan."
    Sage "For now, we can make use of that great skill for disguises that you have."
    Sage "Our \"vivid fella\", as you call him, will have an encounter with the law, very soon, and you'll be there to keep things in order."
    Pascal "Very well."
    stop music
    call nextday from _call_nextday_11
    jump prologue_day2morning

#ANIMATIONS
